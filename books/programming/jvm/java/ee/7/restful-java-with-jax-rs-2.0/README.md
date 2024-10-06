# Chapter 1: Introduction to REST
## The Uniform, Constrained Interface

HTTP method | operations          | practical features  
------------|---------------------|-------------------------------------------------------------------------------------------------------------------
`PUT`       | *insert*, *update*  | client knows the identity of the resource to be created or updated. Analogy: MS word document that you are editing
`DELTE`     | *delete*            | ...
`POST`      | ?                   | non-idempotent: to change state of resource

## Representation-Oriented
Header:

* `content-type` tells the client/server about the data format it is receiving
* with `Accept` a client can list its preferred response format
* `MIME` type can `version`

## Communicate Statelessly (20241006)
 
 * no client session data stored on the server. If there is need to be session-specific data, it should be held and maintained by the client and transferred to the server with eash request as needed

**OWN COMMENT**
So it doesn't mean the server is fully stateless. The server can have state and should have usually, but the state is about whole data resources regardless of any individual request. For instance, frequently requested data can be cached so that retrieval of it is fast. But the cache is to the whole data resource. The purpose of such architecture is the *horizontal salability*

# Chapter 2: Designing RESTful Services
## Model the URIs
`LineItem`s are aggregated within `Order` => `LineItem` is a sub-resource

# Chapter 3: Your First JAX-RS Service
## Developing a JAX-RS RESTful Service
### CustomerResource: Our JAX-RS Service
#### Retrieving Customers
**Practical tips** : `WebApplicationException(Response.Status.NOT_FOUND)` for resource not found
### JAX-RS and Java Interfaces

# Chapter 4: HTTP Method and URI Matching
## `@Path`
### `@Path` Expressions
#### *Template parameters*
#### *Regular expressions*
#### *Precedence Rules*
on base of *most specific match wins*
### *Matrix Parameters*

# Chapter 5: *JAX-RS* Injection
## `@PathParam`
### `PathSegment` and *Matrix Parameters*
### Programmatic URI Information
`@Context UriInfo info`

## `@MatrixParam`
Practical tip: use either `PathSegment` or `@MatrixParam`, but not both

## `@CookieParam`
Practical tip: 
* Cookies can be used to remember identity and user preferences between requests

# Chapter 6: JAX-RS Content Handlers
## JAXB
### JAXB JAX-RS Handlers
Often times you need to configure your own `JAXBContext` instances to get the output you desired => `javax.ws.rs.ext.ContextResolver` with generic type is used to override the default `JAXBContext` creation

**My own practical comment:** In practice, `ContextResolver` can be used not only to configure `JAXBContext` but also `Jsonb` (new feature of Java EE 8) for instance to convert some special type of attributes in *json* input
example use case: https://github.com/rxue/dictionary/issues/141
- example code as the solution: https://github.com/rxue/dictionary/tree/129-unidirectional-one-lexical-item-to-many-explanations/web/java/app/src/main/java/rx/dictionary/rest/config/jsonb

# Chapter 7: Server Responses and Exception Handling
## Exception Handling
### `javax.ws.rs.WebApplicationException`

# Securing JAX-RS
## Authentication and Authorization in JAX-RS
> To enforce authentication, you must specify a URL pattern you want to secure.
