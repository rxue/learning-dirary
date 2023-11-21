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

The picture implies practical tips:
* `persist` is used to add entity into database
* `merge` is used to update entity inside database

NOTE also that `EntityManager.perisit` is `void`, whereas `EntityManager.merge` returns generic type `T`

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
# Chapter 11: Metadata for Object/Relational Mapping (spec)
## 11.1 Annotations for Object/Relational Mapping
### 11.1.48 `SequenceGenerator` Annotation
`allocationSize` : amount to increment by when allocating sequence numbers from the sequence. default: 50

**Practical tips in *Hibernate* implementation**

My previous misunderstanding: each insert will trigger the *sequence* 's `increment by`. But in the same time I also wonder why the ids of inserted rows are still incremented by 1 even though the default value of `allocationSize` is 50. Shouldn't it be so that the id of the inserted current row should be 50 more than the last that of the last inserted row?

Rectification: the purpose of using `allocationSize` is to avoid the trigger of *sequence* to get the next value during each insert since using sequence has performance impact. Assum `allocationSize` is the default 50, right after the JPA framework start and before the 1st row is inserted, the next value of the sequence, assume it as `a` is retrived once, and then the ids of the next 50 rows are all calculated by using the same value, `a`; then before inserting the 51th row, the next value of the sequence is retrieved for the second time, and then repeast this loop

Practical reference: https://github.com/rxue/dictionary/issues/124

Another practical tip on using the `allocationSize` is that in distributed system `allocationSize` is better off large such as 1000 since it then could be allocated for a single node

### 11.1.52 *Transient* Annotation
**Practical tips in *Hibernate* implementation**
*Hibernate* recognize the `@Transient` only on the getter, i.e. in case `@Transaction` is annotated on the *instance field* level, it would not be recognized

# Chapter 40: Using the *Criteria API* to Create Queries
## 40.3 Using the *Criteria API* and *Metamodel API* to Create Basic Typesafe Queries
### Executing Queries
#### *Single-Valued Query Result*

**Practical Tips about TypedQuery.getSingleResult**
This method call is assumed to get a single result, say in case of no result there will be `NoResultException`
 
## Practical Tips
Note! According to the [API doc of `EntityManager`](https://docs.oracle.com/javaee/7/api/javax/persistence/EntityManager.html) on each `createQuery` method, `persistence context` is not mentioned at all, which indicates that those returned list of *entities* are in *Detached* state and, update the queried result *entities* or remove them, it is always compulsory to `merge` these entities into the *persistence context* in the first step.

### *Entities* returned from `find` VS `createQuery`

Take its implementation in *Hibernate* (4.3.11.Final) as an example, in the source code https://github.com/hibernate/hibernate-orm/blob/4.3.11.Final/hibernate-entitymanager/src/main/java/org/hibernate/jpa/spi/AbstractEntityManagerImpl.java , its implementation on `<A> A find(Class<A> entityClass, Object primaryKey, LockModeType lockModeType, Map<String, Object> properties)` returns result by `session.get`. Whereas in the implementation of `<T> TypedQuery<T> createQuery(String jpaqlString, Class<T> resultClass)`, it returns an instance of `org.hibernate.jpa.internal.QueryImpl`
