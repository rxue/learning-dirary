# Optimistic Offline Lock
## How It Works
> ... associate a version number with each record in your system.

## When to Use It
> Optimistic concurrency management is appropriate when the chance of *conflict* between any two business transactions is low. ... *Pessimistic Offline Lock* is more appropriate when the chance of conflict is high or the expense of a conflict is unacceptable.

> ... consider using it (optimistic locking) as the default approach to business transaction conflict management in any system you build.
 
# Pessimistic Offline Lock
The problem of *Optimistic lock* is

> If several people access the same data within a business transaction, one of them will commit easily but the others will conflict and fail. Since the conflict is only detected at the end of the business transaction, the victims will do all the transaction work only to find at the last minute that the whole thing will fail and their will have been wasted. If this happens a lot on lengthy business transactions the system will soon become very unpopular.

## When to use it

> 
