# Radare2

*radare2* is a cli based reverse engineering and binary analysis tool. It can be called by running `r2 [binary]` or `radare2 [binary]`

## Basics

When you enter radare2, the first thing you see is a prompt indicating where you are in the binary, this is called *seek*.

## Views

You can enter visual mode by running the command `V`, in visual mode there are multiple views. You can use the keys `p` for moving forwards and `P` for moving backwards. You can use the `hjkl` keys to move around in a view. In visual mode, your *seek* is at the top of the file. You can exit visual mode using `q`

## Moving around in visual mode

## Getting Help

? can be used to list the available commands. You can also list the subcommands of a commands by running `[command]?` for instance if you want to learn the details of the command p, you can run `p?`

## Moving around

Radare2 allows users to scroll around with vim-like keybindings. You can enter visual mode with the command `V` and exit it with `q`. Or, you can run commands in visual mode with colon(:). Search with /

## Analysing Functions
