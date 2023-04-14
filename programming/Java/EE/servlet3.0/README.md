
> If you encounter a naming conflict, you can use the name attribute of the `@WebServlet` annotation to specify a unique mapping name for the servlet

> If you use both the `web,xml` and the `@WebServlet` annotation to map the same servlet name to one or more URLs, the mapping in the web.xml file overrides the same servlet name to one or more UTLs, the mapping in the `web.xml` file overrides the mapping in the annotation.

reference: Murach's Java Servlets and JSP Programming > Chapter 5 How to Develop Servlets > How to Create and Map a Servlet > How to map a servlet with an annotation

# `javax.servlet`
## `HttpServletResponse`
### Status code constants
 * `SC_ACCEPTED` - 202
 * `SC_NOT_FOUND` - 404
`


## `SingleThreadModel` is deprecated nowadays
refernce: https://github.com/jakartaee/servlet/issues/269

Disappearance of it in *jakartaee 10* is the proof
# `javax.servlet.http`
## `HttpServlet`
### Design logic of `HttpServlet`
the `protected` `do` methods on `HttpServlet` corresponds to all the *methods* of [http/1.1](https://www.ietf.org/rfc/rfc2616.txt) except for the *CONNECT*, which is typically used in connection with proxy server

## `HttpServletRequest`
### `HttpServletRequest.getSession()` is equivalent to `HttpServletRequest.getSession(true)`
Meaning if the request does not have a session, a new session will be created and returned

Guess on the design logic: avoid NPE (`NullPointerException`)

### practical knowledge of `getParameter(String name)`
On the bottom level:

* in case of `GET` with default `enctype` (`application/x-www-form-urlencoded`), the `getParameter(String name)` fully corresponds to `getQueryString()`, say gets all parameters from URL
* in case of `POST` with default `enctype` (`application/x-www-form-urlencoded`), the `getParameter(String name)` get data from the HTTP *body* and URL
* NOTE! in case of `POST` with `enctype` (`multipart/form-data`), the `getParameter(String name)` get data from URL only just like the case of `GET` since the *body* data could only be retrieved from `ServletRequest.getInputStream`

Code reference: https://github.com/rxue/full-stack-kata/blob/main/backend/Java/EE/Jakarta/10/helloworld/src/main/java/book/hfsj/ch04/BeerSelect.java


## `HttpSession`
### Implementation of `HttpSession.invalidate()`
Take *Wildfly* as an example, a servlet invoking the `HttpSession.invalidate()` causes a *reponse* with `Set-Cookie` header something like

`Set-Cookie: JSESSIONID=PcAmFyTumd4yOxAUeZRfOahnMv0DdmWVqyVyB1ph.4e8cf55aef28; path=/helloworld; Max-Age=0; Expires=Thu, 01-Jan-1970 00:00:00 GMT`

Worth noting about the `Max-Age=0` and `Expires=Thu, 01-Jan-1970 00:00:00 GMT`. This practical exercise proves that zeroing of `Max-Age` terminates a *cookie* and, it corresponds the Java Doc of `Cookie.setMaxAge(int)`:
 
> A zero value causes the cookie to be deleted

### Set value of `HttpSession.setMaxInactiveInterval` vs `Cookie.setMaxAge`
value                                 | <0                                                        | 0                                                    | >0
--------------------------------------|-----------------------------------------------------------|------------------------------------------------------|------------------------------------------------------------
`HttpSession.setMaxInactiveInterval`  | NO VALID INACTIVE INTERVAL => Session never timeout       | NO VALID INACTIVE INTERVl => Session never timeout   | Session closed after the given seconds of INACTIVE INTERVAL
`Cookie.setMaxAge`                    | Cookie deleted when browser exits, i.e. *session cookie*  | Cookie deleted                                       | Cookie deleted after the given seconds

Cookie's `Max-Age` set to negative value makes the cookie on client side a [*session cookie*](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies). With Chrome's developer tool, we can see that sometimes the value of `Expires/Max-Age` is set to *Session*, which means a "browser's" *session cookie* and its life ends when browser is closed.
