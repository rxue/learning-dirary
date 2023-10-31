# Part I
## Chapter 1: Changing Software
> Behavior is the most important thing about software.

## Chapter 2: Working with Feedback
### Working with Feedback
> We can do "testing to detect change."
> In traditional terms, this is called *regression testing*

> We start to refactor the code a bit. We extract some methods and move some conditional logic. After every little change that we make, we run that little *suite* of unit tests.

### What is Unit Testing
> Common to most conceptions of unit tests is the idea that they are **tests in isolation of individual components of software.** What are components? The definition varies, but in unit testing, we are usually concerned with **the most atomic behavioral units** of a system. In procedural code, the units are often functions. **In object-oriented code, the units are classes**.

```
> In the industry, people often go back and forth about whether particular tests are unit tests...I go back to the two qualities: Does the test run fast? Can it help localize errors quickly? ...Some tests are larger, and they use several classes together. In fact, they may seem to be little integration tests. By themselves, they might seem to run fast, but what happens when you run them all together?

> A unit test that takes 1/10th of a second to run is a slow unit test.


Other kinds of tests often masquerade as unit tests. A test is not a unit test if:

 1. It talks to a database.
 2. It communicates across a network.
 3. It touches the file system.
 4. You have to do special things to your environment (such as editing configuration files) to run it.
```

### *Higher-Level Testing*
> Unit tests are great, but there is a place for higher-level tests, tests that cover scenarios and interactions in an application. Higher-level tests can be used to pin down behavior for a set of classes at a time. When you are able to do that, often you can write tests for the individual classes more easily.

## Chapter 3: The *Seam* Model
### Seams
> A seam is a place where you can alter behavior in your program without editing in that place.

### Seam Types
#### ~~Preprocessing Seams~~
##### Enabling Points
> Every seam has an enabling point, a place where you can make the decision to use one behavior or another.

#### ~~Link Seams~~
#### Object Seams

## Chapter 5: Tools
### Automated Refactoring Tools
> refactoring (n.). A change made to the internal structure of software to make it easier to understand and **cheaper to modify without changing the existing behavior**.

### Unit-Testing Harnesses
Key features of xUnit:

* It lets programmers write tests in the language they are developing in.

* All tests run in isolation.

* **Tests can be grouped into *suites* so that they can be run and rerun on demand**
