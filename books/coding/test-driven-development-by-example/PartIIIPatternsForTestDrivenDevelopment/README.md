# Part III: Patterns for Test-Driven Development
## Chapter 25. Test-Driven Development Patterns
### Test
*feedback loop*
### Isolated Test

Tip:
* seek test at a smaller step than the whole application
* isolation: If I had one test broken, I wanted one problem. If I had two tests broken, I wanted two problems.
* isolated tests are order independent
* implication of isolated test: have to break you problem into little orhtogonal dimensions

### Test List
Before start, write a list of all tests you know you will have to write

Tip:
* never take a step forward unless we know where our foot is going to land
* the less attention I had for what I was doing, the less I accomplished
* list also the refactoring that you think you will have to do in order to have clean code at the end of this session
* If you want to get to green quickly, you have to throw all ten tests away. If you want to get all of the tests working, then you are going to be staring at a red bar for a long time.

The pure form of TDD, wherein you are never more than one change away from a green bar, is like that three-out-of-four rule. 

### Test First
the more stress you have, the less likely you are to test enough

### Test Data
Use data that makes the tests easy to read and follow

> If there isn't a conceptual difference between 1 and 2, use 1
> don't use have a list of then items as the input data if a list of three items will lead you to the same design and implementation decisions.
> try never to use the same constant to mean more than one thing

*Realistic data* is useful when:

...

### Evident Data
When we've written the expression in the assertion, we know what we need to program.

## Chapter 26. Red Bar Patterns
### Explanation Test
### Learning Test
### Another Test
### Regression Test

## Chapter 27. Testing Patterns
### Child Test
Break a big test into smaller tests (divide & conquer)
### Mock Object
### *Self Shunt*
### *Long String*
important in testing on *observer* pattern
### Crash Test Dummy
A *test dummy*, which could crash
### Borken Test
A clue for what to work on next
### Clean Check-in
Broken test is pretty strong evidence that you didn't known enough to program what you just programmed

*checking in* more often is a good thing

Commenting out test to make suite pass is strictly verboten

## Chapter 28. Green Bar Patterns
### *Fake It*
A couple of effect that Fake It powerful
### Triangulate
Use when you are unsure about the correctness of abstraction
### One to Many

## Chapter 29. xUnit Patterns
### *Fixture*
also known as *scaffolding*
`setUp()`
### *External Fixture*
! The goal of each test is to leave the word in exaclty the same state as before it ran.

## Chapter 30. Design Patterns
### Pluggable Object
### Pluggable Selector
My guess: reflection in Java is probably relevant
### Imposter
### Collecting Parameter

## Chapter 31. Refactoring
### Migrate Data
### Method Object
## Chapter 32. Master TDD
### How does TDD lead to frameworks
### How much feedback do you need

