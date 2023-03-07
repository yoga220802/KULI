from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data, end=" | ")
            currentNode = currentNode.next
        print()

    def insertAtBeginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode

    def insertAfterNode(self, prevNode, data):
        if prevNode is None:
            print("Node sebelumnya tidak ada dalam list.")
            return
        
        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode

    def searchNode(self, key):
        currentNode = self.head
        while currentNode:
            if currentNode.data == key:
                return currentNode
            currentNode = currentNode.next
        return False

    def deleteNode(self, key):

        node = self.head
        prev = None

        try:
            while node is not None:
                if node.data == key:
                    break

                prev = node
                node = node.next

            if node is None:
                raise ValueError("Data tidak ditemukan dalam list")

            if prev is None:
                self.head = node.next
            else:
                prev.next = node.next
            print("Node berhasil dihapus:", key)
        except ValueError as e:
            print(e)