---
title:  Taking Notes With Obsidian
date: 2022-06-20T07:58:36+02:00
description: 
tags: ['obsidian']
aliases: ['']
---

I use [Obsidian](https://obsidian.md/) to take notes and publish them using [GitHub Pages](https://pages.github.com/) and [Quartz](https://github.com/jackyzha0/quartz)(It's very cool, you should check it out.). 

## Obsidian
I use plugins to make my note-taking experience much smoother. Here is a list:

- [Admonition](https://github.com/valentine195/obsidian-admonition) Adds support for blocks I can use for emphasis or anything
- [Checklist](https://github.com/delashum/obsidian-checklist-plugin) Helps me manage the todos I have created in a central location
- [Cycle Through Panes](https://github.com/phibr0/cycle-through-panes) Pretty self-explanatory
- [Linter](https://github.com/platers/obsidian-linter) Makes sure that my markdown is *pretty*.
- [Vale](https://github.com/marcusolsson/obsidian-vale) I am a terrible so something that checks my spelling and wording is a must
- [Templater](https://github.com/SilentVoid13/Templater) This allows me to insert snippets into notes so that initializing new nodes is as simple as pressing a hotkey
- [Meld Encrypt](https://github.com/meld-cp/obsidian-encrypt) This plugin's encryption capabilities are priceless when I am taking personal notes
- [Obsidian Gnuplot](https://github.com/theFr1nge/obsidian-gnuplot) (written by me). This allows me to plot mathematical functions within obsidian.

## Quartz
In order to make quartz work with my setup, I had to make changes but now I can write notes in obsidian without worrying about whether I will be able to publish them. If you ever decide to implement my workflow, I strongly suggest building off-of my note-taking repository instead of using the default quartz one.

## The way I take notes
When studying, I create notes for each new concept, idea or terminology that I run into and link to that note whenever it is being referred in one of my notes. It is not really a Zettelkasten, but not a wiki either. Maybe a ZettelWiki, or a WikiKasten (name is a WIP). 

### Custom Shortcodes

#### Plots
My edits allows you to draw plots. For instance, the following codeblock:

````md
```plot
size: 350em
plot cos(x)
```
````

Generates the following.
```plot
size: 350em

plot cos(x)
```

You can also create interactive plots where the user can control:

````md
```plotinteractive
size: 350em
plot sin(x)/x
```
````

Generates the following.
```plotinteractive
size: 350em

plot sin(x)/x
```


#### Admonitions
You can also insert admonitions like so

````md
```ad-info
This is an admonition
```
````

```ad-info
This is an admonition
```