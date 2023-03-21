
> If you encounter a naming conflict, you can use the name attribute of the `@WebServlet` annotation to specify a unique mapping name for the servlet

> If you use both the `web,xml` and the `@WebServlet` annotation to map the same servlet name to one or more URLs, the mapping in the web.xml file overrides the same servlet name to one or more UTLs, the mapping in the `web.xml` file overrides the mapping in the annotation.

reference: Murach's Java Servlets and JSP Programming > Chapter 5 How to Develop Servlets > How to Create and Map a Servlet > How to map a servlet with an annotation

# `javax.servlet`
## `SingleThreadModel` is deprecated nowadays
refernce: https://github.com/jakartaee/servlet/issues/269

Disappearance of it in *jakartaee 10* is the proof

# `HttpSession`
## Implementation of `HttpSession.invalidate()`
Take *Wildfly* as an example, a servlet invoking the `HttpSession.invalidate()` causes a *reponse* with `Set-Cookie` header something like

`Set-Cookie: JSESSIONID=PcAmFyTumd4yOxAUeZRfOahnMv0DdmWVqyVyB1ph.4e8cf55aef28; path=/helloworld; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:00 GMT`

Worth noting about the `Max-Age=0` and `Expires=Thu, 01-Jan-1970 00:00:00 GMT`. This practical exercise proves that zeroing of `Max-Age` terminates a *cookie* and, it corresponds the Java Doc of `Cookie.setMaxAge(int)`:
 
> A zero value causes the cookie to be deleted

## Set value of `HttpSession.setMaxInactiveInterval` vs `Cookie.setMaxAge`
value                                 | <0                                                    | 0                                                    | >0
--------------------------------------|-------------------------------------------------------|------------------------------------------------------|------------------------------------------------------------
`HttpSession.setMaxInactiveInterval`  | NO VALID INACTIVE INTERVAL => Session never timeout   | NO VALID INACTIVE INTERVl => Session never timeout   | Session closed after the given seconds of INACTIVE INTERVAL
`Cookie.setMaxAge`                    | Cookie deleted when the browser exits                 | Cookie deleted                                       | Cookie deleted after the given seconds

