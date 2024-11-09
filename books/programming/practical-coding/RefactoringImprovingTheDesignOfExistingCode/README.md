# Chapter 2: Principles in Refactoring
## Refactoring, Architecture and YAGNI
# Chapter 6: A First Set of Refactorings
## Inline Function
### Self Comment
NOTE! In this book, the *inline function* is not *nested function* but just a fairly simple and descriptive statement, which is not necessary to be extracted as a separate function. *Ternary operator* is typically used in *inline function* as demonstrated in the book.

In chapter 1,

> Refactoring changes the programs in *small steps*, so if you make a mistake, it is easy to find where the bug is.

In my opinion, the sizes of the refactoring steps are in the following order: 

*inline function* < *nested function* (*Functional Interface* in Java) < *method*
## Extract Variable

## Inline Variable
### Self Comment
In Java IDE IntelliJ, there is *invline variable* functionality

# Chapter 8: Moving Features
## Move Function
### Mechanics
> If I find a called function that should also move, I usually move it first. That way, moving a clusters of functions begins with the one that has the least dependency on the others in the group.

# Chapter 10: Simplifying Conditional Logic
## Replace nested conditional with guard clauses
An important core of guard clause is to return as early as possible to reduce time of thinking by developers

Simple but important tip: Leaving *not* (`!`) in a conditional twists coder's mind around at a painful angle

# Chapter 12: Dealing with Inheritance
## Replace subclass with delegate
> if I want to vary behavior of people by their age category and by their income level, I can either have subclasses for young and senior, or for well-off and poor - I can't have both


 


