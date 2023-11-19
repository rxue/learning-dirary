# [EJB Invocation from Remote Server Instance](https://docs.jboss.org/author/display/WFLY10/EJB%20invocations%20from%20a%20remote%20server%20instance.html)
## References
* https://docs.jboss.org/author/display/WFLY10/EJB%20invocations%20from%20a%20remote%20server%20instance.html
* https://docs.wildfly.org/26/Client_Guide.html#jboss-ejb-client
* https://groups.google.com/g/wildfly/c/oZkTwnHfxYs?pli=1

Important **NOTE** in https://docs.jboss.org/author/display/WFLY10/EJB%20invocations%20from%20a%20remote%20server%20instance.html :

> If your application is deployed as a top level .war deployment, then the jboss-ejb-client.xml is expected to be placed in .war/WEB-INF/ folder (i.e. the same location where you place any web.xml file).

In addition to this, in the configuration of the *remoting* subsystem in the `standalone-full.xml` of the *client server* :

```
<subsystem xmlns="urn:jboss:domain:remoting:1.1">
....
  <outbound-connections>
    <remote-outbound-connection name="remote-ejb-connection" outbound-socket-binding-ref="remote-ejb" protocol="http-remoting" security-realm="ejb-security-realm" username="ejb">
      <properties>
        <property name="SASL_POLICY_NOANONYMOUS" value="false"/>
        <property name="SSL_ENABLED" value="false"/>
      </properties>
    </remote-outbound-connection>
  </outbound-connections>
</subsystem>
```

the attributes `protocol`, `security-realm` and `username` in the `remote-outbound-connection` element are *deprecated* and replaced with the element `authentication-context` under `subsystem elytron` > `authentication-client`. The `authentication-client` looks something like:
```
  <authentication-client>
    <authentication-configuration name="auth-conf" authentication-name="jmsuser" host="172.22.0.2" port="8081" forwarding-mode="authentication">
      <credential-reference clear-text="jmspassword" />
    </authentication-configuration>
    <authentication-context name="remote_ejb">
      <match-rule match-host="172.22.0.2" match-port="8081" authentication-configuration="auth-conf"/>
    </authentication-context>
  </authentication-client>
```
Note that the `authentication-name` attribute of `authentication-configuration` element is the *username* and `clear-text` attribute of `credential-reference` is the *password*

