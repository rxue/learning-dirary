# How to use a different version of Java from the default version of the operating system (OS) with Maven (20220625)
## Current OS' configuration description
* Operating System: Ubuntu 20
* Output of `mvn --version` :

```
Apache Maven 3.6.3
Maven home: /usr/share/maven
Java version: 11.0.15, vendor: Private Build, runtime: /usr/lib/jvm/java-11-openjdk-amd64
Default locale: en_US, platform encoding: UTF-8
OS name: "linux", version: "5.13.0-51-generic", arch: "amd64", family: "unix"
```
## Problem: When compiling a [legacy Java EE project (in Java SE 8)](https://github.com/javaee/tutorial-examples), there is compilation error

## Change Request: In order to build the project successfully, Java 8 is needed

## Solution and Analysis
Reasoning: *Maven* builds project with the operating system's default Java in case *JAVA_HOME* environment is absent

=>

Solution: Set the `JAVA_HOME` environment variable to be that of legacy *Java 8* : `export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64`

As a result, the output of `mvn --version` would become:

```
Apache Maven 3.6.3
Maven home: /usr/share/maven
Java version: 1.8.0_312, vendor: Private Build, runtime: /usr/lib/jvm/java-8-openjdk-amd64/jre
Default locale: en_US, platform encoding: UTF-8
OS name: "linux", version: "5.13.0-51-generic", arch: "amd64", family: "unix"
```

# Tests with *JUnit 5* are not executed with `mvn` command
## Description
In my work project, after updating the unit tests code from JUnit 4 to *JUnit 5*, along with it there is also test dependency update, the tests are not executed with `mvn` command, e.g. `mvn clean package`
![o test executed](https://user-images.githubusercontent.com/3033388/172617932-28a62f0e-364c-4784-bec9-3940267cbfc8.png)
## Solution
reference: https://stackoverflow.com/questions/36970384/surefire-is-not-picking-up-junit-5-tests

NOTE! The correct answer is not the checked one but from the second one Mikhail Kholodkov. Based on the reference link above, that is an [surefire plugin issue](https://issues.apache.org/jira/browse/SUREFIRE-1330) in the old version and, it was resolved in *surefire 2.22.0* , which is not the default version.

Analysis helper Maven command: `mvn help:effective-pom`
This helps find the default version of *surefire plugin*  
