# Chapter 1: Clean Code
## The Total Cost of Owning a Mess
### What is Clean Code
#### "Big" Dave Tomas, founder of OTI, godfather of the Eclipse strategy
> minimal dependencies, which are explicitly defined, and provides a clear and minimal API
> clean code makes it easy for other people to enhance it

> code without tests is not clean

> literate 

=> Knuth's *literate programming*

#### Michael Feather: author of Working Effectively with legacy code
> clean code always looks like it was written by someone who cares.

#### Ron Jeffries: author of Extreme Programming Installed and Extreme Programming Adventures in C#

> Run all tests
> Contains no duplication
## The Boy Scout Rule
If we checked-in our code a little cleaner than when we checked it out, the code simply could not rot.
 
# Chapter 2: Meaningful Names
## Use Intention-Revealing Name
If a name requires a comment, then the name does not reveal its intent

## Avoid Disinformation
It is very useful if names for very similar things sort together alphabetically and if the differences are very obvious, because the developer is likely to pick an object by name without seeing you copious comments or even the list methods supplied by that class.

## Making Meaningful Distinctions
It is not sufficient to add number series or noise words even though the compiler is satisfied. If names must be different, then they should also mean something different.

Noise words are another meaningless distinction. Imagine that you have a `Product` class. If you have another called `ProductInfo` or `ProductData`, you might have made the names without making them mean anything different. `Info` and `Data` are instinct noise words like `a`, `an`, `the`.

Noise words are redundant. The word `variable` should never appear in a variable name. The word `table` should never appear in a table name. How is `NameString` better than `Name`? Would a `Name` ever be a floating point number? If so it breaks an earlier rule about disinformation. Imagine finding one class named `Customer` and another named `CustomerObject`. What should you understand as a distinction? Which one will represent the best path to a customer's payment history?

There is an application we know of where this is illustrated. We've changed the names to protect the guilty, but here is the exact form of the error:

```
  getActiveAccount();
  getActiveAccounts();
  getActiveAccountInfo();
```
How are the programmers in this project are supposed to know which of these functions are supposed to call?


## Use Searchable Names 

Likewise, the word `e` is a poor choice for any variable for which a programmer might need to search. It is the most common letter in the English language and likely to show up in every program. In this regard, **longer names trump shorter names, and any searchable names trumps a constant in code**  

My personal preference is that single-letter names can ONLY be used as local variables inside short methods. *The lenghth of a name should correspond to the size of its scope*

## Avoid Encoding
### Member Prefixes
### Interfaces and Implementations

## Avoid Mental Mappings
> Clarity is king

## Class Names
A class name should not be a verb.

## Method Names
When constructors are overloaded, use static factory methods with names and describe the arguments. 

## Pick One Word Per Concept

Likewise, it is confusing to have a `controller` and a `manager` and a `driver` in the same code base.

A consistent lexicon is a grate boon to the programmers who must use your code.

## Don't Pun
Our goal, as authors, is to make our code as easy as possible to understand.

## Use Solution Domain Names
## Use Problem Domain Names
## Adding Meaningful Context
## Don't Add Gratuitous Context
Shorter names are generally better than longer names, so long as they are clear.

The name `accountAddress` or `customerAddress` are fine names for instance of the class `Address` but could be poor names for classes. 
