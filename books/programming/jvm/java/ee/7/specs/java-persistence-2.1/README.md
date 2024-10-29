# Chapter 4 Query Language
## 4.6 Conditional Expression
### 4.6.9. `IN` Expressions
```
in_expression ::=
  {state_valued_path_expression | type_discriminator} [NOT] IN
    { ( in_item {, in_item}* ) | (subquery) | collection_valued_input_parameter } in_item ::= literal | single_valued_input_parameter }
```
**KEY TAKEAWAY**

Note about the `single_valued_input_parameter`. There is no bracket and the value can be assigned with .e.g. `setParameter(list)`. This feature is way different from the `IN` expression in *SQL* in that *SQL* 's `IN` has to look sth like `IN (1,2,3,4)` with brackets

# Chapter 8 Entity Packaging
## 8.2. Persistence Unit Packaging
> A *persistence unit* is defined by a `persistence.xml` file

