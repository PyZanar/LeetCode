from typing import Optional, List
from nodeTools import build_linked_list, linked_list_to_list
import pytest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
リストを2分割 → 後半を反転 → 交互にマージ の流れ
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # リストの中央を探す
        dummy = ListNode(-1)
        dummy.next = head
        fast, slow = dummy, dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next


        # 後半を反転する
        node = slow.next
        slow.next = None
        prev = None
        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next
            
        head_later = prev

       
        # 交互にマージする
        first, second = head, head_later
        while second:
            next1, next2 = first.next, second.next
            first.next = second
            second.next = next1
            first, second = next1, next2

        return head


@pytest.mark.parametrize(
    "input_list, expected_list",
    [
        ([1,2,3,4], [1,4,2,3]),
        ([1,2,3,4,5], [1,5,2,4,3]),
    ]
)
def test_case(input_list, expected_list):
    head = build_linked_list(input_list)
    actual_list = linked_list_to_list(Solution().reorderList(head))
    assert actual_list == expected_list



        