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

