# [Introduction to Build the Lifecycle](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html)
## Build the Lifecycle Basics
### A *Build Lifecycle* is made up of phases

IMPORTANT to know:

> These lifecycle phases (plus the other lifecycle phases not shown here) are **executed sequentially** to complete the default lifecycle

The sentence above that all the *phases* in the **Lifecycle References** section are executed in the order of that in the table by default. For instance, 

* `package` phase is before `verify`, thus `mvn package` command will not execute the *integration test* since it is after the `package` phase
* similarly `mvn package` would not install the built package since `install` phase is after `package` also

### `install`
Install package to the *local repository*

### `mvn clean` does not remove the installed package from the *local repository*

## [*Plugin* bindings for default lifecycle reference](https://maven.apache.org/ref/3.8.6/maven-core/default-bindings.html)
The xml code for the binding configuration on the link page above explains why unit tests with JUnit can work out-of-the-box, whereas the integration test does not work out-of-the-box

