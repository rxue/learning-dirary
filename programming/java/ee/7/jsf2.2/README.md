# [JSF 2.2 API Doc](https://docs.oracle.com/javaee/7/index.html)

 * [Facelets Tag Library](https://docs.oracle.com/javaee/7/javaserver-faces-2-2/vdldocs-facelets/toc.htm)

## JavaServer Faces Technology
### [The Lifecycle of a JavaServer Faces Application](https://docs.oracle.com/javaee/7/tutorial/jsf-intro006.htm)
![lifecycle](https://docs.oracle.com/javaee/7/tutorial/img/jeett_dt_016.png)

## Introduction to Facelets
### Using Facelets Templates
Tag           | Description
--------------|----------------------------------------------------------------------------------------------------------------------------
`ui:component`| Inserts a new UI component into the JSF component tree. **Any component or content fragment outside this tag is ignored.**
`ui:fragment` | Similar to `ui:component`, but does not disregard content outside this tag.

## Locale
### [`default-locale` and `supported-locale` Corresponds to the `Accept-Language` in the *Http Header*](https://docs.oracle.com/javaee/7/tutorial/jsf-configure005.htm)

> The `locale-config` element lists the default locale and the other supported locales. The `locale-config` element enables the system to find the correct locale based on the browser's language settings.

> The `supported-locale` and `default-locale` tags accept the lowercase, two-character codes defined by ISO 639-1 (http://www.loc.gov/standards/iso639-2/php/English_list.php)

### [Supported Locale by JRE since Java 8](https://www.oracle.com/java/technologies/javase/jdk8-jre8-suported-locales.html)

### Comment 
The precedence of the *locale* is `<f:view locale=..` in the jsf file > `<locale-config>`. So 

* If the locale is defined in `<f:view locale='...'`, the `<locale-config>` will be ignored.
* Otherwise, the JSF backend will look at the `Accept-Language` http request header and then check the `default-locale` and `supported-locale` in the `<locale-config>` element



