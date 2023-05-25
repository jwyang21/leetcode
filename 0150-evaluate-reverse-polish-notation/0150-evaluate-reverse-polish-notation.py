from math import trunc
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in {'+', '-', '*', '/'}:#if t is not operator
                stack.append(int(t))#append t to the list of operands (stack)
            else:
                b, a = stack.pop(), stack.pop()
                if t == '+': stack.append(a+b)
                elif t=='-': stack.append(a-b)
                elif t=='*': stack.append(a*b)
                else: stack.append(trunc(a/b))
        return stack[0]#https://deeprun.tistory.com/128