---
title: Leaderboard
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


<div>
	<div class="card" style="display: flex;flex-direction: column; align-items: center; justify-content: center;">${search}</div>
	<div class="card" style="display: flex;flex-direction: column">${Inputs.table(searchValue, {rows: 26})}</div>
</div>



```js
const lbData = await FileAttachment("./data/leaderboard.json").csv();


```


```js

const search = Inputs.search(lbData, {"placeholder":"Enter blurred name here"});

const searchValue = Generators.input(search);


```




