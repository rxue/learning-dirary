# Chapter 4: Being a Servlet: request and response

## Servlet Initialization and Threads
![One servlet instance corresponds to multiple threads](https://user-images.githubusercontent.com/3033388/225286901-b545b01b-7762-4b13-9418-a5af11ed9da6.png)

`ServletRequest.getInputStream` returns the *content of the http body*

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

# Chapter 5: Being a webapp: attributes and listeners
## *Init Parameters* and `ServletConfig` to the rescure
> You can't use servlet init parameters until the servlet is initialized

In another word, you can't call `ServletConfig.getInitParameter` inside a servlet constructor

The only one `init` method of `HttpServlet` you need to *override* is the one with *no-arg*

## Servlet and Context Listeners

> Think of init parameters as deploy-time constants!

> You can get them at runtime, but you can't set them There is no setInitParameter().

Reference above is on page 60

## Context Parameter Limitations
> You can put the DataSource lookup name in the in a context init parameter, and that's probably the most common use of the context parameters.

Reference above is on page 164

## Request attributes are *thread-safe*

> only request variables and local variables are *thread-safe* !

<blockquote>
...Look at a well-writen servlet, and chances are you won't find any *instance variables*. Or at least any that are non-final. ...

So just don't use instance variable if you need thread-safe state, because all threads for that servlet can step on instance variables.

Q: Then what SHOULD you need if you need multiple instances of the servlet to share something?

A: ... if you need all the threads to access a value, decide which attribute state makes the most sense, and store the value in an *attribute*. Chances are, you can solve your problems in one of two ways:

1. declare the variable as local variable within the service method, rather than as instance variable.

or

2. Use an attribute in the most appropriate scope.

</blockquote>
Reference above is on page 204



# Chapter 13: The Power of Filters: wrappers and filters
## Container's rule for ordering filters:

<blockquote>
When more than one filters is mapped a given resource, the container uses the following rules:  

1. All filters with URL patterns are located first...Filters with matching URL patterns are placed in the chain in the order in which they are declared in the DD
2. Once all filters with matching URLs in the chain, the container does the thing...
</blockquote>
