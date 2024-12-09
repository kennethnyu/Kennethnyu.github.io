---
title: Parses
toc: false
theme: [dashboard, midnight]
---


```js
var allData = await FileAttachment("./data/parse_aegirg1.json").csv({"typed":true});
allData.push(...await FileAttachment ("./data/parse_aegirg2.json").csv({"typed": true}));
allData.push(...await FileAttachment ("./data/parse_argeos.json").csv({"typed": true}));
allData.push(...await FileAttachment ("./data/parse_behemothg1.json").csv({"typed": true}));
allData.push(...await FileAttachment ("./data/parse_behemothg2.json").csv({"typed": true}));
allData.push(...await FileAttachment ("./data/parse_echidnag1.json").csv({"typed": true}));
allData.push(...await FileAttachment ("./data/parse_echidnag2.json").csv({"typed": true}));
allData.push(...await FileAttachment ("./data/parse_thaemineg1.json").csv({"typed": true}));
allData.push(...await FileAttachment ("./data/parse_thaemineg2.json").csv({"typed": true}));
allData.push(...await FileAttachment ("./data/parse_thaemineg3.json").csv({"typed": true}));
allData.push(...await FileAttachment ("./data/parse_thaemineg4.json").csv({"typed": true}));
allData.push(...await FileAttachment ("./data/parse_veskal.json").csv({"typed": true}));
allData.push(...await FileAttachment ("./data/parse_ivoryg1.json").csv({"typed": true}));
allData.push(...await FileAttachment ("./data/parse_ivoryg2.json").csv({"typed": true}));
allData.push(...await FileAttachment ("./data/parse_ivoryg4.json").csv({"typed": true}));
allData.push(...await FileAttachment ("./data/parse_gargadeth.json").csv({"typed": true}));
```


<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-95BF1EHTG5"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-95BF1EHTG5');
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

<div>
  <div class="card" style="display: flex;flex-direction: column; align-items: center; justify-content: center;">${search}</div>
</div>

<div>
  <div class="card" style="display: flex;flex-direction: column; align-items: center; justify-content: center; font-weight: bolder; text-align: center;">Score DOES NOT account neither gearscore nor arkpassive. It is just your dps relative to others in that fight and spec.<br>
    If you want to be added here, you can dm kennethnyu on discord with screenshot of your roster to proof it indeed your character.<br>
    Replace the character name and region with yours.<br>
  "Character1 - NAE", "Character2 - NAE", "Character3 - NAE", "Character4 - NAE", "Character5 - NAE", "Character6 - NAE"</div>
</div>


```js
if (searchedData) {
  display(searchedTable)
}
```


```js

const urlstring = new URLSearchParams(window.location.search);
const searchparams = urlstring.get("searchparams");
 
const search = Inputs.search(allData, 
{
  "placeholder": "Enter character name here",
  "query": searchparams,
  "autocomplete": "on"
}
);

const searchedData = Generators.input(search);

```

```js

function gradeNum(q90,q80,q70,q60,q50,q40,q30,q20,q10) {
  return (x) => 
  x >= q90
  ? htl.html`<div style="color: #57BB8A;">${x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}`
  : x >= q80
  ? htl.html`<div style="color: #7DC899;">${x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}`
  : x >= q70
  ? htl.html`<div style="color: #A2D4A8;">${x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}`
  : x >= q60
  ? htl.html`<div style="color: #C8E0B7;">${x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}`
  : x >= q50
  ? htl.html`<div style="color: #EDECC5;">${x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}`
  : x >= q40
  ? htl.html`<div style="color: #FCE4C2;">${x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}`
  : x >= q30
  ? htl.html`<div style="color: #F6CAAE;">${x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}`
  : x >= q20
  ? htl.html`<div style="color: #F1B09A;">${x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}`
  : x >= q10
  ? htl.html`<div style="color: #EB9686;">${x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}`
// Under q10
  : htl.html`<div style="color: #E67C73;">${x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}`
}

const char_format = (d, i, data) =>
htl.html`<div style="text-align: center; color: #96e398;"><a href="/player_summaries?searchparams=${d}" target="_blank">
${d}
</a></div>`

const spec_to_color_dict={"Berserker Technique":"#EE2E48","Mayhem":"#EE2E48",
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
const spec_format = (d, i, data) =>
htl.html`<div style="text-align: center; color: ${spec_to_color_dict[d]};">${d}</div>`

const raidId_format = (d, i, data) =>
htl.html`<div style="text-align: center; color: #96e398;"><a href="https://logs.snow.xyz/logs/${d}" target="_blank">
${d.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}
</a></div>`

const arkPsvActv_format = (d, i, data) =>
data[i].arkPsvActv=="On" // Dead
? htl.html`<div style="text-align: center; color: #96e398;">${d}</div>`
// Else white
: htl.html`<div style="text-align: center; color: #ffffff;">${d}</div>`

const isDead_format = (d, i, data) =>
data[i].isDead==1 // Dead
? htl.html`<div style="text-align: center; color: #ff8585;">${d}</div>`
// Else white
: htl.html`<div style="text-align: center; color: #ffffff;">${d}</div>`

const score_format = (d, i, data) =>
data[i].score>=100 // Legendary
? htl.html`<div style="color: #e5cc80;">${d}</div>`
: (data[i].score>=99) // Pink
? htl.html`<div style="color: #e268a8;">${d}</div>`
: (data[i].score>=95) // Orange
? htl.html`<div style="color: #ff8000;">${d}</div>`
: (data[i].score>=75) // Purple
? htl.html`<div style="color: #a335ee;">${d}</div>`
: (data[i].score>=50) // Blue
? htl.html`<div style="color: #0070ff;">${d}</div>`
: (data[i].score>=25) // Green
? htl.html`<div style="color: #1eff00;">${d}</div>`
// Else white
: htl.html`<div style="color: #ffffff;">${d}</div>`

const searchedTable = Inputs.table(searchedData, 
{
  columns: [
    "char","spec","boss","difficulty","dps","gearScore","arkPsvActv","isDead","serverdate","score","raidId"
    ],
  header: {
    "char":"Character",
    "spec":"Spec",
    "boss":"Boss",
    "difficulty":"Difficulty",
    "dps":"DPS",
    "gearScore":"GS",
    "arkPsvActv":"Ark Passive",
    "isDead":"Dead",
    "serverdate":"Date",
    "score":"Parse",
    "raidId":"Raid ID",
  },
  align: {
    char: "center",
    spec: "center",
    boss: "center",
    difficulty: "center",
    dps: "center",
    gearscore: "center",
    arkPsvActv: "center",
    isDead: "center",
    serverdate: "center",
    score: "center",
    raidId: "center",
  },
  width: {
    char: 130,
    spec: 170,
    boss: 170,
    difficulty: 60,
    dps: 110,
    gearscore: 60,
    arkPsvActv: 80,
    isDead: 40,
    serverdate: 70,
    score: 60,
    raidId: 60,
  },
  sort: "serverdate",
  reverse: true,
  format: {
    char: char_format,
    spec: spec_format,
    dps: gradeNum(
      d3.quantile(searchedData, 0.90, (d) => d.dps),
      d3.quantile(searchedData, 0.80, (d) => d.dps),
      d3.quantile(searchedData, 0.70, (d) => d.dps),
      d3.quantile(searchedData, 0.60, (d) => d.dps),
      d3.quantile(searchedData, 0.50, (d) => d.dps),
      d3.quantile(searchedData, 0.40, (d) => d.dps),
      d3.quantile(searchedData, 0.30, (d) => d.dps),
      d3.quantile(searchedData, 0.20, (d) => d.dps),
      d3.quantile(searchedData, 0.10, (d) => d.dps)
      ),
    gearscore: gradeNum(
      d3.quantile(searchedData, 0.90, (d) => d.gearscore),
      d3.quantile(searchedData, 0.80, (d) => d.gearscore),
      d3.quantile(searchedData, 0.70, (d) => d.gearscore),
      d3.quantile(searchedData, 0.60, (d) => d.gearscore),
      d3.quantile(searchedData, 0.50, (d) => d.gearscore),
      d3.quantile(searchedData, 0.40, (d) => d.gearscore),
      d3.quantile(searchedData, 0.30, (d) => d.gearscore),
      d3.quantile(searchedData, 0.20, (d) => d.gearscore),
      d3.quantile(searchedData, 0.10, (d) => d.gearscore)
      ),
    arkPsvActv: arkPsvActv_format,
    isDead: isDead_format,
    score: score_format,
    raidId: raidId_format,
  },
  rows: 26,
})
```

