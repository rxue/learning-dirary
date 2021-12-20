EJB Type		| From how many different clients	| Client Invocation Scenario	| Amounto of EJB Instances
------------------------|---------------------------------------|-------------------------------|-------------------------
Session > `@Stateless`	| 1					| 2 separate calls to this EJB	| 2
Session > `@Stateful`	| 1 					| 2 separate calls to this EJB	| 1
Session > `@Stateful`	| 2 					| 2 separate calls to this EJB	| 2
Session > `@Singleton`	| 2 					| 2 separate calls to this EJB	| 1
`@MessageDriven`	| 2					| 2 separate calls to this EJB	| ????



