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

## Communicate Statelessly
* no client session data stored on the server. If there is need to be session-specific data, it should be held and maintained by the client and transferred to the server with eash request as needed

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


# Chapter 7: Server Responses and Exception Handling
## Exception Handling
### `javax.ws.rs.WebApplicationException`
