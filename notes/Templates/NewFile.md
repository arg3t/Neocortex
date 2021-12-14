<%*
  let title = tp.file.title
  if (title.startsWith("Untitled")) {
    title = await tp.system.prompt("Title");
    await tp.file.rename(`${title}`);
  } 
  tR += "---"
%>
title:  <%* tR += `${title}` %>
date: <% tp.date.now("YY-MM-DDThh:mm:ss.sTZD") %>
created: <% tp.date.now("YY-MM-DDThh:mm:ss.sTZD") %>
modified: <% tp.date.now("YY-MM-DDThh:mm:ss.sTZD") %>
description: 
tags: ['']
aliases: ['']
---
# <%* tR += `${title}` %>