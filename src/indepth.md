<!-- ---
title: Introduction
toc: false
theme: "dashboard"
---


Item Level Range
${iLevelMinRange}
${iLevelMaxRange}

```js
const describe = await FileAttachment("./data/describe.json").json();
```

```js queryString processor
const urlParams = new URLSearchParams(window.location.search);
```

```js ilevel ranges
const bossIlevelDefaults = {
  Argeos: { Normal: [1640, 1679]},
  Gargadeth: [1610, 1629],
  Veskal: [1630, 1675],
  Brelshaza: { Hard: [1580, 1609] },
  Kayangel: { Hard: [1580, 1599] },
  Akkan: { Normal: [1580, 1599], Hard: [1600, 1619] },
  Ivory: { Normal: [1600, 1619], Hard: [1620, 1740] },
  Thaemine: { Normal: [1610, 1629], Hard: [1630, 1740] },
  Echidna: { Normal: [1620, 1629], Hard: [1630, 1740] },
};

const iLevelDefaults = bossIlevelDefaults["Argeos"]
  ? bossIlevelDefaults["Argeos"]["Normal"]
    ? bossIlevelDefaults["Argeos"]["Normal"]
    : bossIlevelDefaults["Argeos"]
  : [1580, 1740];
const iLevelMinRange = Inputs.range([1580, 1740], {
  value: urlParams.get("iLevelMin")
    ? Number(urlParams.get("iLevelMin"))
    : iLevelDefaults[0],
  step: 1,
});
const iLevelMin = Generators.input(iLevelMinRange);

const iLevelMaxRange = Inputs.range([1580, 1740], {
  value: urlParams.get("iLevelMax")
    ? Number(urlParams.get("iLevelMax"))
    : iLevelDefaults[1],
  step: 1,
});
const iLevelMax = Generators.input(iLevelMaxRange);
```


```js

var spec_to_color={"Berserker Technique":"#EE2E48","Mayhem":"#EE2E48",
               "Gravity Training":"#7B9AA2","Rage Hammer":"#7B9AA2",
               "Combat Readiness":"#E1907E","Lone Knight":"#E1907E", "Princess Maker":"#E1907E",
               "Predator":"#DB6A42","Punisher":"#DB6A42",
               "Order of the Emperor":"#B38915","Grace of the Empress":"#B38915",
               "Communication Overflow":"#22AA99","Master Summoner":"#22AA99",
               "Igniter":"#66AA00","Reflux":"#66AA00",
               "Esoteric Skill Enhancement":"#AAAA11","First Intention":"#AAAA11",
               "Ultimate Skill: Taijutsu":"#990099","Shock Training":"#990099",
               "Energy Overflow":"#316395","Robust Spirit":"#316395",
               "Control":"#F6DA6A","Pinnacle":"#F6DA6A",
               "Deathblow":"#994499","Esoteric Flurry":"#994499",
               "Asura's Path":"#4DE3D1","Brawl King Storm":"#4DE3D1",
               "Remaining Energy":"#A91A16","Surge":"#A91A16",
               "Demonic Impulse":"#0099C6","Perfect Suppression":"#0099C6",
               "Hunger":"#109618","Lunar Voice":"#109618",
               "Full Moon Harvester":"#C16ED0","Night's Edge":"#C16ED0",
               "Death Strike":"#DD4477","Loyal Companion":"#DD4477",
               "Enhanced Weapon":"#4442A8","Pistoleer":"#4442A8",
               "Barrage Enhancement":"#33670B","Firepower Enhancement":"#33670B",
               "Arthetinean Skill":"#3B4292","Evolutionary Legacy":"#3B4292",
               "Peacemaker":"#6BCEC2","Time to Hunt":"#6BCEC2",
               "Drizzle":"#084BA3","Wind Fury":"#084BA3"};

const width = 1200;
const plotHeight = 650;
const margins = { top: 10, right: 10, bottom: 10, left: 10 };
const xAxisHeight = 50;
const yAxisWidth = 250;
const minWidth = 550;
const height = plotHeight + margins.top + margins.bottom + xAxisHeight;


const data = await aq.from(describe)
.filter(d => d.boss == "Argeos")
.filter(aq.escape((d) => d.gearScore >= iLevelMin && d.gearScore <= iLevelMax))

const logsCount = data.numRows()
;

const summary = data
  .groupby("spec")
  .rollup({
  	count: aq.op.count(),
    min: aq.op.min("dps"),
    q01: aq.op.quantile("dps", 0.01),
    q25: aq.op.quantile("dps", 0.25),
    median: aq.op.median("dps"),
    q75: aq.op.quantile("dps", 0.75),
    q99: aq.op.quantile("dps", 0.99),
    max: aq.op.max("dps"),
  })
  .derive({
    specCount: (d) => d.spec + ` (${d.count})`,
  })
  .orderby("median")
  .reify();


const summaryTable = Inputs.table(summary, {
  format: {
    spec: (d) => d,
    min: d3.format(".3s"),
    q01: d3.format(".3s"),
    q25: d3.format(".3s"),
    median: d3.format(".3s"),
    q75: d3.format(".3s"),
    q99: d3.format(".3s"),
    max: d3.format(".3s")
  },
  layout: "auto",
});

var asdf=[{"max":25},{"max":30},{"max":35}];

const finalData = Generators.input(summaryTable);

// Create x-scale (based on dps)
const maxCol = "max";
const xLeft = width > minWidth ? yAxisWidth + margins.left : margins.left;
const xScale = d3
.scaleLinear()
.domain([0, d3.max(data.array("dps"))*1.1])
.range([xLeft, width - margins.right]);

// Create y-scale (categorical for each class)
const yScale = d3
.scaleBand()
.domain(summary.objects().map((d) => d.specCount))
.range([margins.top, height - margins.bottom - xAxisHeight])
.padding(0.2);

// Create SVG container
const svg = d3
.create("svg")
.attr("width", width)
.attr("height", height)
.style("background", "transparent");


svg.selectAll("line.vertical-grid").data(xScale.ticks(10)).enter()
.append("line")
.attr("class","vertical-grid")
.attr("x1",function(d){ return xScale(d);})
.attr("x2",function(d){ return xScale(d);})
.attr("y1",margins.bottom)
.attr("y2",plotHeight+margins.bottom)
.attr("stroke","white")
.attr("opacity",0.1)
.attr("z-index",5)
.attr("stroke-width","1px");

const g = svg.append("g").selectAll("g").data(summary.objects()).join("g");

// Add main box (q25 and q75)
g.append("rect")
.attr("x", (d) => xScale(d.q25))
.attr("y", (d) => yScale(d.specCount))
.attr("width", (d) => xScale(d.q75) - xScale(d.q25))
.attr("height", yScale.bandwidth())
.attr("fill", (d) => (spec_to_color[d.spec]));

// Add median line
g.append("line")
.attr("x1", (d) => xScale(d.median))
.attr("x2", (d) => xScale(d.median))
.attr("y1", (d) => yScale(d.specCount))
.attr("y2", (d) => yScale(d.specCount) + yScale.bandwidth())
.attr("stroke", "white");

// Add lower whisker
g.append("line")
.attr("x1", (d) => xScale(d.q01))
.attr("x2", (d) => xScale(d.q25))
.attr("y1", (d) => yScale(d.specCount) + yScale.bandwidth() / 2)
.attr("y2", (d) => yScale(d.specCount) + yScale.bandwidth() / 2)
.attr("stroke", (d) => (spec_to_color[d.spec]))
.attr("stroke-width", 3);

// Add whisker cap
g.append("line")
.attr("x1", (d) => xScale(d.q01))
.attr("x2", (d) => xScale(d.q01))
.attr("y1", (d) => yScale(d.specCount) + yScale.bandwidth() / 4)
.attr("y2", (d) => yScale(d.specCount) + (yScale.bandwidth() * 3) / 4)
.attr("stroke", "var(--theme-foreground)")
.attr("stroke-width", 3);

// Add upper whisker
g.append("line")
.attr("x1", (d) => xScale(d.q75))
.attr("x2", (d) => xScale(d.q99))
.attr("y1", (d) => yScale(d.specCount) + yScale.bandwidth() / 2)
.attr("y2", (d) => yScale(d.specCount) + yScale.bandwidth() / 2)
.attr("stroke", (d) => (spec_to_color[d.spec]))
.attr("stroke-width", 3);;

// Add whisker cap
g.append("line")
.attr("x1", (d) => xScale(d.q99))
.attr("x2", (d) => xScale(d.q99))
.attr("y1", (d) => yScale(d.specCount) + yScale.bandwidth() / 4)
.attr("y2", (d) => yScale(d.specCount) + (yScale.bandwidth() * 3) / 4)
.attr("stroke", "var(--theme-foreground)")
.attr("stroke-width", 3);

// Create x-axis
const xAxis = d3.axisBottom(xScale).ticks(10, "s");
svg
.append("g")
.attr("transform", `translate(0, ${height - margins.bottom - xAxisHeight})`)
.call(xAxis);

// Add x-axis label
svg
.append("text")
.attr(
	"transform",
	`translate(${
		width > minWidth ? (width - yAxisWidth) / 2 + yAxisWidth : width / 2
	}, ${height - margins.bottom - xAxisHeight / 2})`
	)
.attr("dy", "1em")
.attr("text-anchor", "middle")
.attr("font-size", "16px")
.attr("font-family", "var(--sans-serif)")
.attr("fill", "var(--theme-foreground)")
.text("DPS (millions)");

// Create y-axis
const yAxis = d3.axisLeft(yScale);
var yAxisGroup = svg
.append("g")
.attr("visibility", width > minWidth ? "visible" : "hidden")
.attr("transform", `translate(${margins.left + yAxisWidth}, 0)`)
.attr("pointer-events", "none")
.call(yAxis);

yAxisGroup
.selectAll("text")
.attr("font-size", "14px")
.attr("visibility", "visible")
.attr("opacity", width > minWidth ? 1 : 0.25)
.attr("text-anchor", width > minWidth ? "end" : "start")
.attr("transform", width > minWidth ? "" : `translate(${-yAxisWidth}, 0)`)
.text((d) => (width > minWidth ? d : d.split(" (")[0]));

// Create a new dictionary where spec is the key and color is the value
const specColorDict = summary.objects().reduce((acc, curr) => {
  acc[curr.spec] = spec_to_color[curr.spec]; // Set spec as the key and color as the value
  return acc;
}, {});

yAxisGroup
.selectAll("line")
.style( "stroke", function(d)    {
	console.log(d);
	return specColorDict[d.split(" (")[0]]
})
.style("stroke-width","10")

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
  .attr("x", (d) => xScale.range()[0] - yAxisWidth + 25)
  .attr("y", (d) => yScale(d.specCount))
  .attr("width", (d) => xScale.range()[1] - xScale.range()[0] + yAxisWidth - 25)
  .attr("height", yScale.bandwidth())
  .attr("fill", "transparent")
  .on("mouseover", (event, d) => {
    tooltip.style("opacity", 1).html(`
      <div class="card" style="padding: 7px;">
        <div>Rank ${summary.objects().length-summary.array("spec").indexOf(d.spec)}/${
      summary.objects().length
    }</div>
        <div>${d.specCount.split(" (")[0]}</div>
        <div>${d.specCount.split(" (")[1].replace(")", "")} logs</div>
        <br/>
        <div>Worst: ${d3.format(".3s")(d.min)}m</div>
        <div>Floor: ${d3.format(".3s")(d.q01)}m</div>
        <div>Q1: ${d3.format(".3s")(d.q25)}m</div>
        <div>Median: ${d3.format(".3s")(d.median)}m</div>
        <div>Q3: ${d3.format(".3s")(d.q75)}m</div>
        <div>Ceiling: ${d3.format(".3s")(d.q99)}m</div>
        <div>Best: ${d3.format(".3s")(d.max)}m</div>
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

g.append("path")
  .attr("d", d3.symbol(d3.symbolStar).size(60))
  .attr(
    "transform",
    (d) =>
      `translate(${xScale(d.max)}, ${yScale(d.specCount) + yScale.bandwidth() / 2})`
  )
  .attr("fill", (d) => (spec_to_color[d.spec]))
  .attr("opacity", "0.5")
  .style("cursor", "pointer")
  .on("mouseover", (event, d) => {
    d3.select(event.target).attr("opacity", "1");

    // Find the link to the best log
    

    tooltip.style("opacity", 1).html(`
      <div class="card" style="padding: 7px;">
        <div>${d.specCount.split(" (")[0]}</div>
        <div>${d3.format(".3s")(d.max)}m DPS</div>
      </div>
    `);
  })
  .on("mouseout", (event, d) => {
    d3.select(event.target).attr("opacity", "0.5");
    d3.select(this).style("cursor", "");

    // Hide tooltip
    d3.selectAll(".tooltip").attr("opacity", 0).style("left", "-9999px");
  })
  .on("mousemove", (event) => {
    if (event.offsetX > width / 2) {
      tooltip.style("left", event.offsetX - 140 + "px");
    } else {
      tooltip.style("left", event.offsetX + 30 + "px");
    }

    tooltip.style("top", event.pageY - 30 + "px");
  })
  .on("click", (event, d) => {
    window.open(
      `https://logs.fau.dev/log/${
        data
          .filter(
            aq.escape(
              (log) => log.dps === d.Max && log.class === d.Build.split(" (")[0]
            )
          )
          .array("id")[0]
      }`,
      "_blank"
    );
  });

svg
  .on("mousemove", (event) => {
    const x = event.offsetX;
    const y = event.offsetY;

    // Update line
    svg
      .selectAll(".mouseLine")
      .attr("x", x + 1)
      .attr("y", margins.top)
      .attr("width", 1)
      .attr("height", height - xAxisHeight - margins.bottom)
      .attr("fill", "var(--theme-foreground-muted)")
      .attr("opacity", 0.5)
      .attr("visibility", x > yAxisWidth ? "visible" : "hidden");
  })
  .on("mouseout", () => {
    svg.selectAll(".mouseLine").attr("visibility", "hidden");
  });

// Add total logs string
svg
  .append("text")
  .attr(
    "transform",
    `translate(${width}, 140)`
  )
  .attr("text-anchor", "end")
  .attr("font-family", "var(--sans-serif)")
  .attr("font-size", "12px")
  .attr("fill", "var(--theme-foreground)")
  .text(`Total logs: ${logsCount}`);


svg.append("svg:image")
.attr("href", `_file/data/Argeos.png`)
.attr("x", width-83)
.attr("width", "83px")
.attr("height", "120px")

display(svg.node())

```

 -->