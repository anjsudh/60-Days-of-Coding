from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        head = self
        string_val = ''
        while head is not None:
            string_val += str(head.val) + " -> "
            head = head.next
        return string_val + 'NULL'

def convertListToLinkedList(l: List[int]):
    head = None
    end = None
    for i in l:
        if end is None:
           head = ListNode(i)
           end = head
        else:
           end.next =  ListNode(i)
           end = end.next
    return head

#Solution
def reverseList(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    
    reverse_head = head
    curr = head.next
    reverse_head.next = None
    while(curr is not None):
        temp  = curr.next
        curr.next = reverse_head
        reverse_head = curr
        curr = temp
    return reverse_head

input = convertListToLinkedList([1,2,3,4,5])
print("Input: ", input, " Solution: ", reverseList(input))