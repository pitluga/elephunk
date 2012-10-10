$(function() {
  var w = 1170,
      h = 600;

  var cellToolTip = function(cell) {
    return cell.data.name + " " + cell.data.value + " bytes";
  }
  var color = function(cell) {
    return cell.data.isBloat ? "#636363" : "#99CCFF";
  }

  var treemap = d3.layout.treemap()
      .size([w + 1, h + 1])
      .value(function(d) { return d.value; })
      .sticky(true);

  var svg = d3.select("#treemap")
    .append("svg:svg")
    .style("width", w)
    .style("height", h)
    .style("opacity", 0.8)
    .append("svg:g").attr("transform", "translate(-.5,-.5)");

  var cell = svg.data([bloatData]).selectAll("g").data(treemap)
    .enter().append("svg:g")
      .attr("class", "cell")
      .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

  cell.append("svg:rect")
    .attr("width", function(d) { return d.dx; })
    .attr("height", function(d) { return d.dy; })
    .attr("title", function(d) { return d.children ? d.data.name : cellToolTip(d); })
    .style("opacity", function(d) { return d.data.isBloat ? 0.4 : 0.8; })
    .style("fill", function(d) { return d.children ? null : color(d); });

  $('g.cell rect').tooltip({placement: 'bottom'});
});
