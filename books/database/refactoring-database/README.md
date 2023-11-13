# Chapter 1. Evolutionary Database Development
## 1.5. Developer Sandboxes
## 1.6. Implementations to Evolutionary Database Development Techniques
last 1970s - early 1980s : *code-and-fix*


# Chapter 2. Database Refactoring
## 2.2. Database Refactoring
### 2.2.3. Maintaining Semantics
> On the surface, the Introduce Column sounds like a perfectly fine refactoring; adding an empty column to a table does not change the semantics of that table until new functionality begins to use it. We still consider it a transformation (but not a refactoring) because it could inadvertently change the behavior of an application. For example, if we introduce the column in the middle of the table, any program logic using positional access (for example, code that refers to column 17 rather than the column's name) will break.
