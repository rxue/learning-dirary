# 1 Introduction
## Transaction Models
*Programmatic Transaction Model* in JTA

It is used to manages *transactions*, not *connections* in local transaction model, with `javax.transaction.UserTransaction` interface

`UserTransaction`:
* `begin()`
* `commit()`
* `rollback()`
## The Programmatic Transactional Model
### Programmatic Transaction Coding Traps

label: `1Z0-900`

# 4 The Declarative Transaction Model
## Transaction Attributes
**REQUIRED**
If the process is in existing transaction context, the container does nothing, otherwise the container would start a new transaction
