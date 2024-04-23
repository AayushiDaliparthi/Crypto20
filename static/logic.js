d3.json("heatmap_data.json", function (data) {
    // Set dimensions and margins for the graph
    const margin = { top: 20, right: 30, bottom: 40, left: 90 },
      width = 960 - margin.left - margin.right,
      height = 500 - margin.top - margin.bottom;
  
    // Append the SVG object to the div
    const svg = d3
      .select("#my_dataviz1")
      .append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
  
    // X axis
    const x = d3
      .scaleBand()
      .domain(Object.keys(data))
      .range([0, width]);
    svg
      .append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x))
      .selectAll("text")
      .style("text-anchor", "end")
      .attr("transform", "rotate(-45)");
  
    // Y axis
    const y = d3
      .scaleBand()
      .domain(Object.keys(data))
      .range([0, height]);
    svg.append("g").call(d3.axisLeft(y));
  
    // Color scale
    const color = d3.scaleLinear().domain([0, 1]).range(["white", "steelblue"]);
  
    // Draw rectangles
    svg
      .selectAll("rect")
      .data(Object.keys(data))
      .enter()
      .append("rect")
      .attr("x", (d) => x(d))
      .attr("y", (d) => y(d))
      .attr("width", x.bandwidth())
      .attr("height", y.bandwidth())
      .style("fill", (d) => color(data[d]));
  });
  

