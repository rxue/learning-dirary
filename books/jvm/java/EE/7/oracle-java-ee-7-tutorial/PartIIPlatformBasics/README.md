# 3. Resource Creation
## Resource and JNDI Naming
> ... In Java EE platform, the JNDI service enables components to locate other components and resources.

> A **resource** is a program object that provides connection to systems, such as database systems and messaging systems. (A Java Database Connectivity resource is sometimes referred to as a data source.)

# 4. Injection
## Resource Injection
> **Resource injection** enables you to inject any resource available in the *JNDI* namespace into any container-managed object, such as ...
## The Main Differences between *resource injection* and *dependency injection*
Injection mechanism | Can inject JNDI resources directly  | Can inject regular classes directly | Resolved by   | *typesafe*
--------------------|-------------------------------------|-------------------------------------|---------------|-----------
Resource injection  | Yes                                 | No                                  | Resource name | No
Dependency injection| No                                  | Yes                                 | Type          | Yes
