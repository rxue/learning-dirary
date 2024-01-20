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

*dirty checking* : Hibernate automatically detect state changes in order to synchronize the updated state with database

# Chapter 6. Mapping Inheritance
## 6.8 *Polymorphic associations*
### 6.8.1 Polymorphic *many-to-one* associations
### 6.8.2 Polymorphic collections
# Chapter 7. Managing collections and entity associations
Heart of ORM : manage associations between classes and relationships between tables
**Major new features in JPA 2**
## 7.1. Sets, bags, lists and maps of value types
### Selecting a collection interface
`java.util.Collection` - *bag* semantics
### 7.1.5. Mapping an identifier *bag*
*Bag* : an *unordered collection* that allows duplicate elements

## 7.2. Collections of components
### 7.2.2. Set of components

## 7.3. Mapping entity associations
> The term *parent/child* implies some kind of *life cycle dependencies*

*Association* between entity classes don't have a dependent life cycle: An instance can be saved, updated, and removed without affecting any other

# Chapter 8. Advanced entity association mappings
## 8.2 one-to-many associations

# Chapter 11. Transactions and Concurrency
## 11.2 Controlling Concurrent Access
# Chapter 5. Mapping Value Types
## 5.3. Mapping Java and SQL types with converters
*Java-to-SQL type conversion*
### 5.3.1. built-in types
#### Primitives and Numeric Types

### 5.3.2. Creating Custom JPA Converters
*value-typed class* 
 * *immutable* 
 * should `implements Serializable` when Hibernate stores entity instance data in the shared second-level cache
#### CONVERTING BASIC PROPERTY VALUES

#### Character Types

# Chapter 7. Mapping collections and entity associations
## 7.3. Mapping entity associations
### 7.3.1. The simplest possible association
> when you see a *foreign key* column and two entity classes involved, you should probably map it with `@ManyToOne` and nothing else

**My own practice of unidirectional `@OneToMany`:** https://github.com/rxue/dictionary/issues/129

### 7.3.2. Making it bidirectional
primary benifit of `@OneToMany` : *navigational access* to data

# Chapter 11. Transactions and Concurrency

### 11.2.2 Optimistic Concurrency Control
*Versioning* is turned off by default. 
It is a *first commit win*
It results in *first commit win*
Versioning is enabled with `@Version`

You shouldn't have setter method `setVersion`

version field can be `int`, `short`, `long` along with their auto-boxing types. Hibernate wraps and start from 0 again if version number reaches the limit of the data type

![How does the automatic optimistic locking work](https://private-user-images.githubusercontent.com/3033388/294563779-a0986792-3703-423c-a446-03036babb48a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDQ0NzUxMzYsIm5iZiI6MTcwNDQ3NDgzNiwicGF0aCI6Ii8zMDMzMzg4LzI5NDU2Mzc3OS1hMDk4Njc5Mi0zNzAzLTQyM2MtYTQ0Ni0wMzAzNmJhYmI0OGEucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI0MDEwNSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNDAxMDVUMTcxMzU2WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ODg3YjhjZTc0OTBjNDg4MTI2MDNlM2FiMWMwMGY0MmRlNWU5MmExNDc2OTFlOGZlMjhhMWU3NTA1NDFmMGQ3NSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmYWN0b3JfaWQ9MCZrZXlfaWQ9MCZyZXBvX2lkPTAifQ.K9DsdrHDWpi0t_t3PEfQKcWGkCZ8Hk4D-mOAhcw8bak)

The failed transaction will encounter `javax.persistence.OptimisticLockException`

#### MANUAL VERSION CHECKING


### Explicit Pessimistic Locking

# Chapter 12. Fetch plans, strategies and profiles
## 12.1. Lazy and eager loading
### 12.1.1. Understanding entity proxies

