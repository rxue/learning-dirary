# Chapter 5: Being a webapp: attributes and listeners
## *Init Parameters* and `ServletConfig` to the rescure
In the DD file:
```
<servlet>
  	<servlet-name>BeerParamTests</servlet-name>
  	<servlet-class>BeerInitParams</servlet-class>

	<init-param>
		<param-name>adminEmail</param-name>
		<param-value>likewecare@wickedlysmart.com</param-value>
	<init-param>
</servlet>
```

Page 150

> You can't use servlet init parameters until the servlet is initialized

page 151

In another word, you can't call `ServletConfig.getInitParameter` inside a servlet constructor

The only one `init` method of `HttpServlet` you need to *override* is the one with *no-arg*

## Context init parameters to the rescue
```
<servlet>
  	<servlet-name>BeerParamTests</servlet-name>
  	<servlet-class>BeerInitParams</servlet-class>
</servlet>

<context-param>
	<param-name>adminEmail</param-name>
	<param-value>clientheaderror@wickedlysmart.com</param-value>
</context-param>
```

Page 157

## Servlet and Context Init Parameters (page 160/pdf page 185)

The most use case of `context parameter` : storing the database lookup name

> Think of init parameters as deploy-time constants!

> You can get them at runtime, but you can't set them There is no `setInitParameter().`

=> if the init parameter, either servlet or context, changes in the *DD*, only redeployment could reflect the change

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


