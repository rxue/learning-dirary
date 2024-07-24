# Part 3. Transactional data processing
## Chapter 10. Managing data
**New features in JPA 2***
`EntityManager#unwrap()` to get *vendor-specific* API

### 10.2 `EntityManager` interface
#### 10.2.2. Making data persistent
NOTE! When using *Hibernate*, `PersistenceUnitUtil#getIdentifier(e)` never returns `null` your identity is a *primitive*. This is also a key reason for using auto-boxed object type instead of *primitive*

**MY OWN**
The states correspondence in this book against that in JPA spec
This book's state | state in JPA spec | state of id | in *persistence context* or not(`EntityManager#contains(e)`)  | explanation
------------------|-------------------|-------------|---------------------------------------------------------------|---------------------
 transient        | *new*             | unassigned  | `false`                                                       | ?
 persistent       | *managed*         | assigend    | `true`                                                        | when `persist()` is called, *id* of the entity is assigned and the entity is managed by the *persistence context*
 detached         | *detached*        | assigned    | `false`                                                       | detached from *persistence context*
 removed          | *removed*         | assigned    | `false`                                                       | `EntityManager#remove()` - scheduled for being removed from the database

#### 10.2.3 Retrieving and modifying persistent data

**Key takeaways**
 
* *Hibernate* propagate state change to the database as late as possible, towards the end of the transaction
* DML statements usually create locks in the database that are held until transaction completes 
* If one wants to include only modified columns in the Hibernate's generated SQL statement, *dynamic SQL generation* should be enabled, refer to section 4.3.2
* *persistence context* enables *repeatable read*

#### 10.2.4. Getting a reference
managed entity becomes *detached* when its residing persistence context is closed

#### 10.2.5. Making data transient

#### 10.2.6. Refreshing data
In practice, most applications don't have to mannually refresh in-memory state; concurrent modifications are typically resolved at transaction commit time

#### 10.2.9. *Flushing* the *persistence context*
*Hibernate*, as a JPA implementation, synchronizes at the following time:
* when a joined JTA system transaction is *committed*
* Before a query is executed - not `find()` but when using API such as `javax.persistence.Query` etc.
* explicit `flush()`


### 10.3. Working with *detached* state
#### 10.3.2. implementing equality methods
**Key takeaways**
It is a bad practice to use the `id` field only to implement `equals`
main reason: identifier values aren't assigned by Hibernate until instance becomes persistent. *hashCode* value changes before and after the entity becomes *managed* with id value generated. 

Think about an entity `Person` including a `Set` of `Child` with `@OneToMany(cascade = CascadeType.ALL)` associations, meaning a *new* `Person` entity with a `Set` of `Child`  is expected to be persisted to the *persistence context* in cascade. In this case if the `Child.equals` is implemented by using `id`, it is possible to add only one new `Child` (without id yet) to the `Person`'s `Set<Children>`

#### 10.3.3. Detaching entity instances
**Key takeaways**
modifying the loaded entity after the *persistence context* is closed will not be persisted to database

## Chapter 11. Transactions and Concurrency
### 11.2 Controlling Concurrent Access
#### 11.2.1 Understanding database-level concurrency
##### Choosing an isolation level
* eliminate *read uncommitted*
* *Phantom read* aren't usually problematic

JPA spec's assumption of the default level: *read committed* => developers using JPA have to deal with *unrepeatable read*, *phantom read* and the *last commit wins* problems
versioning switches to *first commit win*

In a *JPA* application using *Hibernation* implementation, *JDBC* `Connection` can be obtained from native `org.hibernate.Session` API

#### 11.2.2 Optimistic Concurrency Control
use case: when concurrent modifications are rare
*Versioning* is turned off by default => Hibernate results in *last commit win* without any extra configuration
##### ENABLE VERSIONING
Versioning is enabled with `@Version` on an additional property of your entity class, i.e. it does not have any business meaning by default
It is a *first commit win*
It results in *first commit win*

NOTE! You shouldn't have setter method `setVersion`, since this is only used by Hibernate internally

version field can be `int`, `short`, `long` along with their auto-boxing types. Hibernate wraps and start from 0 again if version number reaches the limit of the data type

Hibernate compares version when executing `delete` and `update` SQL statement 

![How does the automatic optimistic locking work](https://private-user-images.githubusercontent.com/3033388/294563779-a0986792-3703-423c-a446-03036babb48a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDQ0NzUxMzYsIm5iZiI6MTcwNDQ3NDgzNiwicGF0aCI6Ii8zMDMzMzg4LzI5NDU2Mzc3OS1hMDk4Njc5Mi0zNzAzLTQyM2MtYTQ0Ni0wMzAzNmJhYmI0OGEucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI0MDEwNSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNDAxMDVUMTcxMzU2WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ODg3YjhjZTc0OTBjNDg4MTI2MDNlM2FiMWMwMGY0MmRlNWU5MmExNDc2OTFlOGZlMjhhMWU3NTA1NDFmMGQ3NSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmYWN0b3JfaWQ9MCZrZXlfaWQ9MCZyZXBvX2lkPTAifQ.K9DsdrHDWpi0t_t3PEfQKcWGkCZ8Hk4D-mOAhcw8bak)

The failed transaction will encounter `javax.persistence.OptimisticLockException`

##### VERSIONING WITH TIMESTAMPS
* JPA only considers `java.sql.Timestamp` portable
* in theory versioning with timestamp is unsafe since there is tiny possbility that 2 operations happens during the same milliseconds, which is the Java's timestamps' minimum accuracy

##### VERSIONING WITHOUT VERSION NUMBERS OR TIMESTAMPS
*Hibernate* specific feature

##### MANUAL VERSION CHECKING
`setLockMode(LockModeType.OPTIMISTIC)` to achieve *repeatable read* : check the entity version at flush time

example use case: in a `@ManyToOne` releationship - `item#category`, if we want to sum up the price of each category in a read-committed transaction, there is possibility of *unrepeatable read* that item in one category are moved to another category. In this case price of that moved item might be added to 2 different categories => manual version checking is needed

NOTE! The core of the example is that the item is not to be updated in the transaction using the `OPTIMISTIC` lock

no batch support : if you update 100 entities (e.g. `Item` in the example), you get 100 additional SQL query on the version at flush time
##### FORCING A VERSION INCREMENT
`LockModeType.OPTIMISTIC_FORCE_INCREMENT`

#### 11.2.3. Explicit Pessimistic Locking

##### What about lock modes `READ` and `WRITE`
They are legacy from JPA 1.0 and not preferred for new applications

`LockModeType.READ` = ``LockModeType.OPTIMISTIC`
`LockModeType.WRITE` = ``LockModeType.OPTIMISTIC_FORCE_INCREMENT`

### 11.3. *Non-transactional data access*
#### 11.3.1. Reading data in *auto-commit mode*

## Chapter 12. Fetch plans, strategies and profiles
### 12.1. Lazy and eager loading
#### 12.1.1. Understanding entity proxies
#### 12.1.4. Eager loading of associations and collections
in `@OneToMany` association, the *default* value of its `fetch` attribute is `FetchType.LAZY`. This indicates that `FetchType.EAGER` is not recommended in practice
 
### 12.2. Selecting a fetch strategy
#### 12.2.1. The *n+1 selects* problem
#### 12.2.2. The *Cartesian product* problem
demo code for Entity causing *cartesian product* : [`org.jpwh.model.fetching.cartesianproduct.Item`](http://jpwh.org/examples/jpwh2/jpwh-2e-examples-20151103/model/src/main/java/org/jpwh/model/fetching/cartesianproduct/Item.java)

> Eager fetching more than one collection at once with SQL `join` operator is the fundamental issue, no matter what the collection content is

NOTE! The *cartesian product* in the given example is as per that one `Item` entity instance. At the end of this section it was mentioned that solution for such cartesian product is to use 3 separate queries

#### 12.3. Using fetch profiles
##### 12.3.2. Working with entity graphs
*enity graph* is used to change the *default lazy fetch* of entities to *eager fetch*

