# Chapter 2: Principles in Refactoring
## Refactoring, Architecture and YAGNI
# Chapter 6: A First Set of Refactorings
## Inline Function
### Commentary
NOTE! In this book, the *inline function* is not *nested function* but just a fairly simple and descriptive statement, which is not necessary to be extracted as a separate function. *Ternary operator* is typically used in *inline function* as demonstrated in the book.

In chapter 1,

> Refactoring changes the programs in *small steps*, so if you make a mistake, it is easy to find where the bug is.

In my opinion, the sizes of the refactoring steps are in the following order: 

*inline function* < *nested function* (*Functional Interface* in Java) < *method*

# Chapter 12: Dealing with Inheritance
## Replace subclass with delegate
> if I want to vary behavior of people by their age category and by their income level, I can either have subclasses for young and senior, or for well-off and poor - I can't have both


 


