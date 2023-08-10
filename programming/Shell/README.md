# `grep`
## `--invert-match` aka. `-v`
## `--exclude-dir=subdir`
The value of `--exclude-dir` is [*GLOB*](https://tldp.org/LDP/abs/html/globbingref.html)
Example: `grep --exclude-dir={python,debian_configuration} -r "mail" .`
# Practical Tip: In case of Bash with debug option `-x`, use `bash -x <script>.sh` instead of `source <script>.sh` with `set` inside the script
## Failure story on 20230131 when running `source <script>.sh` with MacBook's terminal
# `find`
## make use of `find` to truncate a directory
`find <dir> -mindepth 1 -delete`
# `tr` for string substitution (on multiple rows)

# `eval` to execute output text as command

# `sudo -s` in general VS `su` in Debian-based system (20230621)

# `rm`
* it has the verbose option `-v` to display the deleted items or ...
* wildcard `*` can be used flexibly. e.g. `rm /usr/local/*` to delete everything inside the directory `/usr/local`
# [`set`](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html)

# Difference between executing a script as executable and as a script with `source` command or `.` in one terminal session
