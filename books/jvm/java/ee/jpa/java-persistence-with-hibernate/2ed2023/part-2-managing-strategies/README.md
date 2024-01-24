# Part 2. Mapping strategies
## Chapter 4. Mapping persistent classes
### 4.1. Understanding *entities* and *value types*
#### 4.1.1. Fine-grained domain models
design tip: when designing an `EmailAddress` *value* class, it may provide a `prepareEmail()` method (but not `sendEmail()` because it is a bad idea to make this `EmailAddress` class have dependency on the email sub-system)
#### 4.1.2. Defining application concepts
design tip: 
 * since you want to have CRUD operation on `User` => `User` is an entity
 * take `Address` as an example, if there exists `Address` being shared among multiple `User` then the `Address` is an `Entity` - think about it, when removing a `User` you cannot remove the `Address` if it is shared by other users

> An instance of *value type* has no persistence identifier property, it belongs to an entity instance. Its lifespan is bound to the owning entity instance. => A value type doesn't support shared references. 

#### 4.1.3. Distinguishing entities and value types
design tip: 
 * use stereotype in UML to differentiate between *entity* and *value type*
 * relationship between an entity and its *value types* is *composition* especially from the lifecycle aspect
 * prefer always *value type* to *entity* (this kinda corresponds to the OO design principle - favor composition over inheritance)
 * strive for simplicity: persistent collections, e.g., frequently add complexity without any benifit. For instance, instead of mapping `Item#bids` and `User#bids`, query all `bids` for `Item`/`User`

## Chapter 5. Mapping Value Types
### 5.3. Mapping Java and SQL types with converters
*Java-to-SQL type conversion*
#### 5.3.1. built-in types
##### Primitives and Numeric Types

#### 5.3.2. Creating Custom JPA Converters
*value-typed class* 
 * *immutable* 
 * should `implements Serializable` when Hibernate stores entity instance data in the shared second-level cache
##### CONVERTING BASIC PROPERTY VALUES

##### Character Types

## Chapter 6. Mapping Inheritance
### 6.8 *Polymorphic associations*
#### 6.8.1 Polymorphic *many-to-one* associations
#### 6.8.2 Polymorphic collections
## Chapter 7. Managing collections and entity associations
Heart of ORM : manage associations between classes and relationships between tables
**Major new features in JPA 2**
### 7.1. Sets, bags, lists and maps of value types
#### Selecting a collection interface
`java.util.Collection` - *bag* semantics
#### 7.1.5. Mapping an identifier *bag*
*Bag* : an *unordered collection* that allows duplicate elements

### 7.2. Collections of components
#### 7.2.2. Set of components

### 7.3. Mapping entity associations
> The term *parent/child* implies some kind of *life cycle dependencies*

*Association* between entity classes don't have a dependent life cycle: An instance can be saved, updated, and removed without affecting any other

#### 7.3.1. The simplest possible association
> when you see a *foreign key* column and two entity classes involved, you should probably map it with `@ManyToOne` and nothing else

**My own practice of unidirectional `@OneToMany`:** https://github.com/rxue/dictionary/issues/129

#### 7.3.2. Making it bidirectional
primary benifit of `@OneToMany` : *navigational access* to data

## Chapter 8. Advanced entity association mappings
### 8.2 one-to-many associations

