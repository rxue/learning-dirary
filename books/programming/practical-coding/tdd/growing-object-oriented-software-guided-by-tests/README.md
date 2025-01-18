# Part I: Intoduction
## Chapter 1: What is the Point of Test-Driven Development?
### The Bigger Picture
### Testing End-to-End
*acceptance test* should excercise the system end-to-end instead of invoking the internal code directly

entry-point of *end-to-end tests*

* user interface
* send messages from third party system
* web service
* parse report
* ...

> end-to-end build cycle is an ideal candidate for automation
# Part II: The Process of Test-Driven Development
## Chapter 5: Maintaining the Test-Driven Cycle
### Start Each Feature with an *Acceptance Test*

First write failing acceptance test - this proves that the feature is not implemented yet


Write acceptance test using only terminology from the application's domain, i.e. look at the system from the user's point of view, other than the underlying technologies

![innter and outer feedback loops in TDD](https://private-user-images.githubusercontent.com/3033388/399732812-52d8324e-8eeb-423a-aa69-86f037a88790.jpeg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzU4MzA0MDMsIm5iZiI6MTczNTgzMDEwMywicGF0aCI6Ii8zMDMzMzg4LzM5OTczMjgxMi01MmQ4MzI0ZS04ZWViLTQyM2EtYWE2OS04NmYwMzdhODg3OTAuanBlZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAxMDIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMTAyVDE1MDE0M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPThjNDY0MTA3YTQ2Yjc3YTgxMGYwNmZjYWYwNTRiZjEzOTNiZTlkYWVhNGM1OWZiN2UyNzNiMzI5MGU5OWFjZDgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.lTEPrM8D9RS20BllsIVHwjFk2d7F1JCtxUdAebzBhmk)

### Separate Tests The Measures Progress from Those That Catch Regressions
Requirement change should need the existing acceptance tests be moved out of the **regression suite** back into the **in-progress suite*. The **in-progress suite** should be updated on base of the new requirement

### Start Testing with the Simplest Success Case

> the simplest thing that could possibly work [Beck02]

=> start by testing the simplest **success** case

### Write the Test That You'd Want to Read
Error message should clearly describe what needs to be done

### Develop from the Inputs to the Outputs
> from the objects that receive external events, through the intermediate layers, to the central domain model, and then on to other boundary objects that generate an externally visible response.

### Unit-Test Behavior, Not Methods
> Many developers who adopt TDD find their early tests hard to understand when they revisit them later, and one common mistake is thinking about testing methods. A test called testBidAccepted() tells us what it does, but not what it’s for.

Tests should be driven by the behavior other than the concrete implementation!!!

### Tuning the Cycle
**tips**
more integration tests needed in case

* unhandled exception
* unexpected system failure
## Chapter 6: Object-Oriented Style
### Introduction
> Implementing a feature in the most direct way can demage the maintainability of the system

### Desiging for Maintainability
#### High levels of abstraction
> We can get more done if we program by combining components of useful functionality rather than manipulating variables and control flow
### Context Independence

## Chapter 7: Achieving Object-Oriented Design
### Building Up to Higher-Level Programming
*implementation layer* : how
*declarative layer* : what - a small *domain-specific language* embedded

## Chapter 8: Building on Third-Party Code
### Only Mock Types That You Own

Do not mock third-party object!

#### Write an *Adapter Layer*
# Part III: A Worked Example
## Chapter 10. The Walking Skeleton
**Iteration Zero**
## Chapter 12 Getting Ready to Bid
### A Test for Bidding
#### Outside-In Development
start with the outside event that triggers the behavior we intend to implement
## Chapter 16: Snipping for Multiple Items
### Adding Items through the User Interface
#### Another Level of Testing
*integration test* tests how our code works with third-party library

# Part IV: Sustainable Test-Driven Development
## Chapter 20: Listening to the Tests
### Logging Is a Feature
#### Notification Rather Than Logging
### Mocking Concrete Classes

 
