# 20190612: `git pull --rebase` is equivalent to `git rebase`

**Reasoning:** In `git pull --help`, the following sentence is found:

> With `--rebase`, it runs `git rebase` instead of `git merge`

# 20190613: Git Basic Video Tutorial
https://www.youtube.com/watch?v=HRR8xcTmpe4

# 20190614: Revert the Last Commit

`git reset --hard HEAD`

Reference: 
* [How to delete a git commit from log like it had never existed](https://stackoverflow.com/questions/8901542/how-to-delete-a-git-commit-from-log-like-it-had-never-existed)
* [Deleting a git commit](https://www.clock.co.uk/insight/deleting-a-git-commit)

# 20190618: **Git in Practice**: Working on a Local Branch Created from Master

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
2. `git reset --hard origin/master`

Reference: [Don't Mess With the Master Working with Branches in `git` and *github*](https://thenewstack.io/dont-mess-with-the-master-working-with-branches-in-git-and-github/)

# 20190621
## [Git States Control Flow](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
![Git States Control Flow](https://git-scm.com/book/en/v2/images/lifecycle.png)
## `git diff` Compares the *Unmodified* Files with *Modified* Files
## `git diff --cached` Compares the *Unmodified* Files with *Staged* Files

# 20190622
[`git reset`](https://www.youtube.com/watch?v=QEuqlpMOL9E&list=PLXO45tsB95cKysjmSNln65YoUt9lwEl7-&index=6) (中文)
Still something I cannot understand
