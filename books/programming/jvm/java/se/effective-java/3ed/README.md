# Chapter 1 Creating and Destroying Objects
## Item 1: Consider static factory methods instead of constructors
> A *service provider framework* is a system in which providers implement a service, and the system makes implementations available to clients, decoupling the clients from implementations.

# Chapter 4 Classes and Interfaces
## Item 15: Minimize the accessibility of classes and members
*stray class*

## Item 16: In public classes, use accessor methods, not public fields
*degenerate class*

> If a class is *package-private* or is a private *nested class*, there is nothing inherently wrong with exposing its data fields

## Item 17: Minimize mutability (202302)

* *functional* approach
* `BitSet` as a better mutable alternative in some cases like multistep operations
* *mutable companion*
* static factory factory method along with private constructor as replacement of final class to achieve the immutability

## Item 20: Prefer Interfaces to Abstract Classes (20230704, 20230905)
**Takeaways**:

* Java's *single inheritance* on *abstract classes* severely constraints their use as *type definitions*.
* Interfaces are ideal for defining mixins (a type that a class can implement in addition to its "primary type"). NOTE! *Abstract classes* can't be used to define mixins for because they can't be retrofitted onto existing classes in that a class cannot have more than one parent
* *skeletal implementation class* - *Abstract Interface* : application in *collections framework* in Java SE: `AbstractCollection` , `AbstractSet` , `AbstractList` , `AbstractMap`
 * *simulated multiple inheritance*
# Chapter 5 Generics
## Item 28: Prefer lists to arrays
`List.of(...)` introduced, and note that there is `List.of()` without any parameters to initialize an empty list

# Chapter 6: `enum`s and *Annotations*
## Item 34: Use `enum`s instead of `int` constants
a way to associate different behavior with different constants: declare *abstract methods* in the `enum` and implement them in each `enum` element - *constant-specific method implementations*
## Item 35: Use instance fields instead of ordinals
> never derive a value associated with its ordinal; store it in an instance field instead

# Chapter 7: Lambda and Streams
## Item 45: Use Streams Judiciously (202301)
stream operations:

 * *intermediate*
 * *terminal*


* `computeIfAbsent` in `Map` since Java 8
* `sort` in `Arrays` in legacy Java

**practical takeaways**
benefit of using traditional code blocks over *lambda*:

 * read or modify any local variable in scope VS from a *lambda* you can **only** read `final` or *effectively final* variables => no way to modify any local variables
 * `return` value from encloding method
 * `break`/`continue` enclosing loop
 * `throw` *checked exception*

None of the above are possible in *lambda*

## Item 46: Prefer side-effect-free functions in streams (20230128, 20240628)
`forEach` is among the least powerful of the *terminal operations* and the least stream-friendly

> The `forEach` operation should be used only to report the result of a *stream* computation, not to perform the computation.


## Item 47: Prefer `Collection` to `Stream` as a return type

 `Stream` <-> `Iterable`

 `Stream.of` accept array data

> do not store a large sequence in memory just to return it as a `Collection`

> In order to write a `Collection` implementation atop `AbstractCollection`, you need to implement only two methods beyond the one required for `Iterable`:  `contains` and `size`

`Stream.concat`

# Chapter 8. Methods
## Item 51: Design method signatures carefully
* Choose method names carefully
* Don't go overboard in providing convenience method
> ...Too many methods make a class difficult to learn, use, document, test, and maintain.
* Avoid long parameter lists
* For parameter types, favor interfaces over classes
* Prefer two-element `enum` types to `boolean` parameters

## Item 55: Return optionals judiciously

Motivation of using optional

 * throwing Exception is expensive, entire stack trace is captured when an exception is created
 * `NullPointerException` caused by returning `null`

* `Optional.orElse()` is used to specify default value
* `Òptional.orElseThrow()` is an *exception factory

New features in Java SE 9

* `Optional.or()`
* `Optional.ifPresentOrElse()`

> Many uses of `ìsPresent()` can profitabily be replaced by one of the methods mentioned above

=> Use `isPresent()` as the last resort

> Never return a null value from an Optional-returning method

> Container types, including *collections*, `Map`, `Stream`, *arrays* and `Optional` should not be wrapped in optionals

> Never return an optional of a boxed primitive type

> Never use `Optional` as map values

Storing `Optional` in an *instance field* is a "bad" code smell


## Item 56: Write doc comments for all exposed API elements
> **The doc comment for a method should describe succinctly the contract between the method and its client** ... Typically *preconditions* are described implicitly by the `@throws` tags for *unchecked exceptions*;
> To describe a method's contract fully, the doc comment should have an `@param` tag for every parameter, and `@return` tag unless the method has a void return type, and an `@throws` for every exception thrown by the method, whether checked or unchecked.

# Chapter 9. General Programming
## Item 61: Prefer primitive types to boxed primitives
### Key Notes for Myself
* primitive are more time- and space-efficient than boxed primitives
* When your program compares two *boxed primitives* with the `==` operator, it does an (object) identity comparison, which is almost certainly not what you want
* when your program does unboxing, it can throw a ``NullPointerException`
## Item 67: Optimize judiciously
> pervasive architectual flaw that limit performance can be impossible to fix without rewriting the system

## Item 67: Optimize judiciously

# Chapter 10. Exceptions
## Item 70: Use checked exceptions for recoverable conditions and runtime exceptions for programming errors

## Item 74: Document all exceptions thrown by each method
> **Always declare checked exception individually, and document precisely the conditions under which each one is thrown** using the Javadoc `@throws` tag. Don’t take the shortcut of declaring that a method throws some superclass of multiple exception classes that it can throw. As an extreme example, don’t declare that a public method throws Exception or, worse, throws `Throwable`.

### Key Notes for Myself
As to the following sentence:

>  As an extreme example, don’t declare that a public method throws Exception or, worse, throws `Throwable`

This is primarily a tip about the *concrete classes* in my opinion. `throws Exception` indeed appears for instance in Java SE API:

 * `Autocloseable`: `void close() throws Exception`
 * `Callable<V>` : `V call() throws Exception`

In Java EE 7 API:
 * `javax.batch.api.chunk.ItemReader` : `Object readItem() throws Exception`

However, they are rare cases, and kinda last resort and on the other hand, 

> While the language does **not require** programmers to **declare the unchecked exceptions that a method is capable of throwing** , it is wise to document them as carefully as the checked exceptions.

> **Use the Javadoc `@throws` tag to document each exception that a method can throw, but do not use the `throws` keyword on unchecked exceptions**

> In summary, ... Declare each checked exception individually in a method's `throws` clause, but do not declare *unchecked exceptions*. ...

### Takeaway
NOTE that in Java language syntax uncheked exceptions can be declared in a method's `throws` clause, but that is probably merely due to the case of declaring any types of exceptions in the `main` method, and in all other methods it does not make sense to declare unchecked exceptions
