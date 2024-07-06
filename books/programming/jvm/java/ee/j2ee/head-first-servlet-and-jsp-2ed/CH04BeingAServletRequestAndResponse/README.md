# Chapter 4: Being a Servlet: request and response

## The Three Big Lifecycle Moments

> You should NOT override the `service()` method. Your job is to override the `doGet()` and/or `doPost()` methods and let the `service()` implementation from `HTTPServlet` worry about calling the right one.

Book page 99

> ... the *Container* calls my servlet's `init()` method, but if I don't override `init()`, the one from `GenericServlet` runs. Then when a request comes in, the Container starts or allocates a thread and calls the `service()` method. from `HttpServlet` runs. The `HttpServlet` `service()` method then calls my overridden `doGet()``or `doPost()`. So each time my `doGet()` or `doPost()` runs, it's in a separate thread.

> The `service()` method figures out which *HTTP method* (`GET`, `POST` etc.) is in the request, and invokes the matching `doGet()` or `doPost()` method. The `doGet()` and `doPost()` inside `HttpServlet` don't do anything, so you have to override one or both. This thread dies (or is put back in a *Container-managed pool*) when service completes.

Book page 100

## Each request runs in a separate thread!
![One servlet instance corresponds to multiple threads](https://user-images.githubusercontent.com/3033388/225286901-b545b01b-7762-4b13-9418-a5af11ed9da6.png)

> one servlet per request. The container doesn't care who makes the request - every incoming request means a new thread thread/stack

Book page 101

### `ServletConfig` and `ServletContext`
* one `ServletConfig` object per `Servlet` and `ServletConfig` is used to access the `ServletContext`
* one `ServletContext` per web app

page 104 (pdf page 129)

## A Servlet's REAL job is to handle *GET* and *POST* requests
> CONNECT says to connect for the purpose of tunneling
### The difference between *GET* and *POST*
> *POST* has a body. That's the key. Both *GET* and *POST* can send parameters, but with *GET*, the parameter data is limited to what you can stuff into the request line.

![GET VS POST](https://user-images.githubusercontent.com/3033388/230796557-4dbacca4-f481-45b0-91c5-ede970ac4687.png)

page 110 (pdf page 135)

> Besides size, security and bookmarking, there is another crucial difference between the GET and POST - the way they are supposed to be used. GET is meant to be used for getting things. ... the point is - you are not making any changes on the server! *POST* is meant to be used for sending data to be processed. ... when you think of *POST*, think: update. Think: use the data from the *POST* body to *change something on the server*

page 111 (pdf page 136)

## Sending and using parameter(s)
> Q: Why would I ever want to get an `InputStream` from the request?

> A: With a *GET* request, there is nothing but the request header info. In other words, there is no body to care about. BUT... with an HTTP POST, there is a *body* info. Most of the time, all you care about from the body is sucking out the parameter values using `request.getParameter()` but those values might be large. It is also possible to create a servlet that processes a computer-driven request in which the body of the request holds textual or binary content to be processed. In this case you can use `getReader` or `getInputStream` methods. These streams will only contain the *body* of the http request and not the header.

page 123 (pdf page 148)


## So that's the Requests... let's see the *Response*

> The `getResourceAsStream()` requires you to start with forward slash `/`, which represent the root of your web app.

`response.setContentType("application/jar")`

> when we say *content type* we mean the same thing as *MIME type*. Content Type is an http header that must be included in the HTTP response.

Comment MIME types

 * `text/html`
 * `application/pdf`
 * `video/quicktime`
 * `application/java`
 * `image/jpeg`
 * `application/jar`
 * `application/octet-stream`
 * `application/x-zip`

## Servlet Redirect VS Dispatcher

On page 137:
> if you look up `sendRedirect` in the API, you will see that it throws an `IllgelStateException` if you try to invoke it after the response has already been *committed*

> you can't write to response and then send to redirect


## Review: Servlet lifecyle and API
* The `init()` method gives servlet access to the `ServletConfig` and `ServletContext` objects, which the servlet needs to get information about the servlet configuration and the web app

