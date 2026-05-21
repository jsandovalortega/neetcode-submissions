class ListNode: 
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head=ListNode(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        curr = self.head.next
        # helps find index
        i = 0 
        while curr:
            if i == index:
                return curr.val
            i+=1
            curr = curr.next
        return -1 # could not find a correct index
        

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode

        if not newNode.next:
            # list was empty
            self.tail = newNode
        

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        i = 0 
        curr = self.head
        while i < index and curr: 
            i += 1
            curr = curr.next
        # made it to the node to remove
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
        

    def getValues(self) -> List[int]:
        curr = self.head.next
        listOfVals = []
        while curr: 
            listOfVals.append(curr.val)
            curr = curr.next
        return listOfVals
        
