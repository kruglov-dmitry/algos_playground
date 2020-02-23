#
#   https://leetcode.com/problems/valid-parentheses/
#


def valid_parentheses(some_string):

    brackets = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    my_stack = []
    for entry in some_string:
        if entry in brackets:
            my_stack.append(entry)
        elif entry in brackets.values():
            if not my_stack:
                return False
            last = my_stack.pop()
            if brackets[last] != entry:
                return False

    if my_stack:
        return False

    return True


assert valid_parentheses("()()()")

assert valid_parentheses("{()()}[]")

assert valid_parentheses("({[]})")

assert valid_parentheses(")(()()") is False

assert valid_parentheses("([)]") is False

assert valid_parentheses("[{((})]") is False
