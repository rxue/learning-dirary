# 45. Java Message Service Concept
## Basic JMS API Concepts
### JMS API Architecture
A JMS application is composed of the following parts:
 * JMS provider
 * JMS clients
 * Messages
 * Adinistered objects
## 45.3. The JMS API Programming Model
### `JMSContext` Objects
You use `JMSContext` to create the following objects:

 * Message producers
 * Message consumers
 * Messages
 * Queue browsers
 * Temporary queues and topics

## 45.4. Using Advanced JMS Features
### Creating Temporary Destinations
> Normally, you create JMS destinations (queues and topics) administratively rather than programmatically. Your JMS provider includes a tool to create and remove destinations, and it is common for destinations to be long-lasting.

> The JMS API also enables you to create destinations (`TemporaryQueue` and `TemporaryTopic` objects) that <ins>last only for the duration of the connection</ins> in which they are created. 
