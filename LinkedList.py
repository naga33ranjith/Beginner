class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None

    def InsertingNodeAtFront(self,data):
        node=Node(data)

        if self.head is None:
            self.head=node
        else:
            node.next=self.head
            self.head=node
        
    def InsertingNodeAfterGivenNode(self,previousNode,data):
        node=Node(data)

        if previousNode is None:
            print("Given Node doesn't exist")
            return
        
        node.next=previousNode.next
        previousNode.next=node

    def InsertingNodeAtEnd(self,data):
        node=Node(data)

        if self.head is None:
            self.head=node
            return
        
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=node
    

    def printlist(self):
        temp=self.head
        while temp is None:
            print(temp.data)
            temp=temp.next
        
    
if __name__ == "__main__":
    object1=LinkedList()
    object1.InsertingNodeAtFront(5)
    object1.InsertingNodeAtFront(4)
    object1.InsertingNodeAtEnd(8)
    object1.InsertingNodeAfterGivenNode(object1.head.next,6)
    object1.printlist()