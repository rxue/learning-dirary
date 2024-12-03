# `git rebase`

Assuming the current branch is dev, git rebase master will make all the commits on the current branch be based on the master branch. As a result, all the commits of the dev will be after all the commits of master

### `git pull --rebase` is equivalent to `git rebase`

Reasoning: In `git pull --help`, the following sentence is found:

> With `--rebase`, it runs `git rebase` instead of `git merge`

#### Problem: I am working on one story, and after commit there is need to `rebase` on base of another local branch. `rebase` failed because the `git log` output the last second and last third commit message as duplicate.

## *squash* (0220524,20220712,20241021,20241203) - command: `git rebase -i HEAD~3` and then use `squash`
in the command, the number after tild means how many commits are going to be listed in the interactive output. NOTE! if `git rebase -i` is used without any commits, interactive ouput will contains no list of commit hash

### Video Tutorial: https://www.youtube.com/watch?v=V5KrD7CmO4o&list=PLizL--84rE7T7l97deRGxZRRltRi9iQgA&index=24

NOTE in the video example that **the earliest commit is `ee8ce13 Accessibility fix for frontpage bug` in the first line** and, this earliest commit is the one, which cannot be *squashed*

After `squash` the 2 later commits into this earliest commit, the new combined commit hash has changed from `ee8ce13` to `d775667`

More note about `squash`: 
* the value of the optional `-i` could only accept *tilde* `~`
* Only later commits can be marked `squash`, i.e. in the interactive editor opened followed by `git rebase -i HEAD~<#>` command, among the commit list in the reversed order of `git log`, the commit on the top cannot be marked `squash`, only those after can be marked `squash`
* When seeing the list of commits after the command, note that you have to keep the first few commits unchanged, then `squash` the commits after the first few ones

### Question: How to combine the last 3 commits into one
#### Solution: `squash`: `git rebase -i HEAD~3`

### Question (20241203) : in case the *Merged* message is the last *commit hash*, after *rebase* the top *Merged commit hash* disappeared
### Answer: this is the default, refer to the manual of `--rebase-merges`

> By default, a rebase will simply drop merge commits from the todo list, and put the rebased commits into a single, linear branch

=> in order to rebase the *Merged commit hash*, use this option. Moreover, similarly there is `--preserve-merges`





