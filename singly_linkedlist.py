from proto.node_single import Node


"""
    Single linked List without head node
"""


class SinglyLinkedListWithoutHead:
    def __init__(self):
        self.head = None

    def insert_value_to_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_value_after_node(self, value, node: Node):
        new_node = Node(value)

        if self.head is None and node is None:
            new_node.next = None
            self.head = new_node
        elif self.head is None and node is not None:
            return "Node is not found in linkedlist."

        cur = self.head
        while cur != node and cur.next is not None:
            cur = cur.next

        if cur != node:
            return "Node is not found in linkedlist."

        new_node.next = node.next
        node.next = new_node

    def insert_value_before_node(self, value, node: Node):
        new_node = Node(value)
        if self.head is None or node is None:
            return "Invalid Node"

        if node == self.head:
            self.insert_value_to_head(value)

        cur = self.head
        while cur.next != node and cur.next is not None:
            cur = cur.next

        if cur.next != node:
            return "Node is not found in the linked list"
        new_node.next = node
        cur.next = new_node

    def delete_node_by_value(self, value):
        if self.head is None:
            return "Empty List"

        cur = self.head
        while cur.next:
            if cur.value == value:
                cur.next = cur.next
                break
            else:
                cur = cur.next

    def print_linkedList(self):
        cur = self.head
        print("-- Start to Print --")
        while cur:
            print(cur.value)
            cur = cur.next
        print("-- End of Printing --\n")


if __name__== '__main__':
    l1 = SinglyLinkedListWithoutHead()
    for item in range(1, 7):
        l1.insert_value_to_head(item)
    l1.print_linkedList()

    l2 = SinglyLinkedListWithoutHead()
    for item in range(7):
        l2.insert_value_after_node(item, l2.head)
    l2.print_linkedList()

    for item in range(8, 10):
        l1.insert_value_after_node(item, l1.head)
    l1.print_linkedList()
