# Part 5: Designing client/server applications
## Chapter 18. Design client/server applications
### 18.1. Creating a persistence layer
#### 18.1.3. Implementing entity DAOs
Things to consider: 
* make choice about how callers will access the DAOs
* life cycle of a DAO instance

Practical tips: Caller threads can share a DAO instance. In a multi-threaded Java EE environment, for example, the automatically inject `EntityManager` is effectively thread-safe, because internally it's often implemented as a *proxy* that delegates to some thread- or transaction-bound *persistence context*.

> Of course, if you call `setEntityManager()` on a DAO, that instance can't be shared and should only be used by one (for example, integration/unit test) thread.

**Thread-safety of an injected `EntityManager`**
The Java EE spec of JPA about `@PersistenceContext EntityManager em``: 

> only be accessed in a single-threaded manner

This implies that it can't be injected into inherently multi-threaded components such as EJBs, singleton beans, and servlets

practical tips:

* EJB spec requires that the EJB container serializes calls to each *stateful* and *stateless* session bean instance => injected `EntityManager` in `@Stateful` or `@stateless` EJB is therefore thread-safe
* If in doubt, inject the thread-safe `EntityManagerFactory`, and then create and close your own *application-managed* `EntityManager` in your component's service methods
