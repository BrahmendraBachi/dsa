class Node:
    def __init__(self, value=None, next=None):
        self.val = value
        self.next = next


class LinkedList:
    def __init__(self, elements=None, start_head=None):
        if start_head:
            self.head = start_head
        else:
            self.head = Node(elements[0])
            for element in elements[1:]:
                self.insert_at_end(element, printAfterInsert=False)

    def print_elements(self):
        head = self.head
        while head.next:
            print(head.val, end=' --> ')
            head = head.next
        print(head.val, "\n")

    def get_length(self):
        head = self.head
        ele_count = 0
        while head:
            ele_count += 1
            head = head.next
        return ele_count

    def insert_at_end(self, val, printAfterInsert=True):
        head = self.head
        while head.next:
            head = head.next
        head.next = Node(val)
        if printAfterInsert:
            print(f"Printing list after inserting {val} at end is: ")
            self.print_elements()

    def insert_at_start(self, val, printAfterInsert=True):
        new_head = Node(val, self.head)
        self.head = new_head
        if printAfterInsert:
            print(f"Printing list after inserting {val} at start is: ")
            self.print_elements()

    def insert_at_index(self, val, index=0, printAfterInsert=False):
        if index > self.get_length() or index < 0:
            raise Exception("Invalid Index. Index should lies in (0, len(linked_list)+1")

        if index == self.get_length():
            self.insert_at_end(val)
            return
        if index == 0:
            self.insert_at_start(val)
            return
        head = prev = self.head
        curr_index = 0
        while curr_index < index:
            prev = head
            head = head.next
            curr_index += 1

        new_node = Node(val)
        prev.next = new_node
        new_node.next = head
        if printAfterInsert:
            print(f"After inserting element at index {index} is: ")
            self.print_elements()

    def delete_at_start(self, printAfterDelete=True):
        self.head = self.head.next
        if printAfterDelete:
            print("After deleting element at start is: ", )
            self.print_elements()

    def delete_at_end(self, printAfterDelete=True):
        head = prev = self.head
        while head.next:
            prev = head
            head = head.next
        prev.next = None

        if printAfterDelete:
            print("After deleting element at end: ")
            self.print_elements()

    def delete_at_index(self, index, printAfterDelete=True):
        if index > self.get_length() or index < 0:
            raise Exception("Invalid Index. Index should lies in (0, len(linked_list)+1")

        if index == 0:
            self.delete_at_start(printAfterDelete)
            return
        if index == self.get_length() - 1:
            self.delete_at_end(printAfterDelete)
            return

        prev = head = self.head
        curr_index = 0
        while curr_index < index:
            prev = head
            head = head.next
            curr_index += 1
        prev.next = head.next
        if printAfterDelete:
            print(f"After deleting element at ind {index} is: ")
            self.print_elements()

    def reverse(self, printAfterReverse=True):
        prev, root = None, self.head
        while root:
            next = root.next
            root.next = prev
            prev = root
            root = next
        self.head = prev

        if printAfterReverse:
            print("After reversing linked_list: ")
            self.print_elements()

    def recursiveReverse(self, printAfterReverse=True):
        self.head = self.reverseNodes(None, self.head)

        if printAfterReverse:
            print("After reversing linked_list: ")
            self.print_elements()

    def reverseNodes(self, prev: Node, currNode: Node):
        if not currNode:
            return prev
        temp = currNode.next
        currNode.next = prev
        return self.reverseNodes(currNode, temp)

    def returnHead(self):
        return self.head


if __name__ == '__main__':
    list_elements = [1, 2, 3, 4, 5, 6, 7, 8]
    linked_list = LinkedList(list_elements)
    linked_list.print_elements()
    linked_list.insert_at_end(9)
    linked_list.insert_at_start(0)
    linked_list.insert_at_index(100, 10, True)
    linked_list.delete_at_start()
    linked_list.delete_at_end()
    linked_list.delete_at_index(3)

    linked_list.reverse()
