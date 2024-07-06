# Chapter 3. Hypermedia Design
## 3.6. Designing Consistent Data Writes with Idempotent Actions
### Problem
*double-posting*
### Solution
`PUT` can be easily engineered to prevent *double-posting* ?


# Chapter 5. Hypermedia Services
## 5.14 Increasing Throughput with Client-Supplied Identifiers

## 5.15. Improving Reliability with *Idempotent* Create
### Example
**Key takeaway of implement idempotent `PUT`**
 request for  | requested resource state                      | response code | meaning of response code
--------------|-----------------------------------------------|---------------|-------------------------
 create       | resource does not exist                       | `201`         | *created*
 create       | resource exists already                       | `409`         | *conflict*
 update       | resource exists                               | `200`         | *OK*
 update       | not existing resource or *entity tag* mismatch| `409`         | *conflict*

Question: what is that *Etag* header about?

NOTE! use `PUT` to create new resource is on the base of **generating ID on the client side** so that there is id on the request URL!
