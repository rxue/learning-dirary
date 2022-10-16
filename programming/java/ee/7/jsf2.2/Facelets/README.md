`@Named` annotation makes the *CDI bean* (previously called *managed bean*) accessible through the *EL*.

`ViewScoped` remains active while the client continues to interact with the same page. The scope becomes inactive once the client navigate to a different page. This is useful when coding the pages that you expect to post back to themselves.

Reference: Java EE 7, The Big Picture > Chapter 4: Assembling Dynamic Web Pages: JavaServer Faces > Java EE Managed Beans > `@ViewScoped`

