$(function() {
  var w = 1170,
      h = 600,
      color = d3.scale.category20c();

  var cellToolTip = function(cell) {
    return cell.data.name + "<dl class='dl-horizontal'><dt># of Scans</dt><dd>" + cell.data.scans + "</dd><dt>Tuples Read</dt><dd>" + cell.data.tuples + "</dd></dl>";
  }

  var treemap = d3.layout.treemap()
      .size([w + 1, h + 1])
      .value(function(d) { return d.tuples; })
      .sticky(true);

  var svg = d3.select("#treemap")
    .append("svg:svg")
    .style("width", w)
    .style("height", h)
    .style("opacity", 0.8)
    .append("svg:g").attr("transform", "translate(-.5,-.5)");

  var cell = svg.data([indexData]).selectAll("g").data(treemap)
    .enter().append("svg:g")
      .attr("class", "cell")
      .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

  cell.append("svg:rect")
    .attr("width", function(d) { return d.dx; })
    .attr("height", function(d) { return d.dy; })
    .attr("title", function(d) { return d.children ? d.data.name : cellToolTip(d); })
    .style("opacity", function(d) { return d.data.isIndex ? 0.4 : 0.8; })
    .style("fill", function(d) { return d.children ? null : color(d.parent.data.name); });

  cell.append("svg:text")
    .attr("x", function(d) { return d.dx / 2; })
    .attr("y", function(d) { return d.dy / 2; })
    .attr("text-anchor", "middle")
    .text(function(d) { return d.data.name; })
    .style("opacity", function(d) { d.w = this.getComputedTextLength(); return (d.dx > d.w && d.dy > 0) ? 1 : 0; });

  $('g.cell rect').tooltip({placement: 'bottom'});
});
