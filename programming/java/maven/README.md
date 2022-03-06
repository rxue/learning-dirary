# `mvn install`
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

