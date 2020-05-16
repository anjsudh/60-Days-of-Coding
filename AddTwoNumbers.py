from List import ListNode, convertListToLinkedList

def addTwoNumbers(l1: ListNode, l2: ListNode, carry: int = 0):
    if(l1 is None and l2 is None and carry == 0):
        return None
    if(l1 is None):
        l1 = ListNode(0)
    if(l2 is None):
        l2 = ListNode(0)
    sum = l1.val + l2.val + carry
    carry = int(sum / 10)
    sum = sum % 10

    l3 = ListNode(sum)
    l3.next = addTwoNumbers(l1.next, l2.next, carry)
    return l3


# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
A = convertListToLinkedList([2,4,3])
B = convertListToLinkedList([5,6,4])
print("Input: \nA: ", A, "\nB: ", B, "\nSolution: ", addTwoNumbers(A, B))