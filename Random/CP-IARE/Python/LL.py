class Node:
    def __init__(self,data):
        self.data = data
        self.right = None

def insertL(data, head):
    n = Node(data)
    a = head
    if head == None:
        head = n
        return head
    else:
        while a.right != None:
            a = a.right
        a.right = n
        return head

def insertF(data, head):
    n = Node(data)
    a = head
    if head == None:
        head = n
        return head
    else:
        head = n
        head.right = a
        return head

def insertP(data, head, val):
    n = Node(data)
    a = head
    if head == None:
        head = n
        return head
    else:
        while a.data != val:
            a = a.right
        temp = a
        a.right = n
        n.right = temp
        return head

def deleteL(head):
    if head == None:
        return head
    a = head
    while a.right.right != None:
        a = a.right
    a.right = None
    return head

def deleteF(head):
    if head == None:
        return head
    a = head
    head = a.right
    return head

def merge(head1, head2):
    a1 = head1
    a2 = head2
    while a1.right != None:
        a1 = a1.right
    a1.right = a2
    return head1

def displayR(head):
    a = head
    while a != None:
        print(a.data)
        a = a.right

head = None
head2 = None

head2 = insertL(8, head2)
head2 = insertF(7, head2)
head2 = insertL(9, head2)

head = insertL(1, head)
head = insertL(2, head)
head = insertL(3, head)
head = insertL(4, head)
# head = deleteL(head)
# head = deleteF(head)
print("L1")
displayR(head)
print("L2")
displayR(head2)
head = merge(head, head2)
print("Merged")
displayR(head)

print("Exit")
