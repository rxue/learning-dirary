# `git checkout`
Note: 

 * `git checkout` can also *checkout* a remote branch directly to local
 * wildcard `*` cannot be used
 * checkout a full directory could work  

## How to checkout a remote branch (20230130)
`git checkout -b <branch> <remote>/<branch>` <=> `git checkout --track <remote>/<branch>`

Reference: https://git-scm.com/book/en/v2/Git-Branching-Remote-Branches#_tracking_branches 

## Reload/sync a Single File from a Remote Branch (20191008, 20200227)
`git checkout origin/<branch> -- <paths>`

Example: `git checkout origin/master -- abc.java`


