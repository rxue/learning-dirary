# 20190622 
Don't know if this coding style is proper:
```
public class TestClass {
  public static final String CONST_1 = AnotherClass.getValueFromProperties();
}
```
Another question is about the command pattern

# 20190709
## *Hibernate*
### *Bootstrapping of Hibernate*
By means of `javax.persistence` API, the entry point when bootstrapping Hibernate is `EntityManagerFactory`, which can be retrieved by `Persistence.createEntityManagerFactory("persistence-unit name")`. The `persistence-unit` is defined in the `main/resources/META-INF/persistence.xml`.

#### Properties in `persistence.xml`, Which Takes Effect When `Persistence.createEntityManagerFactory("persistence-unit name")`
* `javax.persistence.schema-generation.database.action` - the action for generating the database schema
* `javax.persistence.sql-load-script-source` - the SQL scripts used to import data. In the Hibernate implementation, the default value is `import.sql` in the `resources` directory. So if this property is not defined in the `persistence-unit` but the `import.sql` are defined already in the `resources` directory, the `import.sql` will be executed  

reference: https://docs.oracle.com/javaee/7/tutorial/persistence-intro005.htm
