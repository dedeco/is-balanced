# is-balanced
Check for balanced parentheses in Python

Write a function called "is_balanced" that returns true if the brackets in a given string are balanced. Balanced means that every parenthesis/bracket or brace that is opened must be closed and it must be closed in the right order (Always close the last symbol you opened). The function must handle parens (), square brackets [], and curly braces {}.

## When you are done with the function, try it out with all these test cases:

* "(a[0]+b[2c[6]]) {24 + 53}" -> True
* "f(e(d))" -> True
* "[()]{}([])" -> True
* "((b)" -> False
* "(c]" -> False
* "{(a[])" -> False
* "([)]" -> False
* ")(" -> False
* "" -> True


