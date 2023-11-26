# Chapter 1. Evolutionary Database Development
## 1.5. Developer Sandboxes
## 1.6. Implementations to Evolutionary Database Development Techniques
last 1970s - early 1980s : *code-and-fix*


# Chapter 2. Database Refactoring
## 2.2. Database Refactoring
### 2.2.3. Maintaining Semantics
> On the surface, the Introduce Column sounds like a perfectly fine refactoring; adding an empty column to a table does not change the semantics of that table until new functionality begins to use it. We still consider it a transformation (but not a refactoring) because it could inadvertently change the behavior of an application. For example, if we introduce the column in the middle of the table, any program logic using positional access (for example, code that refers to column 17 rather than the column's name) will break.
# Chapter 5. Database Refactoring Strategies
## 5.5 Prefer Triggers over Views or Batch Synchronization
## 5.9 Encapsulate Database Access
## 5.11 Do Not Duplicate SQL
> the more SQL code you have, the harder it is to refactor your database schema, because there will be potentially more code coupled to whatever you are refactoring.
> It is best if you write SQL in a single package or class, have SQL generated from metadata, or store SQL code in XML files that is accessed at runtime.
## 5.12 Put Database Assets Under Change Control
> it is most helpful when database assets are

# Chapter 6. Structural Refactorings
## Drop Column
### Access Program Update Mechanics
> generally it is not a good idea to `select *` from any table
## Drop View
*Views* are often used to 
* obtain data for reports
* implement *security access control* (SAC) to data values in database
