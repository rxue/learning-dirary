# [Configuring Plug-ins](https://maven.apache.org/guides/mini/guide-configuring-plugins.html)

# [Available Plugins](https://maven.apache.org/plugins/index.html)
Plugins listed in the link in the title are available directly through command line. 

Take the `failsafe` plugin as an example, the `failsafe` plugin can be configured and is usually configured in the following way, https://github.com/rxue/java-from-scratch-to-advanced/commit/674d29b9b2a10e1efedd08f7a7cf0e31f98c5640 , so that the integration tests suffixed with `IT` will be executed with command `mvn clean verify`. However, integration tests can also be executed with command `mvn failsafe:integration-test verify` without any configuration in the `pom.xml`
