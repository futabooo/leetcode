#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # 真ん中を見つけるために、fastとslowポインタを使う
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 奇数長の場合は中央のノードをスキップ
        if fast:
            slow = slow.next

        # 後半部分を反転
        def reverse(node: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        second = reverse(slow)

        # 前半部分と反転した後半部分を比較
        p1, p2 = head, second
        result = True
        while p2:
            if p1.val != p2.val:
                result = False
                break
            p1 = p1.next
            p2 = p2.next

        return result
        
# @lc code=end

