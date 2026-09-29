#876 
class ListNode:
    def __init__(self, val = 0 , next = None):
        self.val = val 
        self.next = next
        
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        count = 0 
        temp = head 
        while temp:
            count += 1 
            temp = temp.next     
        mid_ind = count // 2 
        temp = head
        for i in range(mid_ind):
            temp = temp.next
        return temp


#solution 2
class Solution:
    def middleNode1(self, head: ListNode | None) -> ListNode | None:
        slow = head 
        fast = head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        return slow 

#141 

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            if slow == fast:
                return True 
        return False 
    
#21 merge two sorted lists



#206
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
        
#19        
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        if count == n:
            return head.next
        temp = head
        for i in range(count - n - 1):
            temp = temp.next
        temp.next = temp.next.next

        return head
        









