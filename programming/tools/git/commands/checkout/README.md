# `git checkout`
Note: 

 * `git checkout` can also *checkout* a remote branch directly to local
 * wildcard `*` cannot be used
 * checkout a full directory could work  

## Create a new branch on base a remote branch (20230130, 20240321)
NOTE! the remote branch has to be fetched to local, i.e. `git fetch origin` in the first place

`git checkout -b <branch> <remote>/<branch>` <=> `git checkout --track <remote>/<branch>`

Reference: https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches#_tracking_branches 

Base on official `git checkout --help`, the part `<remote>/<branch>` is coined as `[<start-point>]`

## Reload/sync a Single File from a Remote Branch (20191008, 20200227)
`git checkout origin/<branch> -- <paths>`

Example: `git checkout origin/master -- abc.java`

## Checkout a remote tag
example: `git checkout -b 3.22.5 tags/3.22.5`

## 20240708 Question: I have all code in branch A, I would like to replace all contents in master with all contents in branch A
### Answer
1. checkout to master
2. command: `git checkout A -f .`

## `--orphan` option
Create a new orphan branch, named <new_branch>, started from <start_point> and switch to it. The first commit made on this new branch will **have no parents** and it will be the root of a new history totally disconnected from all the other branches and commits.

The index and the working tree are adjusted as if you had previously run git checkout <start_point>. This allows you to start a new history that records a set of paths similar to <start_point> by easily running git commit -a to make the root commit.

This can be useful when you want to publish the tree from a commit without exposing its full history. You might want to do this to publish an open source branch of a project whose current tree is "clean", but whose full history contains proprietary or otherwise encumbered bits of code.

**Important**

If you want to start a disconnected history that records a set of paths that is totally different from the one of <start_point>, then you should clear the index and the working tree right after creating the orphan branch by running git `rm -rf .`  from the top level of the working tree. Afterwards you will be ready to prepare your new files, repopulating the working tree, by copying them from elsewhere, extracting a tarball, etc.

**Typical use case:** Create `gh-pages` branch for display static html pages in Github
