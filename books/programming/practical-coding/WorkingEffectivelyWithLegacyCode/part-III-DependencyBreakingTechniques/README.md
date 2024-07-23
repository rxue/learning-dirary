# Part III: Dependency-Breaking Techniques
## Chapter 25: Dependency-Breaking Techniques
### *Adapt Parameter*
### *Break out Method Object*
### ~~*Definition Completion*~~
### *Encapsulate Global References*
### *Expose Static Method*
> If you a method that doesn't use instance data or methods, you can turn it into a static method. When it is static, you can get it under test without having to instantiate the class.
### ~~*Extract Implementor*~~
### *Introduce Instance Delegator*
This is solution of *static cling*

References on *static cling* :

* https://deviq.com/antipatterns/static-cling
* https://www.codeproject.com/Articles/26716/Refactoring-Legacy-Code-Part-1-Dealing-with-Static 
 

### ~~*Link Substitutions*~~
### *Parameterize Constructor*
### *Supersede Instance Variable*
> overridden methods can be called from constructors in Java, but I don't recommend doing it in production code.
### ~~*Replace Function with Function Pointer*~~

# My Own Comment
The gist of this book is unit test, test, test... 

In order to achieve full test coverage, some design principles can be even violated in test code. For instance, 

* in order to unit test a `private` method under the circumstance of tight schedule, the accessibility can be modified to `protected` or *package-private*, thus *encapculation* is violated
* the *Subclass and Override Method* technique can easily violate the *LSP*
