# [`git push`](https://git-scm.com/docs/git-push) 
Git can push both *branch* and *tag*, e.g.
* `git push origin branch_name`
* `git push origin tag_name`

## `--delete` option

> All listed refs are deleted from the remote repository. This is the same as prefixing all refs with a colon.

### Use case: Delete a branch from upstream (remote) repository
**Problem**: I created a remote branch in *Bitbucket* only on purpose of executing the regression tests, meaning there is no *pull request* on this branch. Eventually after the success of the regression tests execution, I want to remove this remote branch 

**Solution**: `git push origin --delete <branch name>` (20220530)

Reference: https://www.educative.io/edpresso/how-to-delete-remote-branches-in-git
