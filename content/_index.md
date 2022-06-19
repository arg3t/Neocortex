---
title: Welcome!
date: 2021-11-16T21:07:41+01:00
---

I am Yigit, a first year Computer Science student at TU Delft. But this site is
not about me, it is about my notes. If you want to learn more about to me, you
can visit my [website](https://yigitcolakoglu.com), or my
[blog](https://fr1nge.xyz).

This website is a published version of my zettelkasten. Here, I keep my notes,
each of which I try to keep atomic. The notes are given tags according to the
topics they are related to and also, most notes either contain links to other
notes are linked to by other notes. These two principles allows structure to
naturally emerge from the flat folder structure that makes the zettelkasten.

I am currently attending university in TU Delft I keep many notes related to
CS, here is some of the recent ones:


```js-block
function genIndex(arr, key, comparator){
	return Array.from(Array(arr.length).keys())
  .sort((a, b) => comparator(arr[a][key], arr[b][key]) < 0 ? -1 : (comparator(arr[b][key],arr[a][key]) < 0) | 0);
}

function regexSearchList(r, l){
	let count = 0;
	for(let i in l){
		if(l[i].search(r) != -1){
			count++;
		}
	}
	return count;
}

function truncateString(str, num) {
  if (str.length > num) {
    return str.slice(0, num) + "...";
  } else {
    return str;
  }
}

function genNoteLinkElement(obj){
	let anchor = document.createElement("a") 
	anchor.setAttribute('href', obj['relPath'])
	anchor.setAttribute('rel', "noopener") 
	anchor.setAttribute('class', "internal-link")
	anchor.setAttribute('data-src', obj['relPath'])
	anchor.innerText = obj['title'];

	return anchor;
}

function genTagList(tags){
	let ul = document.createElement("ul");
	ul.setAttribute("class", "tags inline");
	
	for(let i in tags){
		let t = tags[i];
		let li = document.createElement("li");
		let a = document.createElement("a");
		a.setAttribute("href", `/tags/${t}`);
		a.innerText = t;
		li.appendChild(a);
		ul.appendChild(li);
	}
	return ul;
}


async function run(){
  let encoder = (str) => str.toLowerCase().split(/([^a-z]|[^\x00-\x7F])+/)
  let contentTable = [];

  const { content } = await fetchData;
  for (const [key, value] of Object.entries(content)) {
  	value["relPath"] = key; 
  	contentTable.push(value);
  }
  
  let dateIndex = genIndex(contentTable, 'date', (a,b) => {
  	let d1 = Date.parse(a);
	let d2 = Date.parse(b);
	return (d1 > d2) - (d1 < d2)
  });
  
  dateIndex.reverse();
  
  let count = 0;
  let i = 0;
  
  let ul = document.createElement("ul");
  while (count < 15 && i < dateIndex.length){
  	let note = contentTable[dateIndex[i]];
	if(!note){
		i++;
		continue;
	}
	
	if (regexSearchList("cs/.*", note['tags']) != 0
	      && ! note['tags'].includes('cs/security')){
		count++;
		let el = genNoteLinkElement(note);
		let li = document.createElement('li');
		li.appendChild(el);
		li.appendChild(genTagList(note['tags']));
		ul.appendChild(li);
	}
	
	i++;
  }
	
  if(count > 0){
  	outputDiv.appendChild(ul);
  }
  
  let p = document.createElement("p");
  p.innerText = "Even though they are very crude, I also keep some math-related notes:";
  
  outputDiv.appendChild(p);
	
  
  count = 0;
  i = 0;
  
  ul = document.createElement("ul");
  while (count < 15 && i < dateIndex.length){
  	let note = contentTable[dateIndex[i]];
	if(!note){
		i++;
		continue;
	}
	
	if (regexSearchList("math/.*", note['tags']) != 0){
		count++;
		let el = genNoteLinkElement(note);
		let li = document.createElement('li');
		li.appendChild(el);
		li.appendChild(genTagList(note['tags']));
		ul.appendChild(li);
	}
	
	i++;
  }
	
  if(count > 0){
  	outputDiv.appendChild(ul);
  }
  
   
  p = document.createElement("p");
  p.innerHTML = 'The most chaotic ones are my security notes. <em>"He who enter here abandon all hope."</em>';
  
  outputDiv.appendChild(p);
	
  
  count = 0;
  i = 0;
  
  ul = document.createElement("ul");
  while (count < 15 && i < dateIndex.length){
  	let note = contentTable[dateIndex[i]];
	if(!note){
		i++;
		continue;
	}
	
	if (note['tags'] && note['tags'].includes('cs/security')){
		count++;
		let el = genNoteLinkElement(note);
		let li = document.createElement('li');
		li.appendChild(el);
		li.appendChild(genTagList(note['tags']));
		ul.appendChild(li);
	}
	
	i++;
  }
	
  if(count > 0){
  	outputDiv.appendChild(ul);
  }
}

run();
```
