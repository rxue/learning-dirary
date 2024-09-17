# Chapter 20: The Software Quality Landscape
## 20.5 The General Principle of Software Quality
> improving quality reduces costs

company can shorten a development schedule by: 
 * improve the quality of the product
 * decrease amount of time spent debugging and reworking the software

> Reducing debugging by preventing errors improves productivity.
# Chapter 22: Developer Testing

 * *unit testing*
 * *component testing*
 * *integration testing*
 * *regression testing*
 * *system testing*

## 22.4 Typical Errors
## 22.5 Test-Support Tools
### Building Scaffolding to Test Individual Classes
*scaffolding* can be:
* *mock object*
* *stub object*
* *driver* / *test harness*: fake routine that calls real routine being tested
* (small) dummy file - content is **easy** to understand, errors in using it should be conspicuous

Typical example of scaffolding: 
* *JUnit*
* write your own scaffolding code in `main`

# Chapter 23: Debugging
## 23.2 Tips for finding a Defect
### Tips for Finding Defects
> If you're having a hard time finding a defect, it might be because the code isn't well written.

#### Narrow the suspicious region of the code
*binary search* technique

#### Integrate incrementally
> Debugging is easy if you add pieces to a system one at a time. If you add a piece to a system and encounter a new error, remove the piece and test it separately

#### Take a break from the problem
> The onset of anxiety is a clear sign that it's time to take a break

# Chapter 24: Refactoring
## 24.3 Specific Refactorings
### Statement-Level Refactorings
> Return as soon as you know the answer instead of assigning a return value within nested *if-then-else* statements
## 24.4 Refactoring Safely
* Keep refactorings small
* Do refactorings one at time
* Make a list of steps you intend to take
* Review the changes
> if programmers work with a substrantial portion of the code, rather than just a few lines, the change of making a correct modification improves
> as the number of lines changed increases from one to five lines, the chance of making a bad change increases.

### Bad Times to Refactor
* Don't use refactoring as a cover for code and fix
* Avoid refactoring instead of rewriting - sometimes redesign and reimplement might be better than refactor
### Refactoring Strategies
Refactor when you
* add a routine
* add a class
* fix a defect

Target
* error-prone modules
* high-complexity modules - program quality improved dramatically when maintenance programmers focused their improvement efforts on the modules that had the highest complexity

> Code that is never modified doesn't need to be refactored. But when you do touch a section of code, be sure you leave it better than you found it.

> **Define an interface between clean code and ugly code, and then move code across the interface** 
* designate some code as being in the messy real world, some code as being in an idealized new world, and some code as being the interface between the two.
* anytime you touch a section of messy code, you are required to bring it up to current coding standards - give clear variable names, ...
