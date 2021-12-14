---
title:  University Structure Note
date:  2021-12-14T17:24:37+01:00
---

## 🎓 University Notes 
This section has my notes for my academic journey. The folders are structured such that each course is in its specific directory. Here are a list of courses that I have notes for:

```dataview
LIST WITHOUT ID "[" + title + "]" + "(<" + file.path + ">)" FROM "TUDelft" WHERE file.name = "index" AND file.folder != "TUDelft" FLATTEN file.folder
```

### ✍️ Notes Created Last Week 
```dataview
LIST WITHOUT ID file.link + " : " + default(description, "No description available") FROM "TUDelft" WHERE default(modified, default(created, date)) > date(today) - dur(7 d) SORT default(modified, default(created, date)) LIMIT 10
```

### 📈 Tags with the most notes


### 🕸 Notes with the most backlinks

