# Chapter 1: Java WebSocket Fundamentals
## WebSocket Endpoints
2 kinds of Java *WebSocket Endpoint*

* annotated endpoint
* programmatic endpoint
## Programming Endpoints
## Inside the Echo Samples
### WebSocket Messaging
 * Then endpoint obtains `RemoteEndPoint` through `Session` instance, which is the parameter of the callback methods in the programmatic `EndPoint` class or in the annotation base POJO
 * `RemoteEndPoint` has the ability to send message back to the other endpoint

# Chapter 6: WebSocket Path Mapping
## Terminology of URIs
`<websocket-protocol-scheme>://<authority>:<port-number>/<uri-path>?<query-string>`

* *port number* : number on which the web container hosting the *WebSocket* endpoint is listening for incoming opening *handshake requests*. For implementations of the Java *WebSocket API*, this is typically the same as the port number that server is listening to for HTTP requests of any kind, typically 8080. (or 80)

NOTE! logic based on: shandshake must be initialized through HTTP (protocol)

label: `1Z0-900`

