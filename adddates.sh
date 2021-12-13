#!/bin/sh
files=$(git ls-files | grep notes/)
export IFS=$'\n'

for i in $files; do
 if [[ "$i" == *.md ]] && [[ "$i" != *Excalidraw* ]] && [[ "$i" != *Journal* ]]; then
   commit=$(git rev-list HEAD "$i" | tail -n 1)
   date=$(git show -s --format="%ci" $commit | cut -d' ' -f1)
   title=$(cat $i | head -n 1 | sed 's/##\s*//g') 
   printf -- "---\ntitle: %s\ndate: %s\n---\n%s" "$title" "$date" "$(cat $i)" > "$i"
 fi
done


