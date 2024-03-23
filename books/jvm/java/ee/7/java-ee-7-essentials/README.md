# Chapter 2. Servlets
## WebServlet
> The values defined in the deployment descriptor override the values defined using annotations

# Chapter 7. *WebSocket*
*Web Socket* is a [full-duplex](https://github.com/rxue/daybook/tree/master/books/ComputerNetworkingATopDownApproach) and bidirectional communication protocol over a single *TCP* connection. It is a combination of the [*WebSocket protocol*](https://datatracker.ietf.org/doc/html/rfc6455) and [JavaScript WebSocket API](https://datatracker.ietf.org/doc/html/rfc6455)

Web Socket is different from HTTP in that with *Web Socket* prototocal there is no need to create a new TCP connection and exchange message with chock-full of headers between server and client every time. Intial *handshake* happens via HTTP Upgrade (section [14.42](https://www.ietf.org/rfc/rfc2616.txt)) only ONCE, then messages exchange without all the http headers independent of each other.

# Chapter 8. Enterprise Java Beans
## Stateful Session Beans (20240323)
`@Stateful(passivationCapable=false)` : ejb with this annotation will not be passivated. and note that the default value of `passivationCapable` is `true` (check the API doc)

label: `1Z0-900`

# Chapter 9. Contexts and Dependency Injection
## Events
NOTE! `@Observes` is allowed to be annotated merely to the method parameter. Refer to the API documentation: https://docs.oracle.com/javaee/6/api/javax/enterprise/event/Observes.html

label: `1Z0-900`

# Chapter 10. Concurrency Utilities
## Asynchronous Tasks
core interface: `javax.enterprise.concurrent.ManagedExecutorService`

> `ManagedExecutorService` supports at most one quality of service => ensures that the task will execute at most one time
**OWN COMMENT**
This is on base of the [Concurrent Utilities for Java EE 1.0 spec](#) > 3. Managed Objects > 3.1. ManagedExecutorService > 3.1.7 Quality of Service

> `ManagedExecutorService` implementations must support **at-most-once** *quality of service*

This *at-most-once* quality of service requirement guarantees that a task will **run at most one time**

A *task* can implement `ManagedTask` so that `ManagedTaskListener` can be used to receive life-cycle event notifications



# Chapter 12. Java Transaction
## User-Managed Transactions
## Container-Managed Transactions
Based on list of specification in Java EE 6, https://www.oracle.com/java/technologies/javaee/javaeetechnologies.html#javaee6 , *Java EE 6* supports *JTA 1.1*, whereas according to this chapter, `@javax.transaction.Transactional` is a new feature in *JTA 1.2* => `@Transactional` annotation is a new feature in Java EE

> It (`@Transactional` annotation) enables application to *declaratively* control *transaction boundaries* on *CDI beans* , as well as classes defined as *managed beans* such as servlets, JAX-RS resource classes, and JAX-WS service endpoints. 

 Java EE version  | Spec Version    | New Feature                   | New Feature in detail
------------------|-----------------|-------------------------------|----------------------------------
 Java EE 7        | JTA 1.2         | Container-Managed transaction | `javax.transaction.Transactional`

# Chapter 15. Batch Processing
## Chunk-Oriented Processing
`JobOperator` - interface for operating on batch jobs, like `start`, `restart` etc.

# Chapter 16. Build an End-to-End Appication
## Chat Room (Java API for WebSocket)
Note in the Chat Room app that the peers's sessions as synrhonized:

`private static final Set<Session> peers = Collections.synchronizedSet(new HashSet<>())`
