from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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