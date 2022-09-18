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

### Comment:
So need to note that when using `EntityManager`, it is the responsibility of the client per se. to handle the big business transaction. 

### Practical Tips
 Operation| would call method on `EntityManager`
----------|--------------------------------------
 Add      | `persist`
 Update   | `merge`


