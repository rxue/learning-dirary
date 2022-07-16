# Messaging Configuration
## The message producer/consumer needs `guest` role

> Have a look at the WildFly domain and messaging configuration for finding out the actual security requirements. At the time of writing, a user with guest role is required and that’s internally checked using the other security domain. 

Reference: http://docs.wildfly.org/26/Developer_Guide.html#Jakarta_XML_Web_Services_Advanced_User_Guide > 16.5.15 SOAP Over Jarkata Messaging

## 2 default queues exist in `standalone-full.xml`
There are 2 queues existing by default when starting the Wildfly server with full profile configuration, i.e. with `standalone-full.xml`. They are

```
  <jms-queue name="ExpiryQueue" entries="java:/jms/queue/ExpiryQueue"/>
  <jms-queue name="DLQ" entries="java:/jms/queue/DLQ"/>
```

This is visualized in the Admin console:

![2 default queues](https://user-images.githubusercontent.com/3033388/174456874-0c0d403c-68e0-45a5-b6f7-7a339b4e162f.png)

 * DLQ - *dead letter queue/channel*
 * ExpiryQueue - *Expiration Message Queue*

Reference: Enterprise Integration Patterns > 4. Message Channel > Dead Letter Channel


## Add a new Message Queue *destination* through the Admin console
![add message queue](https://user-images.githubusercontent.com/3033388/174456532-652f455a-cbe4-4914-8b5f-34c148636db1.png)

[Relevant Video Tutorial](https://www.youtube.com/watch?v=StqHcny4dGc)

## Consuming JMS Messages from Remote *Wildfly* Server

Reference: http://www.mastertheboss.com/jbossas/jboss-jms/connecting-to-an-external-wildfly-jms-server/#remotejms

### Configuration on the assumption that a queue already exists from the *Wildfly* Server

#### My real practice code: https://github.com/rxue/dictionary/issues/32

## Practical Trouble Shooting
### `AMQ214016: Failed to create netty connection java.net.UnknownHostException` when sending message to `http-remoting://localhost:8081` (the port number depends on the configuration)
#### Analysis
This error probably comes along with a `WARN` log message during the Wildfly startup

```
WARN  [org.apache.activemq.artemis.jms.server] (ServerService Thread Pool -- 84) AMQ122005: Invalid "host" value "0.0.0.0" detected for "http-connector" connector. Switching to "b2f3fd82791e". If this new address is incorrect please manually configure the connector to use the proper one.
```

Based on `Invalid "host" value "0.0.0.0" detected for "http-connector" connector`, the Wildfly server's listening socket is bound to "0.0.0.0". More explanation can be found in the note from [Redhat documentation: 8.3 Connectors](https://access.redhat.com/documentation/en-us/red_hat_jboss_enterprise_application_platform/7.1/html/configuring_messaging/acceptors_and_connectors#configuring_acceptors_and_connectors):

> If the bind address for the public interface is set to 0.0.0.0, you will see the following warning in the log when you start the JBoss EAP server: 

`AMQ121005: Invalid "host" value "0.0.0.0" detected for "connector" connector. Switching to <HOST_NAME>. If this new address is incorrect please manually configure the connector to use the proper one.`

> This is because a remote connector cannot connect to a server using the 0.0.0.0 address and the messaging-activemq subsystem tries to replace it with the server’s host name. The administrator should configure the remote connector to use a different interface address for the socket binding.

The quotation above is the direct reason for this error

#### Solution: set `jboss.bind.address` to a static IP address

