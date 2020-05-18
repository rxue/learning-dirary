# Chapter 9 Unit Tests
## The Three Laws of TDD
TDD asks us to write unit tests first, before we write production code.

> **First Law** You may not write production code until you have written a failing unit test

## Keeping Tests Clean
### Tests Enable the -ilities
If you have tests, you do not fear making changes to the code! Without tests, every change is a possible bug.

The dirtier your tests, the dirtier your code becomes.

## Clean Tests
What makes a clean test. Three things. Readability, readability, readability. What makes tests readable? The same thing that makes all code readable: clarity, simplicity and density of expression. In a test you want to say a lot with as few expressions as possible.

The poor reader is inundated with a swarm of details that must be understood before the tests make any real sense.

The BUILD-OPERATE-CHECK patterkn
### A Dual Standard
There are things that you might never do in a production environment that are perfectly fine in a test environment

## One Assert per Test
every test function in a JUnit test should have one and only one assert statement.

the number of asserts in a test ought to be minimized.

### Single Concept per Test 
test a single concept in each test function

minimize the number of asserts per concept and test just one concept per test function

## F.I.R.S.T

### Independent
Tests should not depend on each other

### Repeatable

### Timely

# Chapter 10 Classes
## Class Organizations
Following the standard Java convention, a class should begin with a list of variables. Public static constants, if any, should come first. Then `private static` variables, followed by `private` instance variables. There is seldom a good reason to have a `public` instance variable. 

Public functions should follow the list of private variables. We would like to put the `private` utilities called by a `public` function right after the `public` function itself. This follows the *stepdown rule* and helps the program read like a newspaper article.

### Encapsulation
We like to keep our variables and utility functions `private`, but we're not fanatic about it. **Sometimes we need to make a variable or utility functions `protected` so that it can be accessed by a test**. For us, **tests rule**.

# Chapter 15 JUnit Internals
## The JUnit Framework
Negatives are slightly harder to understand than positives [G29]

hidding temporal coupling
## Conclusion
No module is immune from improvement, and each of us has the responsibility to leave the code a little better than we found it.
