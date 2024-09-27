# 3. Puzzlers with Character
## Puzzle 20: What's My Class?
## Puzzle 21: What's My Class, Take 2
# 7. Library Puzzlers
## Puzzle 60: One-Liners
**Questions**
> A. Write a method that takes a List of elements and returns a new List containing the same elements in the same order with the second and subsequent occurrences of any duplicate elements removed. For example, if you pass in a list containing "spam" , "sausage" , "spam" , "spam" , "bacon" , "spam" , "tomato" , and "spam" , you’ll get back a new list containing "spam", "sausage", "bacon", and "tomato"

Hint: 
* ordered set - `LinkedHashSet`
* constructor on `ArrayList` - `ArrayList(Collection<? extends E> c)`

> B. Write a method that takes a string containing zero or more tokens separated by commas and returns an array of strings representing the tokens in the order they occur in the input string. Each comma may be followed by zero or more white space characters, which must be ignored by the method. For example, if you pass the string "fear, surprise, ruthless efficiency, an almost fanatical devotion to the Pope, nice red uniforms" , you’ll get back a five-element string array containing "fear" , "surprise" , "ruthless efficiency" , "an almost fanatical devotion to the Pope" , and "nice red uniforms"

Lessons learnt: parameter of `String.split()` is *regex* => one statement can resolve the problem

