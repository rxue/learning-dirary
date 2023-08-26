# Routing
## Display Routing Table (in Linux)
Reference: https://www.rootusers.com/how-to-display-routing-table-in-linux/

`netstat -rn`

# [The WebSocket Protocol](https://www.rfc-editor.org/rfc/rfc6455#section-1.2)
## Introduction
### 1.1 Background
Working PORT: 80 and 443
### Relationship to TCP and HTTP
> The WebSocket Protocol is an independent TCP-based protocol. Its only relationship to HTTP is that its handshake is interpreted by HTTP servers as an Upgrade request.

## Practical Tips
When a web app is using *WebSocket*, in the front-end whenever the page is reloaded, an *HTTP* request is always sent to the server, in the same time the existing *WebSocket* connection is closed and a new *WebSocket* connection is established.

=>

Based on the core rationale of WebSocket protocol, it is only fit for some special scenario. 

I once designed a dictionary web app that the search page contains search history shared among all users. WebSocket is not practical in this scenario since the search is the core function and each search traditionally corresponds to an HTTP request, which corresponds to a handshake of websocket connection.

Reference: https://github.com/rxue/dictionary/issues/105
