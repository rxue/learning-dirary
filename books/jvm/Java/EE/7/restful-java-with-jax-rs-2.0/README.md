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

# Chapter 7: Server Responses and Exception Handling
## Exception Handling
### `javax.ws.rs.WebApplicationException`
