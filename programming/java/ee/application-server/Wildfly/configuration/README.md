# Changes in Wildfly
## [Changes in Wildfly 25](https://www.wildfly.org/news/2021/09/27/WildFly-Changes/)
> Our standard configuration files no longer include *legacy security realms* These are the **`security-realm`** elements found under the `management` element in a standalone.xml or host.xml file, administered via the CLI at `/core-service=management/security-realm=*` addresses. The xml parsers no longer support these elements and the management API no longer provides resources at these addresses. Elytron subsystem resources are now used

# Cheat Sheet
## Question: How to be able to execute subsystem command such as `/subsystem=elytron/filesystem-realm=example-realm:add(path=/tmp/example-realm)`
### Answer: login to the Wildfly server, then execute `./bin/jboss-cli.sh`, then type `connect`, then one can start to type command
