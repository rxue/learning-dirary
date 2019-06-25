# 20190612: `git pull --rebase` is equivalent to `git rebase`

**Reasoning:** In `git pull --help`, the following sentence is found:

> With `--rebase`, it runs `git rebase` instead of `git merge`

# 20190613: Git Basic Video Tutorial
https://www.youtube.com/watch?v=HRR8xcTmpe4

# 20190614: Revert the Last Commit

Reference: 
* [How to delete a git commit from log like it had never existed](https://stackoverflow.com/questions/8901542/how-to-delete-a-git-commit-from-log-like-it-had-never-existed)
* [Deleting a git commit](https://www.clock.co.uk/insight/deleting-a-git-commit)

# 20190618:
## Command to Create new Branch
`git checkout -b <new_branch>`
NOTE! This command also switches to the created branch automatically
Then stage, aka. `add`, and `commit` new files will go to the new branch
**Git in Practice**: The name of the branch should be descriptive, for instance, it can be the name of the task you are working on. Moreover, if you have multiple tasks, you can create multiple branches as per tasks  
## Command to Go to Another Branch
`git checkout <another_branch>`
## HEADs Indicates a Local Branch You are Currently on

## How to discard all the changes on the current branch
1. `git fetch origin`
2. `git reset --hard origin/master` or `git reset --hard HEAD` (revert to the last commit)

Reference: [Don't Mess With the Master Working with Branches in `git` and *github*](https://thenewstack.io/dont-mess-with-the-master-working-with-branches-in-git-and-github/)

# 20190621
## [Git States Control Flow](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
![Git States Control Flow](https://git-scm.com/book/en/v2/images/lifecycle.png)
## `git diff` Compares the *Unmodified* Files with *Modified* Files
## `git diff --cached` Compares the *Unmodified* Files with *Staged* Files

# 20190622
[`git reset`](https://www.youtube.com/watch?v=QEuqlpMOL9E&list=PLXO45tsB95cKysjmSNln65YoUt9lwEl7-&index=6) (中文)
Question:
* what is `git reset --hard origin/master`

`git fetch origin` does not sync local content from the remoate origin yet, will continue to research on how this is working

`merge` a *conflict* does not generate an automatic *commit* message

# 20190624: 
## Display the current HEAD
`git rev-parse HEAD`

## Understanding on `rebase`
Assuming the current branch is `dev`, `git rebase master` will make all the commits on the current branch be based on the master branch. As a result, all the commits of the `dev` will be after all the commits of master 

## **Practical Work Approach in a Development Team with multiple Developers Working on Merely One Branch - Master**: 
1. work on a local branch created from master, commit on the local branch
2. switch to the local master branch to *sync* it from the *remote*
3. `git rebase master` in the current branch
4. `git push origin master` or with *refspec* `git push origin HEAD:refs/remote/master` on the current branch

# 20190625
Add only modified files: `git add -u`

## push a local branch to a remote `origin` branch with another name
Example: `git push origin change_20190624:master` - push the local branch `change_20190624` to remote origin `master`

## List remote
`git ls-remote`

## Delete a remote *refspec* 
`git push origin :<refspec>` e.g. `git push origin :refs/heads/master`
