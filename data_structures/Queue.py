 ## Queue ✔

class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None]*capacity
        self.capacity = capacity
    
    def isFull(self):
        return self.size == self.capacity
    
    def isEmpty(self):
        return self.size == 0
    
    def Enque(self, item):
        if self.isFull():
             print("Full...")
             return
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("%s enqued to the queue... " % str(item))

    def Deque(self):
        if self.isEmpty():
            print("Empty...")
            return
        print("%s dequed from the queue... " % str(self.Q[self.front]))
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size - 1

    def que_front(self):
        if self.isEmpty():
            print("Queue is empty...")
        print("Front item is " + str(self.Q[self.front]))


    def que_rear(self):
        if self.isEmpty():
            print("Queue is empty...")
        print("Rear item is " + str(self.Q[self.rear]))




q = Queue(30)
q.Enque(10)
q.Enque(20)
q.Deque()
q.que_front()
q.que_rear()
print(q.isEmpty())
print(q.isFull())
q.Enque(30) 
q.que_rear()
print(q.Q)