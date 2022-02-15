# JAX-RS 2.0
## Applications
> When an `Application` subclass is present in the archive, if both `Application.getClasses` and `Application.getSingletons` return an empty collection then all *root resource classes* and *providers* packaged in the web application MUST be included and the JAX-RS implementations is REQUIRED to discover them automatically by scanning a `.war` file as described above. If either `getClasses` or `getSingletons` returns a non-empty collection then only those classes or singletons returned MUST be included in the published *JAX-RS* application.

Reference: [JAX-RS 2.0 Spec](https://jcp.org/aboutJava/communityprocess/final/jsr339/index.html) > Chapter 2 Applications > 2.3.2 Servlet
