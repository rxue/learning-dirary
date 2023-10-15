# Chapter 32: Enterprise Beans
*Enterprise bean* : *server-side component* that encapsulates the *business logic* of an application. The *business logic* is the code that fulfills the purpose of the application.
# Chapter 34: Running the Enterprise Bean Examples
## Handling Exceptions
* *System Exception* : `javax.ejb.EJBException` extends `RuntimeException`. Causes container to *roll back* transaction
* *Application Exception* : error in business logic. When an ejb throws an application exception, the container does not wrap it in another exception. Client should be able to handle any application it receives (this indicates that application exception is *checked exception*). Container does *not roll back* application exception 
