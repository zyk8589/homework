class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_node(head, index):
    if index == 0:
        if head is None:
            return None
        return head.next
    
    current = head
    for i in range(index - 1):
        if current is None or current.next is None:
            print("索引超出范围")
            return head
        current = current.next
    
    if current.next is None:
        print("索引超出范围")
        return head
    
    current.next = current.next.next
    
    return head

def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    print(" -> ".join(values) if values else "空链表")

if __name__ == "__main__":
    head = ListNode("a")
    head.next = ListNode("b")
    head.next.next = ListNode("c")
    head.next.next.next = ListNode("d")
    
    print("原始链表:")
    print_linked_list(head)
    
    head = delete_node(head, 2)
    print("删除索引2后:")
    print_linked_list(head)
    
    head = delete_node(head, 0)
    print("删除头节点后:")
    print_linked_list(head)