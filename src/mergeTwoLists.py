from typing import Optional, List
import pytest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(val=-101)
        node1, node2 = list1, list2
        curr = dummy

        while node1 and node2:
            if node1.val <= node2.val:
                curr.next = node1
                node1 = node1.next
            else:
                curr.next = node2
                node2 = node2.next
            
            curr = curr.next

        if not node1:
            curr.next = node2
        if not node2:
            curr.next = node1

        return dummy.next

            

def build_linked_list(values: List[int]) -> Optional[ListNode]:
    """PythonのlistからListNodeの連結リストを作る"""
    dummy = ListNode()  # ダミーノード
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """ListNodeの連結リストをPythonのlistに変換"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result



@pytest.mark.parametrize(
    "list1, list2, expected_list",
    [
        ([1,2,4], [1,3,4], [1,1,2,3,4,4]),
        ([], [], []),
        ([], [0,1], [0,1]),
    ]
)
def test_case(list1, list2, expected_list):
    sol = Solution()
    l1, l2 = build_linked_list(list1), build_linked_list(list2)
    actual_list = linked_list_to_list(sol.mergeTwoLists(l1, l2))
    assert actual_list == expected_list