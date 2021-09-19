# https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        pointer = ans
        carry = sum = 0

        while (l1 or l2):
            sum = carry

            if l1:
                sum += l1.val
                l1 = l1.next

            if l2:
                sum += l2.val
                l2 = l2.next

            carry = sum // 10

            pointer.next = ListNode(sum % 10)
            pointer = pointer.next

        if carry == 1:
            pointer.next = ListNode(1)

        return ans.next

    def alternative_addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp_l1 = l1
        l1_depth = 0
        l1_sum = 0

        while temp_l1:
            l1_depth += 1
            temp_l1 = temp_l1.next

        temp_l2 = l2
        l2_depth = 0
        l2_sum = 0

        while temp_l2:
            l2_depth += 1
            temp_l2 = temp_l2.next

        temp_l1 = l1
        i = 1
        while temp_l1:
            l1_sum += (temp_l1.val) * (10 ** (i))
            temp_l1 = temp_l1.next
            i += 1

        temp_l2 = l2
        i = 1
        while temp_l2:
            l2_sum += (temp_l2.val) * (10 ** (i))
            temp_l2 = temp_l2.next
            i += 1

        print(l1_sum)
        print(l2_sum)

        suml = l1_sum + l2_sum

        print(suml)

        if suml == 0:
            return ListNode(0)

        strl = str(suml)[::-1]

        returned = ListNode(int(strl[0]))

        temp = returned
        for i in range(1, len(strl)):
            temp.next = ListNode(int(strl[i]))
            temp = temp.next

        if (int(strl[0]) == 0):
            return returned.next

        return returned


