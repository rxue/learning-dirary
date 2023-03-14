# Chapter 13: The Power of Filters: wrappers and filters
## Container's rule for ordering filters:

<blockquote>
When more than one filters is mapped a given resource, the container uses the following rules:  

1. All filters with URL patterns are located first...Filters with matching URL patterns are placed in the chain in the order in which they are declared in the DD
2. Once all filters with matching URLs in the chain, the container does the thing...
</blockquote>
