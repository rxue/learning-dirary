EJB Type		| From how many different clients	| Client Invocation Scenario	| Amounto of EJB Instances
------------------------|---------------------------------------|-------------------------------|-------------------------
session > `@Stateless`	| 1					| 2 separate calls to this EJB	| 2
session > `@Stateful`	| 1 					| 2 separate calls to this EJB	| 1
session > `@Stateful`	| 2 					| 2 separate calls to this EJB	| 2
session > `@Singleton`	| 2 					| 2 separate calls to this EJB	| 1
`@MessageDriven`	| 2					| 2 separate calls to this EJB	| ????



