# Chapter 6: Working Classes
## 6.4. Reasons to Create a Class

**Streamline parameter passing**

OWN COMMENT: Same thing as in Refactoring: Improving the Design of Existing Code > Introduce Parameter Object

**Facilitate reusable code**

*gold-plating* : creating of functionality that isn't required and that unnecessarily adds complexity

**OWN COMMENT** : mentioned also in the book, Growing Object-Oriented Software, Guided by Tests

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

*Put parameters in input-modify-output order*
 *input-only* first, *input-and-output* second, *output-only* third

 * limit the number of routine's parameter to about 7
 * Use named parameters - scenario to use it: when you have longer-than-average lists of identically typed arguments that there is higher probability to insert a parameter mismatch and compiler would not detect it!
## 7.6 Considerations in the use Use of Functions
### Setting the Function's Return Value
practical tip: 
 * initialize return value at the beginning of the function to a default value
 * Don't return *references* or *pointers* to *local data*

# Chapter 9: The Pseudocode Programming Process
## 9.3 Constructing Routines by PPP
### Check the Code
**Test the code**


