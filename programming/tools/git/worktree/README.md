# `worktree`
Tutorial: https://www.youtube.com/watch?v=s4BTvj1ZVLM

An important and good feature of worktree is that in one `worktree` client can `checkout` to a branch on another `worktree` in a different directory from the current

## Keep in mind that `git worktree add branch_name` will get cloned on base of the based project

## Problem when using `mvn` to build project under the worktree:
![Problem when using mvn under worktree directory](https://user-images.githubusercontent.com/3033388/227475928-77c94afb-5f10-462f-b992-e292a4a2ec89.png)

Solution: https://github.com/git-commit-id/git-commit-id-maven-plugin/issues/215

## `worktree list`
list all worktrees
