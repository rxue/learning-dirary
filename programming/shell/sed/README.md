`sed` is *stream processing* tool

# `sed -n '<line_number>p' <filename>`
Read one line of content on the specific line number from a text file
## Use case
SQL script large import failure, e.g. with `mysql` client at a specific line number. Use this command to check the content of the failure line
  
# 20231204: how to replace text in a file
with `-i` option: `sed -i`

Based on the *manual* of `sed`, `-i` is the same as `--in-place`
