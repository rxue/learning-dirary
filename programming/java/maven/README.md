# `mvn` Command Arguments
## `-U,--update-snapshots`
> For a check for missing releases and updated snapshots on remote repositories

Use case (`20220329`): Out project removed the previous Nexus mirror and moved all source code from *bitbucket* to *gitlab*, so the *local repository*, i.e. `~/.m2`, should be synced. In this case `-U` comes into play   

# [Build Lifecycle](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html)
## *default*

IMPORTANT to know:

> These lifecycle phases (plus the other lifecycle phases not shown here) are **executed sequentially** to complete the default lifecycle

### `install`
Install package to the *local repository*

## `mvn clean` does not remove the installed package from the *local repository*

# Configuration
## Repositories
### [Using Mirrors for Repositories](https://maven.apache.org/guides/mini/guide-mirror-settings.html)

Some reasons to use a mirror are:

> * There is a synchronized mirror on the internet that is **geographically closer and faster**

> * You want to replace a particular repository with your own internal repository which you have greater control over

> * You want to run a [repository manager](https://maven.apache.org/repository-management.html) to provide a local cache to a mirror and need to use its URL instead

> To configure a mirror of a given repository, you provide it in your settings file (`${user.home}/.m2/settings.xml`)

> Note that there can be at most one mirror for a given repository. In other words, you cannot map a single group of mirrors that all define the same `<mirrorOf>` value. 

> `*,!repo1` = everything except `repo1`

# Multi-Module Project

