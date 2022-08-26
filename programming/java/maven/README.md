# `mvn` Command Arguments
## `-U,--update-snapshots`
> For a check for missing releases and updated snapshots on remote repositories

Use case (`20220329`): Out project removed the previous Nexus mirror and moved all source code from *bitbucket* to *gitlab*, so the *local repository*, i.e. `~/.m2`, should be synced. In this case `-U` comes into play   

# [Build Lifecycle](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html)
## *Default Lifecycle*

IMPORTANT to know:

> These lifecycle phases (plus the other lifecycle phases not shown here) are **executed sequentially** to complete the default lifecycle

### `install`
Install package to the *local repository*

## `mvn clean` does not remove the installed package from the *local repository*

# Configuration
## MUST: [Have a JDK installation on your system. Either set the `JAVA_HOME` environment variable pointing to your JDK installation or have the `java` executable on your `PATH`](https://maven.apache.org/install.html) (20220625)

This statement is from the [Maven install documentation](https://maven.apache.org/install.html). It implies that *Maven* still makes use of the Java compiler from its residing operating system, say it finds the Java compiler on base of the `JAVA_HOME` environment variable and, in case the `JAVA_HOME` is absent Maven will fallback to get the `java` executable like any other program from the operating system.

This implication can be proved by the following experiment in *Linux* system:

 1. install *open jdk 11* in the system. As a result, the `java --version` will tell `openjdk 11.0.15 2022-04-19`
 2. install Maven. As a result, the output of command `mvn --version` would contain line: `Java version: 11.0.15, vendor: Private Build, runtime: /usr/lib/jvm/java-11-openjdk-amd64`, which correspondings to the output of `java --version`
 3. Now that Maven is installed and works with Java 11, if there is a legacy Java 8 project, i.e. the `source` and `target` are defined as 1.8 in the `pom.xml`, the `mvn compile` will in fact still make use of the jdk *11* in the residing operating system, this could be proved by trying `mvn package` with a Java 8 project, e.g. [Java ee 8 tutorial examples](https://github.com/javaee/tutorial-examples), which would result in compilation error

=> 

In order to compile a legacy Java project with a JDK version other than the system's default executable `javac` and `java`, open jdk 8 should be installed on the same system =>

 4. install a secondary JDK, e.g. *open jdk 8* in the same system, but it is not the executable with the `java` or `javac` command, meaning the `java --version` still output the same result as before
 5. In one *terminal* session, `JAVA_HOME` could be set, e.g. with command `export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64`. reference code sample: https://github.com/rxue/dictionary/commit/96d9ae520242caba5aed9091d5deb81c26e97dce#diff-dab0fe4aa5535d091d5a8dcb213abcf28cb6e8a850536cbacbcdf03b43b2aebb
 6. As a result, the output of command `mvn --version` would contain line `Java version: 1.8.0_312, vendor: Private Build, runtime: /usr/lib/jvm/java-8-openjdk-amd64/jre` in the same terminal session, where the `export` command is executed
 7. `mvn package` in this legacy project root directory in this terminal session will succeed

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

