class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(data, head):
    n = Node(data)
    if head == None:
        head = n
        return head
    else:
        a = head
        while a.next != None:
            a = a.next
        a.next = n
        return head

def pop(head):
    if head == None:
        print("Empty stack!")
        return head
    else:
        a = head
        while a.next.next != None:
            a = a.next
        a.next = None
        return head

def display(head):
    if head == None:
        print("Empty Stack!")
    else:
        a = head
        while a != None:
            print (a.data, end = " ")
            a = a.next
        print()

head = None
head = push(2, head)
head = push(3, head)
head = push(4, head)
display(head)
head = pop(head)
display(head)