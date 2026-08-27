class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation = {"+": lambda l ,r: l + r, "-": lambda l ,r: r - l, "*":lambda l ,r: l*r, "/":lambda l, r: r/l}
        stack = []
        for t in tokens:
            if t not in operation:
                stack.append(int(t))
            else:
                r = stack.pop()
                l = stack.pop()
                stack.append(int(operation[t](r,l)))
        return stack.pop()
        