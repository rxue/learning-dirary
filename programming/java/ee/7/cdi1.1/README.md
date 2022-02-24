# CDI 1.1
## Using Scopes
Scope		| Annotation	| Meaning
----------------|---------------|---------
Dependent	| `@Dependent`	| The CDI runtime instantiates a default scope CDI bean instance every that it is injected into a consumer object. The bean instance **inherits the scope of the consume instance**. If a CDI bean does not declare a scope, it defaults to having dependent scope.

## [Tutorial](https://www.youtube.com/watch?v=VNCMwQhWKOw)
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=309s 	Problem: where do we create this instance of the DAO
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=334s	-- problem: using `new` keyword is tight-coupling
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=386s	---- Java EE 5 solution to this problem - `@EJB` the *basic* form of dependency injection
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=400s	------ detail:
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=491s	------ problem 1: `@EJB` only works for EJBs
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=502s	-------- e.g. if we don't want the `DataAccessImplementation` to be EJB
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=518s	---------- strip the `@Stateless` to make it not an EJB anymore, then the `@EJB` will not work
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=553s	---------- it is fair to say that being forced to make a class a full-blown EJB just so you can inject it as a dependency feels a bit **heavy**
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=574s	---------- if you want to access the database directly instead of `EntityManager`, `DataSource` can be injected with `@Resource`
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=666s	------ problem 2: annotations are unclealy named
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=690s	-------- it is not clearly saying that it is an *injection point*
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=733s	------ problem 3: the dependency injections will only work with EJBs
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=774s	------ summary: *classic dependency injection* is limited and not well designed, kinda rushed into the spec

* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=858s	-- **CDI**
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=1055s 	---- demo: note! none of the classes are EJB
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=1162s 	------ in order to make DI work, we need (CDI) container that is going to instantiate the object
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=1181s	-------- possible to run a CDI outside an application server!
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=1380s	------ **`@Inject` is the upgraded replacement of old-fashioned `@EJB`**
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=1447s	------ CDI project configuration
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=1470s	-------- need `META-INF/beans.xml`
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=1494s	---------- recomended to keep the root elements in the `beans.xml`
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=1704s	------ highly recommended features in CDI
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=1897s	-------- problem with multiple implementation on an interface to be inejcted: `AmbiguousResolutionException`
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=1967s	---------- an elegant way of resolving the problem
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=1984s	------------ `@Default` - the regularly used implementation of the interface
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=2009s	------------ `@Alternative`
* https://www.youtube.com/watch?v=VNCMwQhWKOw&t=2070s	------------ make `@Alternative` implementation used by means of `beans.xml`
