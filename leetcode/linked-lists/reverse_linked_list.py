# https://leetcode.com/problems/reverse_linked_list


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = None
        while (head is not None):
            next = head.next
            head.next = node
            node = head
            head = next
        return node

    def alternative_reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        reverse_arr = []

        while temp:
            reverse_arr.append(temp.val)
            temp = temp.next

        if len(reverse_arr) == 0:
            return head

        reverse_head = ListNode(reverse_arr[-1])

        temp_r = reverse_head
        for i in range(1, len(reverse_arr)):
            print(i)
            temp_r.next = ListNode(reverse_arr[len(reverse_arr) - i - 1])
            temp_r = temp_r.next

        return reverse_head
