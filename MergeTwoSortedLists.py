# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        foo = ListNode(0)
        curr = foo

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next  # Move list1 pointer
            else: 
                curr.next = list2
                list2 = list2.next  # Move list2 pointer
            
            curr = curr.next  # Move pointer

        if list1:
            curr.next = list1
        else:
            curr.next = list2

        return foo.next