'''queue operations --> follows FIFO
enqueue-rear
dequeue-front

applications
1) CPU scheduling
2) Disk scheduling
3) Data buffering'''

#queue implementation using python list
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,val):
        self.queue.append(val)

    def is_empty(self):    
        return len(self.queue) == 0
    
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)
    def front(self):
        if self.is_empty:
            return "Queue is empty"
        return self.queue[0]
    def display(self):
        if self.is_empty():
            return "Queue is empty"
        for ele in self.queue:
            print(ele,end = " ")
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
print( q.queue)
print( q.front())
print( q.dequeue())
print( q.queue)
print(q.front())
print( q.is_empty())
