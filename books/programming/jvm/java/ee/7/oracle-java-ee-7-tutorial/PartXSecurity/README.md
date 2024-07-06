# 48. Getting Started Securing Web Applications
## [Securing Web Applications](https://docs.oracle.com/javaee/7/tutorial/security-webtier002.htm)
### Specifiying Security Constraints
`security-constraint`

- `web-resource-collection`
  - `web-resource-name`
  - `url-pattern`
  - `http-method` or `http-method-omission`
 
- `auth-constraint`
  - `role-name`

- `user-data-constraint`
  - `transport-guarantee`: value can be `CONFIDENTIAL`, `INTEGRAL`, `NONE`

#### Specifying a Secure Connection
> The *user data constraint* is handy to use in conjunction with basic and form-based user authentication
#### 48.2.1.4 Specifying Security Constraints for Resources

```
<!-- SECURITY CONSTRAINT #1 -->
<security-constraint>
    <web-resource-collection>
        <web-resource-name>wholesale</web-resource-name>
        <url-pattern>/acme/wholesale/*</url-pattern>
    </web-resource-collection>
    <auth-constraint>
        <role-name>PARTNER</role-name>
    </auth-constraint>
    <user-data-constraint>
        <transport-guarantee>CONFIDENTIAL</transport-guarantee>
    </user-data-constraint>
</security-constraint>

<!-- SECURITY CONSTRAINT #2 -->
<security-constraint>
    <web-resource-collection>
        <web-resource-name>retail</web-resource-name>
        <url-pattern>/acme/retail/*</url-pattern>
    </web-resource-collection>
    <auth-constraint>
        <role-name>CLIENT</role-name>
    </auth-constraint>
    <user-data-constraint>
        <transport-guarantee>CONFIDENTIAL</transport-guarantee>
    </user-data-constraint>
</security-constraint>
```
# Chapter 50: Java EE Security: Advanced Topics
## Working with Digital Certificates
* Self-Signed server certificate => store in server *keystore file* - `keystore.jks`
* Self-Signed client certificate => store in server *truststore file* - `cacert.jks`

Tip: Think in the server's point of view

