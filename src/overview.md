---
title: Overview
toc: false
theme: [dashboard, midnight]
---


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

  .dropbtn {
    background-color: #3B3B3B;
    color: white;
    margin:1px;
    border-color-bottom: #858585;
    border-bottom-left-radius: 0;
    border-color-left: #858585;
    border-top-left-radius: 0;
    border-color-top: #858585;
    border-top-right-radius: 0;
    border-color-right: #858585;
    border-bottom-right-radius: 0;
  }

  .dropdown {
    position: relative;
    display: inline-block;
  }

  .dropdown-content {
    display: none;
    position: absolute;
    background-color: #f1f1f1;
    min-width: 160px;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
  }

  .dropdown-content a {
    color: black;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
  }

  .dropdown-content a:hover {background-color: #ddd;}

  .dropdown:hover .dropdown-content {display: block;}

  .dropdown:hover .dropbtn {background-color: #3e8e41;}

</style>

<div style="display: flex; flex-direction: row; align-items: center; justify-content: center;" id="observablehq-header">

  <div>${classSelect}</div>
  <div>-</div>
  <div>${sortSelect}</div>
  <div>-</div>
  <div>${arkPassiveSelect}</div>
  <div>-</div>
  <div>
    <form class="inputs-3a86ea" style="--input-width: 100%;">
      <select class="inputs-3a86ea-input" name="input" onchange="location = this.value;">
        <option value="#id_aegirg1hm">Jump to Aegir Hard</option>
        <option value="#id_aegirg1nm">Jump to Aegir Normal</option>
        <option value="#id_argeos_1680_1740">Jump to Argeos</option>
        <option value="#id_behemothg1nm">Jump to Behemoth Normal</option>
        <option value="#id_echidnag1hm">Jump to Echidna Hard</option>
        <option value="#id_echidnag1nm">Jump to Echidna Normal</option>
        <option value="#id_thaemineg1hm">Jump to Thaemine Hard</option>
        <option value="#id_thaemineg1nm">Jump to Thaemine Normal</option>
        <option value="#id_veskal">Jump to Veskal</option>
        <option value="#id_ivoryg1hm">Jump to Ivory Hard</option>
        <option value="#id_ivoryg1nm">Jump to Ivory Normal</option>
        <option value="#id_gargardeth">Jump to Gargadeth</option>
      </select>
    </form>
  </div>
</div>



```js
const describe = await FileAttachment("./data/data_AegirG1_01.json").csv({"typed": true});
describe.push(...await FileAttachment ("./data/data_AegirG1_02.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_AegirG1_03.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_AegirG1_04.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_AegirG1_05.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_AegirG1_06.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_AegirG1_07.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_AegirG1_08.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_AegirG1_09.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_AegirG1_10.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_AegirG2_01.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_AegirG2_02.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_AegirG2_03.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_AegirG2_04.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_AegirG2_05.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_AegirG2_06.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_AegirG2_07.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_AegirG2_08.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_AegirG2_09.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_AegirG2_10.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_Argeos_01.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_Argeos_02.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_Argeos_03.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_Argeos_04.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_Argeos_05.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_Argeos_06.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_Argeos_07.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_Argeos_08.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_Argeos_09.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_Argeos_10.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_BehemothG1_01.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_BehemothG1_02.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_BehemothG1_03.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_BehemothG1_04.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_BehemothG1_05.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_BehemothG1_06.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_BehemothG1_07.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_BehemothG1_08.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_BehemothG1_09.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_BehemothG1_10.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_BehemothG2_01.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_BehemothG2_02.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_BehemothG2_03.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_BehemothG2_04.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_BehemothG2_05.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_BehemothG2_06.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_BehemothG2_07.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_BehemothG2_08.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_BehemothG2_09.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_BehemothG2_10.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_EchidnaG1_01.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_EchidnaG1_02.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_EchidnaG1_03.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_EchidnaG1_04.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_EchidnaG1_05.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_EchidnaG1_06.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_EchidnaG1_07.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_EchidnaG1_08.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_EchidnaG1_09.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_EchidnaG1_10.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_EchidnaG2_01.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_EchidnaG2_02.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_EchidnaG2_03.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_EchidnaG2_04.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_EchidnaG2_05.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_EchidnaG2_06.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_EchidnaG2_07.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_EchidnaG2_08.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_EchidnaG2_09.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_EchidnaG2_10.json").csv({"typed": true}));
// describe.push(...await FileAttachment ("./data/data_thaemineg1.json").csv({"typed": true}));
// describe.push(...await FileAttachment ("./data/data_thaemineg2.json").csv({"typed": true}));
// describe.push(...await FileAttachment ("./data/data_thaemineg3.json").csv({"typed": true}));
describe.push(...await FileAttachment ("./data/data_thaemineg4.json").csv({"typed": true}));
// describe.push(...await FileAttachment ("./data/data_veskal.json").csv({"typed": true}));
// describe.push(...await FileAttachment ("./data/data_ivoryg1.json").csv({"typed": true}));
// describe.push(...await FileAttachment ("./data/data_ivoryg2.json").csv({"typed": true}));
// describe.push(...await FileAttachment ("./data/data_ivoryg4.json").csv({"typed": true}));
// describe.push(...await FileAttachment ("./data/data_gargadeth.json").csv({"typed": true}));


const aegirg1hm = await FileAttachment("./data/cards/AegirG1HM.png").href;
const aegirg2hm = await FileAttachment("./data/cards/AegirG2HM.png").href;
const aegirg1nm = await FileAttachment("./data/cards/AegirG1NM.png").href;
const aegirg2nm = await FileAttachment("./data/cards/AegirG2NM.png").href;
const argeos = await FileAttachment("./data/cards/Argeos.png").href;
const behemothg1nm = await FileAttachment("./data/cards/BehemothG1NM.png").href;
const behemothg2nm = await FileAttachment("./data/cards/BehemothG2NM.png").href;
const echidnag1hm = await FileAttachment("./data/cards/EchidnaG1HM.png").href;
const echidnag2hm = await FileAttachment("./data/cards/EchidnaG2HM.png").href;
const echidnag1nm = await FileAttachment("./data/cards/EchidnaG1NM.png").href;
const echidnag2nm = await FileAttachment("./data/cards/EchidnaG2NM.png").href;
const thaemineg1hm = await FileAttachment("./data/cards/ThaemineG1HM.png").href;
const thaemineg2hm = await FileAttachment("./data/cards/ThaemineG2HM.png").href;
const thaemineg3hm = await FileAttachment("./data/cards/ThaemineG3HM.png").href;  
const thaemineg4hm = await FileAttachment("./data/cards/ThaemineG4HM.png").href;
const thaemineg1nm = await FileAttachment("./data/cards/ThaemineG1NM.png").href;
const thaemineg2nm = await FileAttachment("./data/cards/ThaemineG2NM.png").href;
const thaemineg3nm = await FileAttachment("./data/cards/ThaemineG3NM.png").href;
const veskal = await FileAttachment("./data/cards/Veskal.png").href;
const ivoryg1hm = await FileAttachment("./data/cards/IvoryG1HM.png").href;
const ivoryg2hm = await FileAttachment("./data/cards/IvoryG2HM.png").href;
const ivoryg3hm = await FileAttachment("./data/cards/IvoryG3HM.png").href;
const ivoryg1nm = await FileAttachment("./data/cards/IvoryG1NM.png").href;
const ivoryg2nm = await FileAttachment("./data/cards/IvoryG2NM.png").href;
const ivoryg3nm = await FileAttachment("./data/cards/IvoryG3NM.png").href;
const gargadeth = await FileAttachment("./data/cards/Gargadeth.png").href;
```

```js queryString processor
const urlParams = new URLSearchParams(window.location.search);
```

```js
const sortSelect = Inputs.select(
  new Map([
    ["Sort By Floor", "q01"],
    ["Sort By Q25", "q25"],
    ["Sort By Median", "median"],
    ["Sort By Q75", "q75"],
    ["Sort By Ceiling", "q99"],
    ]),
  {
    value: urlParams.get("sort") ? urlParams.get("sort") : "median",
    label: "",
    width: "100%"
  }
  );
const selectedSort = Generators.input(sortSelect);

const classSelect = Inputs.select(
  new Map([
    ["Class Highlight: Arthetinean Skill", "Arthetinean Skill"],
    ["Class Highlight: Asura's Path", "Asura's Path"],
    ["Class Highlight: Barrage Enhancement", "Barrage Enhancement"],
    ["Class Highlight: Berserker Technique", "Berserker Technique"],
    ["Class Highlight: Brawl King Storm", "Brawl King Storm"],
    ["Class Highlight: Combat Readiness", "Combat Readiness"],
    ["Class Highlight: Communication Overflow", "Communication Overflow"],
    ["Class Highlight: Control", "Control"],
    ["Class Highlight: Death Strike", "Death Strike"],
    ["Class Highlight: Deathblow", "Deathblow"],
    ["Class Highlight: Demonic Impulse", "Demonic Impulse"],
    ["Class Highlight: Drizzle", "Drizzle"],
    ["Class Highlight: Energy Overflow", "Energy Overflow"],
    ["Class Highlight: Enhanced Weapon", "Enhanced Weapon"],
    ["Class Highlight: Esoteric Flurry", "Esoteric Flurry"],
    ["Class Highlight: Esoteric Skill Enhancement", "Esoteric Skill Enhancement"],
    ["Class Highlight: Evolutionary Legacy", "Evolutionary Legacy"],
    ["Class Highlight: Firepower Enhancement", "Firepower Enhancement"],
    ["Class Highlight: First Intention", "First Intention"],
    ["Class Highlight: Full Moon Harvester", "Full Moon Harvester"],
    ["Class Highlight: Grace of the Empress", "Grace of the Empress"],
    ["Class Highlight: Gravity Training", "Gravity Training"],
    ["Class Highlight: Hunger", "Hunger"],
    ["Class Highlight: Igniter", "Igniter"],
    ["Class Highlight: Lone Knight", "Lone Knight"],
    ["Class Highlight: Loyal Companion", "Loyal Companion"],
    ["Class Highlight: Lunar Voice", "Lunar Voice"],
    ["Class Highlight: Master Summoner", "Master Summoner"],
    ["Class Highlight: Mayhem", "Mayhem"],
    ["Class Highlight: Night's Edge", "Night's Edge"],
    ["Class Highlight: Order of the Emperor", "Order of the Emperor"],
    ["Class Highlight: Peacemaker", "Peacemaker"],
    ["Class Highlight: Perfect Suppression", "Perfect Suppression"],
    ["Class Highlight: Pinnacle", "Pinnacle"],
    ["Class Highlight: Pistoleer", "Pistoleer"],
    ["Class Highlight: Predator", "Predator"],
    ["Class Highlight: Princess Maker", "Princess Maker"],
    ["Class Highlight: Punisher", "Punisher"],
    ["Class Highlight: Rage Hammer", "Rage Hammer"],
    ["Class Highlight: Reflux", "Reflux"],
    ["Class Highlight: Remaining Energy", "Remaining Energy"],
    ["Class Highlight: Robust Spirit", "Robust Spirit"],
    ["Class Highlight: Shock Training", "Shock Training"],
    ["Class Highlight: Surge", "Surge"],
    ["Class Highlight: Time to Hunt", "Time to Hunt"],
    ["Class Highlight: Ultimate Skill: Taijutsu", "Ultimate Skill: Taijutsu"],
    ["Class Highlight: Wind Fury", "Wind Fury"],
    ]),
  {
    value: urlParams.get("highlight") ? urlParams.get("highlight") : "Peacemaker",
    label: "",
    width: "100%"
  }
  );
const classHighlight = Generators.input(classSelect);

const arkPassiveSelect = Inputs.select(
  new Map([
    ["All Data (ArkPassiveFilter)", "All"],
    ["Ark Passive Active", "On"],
    ["No Ark Passive", "Off"],
    ]),
  {
    value: urlParams.get("arkPassive") ? urlParams.get("arkPassive") : 1,
    label: "",
    width: "100%"
  }
  );
const arkPassiveStatus = Generators.input(arkPassiveSelect);

const encounterSelect = Inputs.select(
  new Map([
    ["Jump to Aegir G1 HM", "id_aegirg1hm"],
    ["Sort By Q25", "q25"],
    ["Sort By Median", "median"],
    ["Sort By Q75", "q75"],
    ["Sort By Ceiling", "q99"],
    ]),
  {
    value: urlParams.get("encounter") ? urlParams.get("encounter") : "AegirG1HM",
    label: "",
    width: "100%",
    onchange: "location = this.value"
  }
  );
  ```

  <div style="display:flex;flex-direction:column;align-items:center;justify-content:centers;">
    <div class="card" id="id_aegirg1hm">${chartGraph("Akkan, Lord of Death","Hard",1680,1740,aegirg1hm,{classHighlight},{arkPassiveStatus},{width})}</div>
    <div class="card" id="id_aegirg2hm">${chartGraph("Aegir, the Oppressor","Hard",1680,1740,aegirg2hm,{classHighlight},{arkPassiveStatus},{width})}</div>
    <div class="card" id="id_aegirg1nm">${chartGraph("Akkan, Lord of Death","Normal",1660,1680,aegirg1nm,{classHighlight},{arkPassiveStatus},{width})}</div>
    <div class="card" id="id_aegirg2nm">${chartGraph("Aegir, the Oppressor","Normal",1660,1680,aegirg2nm,{classHighlight},{arkPassiveStatus},{width})}</div>
    <div class="card" id="id_argeos_1680_1740">${chartGraph("Argeos","Normal",1680,1740,argeos,{classHighlight},{arkPassiveStatus},{width})}</div>
    <div class="card" id="id_argeos_1640_1679">${chartGraph("Argeos","Normal",1640,1679,argeos,{classHighlight},{arkPassiveStatus},{width})}</div>
    <div class="card" id="id_behemothg1nm">${chartGraph("Behemoth, the Storm Commander","Normal",1680,1740,behemothg1nm,{classHighlight},{arkPassiveStatus},{width})}</div>
    <div class="card" id="id_behemothg2nm">${chartGraph("Behemoth, Cruel Storm Slayer","Normal",1680,1740,behemothg2nm,{classHighlight},{arkPassiveStatus},{width})}</div>
    <div class="card" id="id_behemothg1nm">${chartGraph("Behemoth, the Storm Commander","Normal",1620,1680,behemothg1nm,{classHighlight},{arkPassiveStatus},{width})}</div>
    <div class="card" id="id_behemothg2nm">${chartGraph("Behemoth, Cruel Storm Slayer","Normal",1620,1680,behemothg2nm,{classHighlight},{arkPassiveStatus},{width})}</div>
    <div class="card" id="id_echidnag1hm">${chartGraph("Red Doom Narkiel","Hard",1630,1680,echidnag1hm,{classHighlight},{arkPassiveStatus},{width})}</div>
    <div class="card" id="id_echidnag2hm">${chartGraph("Covetous Master Echidna","Hard",1630,1680,echidnag2hm,{classHighlight},{arkPassiveStatus},{width})}</div>
    <div class="card" id="id_echidnag1nm">${chartGraph("Red Doom Narkiel","Normal",1620,1640,echidnag1nm,{classHighlight},{arkPassiveStatus},{width})}</div>
    <div class="card" id="id_echidnag2nm">${chartGraph("Covetous Master Echidna","Normal",1620,1640,echidnag2nm,{classHighlight},{arkPassiveStatus},{width})}</div>
    <!-- <div class="card" id="id_thaemineg1hm">${chartGraph("Killineza the Dark Worshipper","Hard",1630,1740,thaemineg1hm,{classHighlight},{arkPassiveStatus},{width})}</div> -->
    <!-- <div class="card" id="id_thaemineg2hm">${chartGraph("Valinak, Herald of the End","Hard",1630,1740,thaemineg2hm,{classHighlight},{arkPassiveStatus},{width})}</div> -->
    <!-- <div class="card" id="id_thaemineg3hm">${chartGraph("Thaemine the Lightqueller","Hard",1630,1740,thaemineg3hm,{classHighlight},{arkPassiveStatus},{width})}</div> -->
    <div class="card" id="id_thaemineg4hm">${chartGraph("Thaemine, Conqueror of Stars","Hard",1610,1650,thaemineg4hm,{classHighlight},{arkPassiveStatus},{width})}</div>
    <!-- <div class="card" id="id_thaemineg1nm">${chartGraph("Killineza the Dark Worshipper","Normal",1610,1650,thaemineg1nm,{classHighlight},{arkPassiveStatus},{width})}</div> -->
    <!-- <div class="card" id="id_thaemineg2nm">${chartGraph("Valinak, Herald of the End","Normal",1610,1650,thaemineg2nm,{classHighlight},{arkPassiveStatus},{width})}</div> -->
    <!-- <div class="card" id="id_thaemineg3nm">${chartGraph("Thaemine the Lightqueller","Normal",1610,1650,thaemineg3nm,{classHighlight},{arkPassiveStatus},{width})}</div> -->
    <!-- <div class="card" id="id_veskal">${chartGraph("Veskal","Normal",1630,1740,veskal,{classHighlight},{arkPassiveStatus},{width})}</div> -->
    <!-- <div class="card" id="id_ivoryg1hm">${chartGraph("Kaltaya, the Blooming Chaos","Hard",1620,1740,ivoryg1hm,{classHighlight},{arkPassiveStatus},{width})}</div> -->
    <!-- <div class="card" id="id_ivoryg2hm">${chartGraph("Rakathus, the Lurking Arrogance","Hard",1620,1740,ivoryg2hm,{classHighlight},{arkPassiveStatus},{width})}</div> -->
    <!-- <div class="card" id="id_ivoryg3hm">${chartGraph("Lazaram, the Trailblazer","Hard",1620,1740,ivoryg3hm,{classHighlight},{arkPassiveStatus},{width})}</div> -->
    <!-- <div class="card" id="id_ivoryg1nm">${chartGraph("Kaltaya, the Blooming Chaos","Normal",1600,1650,ivoryg1nm,{classHighlight},{arkPassiveStatus},{width})}</div> -->
    <!-- <div class="card" id="id_ivoryg2nm">${chartGraph("Rakathus, the Lurking Arrogance","Normal",1600,1650,ivoryg2nm,{classHighlight},{arkPassiveStatus},{width})}</div> -->
    <!-- <div class="card" id="id_ivoryg3nm">${chartGraph("Lazaram, the Trailblazer","Normal",1600,1650,ivoryg3nm,{classHighlight},{arkPassiveStatus},{width})}</div> -->
    <!-- <div class="card" id="id_gargardeth">${chartGraph("Gargadeth","Normal",1610,1650,gargadeth,{classHighlight},{arkPassiveStatus},{width})}</div> -->
  </div>


  ```js Chart Graph
  function chartGraph(name, difficulty, minilevel, maxilevel, cardname, classHighlight, arkPassiveStatus, {width} = {}) {

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
    "Asura's Path":"#4DE3D1","Brawl King Storm":"#4DE3D1"
    ,               "Remaining Energy":"#A91A16","Surge":"#A91A16",
    "Demonic Impulse":"#0099C6","Perfect Suppression":"#0099C6",
    "Hunger":"#109618","Lunar Voice":"#109618",
    "Full Moon Harvester":"#C16ED0","Night's Edge":"#C16ED0",
    "Death Strike":"#DD4477","Loyal Companion":"#DD4477",
    "Enhanced Weapon":"#4442A8","Pistoleer":"#4442A8",
    "Barrage Enhancement":"#33670B","Firepower Enhancement":"#33670B",
    "Arthetinean Skill":"#3B4292","Evolutionary Legacy":"#3B4292",
    "Peacemaker":"#6BCEC2","Time to Hunt":"#6BCEC2",
    "Drizzle":"#084BA3","Wind Fury":"#084BA3"};

    const plotHeight = 650;
    const margins = { top: 10, right: 10, bottom: 10, left: 10 };
    const xAxisHeight = 50;
    const yAxisWidth = 250;
    const minWidth = 550;
    const height = plotHeight + margins.top + margins.bottom + xAxisHeight;

    const arkPassivesValue = arkPassiveStatus["arkPassiveStatus"]

    const data = aq.from(describe)
    .filter(aq.escape((d) => d.boss == name && d.difficulty == difficulty))
    .filter(aq.escape((d) => d.gearScore >= minilevel && d.gearScore <= maxilevel))
    .filter(aq.escape((d) => (arkPassivesValue != "All" ? d.arkPsvActv == arkPassivesValue : true)))

    const logsCount = data.numRows();
    const idRecent = d3.max(data.array("raidId"));

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
    .orderby(selectedSort)
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

    const finalData = Generators.input(summaryTable);

// Create a new dictionary where spec is the key and color is the value
    const specColorDict = summary.objects().reduce((acc, curr) => {
acc[curr.spec] = spec_to_color[curr.spec]; // Set spec as the key and color as the value
return acc;
}, {});

    const spec_to_specCount = summary.objects().reduce((acc, curr) => {
acc[curr.spec] = curr.specCount; // Set spec as the key and color as the value
return acc;
}, {});

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

    const specHighlight = classHighlight["classHighlight"];

    if(classHighlight!="") {
// Add Class Highlight
      g.append("rect")
      .attr("fill", "var(--theme-foreground-muted)")
      .attr("opacity", "0.01")
      .attr("class", "specificHighlight")
      .attr("pointer-events", "none")
      .attr("x", xScale.range()[0] - yAxisWidth + 25)
      .attr("y", yScale(spec_to_specCount[specHighlight]))
      .attr("width", xScale.range()[1] - xScale.range()[0] + yAxisWidth - 25)
      .attr("height", yScale.bandwidth());
    }

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

    var xAxisGroup = svg
    .append("g")
    .attr("visibility", width > minWidth ? "visible" : "hidden")
    .attr("transform", `translate(0, ${height - margins.bottom - xAxisHeight})`)
    .attr("pointer-events", "none")
    .call(xAxis);

    xAxisGroup
    .selectAll("text")
    .attr("font-size", "14px")
    .attr("visibility", "visible");

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
    .attr("font-size", "24px")
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

    yAxisGroup
    .selectAll("line")
    .style( "stroke", function(d)    {
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
        <div style="display: flex; align-items: center; justify-content: center;">Rank ${summary.objects().length-summary.array("spec").indexOf(d.spec)}/${
          summary.objects().length
        }</div>
        <div style="display: flex; align-items: center; justify-content: center;">${d.specCount.split(" (")[0]}</div>
        <div style="display: flex; align-items: center; justify-content: center;">${d.specCount.split(" (")[1].replace(")", "")} logs</div>
        <br/>
        <div style="display: flex; align-items: center; justify-content: center;">Worst: ${d3.format(".3s")(d.min)}</div>
        <div style="display: flex; align-items: center; justify-content: center;">Floor: ${d3.format(".3s")(d.q01)}</div>
        <div style="display: flex; align-items: center; justify-content: center;">Q1: ${d3.format(".3s")(d.q25)}</div>
        <div style="display: flex; align-items: center; justify-content: center;">Median: ${d3.format(".3s")(d.median)}</div>
        <div style="display: flex; align-items: center; justify-content: center;">Q3: ${d3.format(".3s")(d.q75)}</div>
        <div style="display: flex; align-items: center; justify-content: center;">Ceiling: ${d3.format(".3s")(d.q99)}</div>
        <div style="display: flex; align-items: center; justify-content: center;">Best: ${d3.format(".3s")(d.max)}</div>
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
        <div>${d3.format(".3s")(d.max)} DPS</div>
        <div>GS: ${
        data
        .filter(
          aq.escape(
            (log) => log.dps == d.max && log.spec === d.spec
            )
          )
        .array("gearScore")[0]
      }</div>
        <div>https://logs.snow.xyz/logs/${
        data
        .filter(
          aq.escape(
            (log) => log.dps == d.max && log.spec === d.spec
            )
          )
        .array("raidId")[0]
      }</div>
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
      console.log(`https://logs.snow.xyz/logs/${
        data
        .filter(
          aq.escape(
            (log) => log.dps == d.max && log.spec === d.spec
            )
          )
        .array("raidId")[0]
      }`)
      window.open(
        `https://logs.snow.xyz/logs/${
          data
          .filter(
            aq.escape(
              (log) => log.dps == d.max && log.spec === d.spec
              )
            )
          .array("raidId")[0]
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
      `translate(${width-(83/2)}, 140)`
      )
    .attr("text-anchor", "middle")
    .attr("font-family", "var(--sans-serif)")
    .attr("font-size", "12px")
    .attr("fill", "var(--theme-foreground)")
    .text(`Data: ${logsCount.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}`);

    svg
    .append("text")
    .attr(
      "transform",
      `translate(${width-(83/2)}, 155)`
      )
    .attr("text-anchor", "middle")
    .attr("font-family", "var(--sans-serif)")
    .attr("font-size", "12px")
    .attr("fill", "var(--theme-foreground)")
    .text(`${minilevel}-${maxilevel}`);

    svg
    .append("text")
    .attr(
      "transform",
      `translate(${width-(83/2)}, 170)`
      )
    .attr("text-anchor", "middle")
    .attr("font-family", "var(--sans-serif)")
    .attr("font-size", "12px")
    .attr("fill", "var(--theme-foreground)")
    .text(`Latest Raid ID:`);

    svg
    .append("text")
    .attr(
      "transform",
      `translate(${width-(83/2)}, 185)`
      )
    .attr("text-anchor", "middle")
    .attr("font-family", "var(--sans-serif)")
    .attr("font-size", "12px")
    .attr("fill", "var(--theme-foreground)")
    .text(`${idRecent.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}`);


    svg.append("svg:image")
    .attr("href", `${cardname}`)
    .attr("x", width-83)
    .attr("width", "83px")
    .attr("height", "120px")


    return display(svg.node())


  }


  ```

