# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow, fast = head, head.next
        while fast and fast.next:
            if fast == slow:
                return True
            else:
                fast = fast.next.next
                slow = slow.next
        return False