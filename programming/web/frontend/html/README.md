# `form`
## Practical knowledge on `enctype` attributes
Value `multipart/form-data` causes client to generate `Content-Length` and `Content-Type` with value `multipart/form-data`. Whereas value `application/x-www-form-urlencoded`, i.e. the default `enctype` value, doesn't generate `Content-Length` nor `Content-type` header

Practice for proof: https://github.com/rxue/full-stack-kata/blob/main/backend/Java/EE/Jakarta/10/helloworld/src/main/java/book/hfsj/ch04/BeerSelect.java
