class Solution:
    def isValid(self, s: str) -> bool:
        back_trace = {")":"(", "}":"{",']':'[' }
        #stack: last in first out using pop
        stack = []
        for l in s:
            if l in back_trace:
                if stack and stack[-1] == back_trace[l]:
                    stack.pop()
                else: return False #two cases 1. starting with ), definitely not closed as wish 2. [({) ) cannot remove {, false}
            else: stack.append(l)
        return True if not stack else False
        


        