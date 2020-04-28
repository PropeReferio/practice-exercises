# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

# In this example, assume nodes with the same value are the exact same node objects.

# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

class Node():

    def __init__(self, val):
        self.val = val
        self.next = None

    def traverse(self):
        while self:
            print(self.val)
            self = self.next

    def listLength(self):
        if not self:
            return 0
        elif not self.next:
            return 1
        else:
            return 1 + self.next.listLength()
    
    def indexList(self, index):
        for i in range(index):
            try:
                self = self.next
            except:
                print('Index out of range')
        return self
        

a = Node(3)
a.next = Node(7)
a.next.next = Node(8)
a.next.next.next = Node(10)

b = Node(99)
b.next = Node(1)
b.next.next = Node(9)
b.next.next.next = Node(10)

# a.traverse()
# print(a.val)

def linkedIntersection(left, right):
    rightlength = right.listLength()
    #An outer foor loop using the shorter linked list,
    #It compares a value to every value in the other list, and if there is a match,
    #It returns that value.
    leftstart = left
    for i in range(rightlength):
        current = right.indexList(i)
        while left:
            if current.val == left.val:
                return current.val
            else:
                left = left.next
        left = leftstart
    return -1

print(linkedIntersection(a, b))

def findIntersection(a, b): #Trying to follow the posted solution:
    m, n = a.listLength(), b.listLength()
    print('Lengths: ', m, n)
    cur_a, cur_b = a, b
    print('Starting Nodes: ', cur_a.val, cur_b.val)

    if m > n:
        for _ in range(m-n):
            cur_a = cur_a.next
    elif n > m:
        for _ in range(n-m):
            cur_b = cur_b.next

    while cur_a.val != cur_b.val:
        print('After equalizing or advancing: ', cur_a.val, cur_b.val)
        cur_a, cur_b = cur_a.next, cur_b.next

    return cur_a.val

print(findIntersection(a, b))


# makeLinkedList([3, 7, 8, 10])
