# `rm`
## `rm --cached`
unstage file, i.e. remove file from index

# `submodule`
`git submodule add git@github.com:rxue/dictionary-jpa.git`

Note that the essence of `git sudmodule add` is that 
* the added `.gitsubmodules` file and the submodule directory are *staged*. This can be proved by `git status` after the command execution
* as a result, there is no need to `git add`, `git commit` and then `git push` will complete the whole process
* Presentation in the git provider is clean. Take *github* as an example, the pushed *submodule* directory is a link to the target project

