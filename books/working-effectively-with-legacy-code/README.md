# Preface
## *Legacy Code*

> In the industry, *legacy code* is often used as a slang term for difficult-to-change code that we don't understand.

But to the author, Michael Feathers

> *legacy code* is simple code without tests.

# Part I
## Chapter 2: Working with Feedback
### What is Unit Testing
> The definition varies, ... In object-oriented code, the units are classes

> Testing in isolation is an important part of the definition of a unit test

> Unit tests run fast. If they don't run fast, they aren't unit tests.
<br /> Other kinds of tests often masquerade as unit tests. A test is not a unit test if:

### *Higher-Level Testing*
> Unit tests are great, but there is a place for higher-level tests, tests that cover scenarios and interactions in an application. Higher-level tests can be used to pin down behavior for a set of classes at a time. When you are able to do that, often you can write tests for the individual classes more easily.

## Chapter 2: The *Seam* Model

## Chapter 5: Tools
### Automated Refactoring Tools
> refactoring (n.). A change made to the internal structure of software to make it easier to understand and **cheaper to modify without changing the existing behavior**.

### Unit-Testing Harnesses
Key features of xUnit:

* Tests can be grouped into *suites* so that they can be run and rerun on demand 
# Part II
## Chapter 8: How Do I Add a Feature?

### Comment: Trick for *cut/copy/paste*
Often times when adding new features or fixing bugs in legacy code base, lots of coders prefer to adding one or more arguments to an existing method signature. This should be averted whenever possible because, adding more arguments also means the more reasons for changing the residing class, which is against the *Single Responsibility Principle*. However, when the last resort is adding one or more arguments to an existing method, *cut/copy/paste* would come into play. Particularly if the method is used many times in the code base (*Find usage* with IDE), directly adding more arguments would cause the changes everywhere the method is called, so do *cut/copy/paste* (*use method overloading*), then mark the previous method as `@Deprecated` if the new method is more handy to be used


## Chapter 10: I Can't Run This Method in a Test Harness
### The Case of the Hidden Method
> If we need to test a private method, we should make it `public`. If making it public bothers us, in most cases, it means that our class is doing too much and we ought to fix it.

### The Case of the Undetacable Side Effect
#### [*Query-Query Separation*](https://www.youtube.com/watch?v=eb3nbt4poic)



## Chapter 11: I Need to Make a Change. What Methods Should I Test?
### Reasoning About Effects
### Reasoning Forward
> When you are sketching effects, make sure that you have found all of the clients of the class you are examining. If your class has a superclass or subclasses, there might ber other clients that you havn't considered.
### Effect Propagation
### Learning from Effect Analysis
> Try to analyze effects in code whenever you get a chance.

> In general, programming gets easier as we narrow effects in a program. We need to know less to understand a piece of code. At the extreme, we end up with *funcitonal programming* in languages such as Scheme and Haskell.

## Chapter 17 My Application Has No Structure
### Telling the Story of the System

## Chapter 20 The Class is Too Big and I Don't Want It to Get Any Bigger
### Moving Forward
#### Strategy
#### Tactics
> 1. Identify a Responsibility that you want to separate into another class
> 2. Figure out whether any instance variables will have to move to the new class. If so, move them to a separate part of the class declaration, away from the other instance variables.

# Part III: Dependency-Breaking Techniques
## Chapter 25: Dependency-Breaking Techniques
### *Parameterize Constructor*

# My Own Comment
The gist of this book is unit test, test, test... 

In order to achieve full test coverage, some design principles can be even violated in test code. For instance, 

* in order to unit test a `private` method under the circumstance of tight schedule, the accessibility can be modified to `protected` or *package-private*, thus *encapculation* is violated
* the *Subclass and Override Method* technique can easily violate the *LSP*
