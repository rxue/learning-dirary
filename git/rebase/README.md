# `git rebase`

Assuming the current branch is dev, git rebase master will make all the commits on the current branch be based on the master branch. As a result, all the commits of the dev will be after all the commits of master

### `git pull --rebase` is equivalent to `git rebase`

Reasoning: In `git pull --help`, the following sentence is found:

> With `--rebase`, it runs `git rebase` instead of `git merge`

#### Problem: I am working on one story, and after commit there is need to `rebase` on base of another local branch. `rebase` failed because the `git log` output the last second and last third commit message as duplicate.

## 20220524
##### Question: How to combine the last few commits into one

##### Solution: `squash`: `git rebase -i HEAD~3`

###### Video Tutorial: https://www.youtube.com/watch?v=V5KrD7CmO4o&list=PLizL--84rE7T7l97deRGxZRRltRi9iQgA&index=24

Note about `squash`: 
	* the value of the optional `-i` could only accept *tilde* `~`
	* When seeing the list of commits after the command, note that you have to keep the first few commits unchanged, then `squash` the commits after the first few ones


