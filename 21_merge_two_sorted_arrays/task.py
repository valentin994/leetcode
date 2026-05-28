from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(node: ListNode):
    while node is not None:
        print(f"{node.val}", end="")
        node = node.next
    print("")


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        start = ListNode(-1)
        current_node = start
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                current_node.next = list1
                list1 = list1.next
            else:
                current_node.next = list2
                list2 = list2.next
            current_node = current_node.next

        if list1 is not None:
            current_node.next = list1
        else:
            current_node.next = list2

        return start.next


head1 = ListNode(val=1)
head2 = ListNode(val=1)

head1.next = ListNode(2)
head2.next = ListNode(3)

head1.next.next = ListNode(4)
head2.next.next = ListNode(4)

s = Solution()

x = s.mergeTwoLists(head1, head2)
