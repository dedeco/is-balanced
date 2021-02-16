def is_balanced(s):
    """
        "is_balanced" that returns true if the brackets in a given string are balanced.

        INCORRET, please see is_balanced_2
    """
    d = {"(": ")", "[": "]", "{": "}"}
    ss = list(s)
    print(ss)
    stop = True
    y = 0
    while stop:
        for i, item in enumerate(ss):
            if item in d.keys():
                for j in range(i, len(ss)):
                    try:
                        # print(ss, item, d.get(item), ss[j], j, i)
                        if ss[j] == d.get(item):
                            # print(ss, "before")
                            del ss[i]
                            del ss[j - 1]
                            # print(ss, "after")
                            break
                        # idx = ''.join(ss).rindex(d.get(item))
                        # del ss[idx]
                    except IndexError:
                        pass
                # print(ss)
            # print(ss)
        y += 1
        if y > 1000:
            break
    for k, v in d.items():
        if k in ss or v in ss:
            return False
    # print(ss)
    return True


def is_balanced_2(s):
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

    assert is_balanced_2(s1) == True
    assert is_balanced_2(s2) == True
    assert is_balanced_2(s3) == True
    assert is_balanced_2(s4) == False
    assert is_balanced_2(s5) == False
    assert is_balanced_2(s6) == False
    assert is_balanced_2(s7) == False
    assert is_balanced_2(s8) == False
    assert is_balanced_2(s9) == True