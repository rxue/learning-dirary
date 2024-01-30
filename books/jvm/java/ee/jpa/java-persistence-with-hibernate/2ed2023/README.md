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

# Chapter 18. Designing client/server applications
## 18.1 Creating a persistence layer
design tip: KISS and create a lean persistence layer on top of JPA when you realize you're duplicating the same query and persistence operations
### 18.1.3. Implementing entity DAOs
DAO classes are *stateless* without considering the `EntityManager` member. But in a multi-threaded Java EE environment, **automatically injected** `EntityManager` is *effectively thread-safe*, because internally it is often implemented as a proxy that delegates to some thread- or transaction-bound on a DAO. On the other hand, if the `EntityManager` is passed through setter of DAO, the `EntityManager` cannot be shared around!

When using EJB stateless session bean through injection, the persistence context injection is effectively thread-safe since that is managed by EJB container

**Thread-safety of an injected `EntityManager`**

Important reference: https://developer.jboss.org/thread/280437
