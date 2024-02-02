# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        curr = head
        binaryString = ''
        myInteger = 0
        exponent = 1

        while curr:
            binaryString += str(curr.val)
            curr = curr.next
         
        for i in range(len(binaryString) - 1, -1, -1): 
            if binaryString[i] == '1': 
                myInteger += exponent
            exponent *= 2
        
        return myInteger