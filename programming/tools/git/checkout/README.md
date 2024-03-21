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


