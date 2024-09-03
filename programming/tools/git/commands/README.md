# `rm`
## `rm --cached`
unstage file, i.e. remove file from index

# `git tag` VS ``git branch`
operations              | `tag`             | `branch`
------------------------|-------------------|--------------
list all local objects  | `git tag`         | `git branch`
remove a local object   | `git tag -d <tag>`| `git branch -D <branch>`


# `submodule`
## List submodules
There is no command such `ls` under `submodule` => `git submodule status`

## `git submdule add`
`git submodule add git@github.com:rxue/dictionary-jpa.git`

Note that the essence of `git sudmodule add` is that 
* the added `.gitsubmodules` file and the submodule directory are *staged*. This can be proved by `git status` after the command execution
* as a result, there is no need to `git add`, `git commit` and then `git push` will complete the whole process
* Presentation in the git provider is clean. Take *github* as an example, the pushed *submodule* directory is a link to the target project

## Remove a submodule
1. `git submodule deinit -f <submodule_path>`
2. remove submodule path: `git rm --cached <submodule-path>`
#2. remove submodule path: `rm -rf <submodule-path>`
3. if there is no other submodules, remove the `.gitmodules` hidden file from git repository level: `git rm .gitmodules`
