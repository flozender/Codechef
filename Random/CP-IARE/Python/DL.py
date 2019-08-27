class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def insertL(data, head, tail):
    n = Node(data)
    if head == None and tail == None:
        tail = n
        head = n
        return head, tail    
    a = tail
    tail = n
    a.right = n    
    n.left = a
    return head, tail

def displayF(head):
    a = head
    while a != None:
        print(a.data)
        a = a.right


head, tail = None, None
head, tail = insertL(1, head, tail)
head, tail = insertL(2, head, tail)
displayF(head)
