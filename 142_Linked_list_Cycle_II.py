from proto.node_single import Node
from utils.singly_linkedlist import SinglyLinkedListWithoutHead


class Solution():
    def detectCycle(self, head: Node):
        d1 = dict()
        cur = head
        i = 0
        while cur:
            if cur in d1:
                return(d1.get(cur))
                # return cur
            else:
                d1[cur] = i
            cur = cur.next
            i = i + 1
        return None

class Solution2(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        d1 = dict()
        while head:
            if head in d1:
                return head
            else:
                d1[head] = 1
            head = head.next
        return None

    
class Solution3():
    def detectCycle(self, head: Node):
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None
    

if __name__ == '__main__':
    #start_time = datetime.datetime.now()
    #print(start_time)
    l1 = SinglyLinkedListWithoutHead()
    for data in range(4):
        l1.insert_value_to_head(data)
    l1.print_linkedList()
    s1 = Solution()
    print("Solution 1: ")
    print(s1.detectCycle(l1.head))

    # make tail linked to head
    cur = l1.head
    while cur.next:
        cur = cur.next
    cur.next = l1.head.next
    #l1.print_linkedList()

    print("\n---Has Cycle ---\n")
    print("Solution 1: ")
    print(s1.detectCycle(l1.head))
