# Wildfly
## [Wildfly Document](https://docs.wildfly.org/) > [Latest JavaEE 7](https://docs.wildfly.org/13/) > Developer Guide > [Getting Started Developing Applications Guide](https://docs.wildfly.org/13/Getting_Started_Developing_Applications_Guide.html)
## Practical Tips
### Maven dependency management
When using *Wildfly*, the dependencies can be managed with *bom*, i.e. there are usually the following dependencies in the `dependencyManagement` element:

    <dependencyManagement>
        <dependencies>
            <!-- JBoss distributes a complete set of Java EE 7 APIs including a Bill
                of Materials (BOM). A BOM specifies the versions of a "stack" (or a collection) 
                of artifacts. We use this here so that we always get the correct versions 
                of artifacts. Here we use the jboss-javaee-7.0-with-tools stack (you can
                read this as the JBoss stack of the Java EE 7 APIs, with some extras tools
                for your project, such as Arquillian for testing) and the jboss-javaee-7.0-with-hibernate
                stack you can read this as the JBoss stack of the Java EE 7 APIs, with extras
                from the Hibernate family of projects) -->
            <dependency>
                <groupId>org.wildfly.bom</groupId>
                <artifactId>jboss-javaee-7.0-with-tools</artifactId>
                <version>${version.jboss.bom}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
            <dependency>
                <groupId>org.wildfly.bom</groupId>
                <artifactId>jboss-javaee-7.0-with-hibernate</artifactId>
                <version>${version.jboss.bom}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>

The possible list of managed dependencies can be found from https://mvnrepository.com/artifact/org.jboss.spec/jboss-javaee-7.0/1.1.1.Final

### Debug configuration on Wildfly
#### Key References
* https://medium.com/@nguyenchitam1993/how-to-remote-debug-java-application-in-wildfly-on-a-docker-container-using-eclipse-b93f673430ff
* https://www.youtube.com/watch?v=2zUKDJNvhnI
#### Practice
https://github.com/rxue/dictionary/issues/25

### Message Queue Configuration
#### 2 default queues exist in `standalone-full.xml`
There are 2 queues existing by default when starting the Wildfly server with full profile configuration, i.e. with `standalone-full.xml`. They are

```
  <jms-queue name="ExpiryQueue" entries="java:/jms/queue/ExpiryQueue"/>
  <jms-queue name="DLQ" entries="java:/jms/queue/DLQ"/>
```

 * DLQ - *dead letter queue/channel*
 * ExpiryQueue - *Expiration Message Queue*

Reference: Enterprise Integration Patterns > 4. Message Channel > Dead Letter Channel


#### Add a new Message Queue through the Admin console
![add message queue](https://user-images.githubusercontent.com/3033388/174456532-652f455a-cbe4-4914-8b5f-34c148636db1.png)

 
