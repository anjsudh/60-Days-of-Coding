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