# pseudo-type: `var`
* must be unambiguous
* not permitted for *fields*

# Tutorial 119: Module Compilation

`--module-source-path`

Main tips:
  `jdeps` for dependency analysis

Example:
 * `jdeps -m java.sql`
 * `jdeps -s -m java.sql`
# Tutorial 120: Module execution

*Non-modular* code has no `module-info.java`

# Tutorial 123: `exports` & `requires` directives 



# Replacement of old static factory with the new `of` method

The `of` method introduced since Java 11 usually returns unmodifiable objects, i.e. *immutable*

Old Method 	|New Method in SE 11
----------------|---------------------
`Arrays.asList`	|`List.of`
`Paths.get`	|`Path.of`

Note that `Arrays.asList` is different from `List.of`!
