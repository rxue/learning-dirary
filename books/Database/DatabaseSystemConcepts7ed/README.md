# Chapter 3: Introduction to SQL
## 3.2. SQL Data Definition
### 3.2.1. Basic Data Types
* `char(n)`: A fixed-length character string with user-specific length `n`
* `varchar(n)`: A variable length character string with user-specific maximum length `n`
# Chapter 4: Intermediate SQL
## 4.1. Join Expressions
### 4.1.1. Natural Join
> ... natural join considers only those pairs of tuples with the same value **on those attributes that appear in the schemas of both relations**.

**Self comments**: With the following code as example, the explanation above means:

```
CREATE TABLE student (
  id CHAR(5) PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);
CREATE TABLE takes (
  id CHAR(5) NOT NULL,
  course_id VARCHAR(7) NOT NULL,
  semester VARCHAR(6) NOT NULL,
  year INT NOT NULL
);
```

1. The word *natural* means join *automatically*, thus there should be columns(s) on both tables with the same name: Both the `student` and `takes` table above have column named `id`. In this case *natural join* will work through this `id` column. NOTE! In case there is no common column, e.g. in the 2 tables above, the `takes.id` column renamed to `takes.student_id`, the *natural join* would not work but *Cartesian product* would be the result instead

2. Result of *natural join* includes only the rows (tuples) with the same value on the joined column(s): For example, if the `student` table has a row with an `id` not existing in the `takes` table, this row would not be in the *natural join* result and vice versa

## 3.10. Summary
> SQL supports basic set operations, including `union` , `intersect` and `except` , which corresponds to the mathematical set operations ...

**Self comments** : *set operations* mean the result is also a set that there is no repeat element
