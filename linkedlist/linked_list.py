import sys


class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node
        

class LinkedList:        
    
    def __init__(self, head):
        self.head = head

    def insert(self, data):
        if self.head.next_node is None:
            temp = Node(data, None)
            self.head.next_node = temp
            return
        temp = self.head.next_node
        while not (temp.next_node is None):
            temp = temp.next_node
        temp.next_node = Node(data, None)

    def delete_by_index(self, index):
        if index == 0:
            if self.head is None:
                raise IndexError
            self.head.data = self.head.next_node.data
            self.head.next_node = self.head.next_node.next_node
            return
        temp = self.head
        for i in range(index - 1):
            if temp is None:
                raise IndexError
            temp = temp.next_node
        temp1 = temp.next_node
        temp1 = temp1.next_node
        temp.next_node = temp1

    def reverse(self):
        if self.head is None:
            return
        if self.head.next_node is None:
            return
        curr = self.head
        prev = None
        while curr is not None:
            next = curr.next_node
            curr.next_node = prev
            prev = curr
            curr = next
        self.head = prev

    def print(self):
        temp = self.head
        print("print start")
        while temp is not None:
            sys.stdout.write(str(temp.data))
            sys.stdout.write(" ")
            sys.stdout.flush()
            temp = temp.next_node
        sys.stdout.write("\n")
        sys.stdout.flush()
        print("print complete")


if __name__ == "__main__":
    root = Node(5, None)
    list = LinkedList(root)
    list.insert(6)
    list.insert(7)
    list.insert(complex(6.0, 9))
    list.insert("root")
    list.print()
    list.delete_by_index(3)
    list.print()
    list.reverse()
    list.print()
