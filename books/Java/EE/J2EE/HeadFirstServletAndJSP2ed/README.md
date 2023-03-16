# Chapter 4: Being a Servlet: request and response

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

# Chapter 13: The Power of Filters: wrappers and filters
## Container's rule for ordering filters:

<blockquote>
When more than one filters is mapped a given resource, the container uses the following rules:  

1. All filters with URL patterns are located first...Filters with matching URL patterns are placed in the chain in the order in which they are declared in the DD
2. Once all filters with matching URLs in the chain, the container does the thing...
</blockquote>
