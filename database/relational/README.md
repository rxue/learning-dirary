# Transaction
## Isolation & Consistency
### [ANSI/ISO Transaction Isolation Levels](https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/data-concurrency-and-consistency.html#GUID-7F2C6927-5482-4144-B43B-5E90EF4E055B)

Isolation levels are defined by 3 preventable phenomenas [phenomena that must be prevented between concurrently executing transactions](https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/data-concurrency-and-consistency.html#GUID-AD960556-7F7B-4242-8B91-6DA22AABA27D)
 * dirty read
 * non-repeatable read - the current transaction would not see the change of amount of rows but see the other transactions' committed `update`
 * phatom read - the current transaction would see other transactions' committed `delete` or `insert` rows


 * [Example in Chinese video tutorial](https://www.youtube.com/watch?v=Afw-zgJ9Wxc)
 * Example in Oracle's Database Concepts: [Conflicting write and lost update in a *Read Committed* transaction](https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/data-concurrency-and-consistency.html#GUID-8A15F1B2-3F64-49E7-929D-4768B2DB7DD7)


#### 4 isolation levels defined by the aforementioned 3 phenomenas

Isolation level   | dirty read  | non-repeatable read   | phantom read
------------------|-------------|-----------------------|--------------
Read uncommitted  | possible    | possible              | possible
Read committed    | not possible| possible              | possible
Repeatable Read   | not possible| not possible          | possible
Serializable      | not possible| not possible          | not possible

> *Serializability* is a useful concept because it allows programmers to ignore issues related to concurrency when they code transactions. ... **The use of weaker levels of consistency places additional burdens on programmers for ensuring database correctness**.

Reference: Database System Concepts 7th Ed > Chapter 17 Transactions > 17.8 Transaction Isolation Levels

#### Default Isolation Level for Different Databases

Database                                                                                                                                                                      | Default Isolation Level
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------
 [Oracle](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/SET-TRANSACTION.html#GUID-F11E1E30-5871-48D1-8266-F80A1DF126A1)                                 | *Read Committed*
 [Postgres](https://www.postgresql.org/docs/current/transaction-iso.html#:~:text=Read%20Committed%20is%20the%20default,query%20execution%20by%20concurrent%20transactions.)   | *Read Committed*
 [MySQL](https://dev.mysql.com/doc/refman/5.6/en/set-transaction.html#:~:text=The%20default%20isolation%20level%20is,%2C%20READ%20UNCOMMITTED%20%2C%20and%20SERIALIZABLE%20.) | *Repeatable Read*




