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

### Self-Comment: Trick for *cut/copy/paste*
Often times when adding new features or fixing bugs in legacy code base, lots of coders prefer to adding one or more arguments to an existing method signature. This should be averted whenever possible because, adding more arguments also means the more reasons for changing the residing class, which is against the *Single Responsibility Principle*. However, when the last resort is adding one or more arguments to an existing method, *cut/copy/paste* would come into play. Particularly if the method is used many times in the code base (*Find usage* with IDE), directly adding more arguments would cause the changes everywhere the method is called, so do *cut/copy/paste* (*use method overloading*), then mark the previous method as `@Deprecated` if the new method is more handy to be used
    

