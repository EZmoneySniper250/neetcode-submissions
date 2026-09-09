class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack, total = [], 0
        for o in operations:
            if o == "+":
                newscore = stack[-1]+ stack[-2]
                total+=(newscore)
                stack.append(newscore)
            elif o == "C":
                r = stack.pop()
                total-=r
            elif o =="D":
                prev = stack[-1]
                newscore = prev*2
                stack.append(newscore)
                total+= newscore
            else:
                stack.append(int(o))
                total+= int(o)
        return total



        