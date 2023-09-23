# [Entities](https://docs.oracle.com/javaee/7/tutorial/persistence-intro001.htm)
## Embeddable Classes in Entities
Use case of `@Embeddable`

[dictionary](https://github.com/rxue/dictionary) project > Issue: [Sub-task of #10 : add an EntryValue composed of entry and language regardless of part of speech](https://github.com/rxue/dictionary/issues/13)

Commit: https://github.com/rxue/dictionary/commit/a343cbb74ae52a37cf04db03f65a29aba2b7f836
 

# Managing Entities
## The `EntityManager` Interface
[Chinese Tutorial](https://www.youtube.com/watch?v=xOMIxnxVUDg&list=PLmOn9nNkQxJFgOLf9mrDfndK55-1JNbPt&index=9i)

> An `EntityManager` and *persistence context* are **not required to be thread-safe**.

Reference: Java EE 7 Essentials > Chapter 13: Java Persistene > Persistene Unit, Persistence Context and Entity Manager

### Entity States
![Entity States](https://user-images.githubusercontent.com/3033388/270134754-9807cc3a-3c04-4cf2-8b8e-d52e3b66afbe.png)

### Finding Entities Using the `EntityManager`
Note! According to the [API doc of `EntityManager`](https://docs.oracle.com/javaee/7/api/javax/persistence/EntityManager.html) on each `find` method,

> If the entity instance is contained in the persistence context, it is returned from there

=> usually the `find` method would return an *Entity* inside the *persistence context*, meaning the returned *Entity* is in *Managed* state. 

### Comment:
So need to note that when using `EntityManager`, it is the responsibility of the client per se. to handle the big business transaction. 

### Practical Tips
 Operation| would call method on `EntityManager`
----------|--------------------------------------
 Add      | `persist`
 Update   | `merge`

# Querying Entities
## Practical Tips
Note! According to the [API doc of `EntityManager`](https://docs.oracle.com/javaee/7/api/javax/persistence/EntityManager.html) on each `createQuery` method, `persistence context` is not mentioned at all, which indicates that those returned list of *entities* are in *Detached* state and, update the queried result *entities* or remove them, it is always compulsory to `merge` these entities into the *persistence context* in the first step.

### *Entities* returned from `find` VS `createQuery`

Take its implementation in *Hibernate* (4.3.11.Final) as an example, in the source code https://github.com/hibernate/hibernate-orm/blob/4.3.11.Final/hibernate-entitymanager/src/main/java/org/hibernate/jpa/spi/AbstractEntityManagerImpl.java , its implementation on `<A> A find(Class<A> entityClass, Object primaryKey, LockModeType lockModeType, Map<String, Object> properties)` returns result by `session.get`. Whereas in the implementation of `<T> TypedQuery<T> createQuery(String jpaqlString, Class<T> resultClass)`, it returns an instance of `org.hibernate.jpa.internal.QueryImpl`
