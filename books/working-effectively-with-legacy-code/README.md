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
 

    
# Part III: Dependency-Breaking Techniques
## Chapter 25: Dependency-Breaking Techniques
### *Parameterize Constructor*

# My Own Comment
The gist of this book is unit test, test, test... 

In order to achieve full test coverage, some design principles can be even violated in test code. For instance, 

* in order to unit test a `private` method under the circumstance of tight schedule, the accessibility can be modified to `protected` or *package-private*, thus *encapculation* is violated
* the *Subclass and Override Method* technique can easily violate the *LSP*
