# HTTP
## [HTTP/1.1](https://www.ietf.org/rfc/rfc2616.txt)
### Idemptotent Methods
> Methods can also have the property of "idempotent" in that (aside from error or expiration issues) the side-effects of `N > 0` identical requests is the same as for a single request. The methods `GET`, `HEAD`, `PUT` and `DELETE` share this property. Also, the methods `OPTIONS` and `TRACES SHOULD NOT` have side effects, and so are inherently idempotent.

## [Response Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
* 300 - 399 Redirection messages

## Response
### Header
 * `Set-Cookie`


# [URI](https://www.ietf.org/rfc/rfc3986.html)
## [Path](https://www.ietf.org/rfc/rfc3986.html#section-3.3)
> Aside from dot-segments in hierarchical paths, a path segment is considered opaque by the generic syntax.  URI producing applications often use the reserved characters allowed in a segment to delimit scheme-specific or dereference-handler-specific subcomponents.  For example, the semicolon (";") and equals ("=") reserved characters are often used to delimit parameters and parameter values applicable to that segment.  The comma (",") reserved character is often used for similar purposes.  For example, one URI producer might use a segment such as "name;v=1.1" to indicate a reference to version 1.1 of "name", whereas another might use a segment such as "name,1.1" to indicate the same.  Parameter types may be defined by scheme-specific semantics, but in most cases the syntax of a parameter is specific to the implementation of the URI's dereferencing algorithm.

A typical use case of semicolon and equals to delimite parameters and parameter values is in the [Servlet 3.1 spec](#), 7.1. Session Tracking Mechanism > 7.1.3 URL Rewriting, where there is an example URL `http://www.myserver.com/catalog/index.html;jsessionid=1234`

