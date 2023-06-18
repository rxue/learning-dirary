# 23. Introduction to Context and Dependency Injection for Java EE
## 23.8 Using Scopes
Scope       | Annotation            | Duration
------------|-----------------------|----------
Request     | `@RequestScoped`      | A user's with a web application in a single HTTP request
Session     | `@SessionScoped`      | ...
Application | `@ApplicationScoped`  | ...
Dependent   | `@Dependent`          | The default scope if none is specified; if means that an object exists to serve exactly one client (bean) and has the same lifecycle as that client (bean)
Conversation| `@ConversationScoped` | A user's interaction with a servlet, including JavaServer Faces applications. The conversation scope exists within developer-controlled boundaries that extend it across multiple requests for long-running conversations. All long-running conversations are scoped to a particular HTTP servlet session and may not cross session boundaries.

> Beans that use *session*, *application*, *conversation* scope must be `Serializable`, but beans that use *request scope* do not have to be `Serializable`.

## 23.9 Giving Beans EL Names
> The `@Named` qualifier allows you to access the bean by using the bean name, with the first letter in smaller case
