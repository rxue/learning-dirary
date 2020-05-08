# Chapter 6: Objects and Data Structures
There is a reason that we keep our variables `private`. We don't want anyone else to depend on them.
## Data Abstraction
Hiding implementation is not just a matter of putting a layer of functions between the variables. Hiding implementation is about abstraction! A class does not simply push its variables out through getters and setters. Rather it exposes abstract interfaces that allow its users to manipulate the essence of the data, without having to know its implementation.

The worst option is to blithely add getters and setters.

## Data/Objects Anti-Symmetry
Objects hides their data behind abstractions and expose functions that operate on that data. Data structure expose their data and have no meaningful functions.

> Procedural code (code using data structure) makes it easy to add new functions without changing the existing data structure. OO code, on the other hand, makes it easy to add new classes without changing the existing functions.

In any complex systems, there are going to be times when we want to add new data types rather than new functions. For these cases objects and OO are more appropriate.

## The Law of Demeter

