# I Fundementals
## Chapter 4: Composing Objects
### 4.5 Documenting synchronization policies
`java.text.SimpleDateFormat` isn't thread-safe, but Javadoc added this to documentation since 1.4. Before 1.4 Synchronization was not mentioned in the documentation of `SimpleDateFormat`
#### Interpreting vague of documentation
JDBC and servlet specifications' drawback: synchronization policy and thread safety are rarely mentioned 
