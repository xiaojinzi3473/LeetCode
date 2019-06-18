from proto.node_single import Node
from utils.singly_linkedlist import SinglyLinkedListWithoutHead


"""
    reverse a singly linked list
    input: 1--> 2 -->3 --> NULL
    Output: 3 --> 2-->1 --> NULL
"""


class Solution:
    def reverseList(self, head: Node) -> Node:

        cur, pre = head, None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next

        return pre


class Solution2:
    def reverseList(self, head: Node) -> Node:
        if head is None or head.next is None:
            return head
        cur = head
        a = None
        while cur.next:
            a = cur.next
            cur.next = a.next
            a.next = head
            head = a
        return head


if __name__ == '__main__':
    l1 = SinglyLinkedListWithoutHead()
    l3 = SinglyLinkedListWithoutHead()
    for item in range(1, 4):
        l1.insert_value_to_head(item)
    l1.print_linkedList()
    s1 = Solution()
    l1.head = s1.reverseList(l1.head)
    l1.print_linkedList()

    l2 = SinglyLinkedListWithoutHead()
    for item in range(1, 2):
        l2.insert_value_to_head(item)
    l2.print_linkedList()
    s2 = Solution2()
    l2.head = s2.reverseList(l2.head)
    l2.print_linkedList()

