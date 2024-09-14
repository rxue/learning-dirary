# Part I - Core CDI
## Chapter 2. CDI Lite
### 2.1 Concepts
#### 2.1.5 Default bean discovery mode

<quote>
The default bean discovery mode for a bean archive is annotated, and such a bean archive is said to be an implicit bean archive as defined in Bean archives. If the bean discovery mode is annotated then:

* bean classes that don’t have bean defining annotation (as defined in Bean defining annotations) are not discovered, and
* producer methods (as defined in Producer methods) whose bean class does not have a bean defining annotation are not discovered, and
* producer fields (as defined in Producer fields) whose bean class does not have a bean defining annotation are not discovered, and
* disposer methods (as defined in Disposer methods) whose bean class does not have a bean defining annotation are not discovered, and
* observer methods (as defined in Declaring an observer method) whose bean class does not have a bean defining annotation are not discovered.
</quote>
