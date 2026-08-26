class MinStack:

    def __init__(self):
        #init
        self.stack = []
        self.minval = float('inf')

        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.minval = val
        # we store diff here, so it will be able to recover
        else:
            diff = val - self.minval
            self.stack.append(diff)
            self.minval = min(self.minval, val)


    def pop(self) -> None:
        if not self.stack:
            return
        pop = self.stack.pop()
        if pop < 0: 
            #here pop = val - self.minval_old, if it's negative that means min was changed by this element, so basically:
            self.minval -= pop
            #self.minval = self.minvalnow - (val - self.mindvalold) = self.minvalnow - self.minvalnow + self.mindvalold

    def top(self) -> int:
        top_diff = self.stack[-1]
        if top_diff > 0:
            return top_diff + self.minval
        else:
            return self.minval


    def getMin(self) -> int:
        return self.minval

        
        
