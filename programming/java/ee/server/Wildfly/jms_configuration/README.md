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
