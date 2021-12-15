#!/bin/sh
files=$(git ls-files | grep notes/)
export IFS=$'\n'

for i in $files; do
 if [[ "$i" == *.md ]] && [[ "$i" != *Excalidraw* ]] && [[ "$i" != *Templates* ]] && [[ "$i" != *Journal* ]] && grep -Exq "date: [0-9]{4}-[0-9]{2}-[0-9]{2}" "$i"; then
   commit=$(git rev-list HEAD "$i" | tail -n 1)
   date=$(git show -s --format="%cI" $commit | cut -d' ' -f1)
   
   sed -E "s/date: [0-9]{4}-[0-9]{2}-[0-9]{2}/date: $date/g" "$i" > /tmp/test
   cp /tmp/test "$i"
 fi
done


