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
