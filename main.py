

def is_balanced(s):
    """
        "is_balanced_2" that returns true if the brackets in a given string are balanced.

        Balanced means that every parenthesis/bracket or brace that is opened must be closed and it must be closed in
        the right order (Always close the last symbol you opened).

        The function must handle parens (), square brackets [], and curly braces {}.
    """
    d = {')': '(', ']': '[', '}': '{'}
    stack = []
    ss = list(s)
    for i in ss:
        if i in d.values():
            stack.append(i)
        elif i in d.keys():
            if (len(stack) > 0) and (d.get(i) == stack[len(stack) - 1]):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    s1 = "(a[0]+b[2c[6]]) {24 + 53}"
    s2 = "f(e(d))"
    s3 = "[()]{}([])"
    s4 = "((b)"
    s5 = "(c]"
    s6 = "{(a[])"
    s7 = "([)]"
    s8 = ")("
    s9 = ""

    assert is_balanced(s1) == True
    assert is_balanced(s2) == True
    assert is_balanced(s3) == True
    assert is_balanced(s4) == False
    assert is_balanced(s5) == False
    assert is_balanced(s6) == False
    assert is_balanced(s7) == False
    assert is_balanced(s8) == False
    assert is_balanced(s9) == True