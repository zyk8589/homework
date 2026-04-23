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
    
    def print_list(self):
        current = self.head
        values = []
        while current:
            values.append(str(current.val))
            current = current.next
        print(" -> ".join(values) if values else "空链表")
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        self.head = prev

def main():
    print("=" * 40)
    print("链表反转测试")
    print("=" * 40)
    
    ll = LinkedList()
    for val in ['a', 'b', 'c']:
        ll.append(val)
    
    print("原链表:")
    ll.print_list()
    
    ll.reverse()
    print("反转后:")
    ll.print_list()

if __name__ == "__main__":
    main()
    
  