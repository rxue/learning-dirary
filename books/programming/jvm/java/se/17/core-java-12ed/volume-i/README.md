# Chapter 4: Objects and Classes
## 4.7. Records
### 4.7.1 The Record Concept
#### NOTE:
`toString()`, `equals()`, `hashCode()` are automatically implemented in `record`

MY OWN TAKEAWAY: the automatic implementations of these 3 methods can be used in any other non-performance-critical classes, i.e. initialize private `record` inside the class and implements those methods by using the sames methods of the `record`
## 4.9. JAR Files
### 4.9.2 The Manifest
`META-INF/MANIFEST.MF`

### 4.9.3 Executable JAR Files
*main class* can be specified in the *manifest* including statement of the form: `Main-Class: com.mycompany.mypkg.MainAppClass`

# Chapter 5: Inheritance
## 5.2. The `equals` Method
Recall from Chapter 4, 

> Record automatically define an `equals``method that compares the fields. Two record instances are equals when the corresponding field values are equal

# Chapter 6: Interfaces, Lambda Expressions, and Inner Classes
## Chapter 6.3. Inner Classes
### 6.3.6. Anonymous Inner Classes
*double brace initialization*

IMO, till JDK 17, since the `Set.of`, `List.of` is way more readable than *double brace initialization*, the only suitable use case of *double brace initializaiton* is the initialization of *immutalbe* `Map`

# Chapter 7: Exceptions, Assertion, and Logging
## Declaring with Errors
### Declaring Checked Exceptions

Caution:

> If you override a method from a superclass, the *checked exceptions* that the *subclass method* declares cannot be more general than those of the *superclass* method. (It is OK to throw more specific exceptions, or not to throw any exceptions in the subclass method.) In particular, if the superclass method throws no checked exception at all, neither can the subclass. 

