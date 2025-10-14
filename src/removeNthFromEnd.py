from typing import Optional
from nodeTools import build_linked_list, linked_list_to_list
import pytest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(-1)
        dummy.next = head

        first, second = dummy, dummy
        for _ in range(n):
            first = first.next

        while first.next:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next



@pytest.mark.parametrize(
    "input_list, n, expected_list",
    [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        ([1, 2, 3], 3, [2, 3]),
    ]
)
def test_case(input_list, n, expected_list):
    head = Solution().removeNthFromEnd(build_linked_list(input_list), n)
    actual_list = linked_list_to_list(head)
    assert actual_list == expected_list
