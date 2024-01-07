# Chapter 6. Mapping Inheritance
## 6.8 *Polymorphic associations*
### 6.8.1 Polymorphic *many-to-one* associations
### 6.8.2 Polymorphic collections
# Chapter 7. Managing collections and entity associations
Heart of ORM : manage associations between classes and relationships between tables
**Major new features in JPA 2**
## 7.1. Sets, bags, lists and maps of value types
### Selecting a collection interface
`java.util.Collection` - *bag* semantics
### 7.1.5. Mapping an identifier *bag*
*Bag* : an *unordered collection* that allows duplicate elements


# Chapter 8. Advanced entity association mappings
## 8.2 one-to-many associations

# Chapter 11. Transactions and Concurrency
## 11.2 Controlling Concurrent Access
### 11.2.2 Optimistic Concurrency Control
*Versioning* is turned off by default. 
It is a *first commit win*
#### ENABLE VERSIONING
Versioning is enabled with `@Version`

You shouldn't have setter method `setVersion`
version field can be `int`, `short`, `long` along with their auto-boxing types. Hibernate wraps and start from 0 again if version number reaches the limit of the data type

![How does the automatic optimistic locking work](https://private-user-images.githubusercontent.com/3033388/294563779-a0986792-3703-423c-a446-03036babb48a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDQ0NzUxMzYsIm5iZiI6MTcwNDQ3NDgzNiwicGF0aCI6Ii8zMDMzMzg4LzI5NDU2Mzc3OS1hMDk4Njc5Mi0zNzAzLTQyM2MtYTQ0Ni0wMzAzNmJhYmI0OGEucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI0MDEwNSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNDAxMDVUMTcxMzU2WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ODg3YjhjZTc0OTBjNDg4MTI2MDNlM2FiMWMwMGY0MmRlNWU5MmExNDc2OTFlOGZlMjhhMWU3NTA1NDFmMGQ3NSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmYWN0b3JfaWQ9MCZrZXlfaWQ9MCZyZXBvX2lkPTAifQ.K9DsdrHDWpi0t_t3PEfQKcWGkCZ8Hk4D-mOAhcw8bak)

### Explicit Pessimistic Locking


