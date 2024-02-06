# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        if not head or not head.next or not head.next.next:
            return [-1, -1]        
        
        curr = head.next
        prev = head 
        position = 1
        criticalPoints = []
        
        while curr.next:
            if prev.val < curr.val > curr.next.val:
                criticalPoints.append(position)
            elif prev.val > curr.val < curr.next.val:
                criticalPoints.append(position)
            
            prev, curr = curr, curr.next
            position += 1
        
        if len(criticalPoints) < 2:
            return [-1, -1]
        
        
        min_distance = float('inf') 
        for i in range(len(criticalPoints) - 1):
            distance = abs(criticalPoints[i + 1] - criticalPoints[i])
            min_distance = min(min_distance, distance) 

        return [min_distance, abs(criticalPoints[-1] - criticalPoints[0])] 
            
        
# Test case
# Example usage: 
head = ListNode(5)
head.next = ListNode(3)
head.next.next = ListNode(1)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(1)
head.next.next.next.next.next.next = ListNode(2)

# Instantiate Solution class
solution_instance = Solution()

# Call the method on the instance
result = solution_instance.nodesBetweenCriticalPoints(head)
print(result)  