# Chapter 6. Conversational state: session management

> **web servers have no short-term memory**

Reference page: 223/pdf 248



## recognizing the client (page 230/pdf 255)
Http protocol is *stateless*, meaning *Http protocol* use *stateless connection* => it is like each request is from a new client



## Session IDs, cookies and other session basics (page 231/pdf 256)
> on the client's first request, the Container generates a unique session ID and gives it back to the client with the response. **The client sends back the session ID with each subsequent request**  
## How do the *client* and *container* exchange *session ID* info (page 232/pdf 257)
![The rationale of exchange of session ID with cookie through http](https://private-user-images.githubusercontent.com/3033388/292659083-519d95b6-d131-4eef-9558-2e808416c969.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDM0MDI0NTIsIm5iZiI6MTcwMzQwMjE1MiwicGF0aCI6Ii8zMDMzMzg4LzI5MjY1OTA4My01MTlkOTViNi1kMTMxLTRlZWYtOTU1OC0yZTgwODQxNmM5NjkucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQUlXTkpZQVg0Q1NWRUg1M0ElMkYyMDIzMTIyNCUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyMzEyMjRUMDcxNTUyWiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YWZkNTU4M2FhYjU2N2Q4YWJlMjI3OGIxZDA3ZDZmMmVmNTg5MjljZWQ3Y2QzNGIzZDExYTFiYTFkNjhkZGUzOCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmYWN0b3JfaWQ9MCZrZXlfaWQ9MCZyZXBvX2lkPTAifQ.0Tu2guloHoMk4kaJzCbcBmZsi2NynuiqOGOI2-xXWEU)

NOTE! the header `Cookie` in the requests after the initial one and the `Set-Cookie` in the response are according to the standard [Http State Management Mechanism](https://www.rfc-editor.org/rfc/rfc6265)

### The best part: the container does virtually all the cookie work! (page 233/pdf 258)
> ... the **container takes care of generating the session ID**, creating a new `Cookie` object, stuffing the session ID into the cookie ...

<blockquote>
...somewhere in your `service` method you ask for a session, and everything else happens **automatically**

* You don't make the new `HttpSession` object yourself
* You don't generate the unique session ID
* You don't make the new `Cookie` object
* You don't associate the session ID with the cookie
* You don't set the Cookie into the response
</blockquote>

`HttpSession session = httpServletRequest.getSession()` creates a new session if there is no `Cookie` in the request header, or get an existing session based on the session ID in the `Set-Cookie` header

### ... (page 234/pdf 259)

´HttpSessionEvent.getSession()´


### URL rewriting: somthing to fall back on (page 237/pdf 262)
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

## Can I use cookies for other things, or are they only for sessions? (page 250/pdf 275)
> By default, a cookie lives only as long as a session; once the client quits his browser, the cookie disappears. That's how the `JSESSIONID` cookie works. **But you can tell a cookie to stay alive even AFTER the browser shuts down**

example use case: 

> Kim wants to display the user's name each time he returns to the beer site => he sets the cookie the first time he receives the client's name, and if he gets the cookie back with a request, he knows not to ask for the name again. *And it doesn't matter if the user restarted his browser and hasn't been on the site for a week*

## Listener examples

Session counter in a *non-distributed system* as a typical use case of `HttpSessionListener`

page 261

## Using Cookies with Servlet API
Setting max age to `-1` makes the cookie disappear when the browser exits

pdf page 277
