# definition of a list node
class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None


class LinkedList:
    def __init__(self, head: ListNode):
        self.head = head

    def insert_node_by_head(self, node: ListNode):
        if node:
            node.next = self.head.next
            self.head.next = node

    def insert_value_by_head(self, value):
        new_node = ListNode(value)
        self.insert_node_by_head(new_node)

    def swap_pairs(self):
        pre = self.head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.head

    def print_all(self):
        pos = self.head.next
        if pos is None:
            return
        while pos.next is not None:
            print(pos.value)
            pos = pos.next
        print(pos.value)


class Solution:
    def swapParis(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next


if __name__ == '__main__':
    head = ListNode(0)
    linkedlist_1 = LinkedList(head)
    for data in range(5):
        linkedlist_1.insert_value_by_head(data)

    linkedlist_1.print_all()

    linkedlist_1.swap_pairs()
    print("\n =============== \n")
    cur = linkedlist_1.head
    print(cur.value)
    print("\n =============== \n")
    linkedlist_1.print_all()

    print("\n =============== \n")
    print("\n =============== \n")

    l1 = Solution()
    cur2 = l1.swapParis(linkedlist_1.head.next)
    while cur2:
        print(cur2.value)
        cur2 = cur2.next
