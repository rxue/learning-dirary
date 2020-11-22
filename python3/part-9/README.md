# [*Static* Features](https://python-s20.mooc.fi/osa-9/5-staattiset-piirteet)
## *Static class*

Java


Python

```
class Person:
  __id_increment = 0
  @classmethod
  new_id(cls):
    Test.__id_increment += 1
    return Test.__id_increment
```

Java Equivalence

```
public class Person {
  private static int idIncrement = 0;
  public static newId() {
    idIncrement += 1;
    return idIncrement;    
  } 
}
```

