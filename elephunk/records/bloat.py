from elephunk.database import Row

class Bloat(Row):

    @property
    def table_id(self):
        return (self.schemaname, self.tablename)

    @property
    def full_table_name(self):
        return "%s.%s" % self.table_id

    @staticmethod
    def sql():
        return """
SELECT
  schemaname,
  tablename,
  reltuples::bigint,
  relpages::bigint,
  relpages * block_size AS usedbytes,
  otta,
  ROUND(CASE WHEN otta=0 THEN 0.0 ELSE sml.relpages/otta::numeric END,1) AS tbloat,
  CASE WHEN relpages < otta THEN 0 ELSE block_size*(sml.relpages-otta)::bigint END AS wastedbytes,
  iname,
  ituples::bigint,
  ipages::bigint,
  ipages * block_size AS iusedbytes,
  iotta,
  ROUND(CASE WHEN iotta=0 OR ipages=0 THEN 0.0 ELSE ipages/iotta::numeric END,1) AS ibloat,
  CASE WHEN ipages < iotta THEN 0 ELSE block_size*(ipages-iotta) END AS wastedibytes
FROM (
  SELECT
    schemaname, tablename, cc.reltuples, cc.relpages, block_size,
    CEIL((cc.reltuples*((datahdr + ma - (CASE WHEN mod(datahdr, ma) = 0 THEN ma ELSE mod(datahdr, ma) END)) + nullhdr2 + 4)) / (block_size-20::float)) AS otta,
    COALESCE(c2.relname,'?') AS iname, COALESCE(c2.reltuples,0) AS ituples, COALESCE(c2.relpages,0) AS ipages,
    COALESCE(CEIL((c2.reltuples*(datahdr-12))/(block_size-20::float)),0) AS iotta -- very rough approximation, assumes all cols
  FROM (
    SELECT
      ma,block_size,schemaname,tablename,
      (datawidth + (hdr + ma - (case when mod(hdr, ma) = 0 THEN ma ELSE mod(hdr, ma) END)))::numeric AS datahdr,
      (maxfracsum * (nullhdr + ma - (case when mod(nullhdr, ma) = 0 THEN ma ELSE mod(nullhdr, ma) END))) AS nullhdr2
    FROM (
      SELECT
        schemaname, tablename, hdr, ma, block_size,
        SUM((1-null_frac)*avg_width) AS datawidth,
        MAX(null_frac) AS maxfracsum,
        hdr+(
          SELECT 1+count(*)/8
          FROM pg_stats s2
          WHERE null_frac<>0 AND s2.schemaname = s.schemaname AND s2.tablename = s.tablename
        ) AS nullhdr
      FROM pg_stats s, (
        SELECT
          (SELECT current_setting('block_size')::numeric) AS block_size,
          CASE WHEN substring(v,12,3) IN ('8.0','8.1','8.2') THEN 27 ELSE 23 END AS hdr,
          CASE WHEN v ~ 'mingw32' THEN 8 ELSE 4 END AS ma
        FROM (SELECT version() AS v) AS foo
      ) AS constants
      GROUP BY 1,2,3,4,5
    ) AS foo
  ) AS rs
  JOIN pg_class cc ON cc.relname = rs.tablename
  JOIN pg_namespace nn ON cc.relnamespace = nn.oid AND nn.nspname = rs.schemaname AND nn.nspname <> 'information_schema'
  LEFT JOIN pg_index i ON indrelid = cc.oid
  LEFT JOIN pg_class c2 ON c2.oid = i.indexrelid
) AS sml
ORDER BY schemaname, tablename
        """


