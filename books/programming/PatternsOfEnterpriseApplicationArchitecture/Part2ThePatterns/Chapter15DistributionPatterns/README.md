# Chapter 15 Distribution Patterns
## Data Transfer Object
* Original intention of using *data transfer object* : one DTO holds all data so that the it can be sent to remote target in one go rather tha many times remote calls
* key issues to consider: convertion between DTO and domain objects

### How It Works
**Important takeaways**

> You can't usually transfer objects from a *Domain Model*. This is because the objects are usually connected in a complex web that’s difficult, if not impossible, to serialize. Also you usually don't want the domain object classes on the client, which is tantamount to copying the whole Domain Model there. Instead you have to transfer a simplified form of the data from the domain objects.

> The fields in a *data transfer object* are fairly simple, being *primitives*, simple classes like like strings and dates, or other *data transfer objects*

**My own practice (20240818)**
In the [dictionary](#) project, the JPA entity, i.e. the *domain object*, `LexicalItem.language` is of type `Locale` and, `LexicalItem` was originally designed to be sent to the client directly as the REST API response. As a result, the whole `LexicalItem.language` as an `Locale` is sent to the REST API client including lots of data due to the featue of `Locale` from Java SE. But the client is only interested in the language tag => `LexicalItemDTO.languageTag` with basic `String` type comes into play.
 
