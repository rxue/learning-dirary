EJB Type		| From how many different clients	| Client Invocation Scenario	| Amounto of EJB Instances
------------------------|---------------------------------------|-------------------------------|-------------------------
session > `@Stateless`	| 1					| 2 separate calls to this EJB	| 2
session > `@Stateful`	| 1 					| 2 separate calls to this EJB	| 1
session > `@Stateful`	| 2 					| 2 separate calls to this EJB	| 2
session > `@Singleton`	| 2 					| 2 separate calls to this EJB	| 1
`@MessageDriven`	| 2					| 2 separate calls to this EJB	| ????

## [Handling Exceptions](https://docs.oracle.com/javaee/7/tutorial/ejb-basicexamples005.htm)
> If a *system exception* occurs within a transaction, the EJB container rolls back the transaction. However, if an *application exception* is thrown within a transaction, the container does not roll back the transaction

NOTE that in the book, Java EE 7 Essentials > Chapter 13 Java Persistence > Transactions and Locking, when explaining the sample code, there is statement "The transaction is automatically rolled back if an exception is thrown in the method". It is based merely on this sample code since the method signature `addStudent(Student student)` does not declare an exception due to the fact that the implementation `em.persist(student)` may only throw *system exception*, i.e. `RuntimeException`.

