# Chapter 27: How Program Size Affects Construction
## 27.5 Effect of Project Size on Development Activities
### Methodology and Size
> On large projects, unconscious choices are inadequate to the task. Successful project planners choose their strategies for large projects explicitly

> Capers Jones points out that a project of 1,000 lines of code will average about 7 percent of its effort on paperwork, whereas a 100,000-lines-of-code project will average about 26 percent of its effort on paperwork (Jones 1998).

> Barry Boehm and Richard Turner caution that you’ll usually do better if you start your methods small and scale up for a large project than if you start with an all-inclusive method and pare it down for a small project (Boehm and Turner 2004)

# Chapter 28: Managing Construction
## 28.3 Estimating a Construction Schedule
### What to Do If You're Behind
#### Reduce the scope of the project
> When you plan the product initially, partition the product's capabilities into "must have", "nice to have" and "optionals".

If you fall behind, ... drop the ones that are the least important.

> Short of dropping a feature altogether, you can provide a cheaper version of the same functionality.

## 28.4 Measurement
> If data is to be used in a scientific experiment, it must be quantified.

> To evaluate software-development methods, you must measure them.

> *To argue againest measurement is to argue that it's better not to know what's really happening on your project*

## 28.5 Treating Programers as People
### Religious Issues
> Use "suggestions" or "guidelines" with respect to area
Avoid setting rigid "rules" or "standards"

Details of a specific standard is often less important than the fact that some standard exists. Don't set standard for your programmers, but do insist they standardize in the areas that are important to you

**Practical tips** :

format code automatically, i.e. by means of IDE

> *To argue againest measurement is to argue that it's better not to know what's really happening on your project* 

# Chapter 29: Integration
## 29.2 Integration Frequency - Phased or Incremental?
### Benefits of Incremental Integration
> An accounting of errors for one project revealed that 39 pcercent were inter-module interface errors. Because developers on many projects spend up to 50 percent of their time debugging, maximizing debugging effectiveness by making errors easy to locate provide benefits in quality and productivity.

## 29.3 Incremental Integration Strategies
### Top-Down Integration
*top* : the main window, the applications control loop, the object that contains `main()` in Java

import aspect of top-down integration: interfaces between classes must be carefully specified
### Bottom-Up Integration
**requirement for applying**
complete design of the whole before you start integration

> Letting low-level details drive the design of higher-level classes contradict principles of information hiding and object-oriented design

## 29.4 Daily Build and Smoke Test
*Smoke test* 
* no need to be exhaustive
* should be capable of exposing major problems
