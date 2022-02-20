# Chapter 5: Concurrency
## Concurrency Problems
```
 concurrency.locking - 7 classes
 concurrency.multiphase - 5 classes
```
* lost update
* inconsistent read

* liveness: how much concurrent activity can go on
## Isolation and Immutability
> You only get concurrency problems if the data you're sharing can be modified

## Transactions
### Reducing Transaction Isolation for Liveness
> If you have full isolation, you get serializable transactions.

> To be sure of correctness you should always use *serialiable* isolation level. The problem is that serializable really messes up the liveness of a system, so much so that you often have to reduce serializability in order to increase throughput. ...

#### Business and System Transactions

> The obvious answer to supporting the ACID properties of a business transaction is to execute the entire business transaction within a single system transaction. Unfortunately **business transactions often take multiple requests to action**, so using a single system transaction to implement one results in a long system transaction. Most transaction systems don't work very efficiently with long transactions.
> 
> This doesn't mean that you should never use long transactions. ...Using a long transaction means you avoid a lot of awkward problems. However, the application won't be scalable because long transactions will turn the database into a major bottleneck. ...
>
> For this reason **many enterprise applications can't risk long transaction. In this case you have to break the business transaction down into a series of short transactions. This means that you are left to your own device to support the ACID properties of business transactions between system transactions - a problem we call *offline concurrency*.** ... 

# Chapter 10: Data Source Architectural Patterns
## Data Mapper
### How It Works
> The problem with a *rich constructor* is that you have to aware of cyclic references. If you have two objects that reference each other, each time you try to load one it will try to load the other, which will in turn try to load the first one, and so on, until you run out of stack space.  Avoid this require special case code, often using *lazy load*. Writing this special case code is messy, so it's worth trying to do without it. You can do this by creating an **empty object**. Use *no-arg constructor* to create a blank object and insert that empty object immediately into the *identity map*. That way you have a cycle, the *identity map* will return an object to stop the recursive loading.
>
> Using an empty object like this means you may need some setters for values that are truly immutable when the object is loaded. A combination of a naming convention and perhaps some status-checking guards can fix this. You can also use reflection for data loading.

# Chapter 15: Distribution Patterns
## Data Transfer Object
> An object that carries data between processes in order to reduce the number of method calls

### Example: Serializing Using XML (Java)
* *marker interface*
* *JAXB*

# Chapter 16: Offline Concurrency Patterns
## Optimistic Offline Lock
### When to Use It
> Optimistic concurrency management is appropriate when the chance of *conflict* between any two business transactions is low. ... *Pessimistic Offline Lock* is more appropriate when the chance of conflict is high or the expense of a conflict is unacceptable.
i
## Pessimistic Offline Lock

# Chapter 18: Base Patterns
> A well-known object that other objects can use to find common objects and services

A *Registry* is essentialy a global object.
## How It Works
> A common kind of *Registry* data is thread scoped. A good example is a database connection. In this case many environments give you some form of thread-specific storage, such as Java's thread local. Another technique is a dictionary keyd by thread whose value is an appropriate data object. A request for a connection results in a lookup in that dictionary by the current thread.

## When to Use It
> Basically, you should only use a *Registry* as a last resot.
