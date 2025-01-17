---
title: Introduction
toc: false
theme: [dashboard, midnight]
---


<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-5HVJ595HD3"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-5HVJ595HD3');
</script>


<style>

	#observablehq-footer{
		display: table;
		text-align: center;
		margin-left: auto;
		margin-right: auto;
	}

	#observablehq-sidebar-close {
		display: none;
	}

</style>

```js
FileAttachment("./data/cards/announcement.png").image()
```

<div >
	<div class="card" style="display: flex;flex-direction: column">${resize((width) => dailyLogs({width}))}</div>
	<div class="card" style="display: flex;flex-direction: column">${resize((width) => gsDistrib({width}))}</div>
	<div class="card" style="text-align: center; vertical-align: middle;">Huge thanks to <a href="https://github.com/evilandrex" target="_blank">EvilAndrex</a>, faust, <a href="https://github.com/molenzwiebel" target="_blank">molenzwiebel</a>, <a href="https://github.com/snoww" target="_blank">snow</a>, and all of you who contributed data.</div>
	<div class="card" style="text-align: center; vertical-align: middle;">You can contact me from my discord kennethnyu. </div>
</div>



```js
const dailyData = await FileAttachment("./data/home_daily.json").json();
const distribData = await FileAttachment("./data/home_distrib.json").json();
```


```js
function dailyLogs({width} = {}){
// Load data
	const aqData = aq.from(dailyData)
	.derive({
		serverdate: (d) => aq.op.parse_date(d.serverdate),
	})
// Graph dimensions
	const plotHeight = 250;
	const margins = { top: 20, right: 20, bottom: 20, left: 20 };
	const xAxisHeight = 75;
	const yAxisWidth = 75;
	const minWidth = 550;
	const height = plotHeight + margins.top + margins.bottom + xAxisHeight;
// Set start and end by 1 day
	const mindate=aq.op.parse_date(d3.min(aqData.array("serverdate")));
	mindate.setDate(mindate.getDate()-1);
	const maxdate=aq.op.parse_date(d3.max(aqData.array("serverdate")));
	maxdate.setDate(maxdate.getDate()+1);

// Declare the x (horizontal position) scale
	const xLeft = margins.left;
	const xScale = d3.scaleUtc()
	.domain([mindate,maxdate])
	.range([margins.left + yAxisWidth, width - margins.right - yAxisWidth]);
	const  x_band = d3
	.scaleBand()
	.domain(aqData.array("serverdate"))
	.range([margins.left, width - margins.right])
	.padding(0.3)
// Declare the y (vertical position) scale.
	const yScale = d3.scaleLinear()
	.domain([0, d3.max(aqData.array("logs"))])
	.range([height - margins.bottom - xAxisHeight,margins.top]);
	const yScaleRight = d3.scaleLinear()
	.domain([0, 100])
	.range([height - margins.bottom - xAxisHeight,margins.top]);

// Create SVG container
	const svg = d3
	.create("svg")
	.attr("width", width)
	.attr("height", height)
	.style("background", "transparent");
	const g = svg.append("g").selectAll("g").data(aqData.objects()).join("g");
// Add daily logs bar chart
	svg.append("g")
	.attr("fill", "#428089")
	.selectAll()
	.data(aqData.objects())
	.join("rect")
	.attr("x", (d) => xScale(d.serverdate)-x_band.bandwidth()/2)
	.attr("y", (d) => yScale(d.logs))
	.attr("width", x_band.bandwidth())
	.attr("height", (d) => yScale(0) - yScale(d.logs))
	.attr("pointer-events", "none");
// Add ark active passive line chart
	svg.append("path")
	.datum(aqData.objects())
	.attr("fill","none")
	.attr("d", d3.line()
		.x(function(d) { return xScale(d.serverdate) })
		.y(function(d) { return yScaleRight(d.arkactive) })
		)
	.attr("stroke", "#b79b8f")
	.attr("stroke-width", "3px")
	.attr("pointer-events", "none");

// Create x-axis
	const xAxis = d3.axisBottom(xScale);
	var xAxisGroup = svg
	.append("g")
	.attr("transform", `translate(0, ${height - margins.bottom - xAxisHeight})`)
	.attr("pointer-events", "none")
	.call(xAxis);
	xAxisGroup
	.selectAll("text")
	.attr("font-size", "14px")
	.attr("visibility", "visible");
// Create y-axis
	const yAxis = d3.axisLeft(yScale);
	const yAxisRight = d3.axisRight(yScaleRight);
	var yAxisGroup = svg
	.append("g")
	.attr("transform", `translate(${margins.left + yAxisWidth}, 0)`)
	.attr("pointer-events", "none")
	.attr("color", "#428089")
	.call(yAxis);
	var yAxisRightGroup = svg
	.append("g")
	.attr("transform", `translate(${width - margins.right - yAxisWidth}, 0)`)
	.attr("pointer-events", "none")
	.attr("color", "#b79b8f")
	.call(yAxisRight);
	yAxisGroup
	.selectAll("text")
	.attr("font-size", "14px")
	.attr("visibility", "visible")
	.attr("transform", width > minWidth ? "" : `translate(${-yAxisWidth}, 0)`);
	yAxisRightGroup
	.selectAll("text")
	.attr("font-size", "14px")
	.attr("visibility", "visible")
	.attr("transform", width > minWidth ? "" : `translate(${-yAxisWidth}, 0)`);

// Add x-axis label
	svg
	.append("text")
	.attr(
		"transform", `translate(${(width - yAxisWidth) / 2 + yAxisWidth}, ${height})`
		)
	.attr("text-anchor", "middle")
	.attr("font-size", "24px")
	.attr("fill", "var(--theme-foreground)")
	.text("Date");
// Add y axis label
	svg
	.append("text")
	.attr(
		"transform", `translate(${margins.left}, ${plotHeight / 2}) rotate(-90.1)`
		)
	.attr("text-anchor", "middle")
	.attr("font-size", "24px")
	.attr("fill", "#428089")
	.text("Daily Logs");
// Add y axis label
	svg
	.append("text")
	.attr(
		"transform", `translate(${width-margins.right}, ${plotHeight / 2}) rotate(90.1)`
		)
	.attr("text-anchor", "middle")
	.attr("font-size", "24px")
	.attr("fill", "#b79b8f")
	.text("Ark Passive Active %");

// Prepare tooltip
	const tooltip = d3
	.select("main")
	.append("div")
	.attr("class", "tooltip")
	.style("position", "absolute")
	.style("opacity", 0);
// Draw vertical line following mouse
	svg
	.append("rect")
	.attr("class", "mouseLine")
	.attr("fill", "black")
	.attr("pointer-events", "none");

// Add invisible box to support mouse over
	g.append("rect")
	.attr("class", "rowMouseBox")
	.attr("x", (d) => xScale(d.serverdate)-x_band.bandwidth()/2)
	.attr("y", (d) => yScale.range()[1])
	.attr("width", (d) => x_band.bandwidth())
	.attr("height", (d) => yScale.range()[0] - margins.bottom)
	.attr("fill", "transparent")
	.on("mouseover", (event, d) => {
		tooltip.style("opacity", 1).html(`
			<div class="card" style="padding: 7px;" >
			<div style="display: flex; align-items: center; justify-content: center;">Date; ${d.serverdate.toISOString().split('T')[0]}</div>
			<div style="display: flex; align-items: center; justify-content: center;">${d.logs} Logs</div>
			<div style="display: flex; align-items: center; justify-content: center;">${d.arkactive}% Ark Passive Active</div>
			</div>
			`);
// Darken row
		d3.select(event.target)
		.attr("fill", "var(--theme-foreground-muted)")
		.attr("opacity", "0.25");
// Change mouse
		d3.select(this).style("cursor", "pointer");
// Keep updating line
		svg.selectAll(".mouseLine").attr("visibility", "visible");
	})
	.on("mouseout", () => {
		d3.selectAll(".tooltip").attr("opacity", 0).style("left", "-9999px");
// Lighten row
		g.selectAll(".rowMouseBox").attr("fill", "transparent");
	})
	.on("mousemove", (event) => {
		if (event.offsetX > width / 2) {
			tooltip.style("left", event.offsetX - 140 + "px");
		} else {
			tooltip.style("left", event.offsetX + 30 + "px");
		}
		tooltip.style("top", event.pageY - 30 + "px");
	});

	svg
	.on("mousemove", (event) => {
		const x = event.offsetX;
		const y = event.offsetY;
// Update line
		svg
		.selectAll(".mouseLine")
		.attr("x", margins.left)
		.attr("y", y + 1)
		.attr("width", width - yAxisWidth - margins.left)
		.attr("height", 1)
		.attr("fill", "var(--theme-foreground-muted)")
		.attr("opacity", 0.5)
		.attr("visibility", x > yAxisWidth ? "visible" : "hidden");
	})
	.on("mouseout", () => {
		svg.selectAll(".mouseLine").attr("visibility", "hidden");
	});

// Return the SVG element.
	return svg.node()
}
```

```js

function gsDistrib ({width} = {}){
// Load data
	const dsData = aq.from(distribData)

// Graph dimensions
	const plotHeight = 250;
	const margins = { top: 20, right: 20, bottom: 20, left: 20 };
	const xAxisHeight = 75;
	const yAxisWidth = 75;
	const minWidth = 550;
	const height = plotHeight + margins.top + margins.bottom + xAxisHeight;
// Set start and end by 1 day
	const mings=d3.quantile(dsData.array("maxgear"),0.001);
	const maxgs=d3.max(dsData.array("maxgear"));

// Bin the data.
	const bins = d3.bin()
	.thresholds(d3.range(mings, maxgs, 5))
	.value((d) => d.maxgear)
	(dsData);

// Declare the x (horizontal position) scale
	const xLeft = margins.left;
	const xScale = d3.scaleLinear()
	.domain([mings,maxgs])
	.range([margins.left + yAxisWidth, width - margins.right - yAxisWidth]);
// Declare the y (vertical position) scale.
	const yScale = d3.scaleLinear()
	.domain([0, d3.max(bins, (d) => d.length)])
	.range([height - margins.bottom - xAxisHeight,margins.top]);

// Create SVG container
	const svg = d3
	.create("svg")
	.attr("width", width)
	.attr("height", height)
	.style("background", "transparent");
	const g = svg.append("g").selectAll("g").data(bins).join("g");
// Add daily logs bar chart
	svg.append("g")
	.attr("fill", "#428089")
	.selectAll()
	.data(bins)
	.join("rect")
	.attr("x", (d) => xScale(d.x0) + 1)
	.attr("y", (d) => yScale(d.length))
	.attr("width", (d) => xScale(d.x1) - xScale(d.x0) - 1)
	.attr("height", (d) => yScale(0) - yScale(d.length))
	.attr("pointer-events", "none");

// Create x-axis
	const xAxis = d3.axisBottom(xScale);
	var xAxisGroup = svg
	.append("g")
	.attr("transform", `translate(0, ${height - margins.bottom - xAxisHeight})`)
	.attr("pointer-events", "none")
	.call(xAxis);
	xAxisGroup
	.selectAll("text")
	.attr("font-size", "14px")
	.attr("visibility", "visible");
// Create y-axis
	const yAxis = d3.axisLeft(yScale);
	var yAxisGroup = svg
	.append("g")
	.attr("transform", `translate(${margins.left + yAxisWidth}, 0)`)
	.attr("pointer-events", "none")
	.attr("color", "#428089")
	.call(yAxis);
	yAxisGroup
	.selectAll("text")
	.attr("font-size", "14px")
	.attr("visibility", "visible")
	.attr("transform", width > minWidth ? "" : `translate(${-yAxisWidth}, 0)`);

// Add x-axis label
	svg
	.append("text")
	.attr(
		"transform", `translate(${(width - yAxisWidth) / 2 + yAxisWidth}, ${height})`
		)
	.attr("text-anchor", "middle")
	.attr("font-size", "24px")
	.attr("fill", "var(--theme-foreground)")
	.text("Gearscore");
// Add y axis label
	svg
	.append("text")
	.attr(
		"transform", `translate(${margins.left}, ${plotHeight / 2}) rotate(-90.1)`
		)
	.attr("text-anchor", "middle")
	.attr("font-size", "24px")
	.attr("fill", "#428089")
	.text("Characters");

// Prepare tooltip
	const tooltip = d3
	.select("main")
	.append("div")
	.attr("class", "tooltip")
	.style("position", "absolute")
	.style("opacity", 0);
// Draw vertical line following mouse
	svg
	.append("rect")
	.attr("class", "mouseLine")
	.attr("fill", "black")
	.attr("pointer-events", "none");

// Add invisible box to support mouse over
	g.append("rect")
	.attr("class", "rowMouseBox")
	.attr("x", (d) => xScale(d.x0) + 1)
	.attr("y", (d) => yScale.range()[1])
	.attr("width", (d) => xScale(d.x1) - xScale(d.x0) - 1)
	.attr("height", (d) => yScale.range()[0] - margins.bottom)
	.attr("fill", "transparent")
	.on("mouseover", (event, d) => {
		tooltip.style("opacity", 1).html(`
			<div class="card" style="padding: 7px;" >
			<div style="display: flex; align-items: center; justify-content: center;">${d.x0}-${d.x1}</div>
			<div style="display: flex; align-items: center; justify-content: center;">${d.length.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")} Logs</div>
			</div>
			`);
// Darken row
		d3.select(event.target)
		.attr("fill", "var(--theme-foreground-muted)")
		.attr("opacity", "0.25");
// Change mouse
		d3.select(this).style("cursor", "pointer");
// Keep updating line
		svg.selectAll(".mouseLine").attr("visibility", "visible");
	})
	.on("mouseout", () => {
		d3.selectAll(".tooltip").attr("opacity", 0).style("left", "-9999px");
// Lighten row
		g.selectAll(".rowMouseBox").attr("fill", "transparent");
	})
	.on("mousemove", (event) => {
		if (event.offsetX > width / 2) {
			tooltip.style("left", event.offsetX - 140 + "px");
		} else {
			tooltip.style("left", event.offsetX + 30 + "px");
		}
		tooltip.style("top", event.pageY - 30 + "px");
	});

	svg
	.on("mousemove", (event) => {
		const x = event.offsetX;
		const y = event.offsetY;
// Update line
		svg
		.selectAll(".mouseLine")
		.attr("x", margins.left)
		.attr("y", y + 1)
		.attr("width", width - yAxisWidth - margins.left)
		.attr("height", 1)
		.attr("fill", "var(--theme-foreground-muted)")
		.attr("opacity", 0.5)
		.attr("visibility", x > yAxisWidth ? "visible" : "hidden");
	})
	.on("mouseout", () => {
		svg.selectAll(".mouseLine").attr("visibility", "hidden");
	});

// Return the SVG element.
	return svg.node()
}


```




