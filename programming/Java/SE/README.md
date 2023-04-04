# Core Java Classes met at work
## Utility
### `java.util.Collections`
* `public static <T> List<T> singletonList(T o)`
* `public static List ÈMPTY_LIST`


# Questions or Problems Met in Real Work
## In my task, a single *key-value* pair is needed. What would be the simplest solution?
### Answer: `AbstractionMap.SimpleEntry`
Reference: https://www.baeldung.com/java-map-new-entry

## How to generate a keystore for https to use
`keytool -genkeypair -alias httpscert -keyalg RSA -keysize 2048 -validity 1 -keystore httpscert.p12 -storetype PKCS12 -storepass testme -keypass testme -dname "CN=Xue Rui, OU=RXUnit, O=RXOrg, L=Espoo, S=Uusimaa, C=FI" -noprompt`
### idempetently
if [ -f httpscert.p12 ]; then rm httpscert.p12; fi && keytool -genkeypair -alias httpscert -keyalg RSA -keysize 2048 -validity 1 -keystore httpscert.p12 -storetype PKCS12 -storepass testme -keypass testme -dname "CN=Xue Rui, OU=RXUnit, O=RXOrg, L=Espoo, S=Uusimaa, C=FI" -noprompt
