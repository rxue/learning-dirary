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

