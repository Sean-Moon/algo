#-*- coding: utf-8 -*-
#괄호 짝
text = input()

stack = []

for c in text:
    if len(stack) == 0: 
        stack.append(c)
    elif stack[-1] == "(" and c == ")":
        stack.pop()
    elif stack[-1] == "{" and c == "}":
        stack.pop()
    elif stack[-1] == "[" and c == "]":
        stack.pop()
    else:
        stack.append(c)
print(stack)

if len(stack) == 0:
    print(True)
else:
    print(False)