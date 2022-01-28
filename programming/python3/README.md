# Java 8 VS Python3.6+

## [Operators](https://docs.python.org/3.4/library/operator.html#module-operator)

Operation       | Java    | Python3   | Result
----------------|---------|-----------|-------
Exponentiation  | `4^2`   | `4**2`    | 16
division        | `9.0/2` | `9/2`     | 4.5
Floor division  | none    | `8.5//2`  | 4.0
Floor division  | `9/2`   | `9//2`    | 4

### Comparison Operators
Python3 Operators |Operations                                                                                                   |Python3 Example          |Java Equivalence
------------------|-------------------------------------------------------------------------------------------------------------|-------------------------|----------------
`>` `<`           |comparision                                                                                                  |`1 < a < 5`              |`a > 1 && a < 5`
`+`               |concatenate int to string                                                                                    |`str(1) + "x"`           |`1 + "x"`
`+`               |append a list to another                                                                                     |`list1 = list1 + list2`  |`list1.addAll(list2)` 
`is`              |test if two object references refer to the same object instance                                              |`a is b`                 |`a == b`
`==`              |test if the object references referring to are the same even though they might be totally different instance |`a == b`                 |`a.equals(b)`    
Reference: //python-s20.mooc.fi/osa-9/1-oliot-ja-viittaukset 
# [Built-in Types](https://docs.python.org/3.7/library/stdtypes.html)
## [True Value Testing](https://docs.python.org/3.7/library/stdtypes.html#truth-value-testing)
Any Object can be tested for true value, for use in an `if` or `while` condition or as operand of the boolean operations below.

## If Condition

## Boolean
Java    | Python3
--------|--------
`true`  |`True`
`false` |`False`

# Class
## Luokka on olion käsikirjoitus
Materiaalissa on jo aiemmin vilahtanut (gleam 闪现) käsite.

## Access modifier
modifer   |Python           |Java
----------|-----------------|-------------------------
*private* |`self.__example` |`private Object example;`

# Functional Programming
In `max`, `min`, the given sequence cannot be empty

# [Command line and environment](https://docs.python.org/3/using/cmdline.html)
