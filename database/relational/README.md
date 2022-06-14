# Transaction
## Isolation & Consistency
### Isolation Level

> *Serializability* is a useful concept because it allows programmers to ignore issues related to concurrency when they code transactions. ... **The use of weaker levels of consistency places additional burdens on programmers for ensuring database correctness**.

Reference: Database System Concepts 7th Ed > Chapter 17 Transactions > 17.8 Transaction Isolation Levels

### Inconsistent problems in isolation level other than *Serialized*

 * non-repeatable read ([example demo](https://www.youtube.com/watch?v=Afw-zgJ9Wxc))

These inconsistent problems happens only when there are multiple transactions running concurrently, i.e. *serialized*. In summary, it is about: transaction A reads data X for the first time, then another transaction other than transaction A updated data X and committed the update, then when transaction A reads data X for the second time, it is different from what was read fro the first time. This difference might be about update corresponding to *non-repeatable read* or more newly inserted rows corresponding to *phantom read* 

#### Default Isolation Level for Different Databases

Database                                                                                                                                                                      | Default Isolation Level
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------
 [Oracle](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/SET-TRANSACTION.html#GUID-F11E1E30-5871-48D1-8266-F80A1DF126A1)                                 | *Read Committed*
 [Postgres](https://www.postgresql.org/docs/current/transaction-iso.html#:~:text=Read%20Committed%20is%20the%20default,query%20execution%20by%20concurrent%20transactions.)   | *Read Committed*
 [MySQL](https://dev.mysql.com/doc/refman/5.6/en/set-transaction.html#:~:text=The%20default%20isolation%20level%20is,%2C%20READ%20UNCOMMITTED%20%2C%20and%20SERIALIZABLE%20.) | *Repeatable Read*

#### Real inconsistent cases in normal transaction level

 * [Conflicting write and lost update in a *Read Committed* transaction](https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/data-concurrency-and-consistency.html#GUID-8A15F1B2-3F64-49E7-929D-4768B2DB7DD7)

