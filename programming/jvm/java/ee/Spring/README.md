# 20190710
## [SimpleDriverDataSource](https://docs.spring.io/spring/docs/current/javadoc-api/org/springframework/jdbc/datasource/SimpleDriverDataSource.html)

# 20230331
## GraphQL request with Spring
https://medium.com/decathlondigital/minimal-graphql-client-request-with-spring-boot-22e0041b170

# Testing
## [Integration Testing](https://docs.spring.io/spring-framework/reference/testing/integration.html)
### [TransactionManagement](https://docs.spring.io/spring-framework/reference/testing/integration.html#testing-tx)
> By default, the framework creates and rolls back a transaction for each test... if a test method deletes the contents of selected tables while running within the transaction managed for the test, the transaction rolls back by default, and the database returns to its state prior to execution of the test.

> If you want a transaction to commit (unusual, but occasionally useful when you want a particular test to populate or modify the database), you can tell the TestContext framework to cause the transaction to commit instead of roll back by using the `@Commit` annotation.
