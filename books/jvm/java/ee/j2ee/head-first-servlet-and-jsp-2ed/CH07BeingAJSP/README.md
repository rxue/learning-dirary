# Chapter 7. Being a JSP: using JSP
## Create a simple JSP using "out" and a page *directive*
> The Container takes what you've written in your JSP, *translates* it into a servlet class source (.java) file, then *compiles* that into a Java servlet class. After that it's just servlets all the way down, ..In other words, the Container loads the servlet class, instantiates and initializes it, makes a separate thread for eash request, and calls the servlet's ``service()` method. 

page 283

### Using the *page directive* to import the packages (20230819, 20240323)

*directive* : 
 * starts with `<%@ ` 
 * a way for you to give special instructions to the Container at page translation time. 

3 flavors of *directives* :
 * `<%@ page`
 * `<%@ include`
 * `<%@ taglib`

label: `1Z0-900`

example of *page directive*

`<%@ page import="foo.*" %>`

Reference: page 287 (pdf page 312)

**SELF-COMMENT AND ANALYSIS**

Typical *directives*:
* in Java: `import` is directive (refer to Core Java book)
* in C: https://cplusplus.com/doc/tutorial/preprocessor/ is the `#include` e.g. `#include <iostream>`


### using *expressions*
*scriptlet* code* : `<% out.println(Counter.getCount()); %>`

<=>

*expression* code : `<%= Counter.getCount() %>`
 - no semi-colon
 - avoid use of `out` implicit object

Reference: page 288 (pdf page 313)



## Time to see a JSPgenerated servlet

*implicit objects* are initialized when a JSP is translated into a servlet

API			| *Implicit Object*
------------------------|------------------------
`JspWriter`		| `out`
`HttpServletRequest`	| `request`
`HttpServletResponse`	| `response`
`HttpServletSession`	| `session`
`ServletContext`	| `application`
`ServletConfig`		| `config`
`Throwable`		| `exception` (only available when `isErrorPage="true"`)
`PageContext`		| `pageContext`
`Object`		| `object`


page 298 / pdf 323

## The Lifecycle and initialization of JSP
### Lifecyle of a JSP
page 306
### Attribute in a JSP
Scope		| In a servlet						| In a JSP (using *implicit objects*)
----------------|-------------------------------------------------------|------------------------------------------
Application	| `getServletContext().setAttribute("foo", barObj)`	| `application.setAttribute("foo", barObj)`
Request		| `request.setAttribute("foo", barObj)`			| `request.setAttribute("foo", barObj)`
Session		| `getSession().setAttribute("foo", barObj)`		| `sesion.setAttribute("foo", barObj)`
Page		| Does not apply					| `pageContext.setAttribute("foo", barObj)`

> ...Remember, when you see "Context", think "application"

(page 311/pdf 336)

#### three directives
(page 314/pdf 339)

##### attributes to the *page directive*

`isErrorPage` - 
 * defines whether the current page represents another JSP's error page. 
 * default value: `false`
 * if `isErrorPage="true"`, 



