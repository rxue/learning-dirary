# Chapter 6: Working Classes
## 6.4. Reasons to Create a Class
### Classes to Avoid
 * *god class*
 * Eleminate irrelevant class - pure data without behavior

Very important cross-reference found by myself: https://www.martinfowler.com/bliki/AnemicDomainModel.html

 * Avoid classes named after verbs - pure behavior without data

# Chapter 7: High-Quality Routines
## 7.6 Considerations in the use Use of Functions
### Setting the Function's Return Value
practical tip: 
 * initialize return value at the beginning of the function to a default value
 * Don't return *references* or *pointers* to *local data*  
