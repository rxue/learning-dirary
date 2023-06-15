# Chapter 11: Deploying your web app: web app deploymet
## Key deployment task, what goes where
> Tag files (.tag) must be inside "WEB-INF/tags" or a sub-directory

page 608

> ...a WAR file, which stands for Web ARchive. And if that sounds suspiciously like a JAR, that's because a WAR is a JAR. A JAR with .war extension instead of .jar

page 611

## WAR files
> ...your Container may handle WAR deployment and naming differently.

page 612

## How servlet mapping REALLY works (20230615)
#### EXACT match: must begin with a slash

`<url-pattern>/beer/*</url-pattern>`

####  DIRECTORY match: must begin with a slash, always ends with an asterisk

`<url-pattern>*.do</url-pattern>`

#### EXTENSION match: MUST begin with an asterisk (never a slash), after the asterisk, it must have a dot extension (.do, .jsp etc.)

Reference above is on page 618

### Key rules about servlet mappings
> 1) The Container looks for matches in the order shown on the opposite pages. In other words, it looks *first* for an *exact match*. If it can't find an exact match, it looks for a *directory match*. If it can't find a directory match, it looks for an extension match.

> 2) If a request matches more than one directory `<url-pattern>`, the container choose the longest mapping. In other words, a request for `/foo/bar/myStuff.do` will map to the `<url-pattern>/foo/bar/*` even though it also matches `<url-pattern>/foo/*`. The most specific match always wins.

page 619

```
<servlet>
  <servlet-name>Two</servlet-name>
  <servlet-class>foo.DeployTestTwo</servlet-class>
</servlet> 
<servlet-mapping>
  <servlet-name>Two</servlet-name>
  <url-pattern>fooStuff/bar</url-pattern>
</servlet-mapping>
<servlet>
  <servlet-name>Four</servlet-name>
  <servlet-class>foo.DeployTestFour</servlet-class>
</servlet> 
<servlet-mapping>
  <servlet-name>Four</servlet-name>
  <url-pattern>fooStuff/bar/*</url-pattern>
</servlet-mapping>
```
`http://localhost:8080/test/fooStuff/bar/` maps to `Four`
`http://localhost:8080/test/fooStuff/bar` maps to `Two`

 
Reference above is on page 621

## Configuring servlet initialization in the DD
> If you have multiple servlets that you want preloaded, and you want to control the order in which they're initialized, the value of `<load-on-startup>` determines the order!

> Any number (load-on-startup) greater than zero mean "initialize the servlet at deployment or server startup time rather than waiting for the first request"

> ...what if there is more than one servlet with a load-on-startup of 4? The container loads the servlets with the same value in the order in which servlets are declared in the DD

Reference above is on page 628

