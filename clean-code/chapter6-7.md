# Chapter 6: Objects and Data Structures
There is a reason that we keep our variables `private`. We don't want anyone else to depend on them.
## Data Abstraction
Hiding implementation is not just a matter of putting a layer of functions between the variables. Hiding implementation is about abstraction! A class does not simply push its variables out through getters and setters. Rather it exposes abstract interfaces that allow its users to manipulate the essence of the data, without having to know its implementation.

The worst option is to blithely add getters and setters.

## Data/Objects Anti-Symmetry
Objects hides their data behind abstractions and expose functions that operate on that data. Data structure expose their data and have no meaningful functions.

> Procedural code (code using data structure) makes it easy to add new functions without changing the existing data structure. OO code, on the other hand, makes it easy to add new classes without changing the existing functions.

In any complex systems, there are going to be times when we want to add new data types rather than new functions. For these cases objects and OO are more appropriate.

## The Law of Demeter

# Chapter 7: Error Handling
## Write Your `try-catch-finally` Stement First
In a way, `try` blocks are like transactions. Your `catch` has to leave your program in a consistent state, no matter what happens in the `try`.

## Use *Unchecked Exceptions*
*C#* doesn't have checked exceptions, and despite valiant attempts, *C++* doesn't either. Neither do *Python* or *Ruby*. Yet it is possible to write possible software in all of these languages.

The price of checked exceptions is an *Open/Close Principles* Violation. If you throw a checked exception from a method in your code and the `catch` is three levels above, *you must declare that exception in the signature of each method between you and the `catch`*. This means that a change at a low level of the software can force signature changes on many higher levels. The changed models must be rebuilt and redeployed, even though nothing they care about changed.

Checked exceptions can sometimes be useful if you are writing a critical library: you must catch them. But in general application development the dependency costs outweigh the benifits.

## Provide Context with Exceptions
In Java, you can get *stack trace* from any exception; However, a *stack trace* can't tell you the intent of the operation that failed.

Create informative *error messages* and pass them along with your exceptions. Mention the exception that failed and the type of failure. If you are logging in your application, pass along enough information to be able to log the error in your `catch`.

## Define Exception Classes in Terms of a Caller's Needs
wrapping a third-party APIs is a best practice. When you wrap a third-party API, you minimize your dependencies upon it. Wrapping also makes it easier to mock out third-party calls when you are testing your own code.

## Define the Normal Flow
SPECIAL CASE PATTERN. You create a class or configure an object so that it handles a special case for you. When you do, the client cede doesn't have to deal with the exceptional behavior. The behavior is encapsulated in the special case object.

## Don't Return Null
When we return `null`, we are essentially creating work for ourselves and foisting problems upon our callers.

If you are tempted to return `null` from a method, consider throwing an exception or returning a SPECIAL CASE object instead. If you calling a `null`-returning method from a third-party API, consider wrapping that method with a method that either throws an exception or returns a special case object.

Java has `Collections.emptyList()`

```
  public List<Employee> getEmployees() {
    if (.. there are no employees .. )
      return Collections.emptyList();
  }
```
If you code this way, you will minimize the chance of `NullPointerException`s and your code will be cleaner.

## Don't Pass Null
Returning `null` from methods is bad, but passing `null` into methods is worse. Unless you are working with an API which expects you to pass `null`, you should avoid passing `null` in your code whenever possible.

In most programming languages there is no good way to deal with a `null` that is passed by a caller accidentally. Because this is the case, **the rational approach is to forbid passing `null` by default.**

## Conclusion
We can write robust clean code if we see error handling as a separate concern.

