# [Transactions](https://docs.oracle.com/javaee/7/tutorial/transactions.htm)
## [Container-Managed Transactions](https://docs.oracle.com/javaee/7/tutorial/transactions003.htm)
> You can use container-managed transactions with any type of enterprise bean: session or message-driven.

Reference: The official tutorial

> by default, every Enterprise Bean method invocation occurs within a Java transaction.

Reference: Java EE 7: The Big Picture > Chapter 10 Advanced Thinking with Enterprise Beans > Transactions and Enterprise Beans

The statements above also implies that any type of Java objects, or *JavaBeans* other than *enterpise bean* cannot use *container-managed tranactions*. For instance, CDI beans annotated with only `@ApplicationScoped` or `@RequestScoped` etc. cannot use *Container-managed transactions*, this is why my issue [#11](https://github.com/rxue/REST-API/issues/11) encountered error: 

`Exception handling request to /security-search-engine/rest/company: org.jboss.resteasy.spi.UnhandledException: javax.persistence.TransactionRequiredException: WFLYJPA0060: Transaction is required to perform this operation (either use a transaction or extended persistence context)` 

since the resource class in JAX-RS is not an enterprise bean
