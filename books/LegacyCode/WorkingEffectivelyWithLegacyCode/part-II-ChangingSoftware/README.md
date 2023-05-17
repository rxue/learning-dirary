# Chapter 13. I Need to Make a Change, but I Don't Know What Tests to Write
> In legacy code, we might not have any tests for the changes we need to make, so there isn't any way to really verify that we're preserving behavior when we make changes. ... but in most legacy code, if we make finding and fixing all of the bugs our goal, we'll never finish

## Characterization Tests
> a *characterization test* is a test that characterizes the actual behavior of a piece of code.

> ...it's very important to have that knowledge of what hte system actually does someplace.

> Characterization tests record the actual behavior of a piece of code. If we find something unexpected when we write them, it pays to get some clarification. It could be a bug. That doesn't mean that we don't include the test in our test suite; instead, we should mark it as suspicious and find out what the effect would be of fixing it.

> ... The important thing to realize is that we aren't writing black-box tests.. We are allowed to look at the code we are characterizing.

### Self-Comment
*characterization test* is the *approval test* , which was discussed in this video tutorial: https://www.youtube.com/watch?v=p-oWHEfXEVs&list=PLizL--84rE7Q8yz_u8CHQ9b7Dg_EiN5Em

  
