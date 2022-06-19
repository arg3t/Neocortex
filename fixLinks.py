import os
import re
import yaml
import datetime

def scanLinks(path, notes, root):
    with open(path, "r") as f:
        data = f.read()

    text = data.split('---\n')[2]

    wiki_links = []
    wiki_link_regex = r"\[\[(.*?)\]\]"
    for match in re.finditer(wiki_link_regex, text):
        out = {
            "wiki_link" : match.group()
        }

        if "|" in match.group(1):
            out["target"], out["text"] = match.group(1).split("|")
        else:
            out["target"] = match.group(1)

        if  out['target'].startswith('images/') or out['target'].startswith('/images'):
            continue

        foo = "." + os.path.join(root, out["target"]).strip('.').split('#')[0] + ".md"
        if foo not in notes:
            print(foo)
            continue

        if 'text' not in out:
            out["text"] = notes[foo]['title']

        # if the link ends with `_index` remove it
        if out["target"].endswith("_index"):
            out["target"] = out["target"][:-6]

        out["source"] = path.strip('.')

        if not out["target"].startswith("/"):
            out["target"] = "/" + out["target"]

        wiki_links.append(out)

    for i in wiki_links:
        if 'source' in i:
            data = data.replace(i["wiki_link"], f"[[{i['target']}|{i['text']}]]", 1)
        else:
            data = data.replace(i["wiki_link"], f"[[{i['target']}]]", 1)


    with open(path, "w") as f:
        f.write(data)

    return wiki_links

def markdownmeta(path):
    with open(path, "r") as f:
        md = f.read()

    metadata = {}
    portions = md.split("---\n")
    if md.startswith("---"):
        metadata = yaml.safe_load(portions[1])

    metadata["lastmodified"] = datetime.datetime.fromtimestamp(os.path.getmtime(path)).isoformat()
    metadata["content"] = portions[2].strip()

    return metadata


def scanNotesDir(path, notes):
    m = notes
    for n in os.listdir(path):
        if True:
            if os.path.isdir(os.path.join(path, n)):
                scanNotesDir(os.path.join(path, n), m)
            else:
                if not n.startswith(".") and n.endswith('.md'):
                    m[os.path.join(path, n)] = markdownmeta(os.path.join(path, n))

def scanLinksDir(path, notes, links):
    m = notes
    for n in os.listdir(path):
        if True:
            if os.path.isdir(os.path.join(path, n)):
                scanLinksDir(os.path.join(path, n), m, links)
            else:
                if not n.startswith(".") and n.endswith('.md'):
                    links.extend(scanLinks(os.path.join(path, n), m, './'))

def scanNotes(path):
    notes = {}
    links = []
    scanNotesDir(path, notes)
    scanLinksDir(path, notes, links)
    return links

scanNotes("./notes")

t1r = r'title:\s+(.*)'
t2r = r'^---\s*\n+#+\s+(.*)$'
t3r = r'^---\s*\n+(#+\s+.*)$'
for a in os.listdir("./notes"):
    i  = os.path.join("./notes", a)
    with open(i, 'r') as f:
        data = f.read()
    t1 = re.search(t1r, data)
    t2 = re.search(t2r, data, re.MULTILINE)
    if not t1:
        continue
    if not t2:
        continue
    t1 = t1.group(1)
    t2 = t2.group(1)
    t3 = re.search(t3r, data, re.MULTILINE).group(1)

    newdata = data.replace(t3 + '\n', '')
    with open(i, 'w') as f:
        f.write(newdata)

