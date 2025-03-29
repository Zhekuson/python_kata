# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digits = []
        rolling_est = 0
        while l1.next and l2.next:
            cur_sum = (l1.val + l2.val + rolling_est)
            digits.append(
                cur_sum % 10
            )
            rolling_est = cur_sum // 10
            l1 = l1.next
            l2 = l2.next

        cur_sum = (l1.val + l2.val + rolling_est)
        digits.append(cur_sum % 10)
        rolling_est = cur_sum // 10
        l1 = l1.next
        l2 = l2.next

        if l1 is None and l2 is None:
            if rolling_est > 0:
                digits.append(rolling_est)
            big_l = None
        elif l1 is None:
            big_l = l2
        elif l2 is None:
            big_l = l1

        if big_l:
            while big_l.next:
                cur_sum = rolling_est + big_l.val
                digits.append(cur_sum % 10)
                rolling_est = cur_sum // 10
                big_l = big_l.next

            cur_sum = rolling_est + big_l.val
            digits.append(cur_sum % 10)
            rolling_est = cur_sum // 10
            if rolling_est > 0:
                digits.append(rolling_est)

        if len(digits) > 0:
            start_node = ListNode(val=digits[-1], next=None)
            i = len(digits) - 2
            while i >= 0:
                start_node = ListNode(digits[i], next=start_node)
                i -= 1
            return start_node
        else:
            return ListNode(val=0)

