#!/bin/python
#
# excalidrawtosvg.py
# Neocortex
#
# Created by Yigit Colakoglu on 11/16/21.
# Copyright 2021. Yigit Colakoglu. All rights reserved.
#

import os, sys
import yaml
from functools import total_ordering
from io import StringIO
from contextlib import redirect_stdout

@total_ordering
class MinType(object):
    def __le__(self, other):
        return True

    def __eq__(self, other):
        return (self is other)

class Table:
    def __init__(self, keys, entries):
        self.keys = keys
        self.entries = entries

    def select(self, key, order=False, limit=0, default=MinType()):
        keyindex = self.keys.index(key)
        if limit > 0:
            return sorted(self.entries, key=lambda x: x[keyindex] or default, reverse=order)[0:limit]
        else:
            return sorted(self.entries, key=lambda x: x[keyindex] or default, reverse=order)


IGNORE = [
    "Excalidraw",
    "Images",
    ".obsidian",
    "..gitignore"
]

zettel = None

def markdownmeta(path):
    with open(path, "r") as f:
        md = f.read()

    metadata = {}
    if md.startswith("---"):
        metadata = yaml.safe_load(md.split("---\n")[1])

    metadata["file.folder"] = os.path.dirname(path)
    metadata["file.name"] = os.path.basename(path)
    metadata["file.path"] = path
    metadata["file.mtime"] = os.path.getmtime(path)
    metadata["file.ctime"] = os.path.getctime(path)

    return metadata

def fixSize(arr, size):
    for i in range(len(arr)):
        arr[i] = arr[i] + (None,) * (size - len(arr[i]))
    return arr

def scannotes(path, keys=[]):
    notes = []
    for n in os.listdir(path):
        if n not in IGNORE:
            if os.path.isdir(os.path.join(path, n)):
                notes += scannotes(os.path.join(path, n), keys=keys)
            else:
                meta = markdownmeta(os.path.join(path, n))
                entry = [None] * max(len(meta), len(keys))
                for k in meta:
                    if k not in keys:
                        keys.append(k)
                    entry[keys.index(k)] = meta[k]
                notes.append(tuple(entry))

    return fixSize(notes, len(keys))

def findandreplace(path):
    for n in os.listdir(path):
        if n not in IGNORE:
            if os.path.isdir(os.path.join(path, n)):
                findandreplace(os.path.join(path, n))
            else:
                with open(os.path.join(path, n), "r") as f:
                    content = f.read()
                if "%%\nstruct_eval_start\n%%" in content:
                    parts = content.split("%%\nstruct_eval_start\n%%\n")
                    new_content = parts[0]
                    second_parts = parts[1].split("\n%%\nstruct_eval_end\n%%")
                    code = "\n".join(second_parts[0].split("\n")[1:-1])
                    if sys.argc < 2 or sys.argv[1] != "release":
                        new_content += "%%\nstruct_eval_start\n%%\n%%\n" + second_parts[0] + "\n%%\n%%\nstruct_eval_end\n%%\n"

                    f = StringIO()
                    with redirect_stdout(f):
                        exec(code)
                    sout = f.getvalue()
                    new_content += sout + second_parts[1]
                    with open(os.path.join(path, n), "w") as f:
                        f.write(new_content)

def main():
    global zettel

    notesdir = "notes/"
    keys = []
    notes = scannotes(notesdir, keys=keys)

    print("Done scanning notes, found %s notes" % len(notes))
    zettel = Table(keys,notes)
    findandreplace(notesdir)

if __name__ == "__main__":
    main()

