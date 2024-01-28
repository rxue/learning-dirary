# Chapter 8. Legacy database and custom SQL
## 8.1. Integrating legacy databases
design tip: when you application inherits an existing legacy database schema, make as few changes to the existing schema as possible
### 8.1.1. Handling primary keys
design tip: many legacy schemas use (natural) composite primary keys, but this is discouraged
#### Mapping a composite natural key
design tip: critical to implement `hashCode` and `equals` methods of *ID class*
#### Composite keys with annotations
With JPA, composite keys are always encapsulated in a separate class, and the composite keys can be expressed in:

1. `@Embeddable` + `@Id` - `@GeneratedValue` : annotation ID class with `@Embeddable` => this annotated ID class can be referenced as a field annotated with `@Id` in the entity class and `@GeneratedValue` has to be ommitted 
2. annotation on the owning entity only without annotation on ID class:
 - `@EmbeddedId` : ID class can be referenced as a field with `@EmbeddedId` annotation
 - `@IdClass(ClassName.class)` + `@Id` : the owning entity class has to be annotated with `@IdClass(ClassName.class)` and all the properties of *ID class* has to be added to the owning entity class with `@Id` annotation (**NOTE! this strategy was added to JPA spec to support some legacy behavior**)


# Chapter 9: Working with objects
## 9.4 Java Persistence API
### 9.4.1 Storing and loading objects
#### Making an entity instance persistent
NOTE:
> `persist()` doesn't return the database identifier value of the entity instance

`public void persist(Object obj)`

### 9.4.2 Working with detached entity instances
#### Merging detached entity instances
`merge()`: In a *persistence context*, given an entity as the input to the `merge`, the *Java Persistence engine* checks the existence of the input inside the *persistence context*.

If the input *entity* does not exist in the *persistence context*, meaning the given instance is in **detached** state, there are 2 cases:

 * case 1: identifier, i.e. `@Id` field, of the *entity* exists in the corresponding persitent database table, a new *persistent instance* is copied from the database and, this new instance is updated on base of the given detached entity and it is the returned instance of this `merge`
 * case 2: identifier, i.e. `@Id` field, of the *entity* does not exists in the corresponding persistent database table, a new *persistence instance* is created and its values are updated on base of the given detached entity and it is the returned instance of this `merge`

