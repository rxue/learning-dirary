# [JSF 2.2 API Doc](https://docs.oracle.com/javaee/7/index.html)

 * [Facelets Tag Library](https://docs.oracle.com/javaee/7/javaserver-faces-2-2/vdldocs-facelets/toc.htm)

## JavaServer Faces Technology
### [The Lifecycle of a JavaServer Faces Application](https://docs.oracle.com/javaee/7/tutorial/jsf-intro006.htm)
![JSF Life-cycle](https://docs.oracle.com/javaee/7/tutorial/img/jeett_dt_016.png)
#### Practical Tip (20220526)
Based on Oracle's official tutorial, during *Invoke Application* phase,

> the JavaServer Faces implementation handles any application-level events, such as submitting a form or linking to another page

Moreover, this is the last phase right before rendering response, say validation and module value update etc. happen all before *Invoke Application*. In my *dictionary* project, the update submission failure in the [bug](https://github.com/rxue/dictionary/issues/19) issue is exactly due to this reason. In order to keep the initially submitted value on the server side, `@RequestScoped` was replaced with `@ViewScoped`.

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

## Upgrade in JSF
### ~~`javax.faces.bean.ViewScoped`~~ -> `javax.faces.view.ViewScoped`
> JSF 2.2 also introduces a new CDI scope: `javax.faces.view.ViewScoped`. Specifying this annotation on a bean binds it with the  [`javax.faces.bean.ViewScopes`](https://github.com/rxue/learning-diary/tree/master/programming/java/ee/jsf2.0#view-scope) is targeted for depreciation in a future version, so it is strongly recommended that you use the newly introduced scope.

Reference: Java EE 7 Essentials > Chapter 3: JavaServer Faces > Facelets

