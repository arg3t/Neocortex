#!/bin/python
#
# excalidrawtosvg.py
# Neocortex
#
# Created by Yigit Colakoglu on 11/16/21.
# Copyright 2021. Yigit Colakoglu. All rights reserved.
#

import os
import re

def findandreplace(directory, query, result, extension, spacereplace=" "):
    reg = re.compile(query)
    for n in os.listdir(directory):
        d = os.path.join(directory, n)
        if os.path.isdir(d):
            findandreplace(d, query, result, extension, spacereplace=spacereplace)
            continue

        if not n.endswith("."+extension):
            continue

        print(d)
        with open(d,"r") as f:
            data = f.read().replace(" ", spacereplace)

        data = reg.sub(result, data)

        with open(d,"w") as f:
            f.write(data)

def main():
    excalidir = "notes/Excalidraw/"
    for n in os.listdir(excalidir):
        with open(os.path.join(excalidir, n), "r") as f:
            lines = f.readlines()

        insvg = False
        svg = ""
        for i in lines:
            if i == '```\n':
                insvg = False
            if insvg:
                svg += i.strip()
            if i == '```html\n':
                insvg = True

        svgname = ".".join(n.split(".")[0:-1]).replace(" ","-") + ".svg"

        with open(os.path.join(excalidir, svgname), "w") as f:
            f.write(svg)

    findandreplace("notes", r"!\[\[(Excalidraw\/Drawing.*).md\]\]", r"![Excalidraw Drawing](/\1.svg)", "md", spacereplace="-")


if __name__ == "__main__":
    main()

