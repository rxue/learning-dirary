# Unit of Work
## Application of Unit of Work
https://stackoverflow.com/questions/3532258/what-is-the-source-of-the-unit-of-work-pattern

# Identity Map
> An *Identity Map* keeps a record of all objects that have been read from the database in a single business transaction. Whenever you want an object, you check the *Identity Map* first to see if you already have it.

COMMENT: It is worth to note that the responsiblity of *Data Mapper* is not only *find* but also **insert and update** 
