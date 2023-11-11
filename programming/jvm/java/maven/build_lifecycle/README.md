# [Build Lifecycle](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html)
## *Default Lifecycle*

IMPORTANT to know:

> These lifecycle phases (plus the other lifecycle phases not shown here) are **executed sequentially** to complete the default lifecycle

### `install`
Install package to the *local repository*

### `mvn clean` does not remove the installed package from the *local repository*

## [*Plugin* bindings for default lifecycle reference](https://maven.apache.org/ref/3.8.6/maven-core/default-bindings.html)
The xml code for the binding configuration on the link page above explains why unit tests with JUnit can work out-of-the-box, whereas the integration test does not work out-of-the-box

## 20231111
NOTE! `package` phase is before `verify`
