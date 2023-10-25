# Chapter 1. Overview
## Java EE 7 APIsi
### 1.7.2 Java Servlet Technology
*request-response programming model*

### 1.7.3 JavaServer Faces Technology
In Java EE 7 platform, new features of JavaServer Faces technology include the following:

* HTML5-friendly markup
* Faces Flows
* Resource library contracts

### Java Message Service API
(Original) features of JMS:
 * allow Java EE  application components to create, send, receive and read messages.
 * enables distributed communication that is loosely coupled, reliable and asynchronous.

New Features in Java EE 7, i.e. *JMS API 2.0*
 * A new simplified API offers a simpler alternative to the previous API. This API includes `JMSContext` object that combines the functions of a `Connection` and a `Session`
 * ...(有争议)  


### [JavaMail API](https://docs.oracle.com/javaee/7/tutorial/overview007.htm#BNACJ)
Java EE apps use JavaMail API to send email notifications. The JavaMail API has 2 parts:
* An application-level interface used by the application-components to send mail
* A service provider interface

### Java Authentication Serivce Provider Interface for Containers
#### Takeway
* Authentication service providers implement the *authentication* mechanism on base of the SPI
* the Java Authentication SPI may be integrated in client or server message-processing containers or runtimes

## Java EE 7 APIs in the Java Platform, Standard Edition 7
### Java Naming and Directory Interface API
The naming environemtn provides 4 logical namespaces:
 * `java:comp` - available to components
 * `java:module` - available to modules
 * `java:app` - available to application
 * `java:global` - shared by all deployed applications

# Chapter 2. Using the Tutorial Examples
## (Tutorial Example) Directory structure
* `src/main/resources` : configuration files for the module, with the exception of web application
* `src/main/webapp` : web pages, style sheets, tag files, and images (web application only)
* `src/main/webapp/WEB-INF` : configuration files for web application (web application only)
