#Stack implementation uisng python list
class Stack:
    def __init__(self):
        self.s = []
    def push(self,val):
        self.s.append(val)
    def is_empty(self):
        return len(self.s) == 0
            
    def pop(self):
        if self.is_empty():
            return "stack is empty"
        return self.s.pop()
    
    def size(self):
        return len(self.s)
            
    
    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.s[-1]
    
    
st = Stack()
print(st.is_empty())
st.push(10)
st.push(20)
st.push(30)
print(st.is_empty())
print(st.pop())
print(st.size())
print(st.peek())


#Stack implementation uisng linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack_LL:
    def __init__(self):
        self.top = None 
    def push(self,val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node 
    def is_empty(self):
        return self.top is None 
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        del_val = self.top.data 
        self.top = self.top.next 
        return del_val 
            
    def size(self):
        count = 0
        curr = self.top

        while curr is not None:
            count += 1
            curr = curr.next

        return count
    def peek(self):
        if self.is_empty():
            return "Stack is empty"

        return self.top.data
ab = Stack_LL()
print(ab.is_empty())  
ab.push(10)
ab.push(20)
ab.push(30)
print(ab.peek())      
print(ab.size())      
print(ab.pop())       
print(ab.pop())       
print(ab.peek())      
print(ab.size())      