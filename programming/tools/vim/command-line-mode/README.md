# shift cursor
## shift current line one line up
`:m -2`
## shift current line one line down
`:m +1`
# search
## case-insensitive search
`/<word>\c` - word followed by `\c`

# delete
## delete word by word
### delete words before cursor
 * `db` - delete the one word before currsor, if the cursor is among a word, it will delete the part of the word before the cursor
 * `5db` - delete `5` words before cursor

