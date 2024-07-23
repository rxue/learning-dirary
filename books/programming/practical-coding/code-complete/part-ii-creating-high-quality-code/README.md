# Chapter 6: Working Classes
## 6.4. Reasons to Create a Class
### Classes to Avoid
 * *god class*
 * Eleminate irrelevant class - pure data without behavior

Very important cross-reference found by myself: https://www.martinfowler.com/bliki/AnemicDomainModel.html

 * Avoid classes named after verbs - pure behavior without data

# Chapter 7: High-Quality Routines
## 7.3 Good Routin Names
*Avoid meaningless, vague, or wishy-washy verbs*
bad names examples: 
* `HandleCalculation()`
* `PerformServices()`
* `OutputUser()`
* `ProcessInput()`
* `DealWithOutput()`

## 7.5 How to Use Reoutine Parameters
 * limit the number of routine's parameter to about 7
 * Use named parameters - scenario to use it: when you have longer-than-average lists of identically typed arguments that there is higher probability to insert a parameter mismatch and compiler would not detect it!
## 7.6 Considerations in the use Use of Functions
### Setting the Function's Return Value
practical tip: 
 * initialize return value at the beginning of the function to a default value
 * Don't return *references* or *pointers* to *local data*  
