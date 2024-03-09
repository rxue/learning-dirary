# How to use a different version of Java from the default version of the operating system (OS) with Maven (20220625)
## Problem: When compiling a [legacy Java EE project (in Java SE 8)](https://github.com/javaee/tutorial-examples), there is compilation error
### Current OS' configuration description
* Operating System: Ubuntu 20
* Output of `mvn --version` :

```
Apache Maven 3.6.3
Maven home: /usr/share/maven
Java version: 11.0.15, vendor: Private Build, runtime: /usr/lib/jvm/java-11-openjdk-amd64
Default locale: en_US, platform encoding: UTF-8
OS name: "linux", version: "5.13.0-51-generic", arch: "amd64", family: "unix"
```

## Change Request: In order to build the project successfully, Java 8 is needed

## Solution and Analysis
Reasoning: *Maven* builds project with the operating system's default Java (Java executable set in the `PATH` environment variable) in case *JAVA_HOME* environment is absent

=>

Solution: Set the `JAVA_HOME` environment variable to be that of legacy *Java 8* : `export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64`

As a result, the output of `mvn --version` would become:

```
Apache Maven 3.6.3
Maven home: /usr/share/maven
Java version: 1.8.0_312, vendor: Private Build, runtime: /usr/lib/jvm/java-8-openjdk-amd64/jre
Default locale: en_US, platform encoding: UTF-8
OS name: "linux", version: "5.13.0-51-generic", arch: "amd64", family: "unix"
```

# Tests with *JUnit 5* are not executed with `mvn` command
## Description
In my work project, after updating the unit tests code from JUnit 4 to *JUnit 5*, along with it there is also test dependency update, the tests are not executed with `mvn` command, e.g. `mvn clean package`
![o test executed](https://user-images.githubusercontent.com/3033388/172617932-28a62f0e-364c-4784-bec9-3940267cbfc8.png)
## Solution
reference: https://stackoverflow.com/questions/36970384/surefire-is-not-picking-up-junit-5-tests

NOTE! The correct answer is not the checked one but from the second one Mikhail Kholodkov. Based on the reference link above, that is an [surefire plugin issue](https://issues.apache.org/jira/browse/SUREFIRE-1330) in the old version and, it was resolved in *surefire 2.22.0* , which is not the default version.

Analysis helper Maven command: `mvn help:effective-pom`
This helps find the default version of *surefire plugin*

# Want to list all the available dependencies in the `bom` in `dependencyManagement`

## Solution
reference: https://stackoverflow.com/questions/52731746/how-to-list-all-dependencymanagment-in-maven

# How to build a single module in a multi-module project
## Solution
Use the `--projects` option

Exmaple: `mvn --projects portfolio-old-data clean package`

# `mvn clean install` encounters encoding error (20240309)

error message:

	[ERROR] Malformed \uxxxx encoding.
	java.lang.IllegalArgumentException: Malformed \uxxxx encoding.
	    at java.util.Properties.loadConvert (Properties.java:653)
	    at java.util.Properties.load0 (Properties.java:455)
	    at java.util.Properties.load (Properties.java:408)
	    at org.eclipse.aether.internal.impl.DefaultTrackingFileManager.read (DefaultTrackingFileManager.java:61)
	    at org.eclipse.aether.internal.impl.DefaultUpdateCheckManager.read (DefaultUpdateCheckManager.java:459)
	    at org.eclipse.aether.internal.impl.DefaultUpdateCheckManager.checkMetadata (DefaultUpdateCheckManager.java:259)
	    at org.eclipse.aether.internal.impl.DefaultMetadataResolver.resolve (DefaultMetadataResolver.java:302)
	    at org.eclipse.aether.internal.impl.DefaultMetadataResolver.resolveMetadata (DefaultMetadataResolver.java:179)
	    at org.apache.maven.repository.internal.DefaultVersionRangeResolver.getVersions (DefaultVersionRangeResolver.java:189)
	    at org.apache.maven.repository.internal.DefaultVersionRangeResolver.resolveVersionRange (DefaultVersionRangeResolver.java:142)
	    at org.eclipse.aether.internal.impl.collect.DependencyCollectorDelegate.cachedResolveRangeResult (DependencyCollectorDelegate.java:406)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.processDependency (DfDependencyCollector.java:202)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.processDependency (DfDependencyCollector.java:156)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.process (DfDependencyCollector.java:138)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.doRecurse (DfDependencyCollector.java:343)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.processDependency (DfDependencyCollector.java:277)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.processDependency (DfDependencyCollector.java:156)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.process (DfDependencyCollector.java:138)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.doRecurse (DfDependencyCollector.java:343)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.processDependency (DfDependencyCollector.java:277)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.processDependency (DfDependencyCollector.java:156)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.process (DfDependencyCollector.java:138)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.doRecurse (DfDependencyCollector.java:343)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.processDependency (DfDependencyCollector.java:277)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.processDependency (DfDependencyCollector.java:156)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.process (DfDependencyCollector.java:138)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.doRecurse (DfDependencyCollector.java:343)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.processDependency (DfDependencyCollector.java:277)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.processDependency (DfDependencyCollector.java:156)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.process (DfDependencyCollector.java:138)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.doRecurse (DfDependencyCollector.java:343)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.processDependency (DfDependencyCollector.java:277)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.processDependency (DfDependencyCollector.java:156)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.process (DfDependencyCollector.java:138)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.doRecurse (DfDependencyCollector.java:343)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.processDependency (DfDependencyCollector.java:277)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.processDependency (DfDependencyCollector.java:156)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.process (DfDependencyCollector.java:138)
	    at org.eclipse.aether.internal.impl.collect.df.DfDependencyCollector.doCollectDependencies (DfDependencyCollector.java:108)
	    at org.eclipse.aether.internal.impl.collect.DependencyCollectorDelegate.collectDependencies (DependencyCollectorDelegate.java:222)
	    at org.eclipse.aether.internal.impl.collect.DefaultDependencyCollector.collectDependencies (DefaultDependencyCollector.java:87)
	    at org.eclipse.aether.internal.impl.DefaultRepositorySystem.collectDependencies (DefaultRepositorySystem.java:305)
	    at org.apache.maven.project.DefaultProjectDependenciesResolver.resolve (DefaultProjectDependenciesResolver.java:151)
	    at org.apache.maven.lifecycle.internal.LifecycleDependencyResolver.getDependencies (LifecycleDependencyResolver.java:224)
	    at org.apache.maven.lifecycle.internal.LifecycleDependencyResolver.resolveProjectDependencies (LifecycleDependencyResolver.java:136)
	    at org.apache.maven.lifecycle.internal.MojoExecutor.ensureDependenciesAreResolved (MojoExecutor.java:368)
	    at org.apache.maven.lifecycle.internal.MojoExecutor.doExecute (MojoExecutor.java:313)
	    at org.apache.maven.lifecycle.internal.MojoExecutor.execute (MojoExecutor.java:212)
	    at org.apache.maven.lifecycle.internal.MojoExecutor.execute (MojoExecutor.java:174)
	    at org.apache.maven.lifecycle.internal.MojoExecutor.access$000 (MojoExecutor.java:75)
	    at org.apache.maven.lifecycle.internal.MojoExecutor$1.run (MojoExecutor.java:162)
	    at org.apache.maven.plugin.DefaultMojosExecutionStrategy.execute (DefaultMojosExecutionStrategy.java:39)
	    at org.apache.maven.lifecycle.internal.MojoExecutor.execute (MojoExecutor.java:159)
	    at org.apache.maven.lifecycle.internal.LifecycleModuleBuilder.buildProject (LifecycleModuleBuilder.java:105)
	    at org.apache.maven.lifecycle.internal.LifecycleModuleBuilder.buildProject (LifecycleModuleBuilder.java:73)
	    at org.apache.maven.lifecycle.internal.builder.singlethreaded.SingleThreadedBuilder.build (SingleThreadedBuilder.java:53)
	    at org.apache.maven.lifecycle.internal.LifecycleStarter.execute (LifecycleStarter.java:118)
	    at org.apache.maven.DefaultMaven.doExecute (DefaultMaven.java:261)
	    at org.apache.maven.DefaultMaven.doExecute (DefaultMaven.java:173)
	    at org.apache.maven.DefaultMaven.execute (DefaultMaven.java:101)
	    at org.apache.maven.cli.MavenCli.execute (MavenCli.java:906)
	    at org.apache.maven.cli.MavenCli.doMain (MavenCli.java:283)
	    at org.apache.maven.cli.MavenCli.main (MavenCli.java:206)
	    at jdk.internal.reflect.NativeMethodAccessorImpl.invoke0 (Native Method)
	    at jdk.internal.reflect.NativeMethodAccessorImpl.invoke (NativeMethodAccessorImpl.java:77)
	    at jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke (DelegatingMethodAccessorImpl.java:43)
	    at java.lang.reflect.Method.invoke (Method.java:568)
	    at org.codehaus.plexus.classworlds.launcher.Launcher.launchEnhanced (Launcher.java:283)
	    at org.codehaus.plexus.classworlds.launcher.Launcher.launch (Launcher.java:226)
	    at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode (Launcher.java:407)
	    at org.codehaus.plexus.classworlds.launcher.Launcher.main (Launcher.java:348)
	[ERROR] 

Solution: https://stackoverflow.com/questions/17043037/ant-malformed-uxxxx-encoding-in-propertyfile-task/71408534#71408534

More resource about the `resolver-status.properties` from ChatGPT: It is part of Maven dependency mechanism, used internally by Maven to keep track of the state of artifact resolution and caching
