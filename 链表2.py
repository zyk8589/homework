class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def has_cycle(self):
        if not self.head or not self.head.next:
            return False
        
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def create_cycle(self, pos):
        if pos < 0:
            return
        current = self.head
        cycle_node = None
        index = 0
        while current:
            if index == pos:
                cycle_node = current
            if not current.next:
                current.next = cycle_node
                break
            current = current.next
            index += 1

def main():
    print("=" * 40)
    print("环检测测试")
    print("=" * 40)
    
    print("\n测试1：无环链表")
    ll1 = LinkedList()
    for val in [1, 2, 3, 4, 5]:
        ll1.append(val)
    print(f"链表是否有环: {ll1.has_cycle()}")
    
    print("\n测试2：有环链表")
    ll2 = LinkedList()
    for val in [1, 2, 3, 4, 5]:
        ll2.append(val)
    ll2.create_cycle(0)
    print(f"链表是否有环: {ll2.has_cycle()}")

if __name__ == "__main__":
    main()