class Row:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class Database():
    def __init__(self, client):
        self.client = client

    def select_all(self, operation, parameters=(), callback=None):
        self.client.execute(operation, parameters, callback = lambda cursor: callback(self._map_cursor(cursor)))

    def _map_cursor(self, cursor):
        names = [x[0] for x in cursor.description]
        return [Row(**dict(zip(names, row))) for row in cursor.fetchall()]
