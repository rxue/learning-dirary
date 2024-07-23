# Functions
## Do One Thing

> Functions should do one thing. They should do it well. They should do it only.

The reason we write functions is to decompose a larger concept into a set of steps at the next level of abstraction.

## One Level of Abstraction per Function

Mixing levels of abstraction within a function is always confusing.

### Reading code from top to bottom: *The Stepdown Rule*
> Functions should do one thing. They should do it well. They should do it only.

## Use Descriptive Names
Choosing good names for small functions that do one thing. A long descriptive name is better than a short enigmatic name

## Function Arguments
Three arguments (Triadic) should be avoided where possible.

Arguments are even harder from a testing point of view.

Output arguments are harder to understand than input arguments.

### Common Monadic Forms
Using an output argument instead of a return value for transformation is confusing. If a function is going to transform its input argument, the transformation should appear as the return value. Indeed, `StringBuffer transform(StringBuffer in)` is better than `void transform(StringBuffer out)`, even if the implementation in the first case simply returns the input argument.

### Flag Arguments
Passing a boolean into a function is a truly terrible practice. It immediately complicates the signature of the methods, loudly proclaiming that this function does more than one thing.

### Dyadic Functions
Even obvious dyadic functions like `assertEquals(expected, actual)` are problematic.

Dyads aren't evil, and you will certainly have to write them. However, you should be aware that they come at a cost and should take advantage of what mechanism may be available to convert them into monads.

### Argument Objects
When a function seems to need more than thre arguments, it is likely that some of those arguments ought to be wrapped into a class of their own.

### Argument Lists
### Verbs VS Keywords
For example, `assertEquals` might be better written as `assertExpectedEqualsActual(expected, actual)`. This strongly mitigates the problem of having to remember the ordering of the arguments.
## Having No Side-Effects
Side effects create a temporal coupling. If you must have temporal coupling, you should make it clear in the name of the function. In this case, we might rename the function `checkPasswordAndInitializeSession`, though that certainly violates "do one thing".
### Output Arguments
In general, output arguments should be avoided

### Command Query Separation
Clean code should either do something or answer something, but not both. Consider, for example, the following function: `public boolean set(String attribute, String value);`

This function sets the value of a named attribute, and return `true` if it is successful and `false` if no such attributes exists. This leads to odd statements like this:

`if (set("username","unclebob"))...`

It is hard to infer the meaning from the call... We could try to resolve this by renaming the `set` function to `setAndCheckIfExists`, but that doesn't much help the readibility of the `if` statements. The real solution is to separate the command from the query so that the ambiguity cannot occur.

```
if (attributeExists("username")) {
  setAttribute("username", "unclebob");
  ...
}
```
### Prefer Exceptions to Returning Error Codes
#### Extract `try`/`catch` Blocks
`try`/`catch` blocks are ugly in their own right. They confuse the structure of the code and mix error processing with normal processing. 
#### Error Handling is One Thing
Thus a function that handles errors should do nothing else. This implies that **if the keyword `try` exists in a function, it should be the very firt word in the function and that there should be nothing after the `catch`/`finally` blocks.**

### Don't repeat yourself
*Structured programming*, *aspect oriented programming*, *component oriented programming*, are all in part, strategies for eliminating duplication.

### Structured Programming
There should be only one `return` statement in a function, no `break` or `continue` statements in a loop, and never, ever, any `goto` statements.

If you keep the function small, then the occasional multiple `return`, `break` or `continue` statement does not harm and can sometimes even be more expressive than the single-entry, single-exit rule.

### Conclusion
Never forget that your real goal is to tell the story of the system.
