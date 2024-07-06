# Repository
> A *repository* mediates between the domain and data mapping layers, acting like an in-memory domain-object collection.

* domain objects aren't typically stored directly in the Repository
* With a Repository, client code constructs the criteria and then passes them to the Repository, asking it to select those of its objects that match
* The object source for the Repository may not be a relational database at all, which is fine as Repository lends itself quite readily to the replacement of the data-mapping component via specialized strategy objects.
* Repository's interface shields the domain layer from awareness of the data source, we can refactor the implementation of the query code inside the repository without changing any calls from clients
> Under the covers, *repository* combines *metadata mapping* with a *query object* to automatically generate SQL code from the criteria.

## When to Use It
In a large system with many domain object types and many possible queries, Repository reduces the amount of code needed to deal with all the querying that goes on.

# Self Summary
*Repository* uses *Query Object*, whereas *Query Object* uses *Metadata Mapping*, which can be retrieved from *Unit of Work*. Direct communication with database, such as `Statement.execute()` etc. in the context of Java, usually happens only in *metadata mapping*, so *repository* does not necessarily communicate with data store, communication with data store just depends depends on the implementation of *repository*

