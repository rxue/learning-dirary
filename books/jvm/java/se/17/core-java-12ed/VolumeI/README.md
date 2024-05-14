# Chapter 5: Inheritance
## 5.2. The `equals` Method
Recall from Chapter 4, 

> Record automatically define an `equals``method that compares the fields. Two record instances are equals when the corresponding field values are equal

# Chapter 7: Exceptions, Assertion, and Logging
## Declaring with Errors
### Declaring Checked Exceptions

Caution:

> If you override a method from a superclass, the *checked exceptions* that the *subclass method* declares cannot be more general than those of the *superclass* method. (It is OK to throw more specific exceptions, or not to throw any exceptions in the subclass method.) In particular, if the superclass method throws no checked exception at all, neither can the subclass. 

