# Tests with *JUnit 5* are not executed with `mvn` command
## Description
In my work project, after updating the unit tests code from JUnit 4 to *JUnit 5*, along with it there is also test dependency update, the tests are not executed with `mvn` command, e.g. `mvn clean package`
![o test executed](https://user-images.githubusercontent.com/3033388/172617932-28a62f0e-364c-4784-bec9-3940267cbfc8.png)
## Solution
reference: https://stackoverflow.com/questions/36970384/surefire-is-not-picking-up-junit-5-tests

NOTE! The correct answer is not the checked one but from the second one Mikhail Kholodkov. Based on the reference link above, that is an [surefire plugin issue](https://issues.apache.org/jira/browse/SUREFIRE-1330) in the old version and, it was resolved in *surefire 2.22.0* , which is not the default version.

Analysis helper Maven command: `mvn help:effective-pom`
This helps find the default version of *surefire plugin*  
