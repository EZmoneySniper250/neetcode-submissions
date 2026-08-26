class MinStack:
    # sol2: onestack for all --> the key part is the thing append in the stack is the diffrence between the val and the min to see if this val creates the min val
    def __init__(self):
        self.stack = []
        self.minval = float('inf')
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0) #append zero diff since val = min at this case
            self.minval = val
        else:
            self.stack.append(val - self.minval)
            if val < self.minval:
                self.minval = val

    def pop(self) -> None:
        # since in the list it stores the difference between val and the minval, so we need to revert the value
        pop = self.stack.pop()
        if pop < 0: # this indicates that the minval was modified by the val at that position so we need to revert minval
            self.minval = self.minval - pop # oldmin = currentmin - diff between curr min and: oldmin = currmin - (currmin - oldmin)
        return
        

    def top(self) -> int:
        top = self.stack[-1]
        if top < 0:
            return self.minval
        else:
            return self.minval + top #top = val - self.minval
        

    def getMin(self) -> int:
        return self.minval
        
