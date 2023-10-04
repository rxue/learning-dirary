# 48. Getting Started Securing Web Applications
## Securing Web Applications
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

# Chapter 50: Java EE Security: Advanced Topics
## Working with Digital Certificates
* Self-Signed server certificate => store in server *keystore file* - `keystore.jks`
* Self-Signed client certificate => store in server *truststore file* - `cacert.jks`

Tip: Think in the server's point of view

