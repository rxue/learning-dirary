# Wildfly
## [Wildfly Documentation](https://docs.wildfly.org/) > [Latest JavaEE 7](https://docs.wildfly.org/13/) > Developer Guide > [Getting Started Developing Applications Guide](https://docs.wildfly.org/13/Getting_Started_Developing_Applications_Guide.html)
NOTE! In the Wildfly Documentation page https://docs.wildfly.org/ , the Wildfly version with the Jakarta EE version correspondence is listed in a table

Publicly maintained Wildly *Docker repository* : https://quay.io/repository/wildfly/wildfly

## Wildfly `27.0.1.Final`
### Version of Dependencies
* `version.com.h2database` : `2.1.210`

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
* https://github.com/rxue/dictionary/issues/25
* https://github.com/rxue/dictionary/issues/81

## Questions
### 20220707 Is it possible at all to make use of `@EJB` annotation to inject a *remote ejb*?

## How to configure JDBC our own datasource
https://docs.wildfly.org/28/Getting_Started_Guide.html#modifying-the-example-datasource
