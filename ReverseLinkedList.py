from List import ListNode, convertListToLinkedList

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