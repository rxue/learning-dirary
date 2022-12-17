# `git branch`
## List all the branches, i.e. both local and remote (20221218)
`git branch -a`

## Delete a branch
### Remove Local branch
* `git branch -d <branch_name>`
* `git branch -D <branch_name>` - `-D` i.e. `git branch -d --force`

### Delete a branch from upstream (remote) repository (20220602)
**Problem**: I created a remote branch in *Bitbucket* only on purpose of executing the regression tests, meaning there is no *pull request* on this branch. Eventually after the success of the regression tests execution, I want to remove this remote branch 

**Solution 1**: `git push origin :<branch name>`

Reference: https://stackoverflow.com/questions/15150671/delete-branches-in-bitbucket

**Solution 2**: `git push origin --delete <branch name>` (20220530)

Reference: https://www.educative.io/edpresso/how-to-delete-remote-branches-in-git
## Rename a branch (20220602)
### Rename a local branch
`git branch -m <current branch name> <new branch name>`
