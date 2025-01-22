class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def ListLength(self):
        curr_node = self.head
        length = 0
        while(curr_node is not None):
            length += 1
            curr_node = curr_node.next
        return length

    def print_LinkedList(self):
        curr_node = self.head
        while(curr_node is not None):
            print(curr_node.data)
            curr_node = curr_node.next

    def insertAtBegin(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
    def insertAtIndex(self, data, index):
        if (index == 0):
            new_node = Node(data)
            self.insertAtBegin(data)
        else:
            curr_node = self.head

            while(index > 1 and curr_node != None):
                curr_node = curr_node.next
                index -= 1

            if curr_node != None:
                new_node = Node(data)
                new_node.next = curr_node.next
                curr_node.next = new_node
            else:
                print("invalid index")

    def removeHead(self):
        if not self.head:
            return
        
        temp = self.head
        self.head = self.head.next
        temp = None

        return self.head

    def removeAtIndex(self, index):
        current_node = self.head
        for _ in range(index-1):
            current_node = current_node.next
        
        current_node.next = current_node.next.next

    

my_list = LinkedList()
my_list.insertAtBegin(2)
my_list.insertAtBegin(1)
my_list.insertAtBegin("apple2")
my_list.insertAtBegin("apple1")

# my_list.insertAtIndex("wtf", 2)
my_list.removeAtIndex(2)
my_list.print_LinkedList()