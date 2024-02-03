# Chapter 1. Understanding object/relational persistence
## 1.3 ORM and JPA
JPA specification:
 * ORM
 * `EntityManager`
 * JPQL
 * peristence engine does: *dirty checking*, association, fetch, etc.
# Chapter 3. Domain models and metadata
new feature in JPA 2
* integration with *bean validation*
* `Metamodel` API
## 3.1. [The example `CaveatEmptor` application](http://www.jpwh.org/examples/jpwh/caveatemptor-jpa-061211/)
### 3.1.1. Layered architecture
cross-cutting concerns: logging, authorization, transaction demarcation
### 3.1.3. The `CaveatEmptor` *domain model*

## 3.2. Implementing the domain model
### 3.2.1. Addressing *leakage of concerns*
cross-cutting concerns: security, concurrency, persistence, transactions, remoteness - intercepting calls to application components
### 3.2.3. Writing persitence-capable classes
The persistence-capable classes
 * can't be `final`
 * JPA (entity) requires constructor with no arguments. The constructor should be at least *package-private*
 * *Hibernate* doesn't require *accessor methods*

*dirty checking* : Hibernate automatically detect state changes in order to synchronize the updated state with database. Hibernate determine dirtiness by *comparing members by values*. But there is an exception **that *collection* members are compared by *identities*!** => alway return the same collection instance from *getter*

### 3.2.4. Implementing associations
# Part 5. Building applications
## Chapter 18. Designing client/server applications
### 18.1 Creating a persistence layer
design tip: KISS and create a lean persistence layer on top of JPA when you realize you're duplicating the same query and persistence operations
#### 18.1.3. Implementing entity DAOs
DAO classes are *stateless* without considering the `EntityManager` member. But in a multi-threaded Java EE environment, **automatically injected** `EntityManager` is *effectively thread-safe*, because internally it is often implemented as a proxy that delegates to some thread- or transaction-bound on a DAO. On the other hand, if the `EntityManager` is passed through setter of DAO, the `EntityManager` cannot be shared around!

When using EJB stateless session bean through injection, the persistence context injection is effectively thread-safe since that is managed by EJB container

**Thread-safety of an injected `EntityManager`**

Based on [JPA 2.0 specification](https://jcp.org/aboutJava/communityprocess/final/jsr317/index.html) (NOTE! Before this version, JPA was part of EJB spec) > Chapter 7. Entity Managers and Persistene Contexts > 7.2. Obtaining an `EntityManager`

> An *entity manager* must not be shared among multiple concurrently executing threads, as the *entity manager* and *persistence context* are not required to be *threadsafe*. **Entity managers must only be accessed in a single-threaded manner**.

`EntityManager` is not required to be *threadsafe*, so **NOTE that access to it must be in single-threaded manner!**

So if the components, inside which `EntityManager` is used, are not *threadsafe*, it is developers' responsibility to maintain the thread-safety. A typical case is the direct use of `EntityManager` inside `Servlet` class. However, according to the [EJB 3.2 specification](https://jcp.org/aboutJava/communityprocess/final/jsr345/index.html) > Chapter 4. Session Bean Component Contract > 4.3. Protocol Between a Session Bean Instance and its Container > 4.3.13. Serializing Session Bean Methods:

> The container serializes calls to each stateful and stateless session bean instance. Most containers will support many instances of a session bean executing concurrently; however, each instance sees only a serialized sequence of method calls. Therefore, a stateful or stateless session bean does not have to be coded as reentrant.

=> design tip: as long as `EntityManager` is used inside a stateful/stateless EJB session bean, call of the `EntityManager` through the bean will be serialized by the EJB container and thus concurrency handling is shifted to the underlying database system without any extra synchronization code, meaning

clients do not need to write any extra synchronization code as long as `EntityManager` is injected into an EJB session bean with `PersistenceContext`

Moreover, according to the [EJB 3.2 specification](https://jcp.org/aboutJava/communityprocess/final/jsr345/index.html) > Chapter 4. Session Bean Component Contract > 4.8. Singleton Session Bean > 4.8.5. Singleton Session Bean Concurrency

> From the client’s perspective, a singleton session bean always supports concurrent access. In general, the client of a singleton session bean does not have to concern itself with whether other clients might be accessing the singleton session bean at the same time.

=> design tip: `@Singleton` session bean can be used easily e.g. with `EntityManager` instance embedded inside without any extra synchronization code

NOTE! Before this version, JPA was part of EJB spec
Important reference: https://developer.jboss.org/thread/280437
