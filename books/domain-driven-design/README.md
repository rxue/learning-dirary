# Part II: The Building Blocks of a Model-Driven Design
## Chapter Four: Isolating the Domain
### Layered Architecture

> The main structural characteristic of the *Layers* pattern is that the service of layer J are only used by layer J+1 - there are no further direct dependencies between layers. This structure can compared with a stack or even an onion. Each individual layer shields all lower layers from direct access by higher layers.

Reference: POSA 1.

## Chapter Five: A Model Expressed in Software
### Associations
> In real life, there are lots of many-to-many associations, and a great numbers are naturally *bidirectional*. The same tends to be true of early forms of a model as we brainstorm and explore the domain. But these general associations complicate implementation and maintenance. Furthermore, they communicate very little about the nature of the relationship.

> There are at least three ways of making associations more tractable.

> 1. Imposing a traversal direction
> 2. Add a qualifier, effectively reducing multiplicity
> 3. reducing non-essential associations

### Value Objects
#### Designing Associations That Involve *Value Objects*
> while bidirectional associations between ENTITIES may be hard to maintain, bidirectional associations between two VALUE OBJECTS just make no sense.
### Services
> A good service has three characteristics.
> 1. The operation relates to a domain concept that is not a natural part of an *ENTITY* or *VALUE OBJECT*.
> 2. The interface is defined in terms of other elements of the domain model.
> 3. The operation is *stateless*

> Statelessness here means that any client can use any instance of a particular *SERVICE* without regard to the instance's individual history. The execution of a SERVICE will use information that is accessible globally, and may even change that global information (that is, it may have side effect). But the *SERVICE* doesnot hold state of its own that affect its own behavior, as most domain objects do.
