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
### Start Each Features with Acceptance Test
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
### Unit-Test Behavior, Not Methods

