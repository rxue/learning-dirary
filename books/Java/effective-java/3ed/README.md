# Chapter 1 Creating and Destroying Objects
## Item 1: Consider static factory methods instead of constructors
> A *service provider framework* is a system in which providers implement a service, and the system makes implementations available to clients, decoupling the clients from implementations.

# Chapter 4 Classes and Interfaces
## Item 17: Minimize mutability (202302)

* *functional* approach
* `BitSet` as a better mutable alternative in some cases like multistep operations
* *mutable companion*
* static factory factory method along with private constructor as replacement of final class to achieve the immutability

## Item 20: Prefer Interfaces to Abstract Classes

# Lambda and Streams
## Item 45: Use Streams Judiciously (202301)

* `computeIfAbsent` in `Map` since Java 8
* `sort` in `Arrays` in legacy Java

## Item 46: Prefer side-effect-free functions in streams (20230128)

# General Programming
## Item 61: Prefer primitive types to boxed primitives
### Takeaways
* primitive are more time- and space-efficient than boxed primitives
* When your program compares two *boxed primitives* with the `==` operator, it does an (object) identity comparison, which is almost certainly not what you want
* when your program does unboxing, it can throw a ``NullPointerException`
