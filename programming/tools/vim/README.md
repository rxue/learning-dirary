# 20190622: 
* Insert a new line below the current line in normal mode: o

# 20190624:
* Move cursor to the first character of the first line - gg
* Copy all contents of a file - :%y a
* redo: ctrl+r

# 20191024: `vimdiff`: how to shift from left pane to the right pane
CTRL + WW - Press CTRL and then click W twice

# 20200107: `vimdiff` two strings
`vimdiff <(echo "hello a", echo "hello b")`

# 20200227
## delete/cut by line numbers
Example: :`12,18d`

# 20200228: [*registers*, *undolist* and *history* in `vim`](https://stackoverflow.com/questions/60431864/how-to-display-the-content-of-the-cache-in-vim/60432156#60432156)

# 20210707: I would like to turn on the language check for US English
i`:set spell spelllang=en_us`

# 20220725: how to display invisible chars such as *tab*, *end of line* etc.
Solution: ``:set list`
Reference: https://linuxhint.com/show-hidden-invisible-characters-vim/

# 20231025: how to search in vim with case-insensitive
## Answer (with example): `/word\c`

# substitute
## `:s` - substitute in the currenct line
## `:%s` - substitute in the entire file
In addition, the `%` can be also the range of lines, e.g. `:1,5s` 
