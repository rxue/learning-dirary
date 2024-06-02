# Chapter 5: Database Programming
## 5.10. Connection Management in Web and Enterprise Applications
`DataSource` is related to

 * `jndi`
 * application server
 * *connection pool*

# Chapter 8: Scripting, Compiling, and Annotation Processing
## 8.5 Standard Annotations
### 8.5.1 Annotations for Compilation
Practical tips about `@Deprecated` : since Java 9, this annotation has 2 optional elements `forRemoval` and `since`

### 8.5.2 Meta-Annotations
Element types of target annotation

Element Type  | Annotation Applies to
--------------|--------------------------
`PARAMETER`   | Method or constructor parameters

# Chapter 9: The Java Platform Module System
## The Module Concept
2 advatanges of using the Java Platform Module System:

1. strong encapsulation
2. reliable configuration

# Chapter 10: Security
## Class Loaders
Debugging of the code demo, https://github.com/rxue/java-from-scratch-to-advanced/blob/main/src/main/java/rx/book/corejava/volume2/ch10/ClassLoaderDemo.java , shows that the parent *class loader* of `PlatformClassLoader` is `BootClassLoader` - the *bootstrap class loader*
![parent of PlatformClassLoader is BootClassLoader](https://user-images.githubusercontent.com/3033388/265276131-9679ad16-ddaa-492c-a8b6-ace581a47399.png)
However, 

> There is no `ClassLoader` object corresponding to the bootstrap class loader.

![parent of PlatformClassLoader is null to client](https://user-images.githubusercontent.com/3033388/265276144-e4e11a05-cbee-4552-8d77-88317a3b18ab.png)

