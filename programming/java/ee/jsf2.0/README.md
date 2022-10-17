# Managed Bean
## Bean Scopes
### View Scope
> *View Scope* was added in *JSF 2.0*. A bean in view scope persists while the same JSF page is redisplayed. (The JSF specification uses the term view for a JSF page.) As soon as the user nagivates to a different page, the bean goes out of scope.

> If you have a page that keeps getting the redisplayed, then you can put the beans that hold the data for the page into view scope, thereby  reducing the size of the session scope. This is particularly useful for Ajax application.

Reference: The Core JavaServer Faces, 3rd Edition > Chapter 2 Managed Bean > Bean Scopes > View Scope
