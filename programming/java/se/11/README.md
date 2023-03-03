# Replacement of old static factory with the new `of` method

The `of` method introduced since Java 11 usually returns unmodifiable objects, i.e. *immutable*

Old Method 	|New Method in SE 11
----------------|---------------------
`Arrays.asList`	|`List.of`
`Paths.get`	|`Path.of`

Note that `Arrays.asList` is different from `List.of`!
