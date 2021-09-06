# Breakdown of Java EE 7
 
`groupId`       | `artifactId`      |Version  |Description                                                    |Reference
----------------|-------------------|---------|-------------------------------------------------------------- |----------------------------
`javax.servlet` |`javax.servlet-api`|3.1      |Servlet API                                                    | ?
`org.glassfish` |`java.faces`       |2.2      |including both API and implementation, and source code checked |[javaserverfaces-spec](https://javaee.github.io/javaserverfaces-spec/)
`org.hibernate` |`hibernate-core`   |5.2      |Implementation of JPA 2.1                                      |<ul><li><a href="https://hib    ernate.org/orm/releases/">Java EE 7 > Java Persistence API</a></li><li><a href="https://hibernate.org/orm/releases/">Hibernate Releases</a></li></ul>

# Java EE 7
## CDI
### [Tutorial](https://www.youtube.com/watch?v=VNCMwQhWKOw)
https://www.youtube.com/watch?v=VNCMwQhWKOw&t=309s 	Problem: where do we create this instance of the DAO
https://www.youtube.com/watch?v=VNCMwQhWKOw&t=334s		problem: using `new` keyword is tight-coupling
https://www.youtube.com/watch?v=VNCMwQhWKOw&t=386s			Java EE 5 solution to this problem - `@EJB`

