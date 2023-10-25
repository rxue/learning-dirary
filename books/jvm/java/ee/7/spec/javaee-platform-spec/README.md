# EE.5: Resources, Naming, and Injection
## 5.2 JNDI Naming Context
### Annotations and Injection
> The specifications for different containers indicates which classes are considered *container-managed* classes; not all classes of a given type are necessarily considered container-managed

翻译成人话: in practice, what classes are *container-managed* are container-specific and, 

 * *resource injection* works ONLY on container-managed classes
 * *resource injection* doesn't work on classes other than container-managed

