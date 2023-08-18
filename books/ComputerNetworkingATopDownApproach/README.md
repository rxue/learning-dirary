# Chapter 2 Application Layer
## 2.1 Principles of Network Applications
### Transport Services Provided by the Internet
*full-duplex* : two processes can send messages to each other over the connection at the same time

## 2.2 The Web and HTTP
### Overview of HTTP
HTTP is a *stateless protocol* in that the server does not store any state information about the client

### HTTP Message Format
> The greate majority of HTTP request messages use the *GET* method.

> ...The *entity body* is empty with the `GET` method, but is used with the `POST` method.

> An HTTP client often uses the POST method when the user fills out a form

### User-Server Interaction: *Cookie*
Cookie is used to create a user session layer on top of *stateless HTTP*

Self-comment: In Java EE, the user session mentioned above is the [`HttpSession`](https://docs.oracle.com/javaee/7/api/javax/servlet/http/HttpSession.html). The user session is a server-side stuff, in this sense it is independent from the HTTP protocol
