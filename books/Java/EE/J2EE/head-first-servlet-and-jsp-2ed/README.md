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

sole purpose in life is to initialize the app (and possibly to uninitialize it) - listener on servlet context

Reference on page 165

## configuring a listener in the DD

> this element (`<listener>`) is simple - it needs only the class name

> the `<listener>` element does not go inside a `servlet` element

Reference above is on page 174
## Eight Listeners: they are not just for context events...
### other listeners
> where there is a lifecyle moment, there is usually a *listener* to hear about it.

Reference above is on page 180

### The `HttpBindingListener`
> A plain old `HttpAttributeListener` is just a class that wants to know when any type of attribute has been added, removed or replaced in a Session. But the `HttpSessionBindingListener` exists so that the attribute itself can find out when it has been added to or removed from a *session*.



Reference above is on page 183

### Listener Chart
#### *Attribute Listeners*
 * `ServletRequestAttributeListener`
 * `ServletSessionAttributeListener`
 * `ServletSessionAttributeListener`



#### *Lifecyle Listeners*
 * `ServletRequestListener`
 * `ServletContextListener`
 * `HttpSessionListener`
 * `HttpSessionBindingListener`
 * `HttpSessionActivationListener`

Reference on page 184 (answer found on page 208)

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

## Request Attributes and Request Dispatching

> You can't forward the request if you've committed a response

`os.flush()` ...That's the line that causes the response to be sent to the client,

#### Getting a `RequestDispatcher` from `ServletRequest`

#### Getting a `RequestDispatcher` from `ServletContext`
You cannot specify a path relative to the current resource => **you must start the path with a forward slash**

Reference above is on page 206

# Chapter 6: Conversational state: session managment

> web servers have no short-term memory

Reference above is on page 223

## Session IDs, cookies and other session basics
> on the client's first request, the Container generates a unique session ID and gives it back to the client with the response. **The client sends back the session ID with each subsequent request**  
Reference above is on page 231
### the joy of *Cookies*
### The best part: the container does virtually all the cookie work!
> ... the container takes care of generating the session ID, creating a new `Cookie` object, stuffing the session ID into the cookie ...
<blockquote>
...somewhere in your `service` method you ask for a session, and everything else happens **automatically**

* You don't make the new `HttpSession` object yourself
* You don't generate the unique session ID
* You don't make the new `Cookie` object
* You don't associate the session ID with the cookie
* You don't set the Cookie into the response
</blockquote>
Reference above is on page 233

## URL rewriting: somthing to fall back on
URL encoding is all about response

Reference above is on page 239

## When sessions get stale; getting rid of bad sessions

<blockquote>
  <session-config>
    <session-timeout>15</session-timeout>
  </session-config>
</blockquote>

> you specify timeouts in the DD using MINUTES, but if you set a timeout programmatically, you specify SECONDS

> ...when you add a *Cookie* to the response, you pass a Cookie object...

> ...there is not a `setCookie()` method. There is only `addCookie()` method!

Reference above is on page 245

## Listener examples

Session counter in a *non-distributed system* as a typical use case of `HttpSessionListener`

page 261

# Chapter 11: Deploying your web app: web app deploymet
## Key deployment task, what goes where
> ...a WAR file, which stands for Web ARchive. And if that sounds suspiciously like a JAR, that's because a WAR is a JAR. A JAR with .war extension instead of .jar

page 611

## WAR files

## How servlet mapping REALLY works
### Servlet mapping can be "fake"
> EXACT match: must begin with a slash

`<url-pattern>/beer/*</url-pattern>`
> DIRECTORY match: must begin with a slash, always ends with an asterisk

`<url-pattern>*.do</url-pattern>`
> EXTENSION match: MUST begin with an asterisk (never a slash), after the asterisk, it must have a dot extension (.do, .jsp etc.)

Reference above is on page 618

### Key rules about servlet mappings
> 1) The Container looks for matches in the order shown on the opposite pages. In other words, it looks *first* for an *exact match*. If it can't find an exact match, it looks for a *directory match*. If it can't find a directory match, it looks for an extension match.

> 2) If a request matches more than one directory `<url-pattern>`, the container choose the longest mapping. In other words, a request for `/foo/bar/myStuff.do` will map to the `<url-pattern>/foo/bar/*` even though it also matches `<url-pattern>/foo/*`. The most specific match always wins.

Reference above is on page 619

```
<servlet>
  <servlet-name>Two</servlet-name>
  <servlet-class>foo.DeployTestTwo</servlet-class>
</servlet> 
<servlet-mapping>
  <servlet-name>Two</servlet-name>
  <url-pattern>fooStuff/bar</url-pattern>
</servlet-mapping>
<servlet>
  <servlet-name>Four</servlet-name>
  <servlet-class>foo.DeployTestFour</servlet-class>
</servlet> 
<servlet-mapping>
  <servlet-name>Four</servlet-name>
  <url-pattern>fooStuff/bar/*</url-pattern>
</servlet-mapping>
```
`http://localhost:8080/test/fooStuff/bar/` maps to `Four`
`http://localhost:8080/test/fooStuff/bar` maps to `Two`

 
Reference above is on page 621

## Configuring servlet initialization in the DD
> If you have multiple servlets that you want preloaded, and you want to control the order in which they're initialized, the value of `<load-on-startup>` determines the order!

> Any number (load-on-startup) greater than zero mean "initialize the servlet at deployment or server startup time rather than waiting for the first request"

> ...what if there is more than one servlet with a load-on-startup of 4? The container loads the servlets with the same value in the order in which servlets are declared in the DD

Reference above is on page 628

# Chapter 13: The Power of Filters: wrappers and filters
## Container's rule for ordering filters:

<blockquote>
When more than one filters is mapped a given resource, the container uses the following rules:  

1. All filters with URL patterns are located first...Filters with matching URL patterns are placed in the chain in the order in which they are declared in the DD
2. Once all filters with matching URLs in the chain, the container does the thing...
</blockquote>

