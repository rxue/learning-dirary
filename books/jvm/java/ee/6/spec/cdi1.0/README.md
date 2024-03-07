# Chapter 3. Programming Model
## 3.9. Initializer Method
Initializer method : non-abstract, non-static, non-generic method of a bean class, or of any Java EE component class supporting injection.
### 3.9.1 Declaring an initializer method
setter is initializer method

**OWN COMMENT**
Note that the `@Inject` annotation cannot be on the method parameter but only on the method level. In this aspect, it is different from [`@Autowired`](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/beans/factory/annotation/Autowired.html) in Spring. Since there is `PARAMETER` in the `@Target` in `@Autowired`, `@Autowired` can be annotated to the method parameter, whereas `@Inject` cannot

