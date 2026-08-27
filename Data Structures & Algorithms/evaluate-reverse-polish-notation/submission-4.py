class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation = {"+": lambda a, b : a+b, "-": lambda a, b: b-a, "*":lambda a, b: a*b, "/":lambda a, b: b/a}
        stack = []
        for t in tokens:
            if t not in operation:
                stack.append(int(t))
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(int(operation[t](a,b)))
        return stack.pop()
        