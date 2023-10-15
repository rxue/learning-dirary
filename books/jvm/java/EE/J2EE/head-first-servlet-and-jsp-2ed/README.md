# Chapter 8: Script-free pages: scriptless JSP
## *EL* functions and handling "null"
### And a few other *EL* operators
The following operators does not have correspondig literals:

Arithmetic Operators
* `+` : note that this cannot be used in string concatenation
* `-`
* `*`
Arithematic Operators with corresponding literal:

Operator  | Literal | Note
----------|---------|------- 
`/`       | `div`   | you can divide by ZERO, and get INFINITY
`%`       | `mod`   | remainder operator against ZERO causes exception

Logical Operators with corresponding literal

Operator  | Literal | Note
`&&`      | `and`   | ...
`||`      | `or`    | ...
`!`       | `not`   | ...


One operator is not supported in EL, i.e. `&`

# Chapter 11: Deploying your web app: web app deploymet
## Key deployment task, what goes where
> Tag files (.tag) must be inside "WEB-INF/tags" or a sub-directory

page 608

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

# Chapter 12. Keep it secret, keep it safe: web app security
## Authentication revisited
> For a J2EE container, authentication comes down to this: ask for a user name and password, then verify that they match

### The 4 authentication types
#### use the browser's standard pop-up form for inputting the name and password
* BASIC
* DIGEST
* CLIENT-CERT
* FORM

page 677

# Chapter 13. The Power of Filters: wrappers and filters
## Exam Objectives
### Fun things to do with filters
#### Request filters can
* perform security checks
* reformat request headers and bodies
* audit or log requests

#### Response filters can
* compress the response stream
* append or alter the response stream
* create a different response altogether

> There is no such thing as a `RequestFilter` or `ResponseFilter` interface - it's just `Filter`. When we talk about a request filter or a response filter, we are talking only about how you use the filter, not the actual `Filter` interface

page 704

### Filters are modular, and configurable in the DD

> The DD controls the order in which the filters run

page 705

## A filter's lifecycle
> ...someone needs to know the order, and that someone is the `FilterChain`, driven by the filter elements you specified in the DD.

> ...`FilterChain` can invoke EITHER a Filter or a Servlet, depending on whether it's the end of the chain

page 708
## Declaring and ordering filters

Rules for `<filter-mapping>`

* The `<filter-name>` is mandatory and it is used to link to the correct `<filter>` element
* Either the `<url-pattern>` or the `<servlet-name>` element is mandatory
* the `<url-pattern>` element defines which web app resources will use this filter 
* the `<servlet-name>` element defines which single web resource will use this filter 

### Container's rule for ordering filters:

<blockquote>

When more than one filters is mapped a given resource, the container uses the following rules:

1. All filters with URL patterns are located first...Filters with matching URL patterns are placed in the chain in the order in which they are declared in the DD
2. Once all filters with matching URLs in the chain, the container does the thing with filters that have matching `<servlet-name>` in the DD

</blockquote>

page 710

### As of version 2.4, filters can be applied to request dispatchers
... what about resources requested from a *forward* or *include*, *requestdispatch* and/or the error handling? Servlet 2.4 comes to the rescue

* you can have from 0 to 4 `dispatcher` elements
* a `REQUEST` value activate the filter for client request. If no `dispatcher` element is present, `REQUEST` is the default

page 711

# Chapter 14: Enterpise Design Patterns: patterns and struts
## YES! It's *Structs* (and *Front Controller*) in a nutshell
> The basic idea of *Front Controller* is that a single component, usually a servlet but possibly a JSP, acts as a single control point for the *presentation* tier of a web application. With the Front Contoller pattern, all of the app's requests go through a single controller, which handles dispatching the request to the appropriate places. 

page 769 
