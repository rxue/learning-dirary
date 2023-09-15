# Chapter 2. Servlets
## WebServlet
> The values defined in the deployment descriptor override the values defined using annotations

# Chapter 7. *WebSocket*

# Chapter 8. Enterprise Java Beans
## Stateful Session Beans
`@Stateful(passivationCapable=false)` : ejb with this annotation will not be passivated. and note that the default value of `passivationCapable` is `true` (check the API doc)

# Chapter 12. Java Transaction
## User-Managed Transactions
## Container-Managed Transactions
Based on list of specification in Java EE 6, https://www.oracle.com/java/technologies/javaee/javaeetechnologies.html#javaee6 , *Java EE 6* supports *JTA 1.1*, whereas according to this chapter, `@javax.transaction.Transactional` is a new feature in *JTA 1.2* => `@Transactional` annotation is a new feature in Java EE

> It (`@Transactional` annotation) enables application to *declaratively* control *transaction boundaries* on *CDI beans* , as well as classes defined as *managed beans* such as servlets, JAX-RS resource classes, and JAX-WS service endpoints. 

 Java EE version  | Spec Version    | New Feature                   | New Feature in detail
------------------|-----------------|-------------------------------|----------------------------------
 Java EE 7        | JTA 1.2         | Container-Managed transaction | `javax.transaction.Transactional`

# Chapter 16. Build an End-to-End Appication
## Chat Room (Java API for WebSocket)
Note in the Chat Room app that the peers's sessions as synrhonized:

`private static final Set<Session> peers = Collections.synchronizedSet(new HashSet<>())`
