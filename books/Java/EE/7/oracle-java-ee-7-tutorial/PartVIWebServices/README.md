# 29 Building RESTful Web Services with JAX-RS
## [What are RESTful Web Services?](https://docs.oracle.com/javaee/7/tutorial/jaxrs001.htm)

> REST is an *architectual style* of client-server application centered around the transfer of representations of resources through requests and responses. In the *REST* architectual style, data and *functionality* are considered *resources* and are accessed using Uniform Resource Identifiers (URIs), typically links on the web.

Simple, lightweight and fast are based on the following principles:

* Resource identification through URI
* Uniform interface: ...`POST` transfers a new state onto a resource
* Self-descriptive messages: resources are *decoupled* from their representation so that their content can be accessed in a variety of formats
* ~~Stateful interactions through links~~: Every interaction with a resource is stateless; that is, **request messages are self-contained.** ... State can be embedded in response messages to point to valid future states of the interaction.

Own Comment:

## Creating a RESTful Root Resource Class
### Developing RESTful Web Services with JAX-RS
> ... JAX-RS annotations are *runtime anntoations*; therefore, runtime reflection will generate the helper classes and artifacts for the resource.

#### Summary of *JAX-RS* Annotations
##### retrieval of HTTP Methods
* `@GET`
* `@POST`
* `@PUT`
* `@DELETE`
* `@HEAD`

##### value from the URI:

* `@ApplicationPath`
* `@Path`
* `@PathParam`
* `QueryParam`

##### Mime Type specification:

* `@Produces`
* `@Consumes`

##### anything that is of interest to JAX-RS runtime

* `@Provider`


# 31 JAX-RS: Advanced Topics and an Example
## Annotations for Field and Bean Properties of Resource Classes
### Advanced JAX-RS Annotations
