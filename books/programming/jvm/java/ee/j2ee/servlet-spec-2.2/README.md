# [Java Servlet Specification 2.2](https://fazenda.pbh.gov.br/siatu/documentos/siatu/download/servlet2_2-spec.pdf)
## Chapter 10. Mapping Requests to Servlets
### 10.2 Specification of Mappings
> In the web application deployment descriptor, the following syntax is used to define mappings:
> * A string beginning with a "/" character and ending with a "/*" postfix is used as a *path mapping*.
> * A string beginning with a "*." prefix is used as an *extension mapping*.
> * All other strings are used as *exact matches* only
> * A string containing only the ’/’ character indicates that servlet specified by the mapping becomes the *"default" servlet* of the application.
