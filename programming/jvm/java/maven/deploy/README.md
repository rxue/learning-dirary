# LAB: `deploy` to [Maven Central Repository](https://repo1.maven.org/)
NOTE that the *namespace* `io.github.rxue` is ready for use by default when loging to the `http://central.sonatype.com` with *Github* credential

## [Publishing by Using the Maven Plugin](https://central.sonatype.org/publish/publish-portal-maven/)
**Key takeaway**
* `settings.xml` needs to be configured in case of running `mvn deploy` locally, i.e. the following `server` element should be added

```
  <server>
      <id>central</id>
      <username>username</username>
      <password>password</password>
    </server>

```

the token, the username and password above, is generated in the `http://central.sonatype.com` **with Github credential** and, the variable `${server}` has to be replaced with `central`

There are the following errors after the first deployment with the minimum configuration

> * Javadocs must be provided but not found in entries

Reference: https://central.sonatype.org/publish/publish-maven/#javadoc-and-sources-attachments

> * Missing signature for file: dictionary-jpa-1.0-SNAPSHOT.jar
> * Missing signature for file: dictionary-jpa-1.0-SNAPSHOT.pom

Reference: https://central.sonatype.org/publish/publish-maven/#gpg-signed-components

NOTE! the `maven-gpg-plugin` relies on the gpg command installed, meaning `gpg` has to be installed locally so that this plugin can be used properly

`gpg --list-keys` returns nothing, which means there is no default secrete key => `gpg --generate-key` to generate a screte key with a name, e.g. `dictionary` and passphrase

Reference: 
* https://stackoverflow.com/questions/10848883/how-to-deal-with-gnupg-error-gpg-no-default-secret-key-no-secret-key-gpg-st
* https://maven.apache.org/plugins/maven-gpg-plugin/usage.html


> * Sources must be provided but not found in entries
> * version cannot be a SNAPSHOT
> * Developers information is missing
> * License information is missing
> * Project URL is not defined
> * Project description is missing
> * SCM URL is not defined
