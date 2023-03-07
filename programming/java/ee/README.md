# Bean Validation (1.1)
## Property to turn on/off validations
`javax.persistence.validation.mode` with values `auto` (by default), 'callback', 'none'

# Practical Questions
## How to keep a `@SessionScoped` CDI bean instance alive for a long time even when the browser is closed
### Analysis
By default, the lifecycle of CDI beans with `@SessionScoped` will end when the browser is shutdown due to the fact that the defaul max age of the session cookie, named with `JSESSIONID` is `-1`.

reference: https://docs.oracle.com/javaee/7/api/javax/servlet/http/Cookie.html#getMaxAge--

### Solution
Application wide, the lifecycle of *session* can be configured through `web.xml` > `session-config` > `cookie-config` > `max-age`. The value of `max-age` should be configured to a positive value whose unit is second.

