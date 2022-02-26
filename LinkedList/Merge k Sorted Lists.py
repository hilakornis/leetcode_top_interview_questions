
# from queue import PriorityQueue
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
        
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k = len(lists)        
        interval = 1        
        while(interval < k):
            for i in range(0, k - interval, interval*2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if k > 0 else None
            
    def merge2Lists(self, l1, l2):
        head = node = ListNode(0)        
        while l1 and l2:
            if(l1.val <= l2.val):
                node.next = l1                
                l1 = l1.next
            else: # l1.val > l2.val
                node.next = l2                
                l2 = l2.next
                # l2 = l1
                # l1 = node.next.next
            node = node.next
        if l1:
            node.next = l1
        elif l2:
            node.next = l2        
        return head.next
        