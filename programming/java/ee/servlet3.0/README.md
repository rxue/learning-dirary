
> If you encounter a naming conflict, you can use the name attribute of the `@WebServlet` annotation to specify a unique mapping name for the servlet

> If you use both the `web,xml` and the `@WebServlet` annotation to map the same servlet name to one or more URLs, the mapping in the web.xml file overrides the same servlet name to one or more UTLs, the mapping in the `web.xml` file overrides the mapping in the annotation.

reference: Murach's Java Servlets and JSP Programming > Chapter 5 How to Develop Servlets > How to Create and Map a Servlet > How to map a servlet with an annotation

# `javax.servlet`
## `SingleThreadModel` is deprecated nowadays
refernce: https://github.com/jakartaee/servlet/issues/269

Disappearance of it in *jakartaee 10* is the proof
