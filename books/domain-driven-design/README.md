# Part II: The Building Blocks of a Model-Driven Design
## Chapter Four: Isolating the Domain
### Layered Architecture

> The main structural characteristic of the *Layers* pattern is that the service of layer J are only used by layer J+1 - there are no further direct dependencies between layers. This structure can compared with a stack or even an onion. Each individual layer shields all lower layers from direct access by higher layers.

Reference: POSA 1.

## Chapter Six: The Lifecycle of a Domain Object
### Aggregates
> An AGGREGATE is a cluster of associated objects that we treat as a unit for the purpose of data changes.
### Repositories
> A subset of persistent objects must be globally accessible through a search based on object attributes. Such access is needed for the roots of AGGREGATES that are not convenient to reach by traversal. They are usually ENTITIES, sometimes VALUE OBJECTS with complex internal structure, and sometimes enumerated VALUES. Providing access to other objects muddies important distinctions. Free database queries can actully brach the encapsulation of domain objects and AGGREGATEs. Exposure of technical infrastructure and database access mechanisms complicated the client and obscures the MODEL-DRIVEN DESIGN.

> The REPOSITORY retrieves the requested object, encapsulating the machinery of database queries and metadata mapping.

> Provide REPOSITORIES only for AGGREGATE roots that actually need direct access.
