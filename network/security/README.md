# Certificate
Based on the following references

* https://github.com/rxue/daybook/tree/master/books/ComputerNetworkingATopDownApproach/Chapter8SecurityInComputerNetworks
* https://zhuanlan.zhihu.com/p/43789231

The certificate contains *information of the specific entity*, e.g. the server in a web application, and the *public key*.

# [`keytool`](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/keytool.html) in Java
## *Keystore*
> A *keystore* is a storage facitlity for *cryptographic keys* and *certificates*

# 20190619
Reference: [Difference between SSO and LDAP](http://www.differencebetween.net/technology/protocols-formats/difference-between-sso-and-ldap/)
## Configure Port Forwarding in 192.168.1.1
`ifconfig` to get your internet connections device, and then find the *inet address* of this device. This *inet address* can be something like `192.168.1.102`. Then forword the port to this address in 192.168.1.1 with `admin` user

# 20190718
TODO: 
* going to learn more about SSO
* SSL certificate
* `keytool` - first go to check is the `keytool` already embedded in the *openJDK* as it is already in the Oracle JDK 
* man in the middle attack

# 20240811
Important thing about using two-factor authentication in github: when you want to add github account to an authenticator on a new phone, the two-factor authentication in github settings has to be disabled and then added again so that the QR code can be generated!

