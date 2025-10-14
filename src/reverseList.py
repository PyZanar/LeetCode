from typing import Optional, List
from nodeTools import build_linked_list, linked_list_to_list
import pytest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


@pytest.mark.parametrize(
    "input_list, expected_list",
    [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
    ]
)
def test_case(input_list, expected_list):
    head = build_linked_list(input_list)
    head_reversed = Solution().reverseList(head)
    actual_list = linked_list_to_list(head_reversed)
    assert actual_list == expected_list