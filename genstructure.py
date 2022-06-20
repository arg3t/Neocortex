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
import re

from json import JSONEncoder
import json
import datetime

import argparse

# Declare function to define command-line arguments
def readOptions(args=sys.argv[1:]):
  parser = argparse.ArgumentParser(description="Indice generator for quartz")
  parser.add_argument("-n", "--notesdir", help="Directory where you keep your notes", required=True)
  parser.add_argument("-i", "--indicedir", help="Directory where you want to store the indice files", required=True)
  parser.add_argument("-I", "--ignore", nargs='+', help="Regex for ignoring")
  opts = parser.parse_args(args)
  return opts

# Call the function to read the argument values
options = readOptions(sys.argv[1:])

if options.ignore != None:
    IGNORE = options.ignore
else:
    IGNORE = []

def markdownmeta(path):
    with open(path, "r") as f:
        md = f.read()

    metadata = {}
    portions = md.split("---\n")
    if len(portions) < 3:
        return None
    if md.startswith("---"):
        metadata = yaml.safe_load(portions[1])

    metadata["lastmodified"] = datetime.datetime.fromtimestamp(os.path.getmtime(path)).isoformat()
    metadata["content"] = portions[2].strip()

    return metadata

def balanceIndex(idx):
    keys = set()
    for i in idx:
        keys.update(idx[i].keys())

    for i in idx:
        for j in keys.difference(idx[i].keys()):
            idx[i][j] = None

def isIgnored(path):
    for i in IGNORE:
        if re.search(i, path):
            return True
    return False

def chop(s, words):
    for w in words:
        if s.startswith(w):
            s = s[len(w):]
            return chop(s, words)

        if s.endswith(w):
            s = s[:-len(w)]
            return chop(s, words)

    return s

def normalize(s):
    allowedChars = ['.', '/', '\\', '_', '#', '+', '~']

    res = ""
    prependHyphen = False

    for i in s:
        isAllowed = i in allowedChars or i.isdigit() or i.isalpha()

        if isAllowed:
            if prependHyphen:
                res += '-'
                prependHyphen = False

            res += i
        elif len(res) > 0 and (i == '-' or i.isspace()):
            prependHyphen = True


    if not res.startswith("/"):
        res = "/" + res

    res = chop(res, ('.md', '.html'))

    return res

def scanLinks(path):
    with open(path, "r") as f:
        text = f.read().split('---\n')[2]

    wiki_links = []
    wiki_link_regex = r"\[\[(.*?)\]\]"
    for match in re.finditer(wiki_link_regex, text):
        out = {
        }

        if "|" in match.group(1):
            out["target"], out["text"] = match.group(1).split("|")
        else:
            out["target"] = match.group(1)
            out["text"] = match.group(1)

        if isIgnored(out["target"]):
            continue

        out["target"] = normalize(out["target"])

        # if the link ends with `_index` remove it
        if out["target"].endswith("_index"):
            out["target"] = out["target"][:-6]

        out["source"] = normalize(path.strip('.'))

        wiki_links.append(out)
    return wiki_links


def genLinkIndex(links):
    idx = {"links" : {}, "backlinks" : {}}

    for i in links:
        if i["source"] not in idx["links"]:
            idx["links"][i["source"]] = []
        idx["links"][i["source"]].append(i)

        foo = {}

        foo["text"] = i["text"]
        foo["target"] = i["source"]
        foo["source"] = i["target"]

        if i["target"] not in idx["backlinks"]:
            idx["backlinks"][i["target"]] = []
        idx["backlinks"][i["target"]].append(i)

    return idx

def scanNotesDir(path, notes, links):
    for n in os.listdir(path):
        if not isIgnored(n):
            if os.path.isdir(os.path.join(path, n)):
                scanNotesDir(os.path.join(path, n), notes, links)
            else:
                if not n.startswith(".") and n.endswith('.md'):
                    key = os.path.join(path, n).strip('.')
                    if key == "/_index.md":
                        key = "index"

                    foo = markdownmeta(os.path.join(path, n))
                    if not foo:
                        continue
                    notes[normalize(key)] = foo
                    links.extend(scanLinks(os.path.join(path, n)))

def getParentTag(tag):
    if '/' not in tag:
        return None

    return '/'.join(tag.split('/')[:-1])

def extendLinkIndexWithTags(links, notes):
    taglinks = []
    tagHierarchy = {}
    for n in notes:
        note = notes[n]
        if not note['tags']:
            continue
        for t in note['tags']:
            link = {"target" : n, "source" : f"/tags/{t}", "text" : t, 'tag': True}
            taglinks.append(link)
            parent = getParentTag(t)
            if parent:
                if parent not in tagHierarchy:
                    tagHierarchy[parent] = set()
                tagHierarchy[parent].add(t)

    for p in tagHierarchy:
        for t in tagHierarchy[p]:
            link = {"target" : f"/tags/{t}", "source" : f"/tags/{p}", "text" : p, 'tag': True}
            taglinks.append(link)
    links["links"].extend(taglinks)

def scanNotes(path):
    notes = {}
    links = []
    scanNotesDir(path, notes, links)
    balanceIndex(notes)
    linkIndex = {"index" : genLinkIndex(links), "links" : links}
    extendLinkIndexWithTags(linkIndex, notes)
    return notes, linkIndex

# subclass JSONEncoder
class DateTimeEncoder(JSONEncoder):
        #Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()

def main():
    root = os.getcwd()

    os.chdir(options.notesdir)

    contentIndex, linkIndex = scanNotes('./')

    os.chdir(root)

    with open(os.path.join(options.indicedir, "linkIndex.json"), "w") as f:
        f.write(json.dumps(linkIndex, indent=4, cls=DateTimeEncoder))

    with open(os.path.join(options.indicedir, "contentIndex.json"), "w") as f:
        f.write(json.dumps(contentIndex, indent=4, cls=DateTimeEncoder))

if __name__ == "__main__":
    main()

