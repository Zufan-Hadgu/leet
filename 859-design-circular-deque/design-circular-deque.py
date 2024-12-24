class MyCircularDeque(object):

    def __init__(self, k):
        self.queue = deque()
        self.k = k
         
    def insertFront(self, value):
        if not self.isFull():
            self.queue.appendleft(value)
            return True
        return False
        


        
        

    def insertLast(self, value):
        if not self.isFull():
            self.queue.append(value)
            return True
        return False
        
        

    def deleteFront(self):
        if not self.isEmpty():
            self.queue.popleft()
            return True
        return False
        

    def deleteLast(self):
        if not self.isEmpty():
            self.queue.pop()
            return True
        return False
        

    def getFront(self):
        if not self.isEmpty():
            return self.queue[0]
            
        return -1
        

    def getRear(self):
        if not self.isEmpty():
            return self.queue[-1]
            
        return -1
        

    def isEmpty(self):
        if len(self.queue) == 0:
            return True 
        return False 
        

    def isFull(self):
        if len(self.queue) == self.k:
            return True
        return False

        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()