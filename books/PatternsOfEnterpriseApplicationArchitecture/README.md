# Chapter 5: Concurrency
```
 concurrency.locking
 concurrency.multiphase
```

# Chapter 10: Data Source Architectural Patterns
## Data Mapper
### How It Works
> The problem with a *rich constructor* is that you have to aware of cyclic references. If you have two objects that reference each other, each time you try to load one it will try to load the other, which will in turn try to load the first one, and so on, until you run out of stack space.  Avoid this require special case code, often using *lazy load*. Writing this special case code is messy, so it's worth trying to do without it. You can do this by creating an **empty object**. Use *no-arg constructor* to create a blank object and insert that empty object immediately into the *identity map*. That way you have a cycle, the *identity map* will return an object to stop the recursive loading.
>
> Using an empty object like this means you may need some setters for values that are truly immutable when the object is loaded. A combination of a naming convention and perhaps some status-checking guards can fix this. You can also use reflection for data loading.
