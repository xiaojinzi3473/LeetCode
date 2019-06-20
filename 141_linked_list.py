from proto.node_single import Node
from utils.singly_linkedlist import SinglyLinkedListWithoutHead
import datetime

"""
    Given a linked list, determine if it has a cycle in it.

    To represent a cycle in the given linked list, we use an integer pos which represents the position 
    (0-indexed) in the linked list where tail connects to. 
    If pos is -1, then there is no cycle in the linked list.
    
"""


# using slow, fast pointer
class Solution():
    def hasCycle(self, head: Node):
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


# check if the linked list has end node point to None
class Solution2():
    def hasCycle(self, head: Node):
        pos = head
        start_time = datetime.datetime.now()
        timeslot = 0
        while pos and pos.next and timeslot > 0.1:
            pos = pos.next
            end_time = datetime.datetime.now()
            timeslot = (end_time - start_time).microseconds
            print(timeslot)
            return True

        return False


class Solution3():
    def hasCycle(self, head: Node):
        """
        :type head: ListNode
        :rtype: bool
        """
        pos = head
        start_time = datetime.datetime.now()
        timeslot = 0
        while pos and pos.next:
            end_time = datetime.datetime.now()
            timeslot = (end_time - start_time).microseconds
            if timeslot > 0.5:
                print(timeslot)
                return True
            pos = pos.next
        return False


# using hash table using dict key to store Node already check
class Solution4():
    def hasCycle(self, head: Node):
        d1 = {}
        while head:
            # if d1.get(head):
            if head in d1:
                return True
            else:
                d1[head] = 1
            head = head.next

        return False


if __name__ == '__main__':
    #start_time = datetime.datetime.now()
    #print(start_time)
    l1 = SinglyLinkedListWithoutHead()
    for data in range(1, 3):
        l1.insert_value_to_head(data)
    l1.print_linkedList()
    s1 = Solution()
    print("Solution 1: ")
    print(s1.hasCycle(l1.head))
    print("\nSolution 2: ")
    s2 = Solution2()
    print(s2.hasCycle(l1.head))
    print("\nSolution 4: ")
    s4 = Solution2()
    print(s4.hasCycle(l1.head))

    # make tail linked to head
    cur = l1.head
    while cur.next:
        cur = cur.next
    #print(cur.value)
    #print(l1.head.value)
    cur.next = l1.head

    print("\n---Has Cycle ---\n")
    print("Solution 1: ")
    print(s1.hasCycle(l1.head))
    print("\nSolution 2: ")
    print(s2.hasCycle(l1.head))
    print("\nSolution 4: ")
    s4 = Solution4()
    print(s4.hasCycle(l1.head))
