# HTTP
## Protocol parameters
### [Uniform Resource Identifiers](https://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.2)
#### General syntax
> The HTTP protocol does not place any a priori limit on the length of a URI. Servers MUST be able to handle the URI of any resource they serve, and SHOULD be able to handle URIs of unbounded length if they provide GET-based forms that could generate such URIs. A server SHOULD return 414 (Request-URI Too Long) status if a URI is longer than the server can handle (see section 10.4.15).

```
      Note: Servers ought to be cautious about depending on URI lengths
      above 255 bytes, because some older client or proxy
      implementations might not properly support these lengths.
```

## Request
#### Idemptotent Methods
> Methods can also have the property of "idempotent" in that (aside from error or expiration issues) the side-effects of `N > 0` identical requests is the same as for a single request. The methods `GET`, `HEAD`, `PUT` and `DELETE` share this property. Also, the methods `OPTIONS` and `TRACES SHOULD NOT` have side effects, and so are inherently idempotent.

#### Request Header
* `Cookie`

## Response
#### [Response Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
 code | description
------|-------------------
204   | No content
500   | Internal server error


* 300 - 399 Redirection messages

#### Response Header
##### `Set-Cookie`
###### Abbtributes
Name      | Value
----------|----------
`Max-Age` | <number>

## Http *Method* Definitions
### [Http/1.0](https://www.rfc-editor.org/rfc/rfc1945#section-8) (20230909)
* `GET`
* `POST`
* `HEAD` - identical to `GET` except that the server must not return *entity-body* in the response 

### [HTTP/1.1](https://www.ietf.org/rfc/rfc2616.txt) 
* `OPTIONS`
* `PUT`
* `DELETE`
* `TRACE`
* `CONNECT`
### Additional *Methods*
* `PATCH`
* `LINK`
* `UNLINK`

## [Cookie](https://www.rfc-editor.org/rfc/rfc6265#section-8.4)
> If a cookie has neither the `Max-Age` nor the Expires attribute, the user agent will retain the cookie until "the current session is over" (as defined by the user agent) 


# [URI](https://www.ietf.org/rfc/rfc3986.html)
## [Path](https://www.ietf.org/rfc/rfc3986.html#section-3.3)
> Aside from dot-segments in hierarchical paths, a path segment is considered opaque by the generic syntax.  URI producing applications often use the reserved characters allowed in a segment to delimit scheme-specific or dereference-handler-specific subcomponents.  For example, the semicolon (";") and equals ("=") reserved characters are often used to delimit parameters and parameter values applicable to that segment.  The comma (",") reserved character is often used for similar purposes.  For example, one URI producer might use a segment such as "name;v=1.1" to indicate a reference to version 1.1 of "name", whereas another might use a segment such as "name,1.1" to indicate the same.  Parameter types may be defined by scheme-specific semantics, but in most cases the syntax of a parameter is specific to the implementation of the URI's dereferencing algorithm.

A typical use case of semicolon and equals to delimite parameters and parameter values is in the [Servlet 3.1 spec](#), 7.1. Session Tracking Mechanism > 7.1.3 URL Rewriting, where there is an example URL `http://www.myserver.com/catalog/index.html;jsessionid=1234`

