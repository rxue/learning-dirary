# Part 1. Getting started with ORM
## Chapter 1. Understanding object/relational persistence
### 1.3 ORM and JPA
JPA specification:
 * ORM
 * `EntityManager`
 * JPQL
 * peristence engine does: *dirty checking*, association, fetch, etc.
## Chapter 2. Starting a project
### 2.2. "Hello World" with JPA
#### 2.2.1. Configuring a persistence unit
Value of `jta-data-source` element of the `persistence.xml` is the *JNDI* lookup name. So NOTE that `jta-data-source` is compulsory when the `transaction-type` of `persistence-unit` is `JTA`, in this case the JPA application will  `javax.naming.InitialContext`, from inside which it executes *JNDI* lookup by the value of `jta-data-source` to initialize `DataSource`
## Chapter 3. Domain models and metadata
new feature in JPA 2
* integration with *bean validation*
* `Metamodel` API
### 3.1. [The example `CaveatEmptor` application](http://www.jpwh.org/examples/jpwh/caveatemptor-jpa-061211/)
#### 3.1.1. Layered architecture
cross-cutting concerns: logging, authorization, transaction demarcation
#### 3.1.3. The `CaveatEmptor` *domain model*

### 3.2. Implementing the domain model
#### 3.2.1. Addressing *leakage of concerns*
cross-cutting concerns: security, concurrency, persistence, transactions, remoteness - intercepting calls to application components
#### 3.2.3. Writing persitence-capable classes
*fine-grained object* - more classes than tables

persistent classes is not required to 
 * implement `java.io.Serializable`. But there are cases `Serializable` is required: instances are stored in an `HttpSession` or *passed by value* using *RMI*
 * have *accessor methods* (specifically for *Hibernate*)

The persistence-capable classes (entity)
 * can be `abstract` and if needed can extends non-persistent class or implements interface
 * must be a top-level class i.e. not nested within another class
 * class itself and any of its methods can't be `final` (from JPA spec)
 * JPA (entity) requires constructor with no arguments. The constructor should be at least *package-private*

With Hibernate, You can make some accessor methods non-public or completely remove them - then configure Hibernate to rely on field access for these properties.

*dirty checking* : Hibernate automatically detect state changes in order to synchronize the updated state with database. Hibernate determine dirtiness by *comparing members by values*. But there is an exception **that *collection* members are compared by *identities*!** => alway return the same collection instance from *getter*

### 3.2.4. Implementing associations

## Chapter 5. Mapping value types
### 5.3. Mapping Java and SQL types with converters
#### 5.3.2. Creating custom JPA converters
##### Converting basic property values (1Z0-900)

`@Converter` is *compulsory* to the converter class, which is also compulsory to `implements AttributeConverter`
sample code: http://jpwh.org/examples/jpwh2/jpwh-2e-examples-20151103/model/src/main/java/org/jpwh/converter/MonetaryAmountConverter.java

`@Convert` is optional on the field of an *entity* annotated with `@Converter(autoApply = true)`

sample code without `@Convert` annotation: http://jpwh.org/examples/jpwh2/jpwh-2e-examples-20151103/model/src/main/java/org/jpwh/model/advanced/Item.java

Note: the `@Convert` does not have `value` attribute but `converter`, which is used to define the *converter* to be used
