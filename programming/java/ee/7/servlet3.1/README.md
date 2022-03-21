# Java EE 7: The Big Picture
## Chapter 2: Java Servlets and Web Applications: Foundations of the Web Tier
### Introducing Java Servlets
#### How to Create a Java Servlet
> If you only ever learn once method of the `HttpServlet` class, it is the `service()` method: it will handle all HTTP request! in reality, much of the time you will be implemnenting either the `doGet()` or the `doPost()` methods because they the most common forms of HTTP requests in the web applications.

# Java Servlet Specification
## Chapter 8: Annotations and Pluggability
### 8.2 Pluggability
#### 8.2.3 Assembling the Desciptor from the web.xml, web-fragment.xml and Annotations

> If the order, in which the *listeners*, *servlets* and *filters* are invoked is important to an application then a *deployment descriptor* must be used.

Reference on filters with jsf: https://stackoverflow.com/questions/8480100/how-implement-a-login-filter-in-jsf

## Chapter 12: Mapping Requests to Servlets
### Specification of Mappings
> In the Web application deployment descriptor, the following syntax is used to define mappings:

> * A string beginning with a '/' character and ending with a '/\*' suffix is used for path mapping
> * A string beginning with a '*.' prefix is used as an extension mapping
> ...

