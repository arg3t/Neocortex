---
title: Welcome!
date: 2021-11-16T21:07:41+01:00
---
# Welcome!

This is an online version of my zettelkasten. I use Obsidian to edit my notes
on my ipad and laptop and use DroneCI's continous integration through gitea to
keep this website up-to-date. 

Since this is Zettelkasten, it should mostly be
made of small notes and a bunch of "random" and "disconnected" knowledge, ideas
and thoughts. If you find it confusing, don't worry, stay calm and read the book
[How to Take Smart
Notes](https://www.amazon.com/How-Take-Smart-Notes-Nonfiction-ebook/dp/B06WVYW33Y)
by Sönke Ahrens.

%%
struct_eval_start
%%
```py
from datetime import datetime, MINYEAR
from dateutil import tz
mintime=datetime(MINYEAR, 1, 1, tzinfo=tz.gettz('Europe/Amsterdam'))
print(zettel.select("date", limit=10, default=mintime))
```
%%
struct_eval_end
%%

Content continues here









