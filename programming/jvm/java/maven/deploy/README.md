# LAB: `deploy` to [Maven Central Repository](https://repo1.maven.org/)
NOTE that the *namespace* `io.github.rxue` is ready for use by default when loging to the `http://central.sonatype.com` with *Github* credential

## [Publishing by Using the Maven Plugin](https://central.sonatype.org/publish/publish-portal-maven/)
**Key takeaway**
* `settings.xml` needs to be configured in case of running `mvn deploy` locally
* When generating the token through the `http://central.sonatype.com` with *Github* credential` the variable `${server}` has to be replaced with `central`

There are the following errors after the first deployment with the minimum configuration

> * Javadocs must be provided but not found in entries
Reference: https://central.sonatype.org/publish/publish-maven/#javadoc-and-sources-attachments

> * Missing signature for file: dictionary-jpa-1.0-SNAPSHOT.jar
> * Missing signature for file: dictionary-jpa-1.0-SNAPSHOT.pom
> * Sources must be provided but not found in entries
> * version cannot be a SNAPSHOT
> * Developers information is missing
> * License information is missing
> * Project URL is not defined
> * Project description is missing
> * SCM URL is not defined
