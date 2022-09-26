################################## Data Structures ################################

# ------------------------------- Singly Linked List -----------------------------

class SinglyLinkedListNode:
    """This class is used to make data elements for singly linked list. |br| 
    Member functions are: |br| 
    1. __init__ |br| 
    2. __str__ |br|

    :Example: |br|  

        >>> from DSA import *
        >>> s = SinglyLinkedListNode(10)
        >>> print(type(s))
        <class 'DSA.SinglyLinkedListNode'>
        >>> s1 = s.__str__()
        >>> print(type(s1))
        <class 'str'>
        >>> print(s1)
        10
    """
    
    def __init__(self, data):
        """This is the default constructor for this  class.

        :param data: Value of the data element passed to the function.
        :type data: object
        """
        self.data = data
        self.next = None
    
    def __str__(self):
        """This function converts the type data element to string.

        :return: Returns the string of data element.
        :rtype: str
        """
        return str(self.data)

class SinglyLinkedList:
    """This class is used to implement singly Linked List. |br| 
    The member functions are: |br| 
    1. __init__  |br| 
    2. insert |br| 
    3. find |br| 
    4. deleteVal |br| 
    5. printer |br| 
    6. reverse |br| 
    
    :Example: |br|

        >>> from DSA import *
        >>> s = SinglyLinkedList()
        >>> print(type(s))
        <class 'DSA.SinglyLinkedList'>
        >>> s.printer()
        []
        >>> s.insert(5)
        >>> s.insert(2)
        >>> s.insert(6)
        >>> s.insert(7)
        >>> s.find(5)
        >>> print(s.find(5))
        None
        >>> print(s.find(6))
        2
        >>> s.printer()
        [5, 2, 6, 7]
        >>> s.reverse()
        >>> s.printer()
        [7, 6, 2, 5]
        >>> s.deleteVal(2)
        True
    """
    
    def __init__(self):
        """This is the default constructor of the class. |br| 
        It constrcuts a list of zero length and initilises the head and tail to null.
        """
        self.head = None
        self.tail = None
   
    def insert(self, data):
        """This function is used to insert elements into the list.

        :param data: The value of element to be inserted.
        :type data: object
        """
        node = SinglyLinkedListNode(data) # new node
        if not self.head: # no head
            self.head = node
        else:
            self.tail.next = node # add behind tail
        self.tail = node # move tail
    
    def find(self, data):
        """This function is used to find an element in the linked list.

        :param data: The value of the element to be found in the linked list.
        :type data: object
        :return: Returns the location of the element previous to the element to be searched for.
        :rtype: pointer
        """
        head = self.head
        prev = None
        while head != None and head.data != data:
            prev = head
            head = head.next
        return prev
    
    def deleteVal(self, data):
        """This fuction deletes an element from the linked list.

        :param data: The value of the element to be deleted.
        :type data: object
        :return: Returns true if deleted else returns false.
        :rtype: bool
        """
        prevPos = self.find(data)
        if prevPos.next == None:
            return False
        prevPos.next.next = prevPos.next
        return True
    
    def printer(self, sep = ', '):
        """This function prints the linked list.

        :param sep: A string element used to separate elements of the list., defaults to ', '
        :type sep: str, optional
        """
        ptr = self.head
        print('[', end = '')
        while ptr != None:
            print(ptr, end = '')
            ptr = ptr.next
            if ptr != None:
                print(sep, end = '')
        print(']')
    
    def reverse(self):
        """This function is used to reverse the orientation of the list.
        """
        head = self.head # head pointer
        prev = None # previous pointer
        while head != None: # while there is forward link left
            newHead = head.next # save extra pointer to next element
            head.next = prev # reverse the link of current element
            prev = head # move pointer to previous element
            head = newHead # use extra pointer to move to next element
        self.tail = self.head
        self.head = prev

def merge(list1, list2):
    """This function is used to merge twp linked lists together.

    :param list1: The first list which needs to be merged.
    :type list1: list
    :param list2: The second list which needs to be merged.
    :type list2: list
    :return: Returns the merged linked list.
    :rtype: list
    :Example: |br| 

        >>> from DSA import *
        >>> s1 = SinglyLinkedList()
        >>> s2 = SinglyLinkedList()
        >>> s1.insert(1)
        >>> s1.insert(2)
        >>> s1.insert(3)
        >>> s2.insert(4)
        >>> s2.insert(5)
        >>> s2.insert(6)
        >>> s1.printer()
        [1, 2, 3]
        >>> s2.printer()
        [4, 5, 6]
        >>> s3 = merge(s1,s2)
        >>> s3.printer()
        [1, 2, 3, 4, 5, 6]
    """
    merged = SinglyLinkedList()
    head1 = list1.head
    head2 = list2.head
    while head1 != None and head2 != None: # both lists not empty
        if head1.data < head2.data: # link node with smaller data
            merged.insert(head1.data)
            head1 = head1.next
        else:
            merged.insert(head2.data)
            head2 = head2.next
    if head1 == None and head2 != None: # list 1 finished
        merged.tail.next = head2 # add remaining list 2 as is
    if head1 != None and head2 == None: # list 2 finished
        merged.tail.next = head1 # add remaining list 1 as is
    return merged

# ------------------------------ Doubly Linked List ----------------------------

class DoublyLinkedListNode:
    """This class is used to create elements for the doubly linked list. |br| 
    The member functions are: |br| 
    1. __init__ |br| 
    2. __str__ |br| 

    :Example: |br| 

        >>> from DSA import *
        >>> d = DoublyLinkedListNode(10)
        >>> print(type(d))
        <class 'DSA.DoublyLinkedListNode'>
        >>> d1 = d.__str__()
        >>> print(type(d1))
        <class 'str'>
        >>> print(d1)
        10
    """
    def __init__(self, data):
        """This is the default constructor of this class.

        :param data: This is the value to which the value of element is initialised.
        :type data: object
        """
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self):
        """This function converts the type data element to string.

        :return: Returns the string of data element.
        :rtype: str
        """
        return str(self.data) 

class DoublyLinkedList:
    """This is the class to implement the Doubly linked list. |br| 
    Member functions: |br| 
    1. __init__ |br| 
    2. insert |br| 
    3. printer |br| 
    4. reverse |br| 

    :Example: |br| 

        >>> from DSA import *
        >>> d = DoublyLinkedList()
        >>> d.printer()
        []
        >>> print(type(d))
        <class 'DSA.DoublyLinkedList'>
        >>> d.insert(5)
        >>> d.insert(2)
        >>> d.insert(6)
        >>> d.insert(7)
        >>> d.printer()
        [5, 2, 6, 7]
        >>> d.reverse()
        >>> d.printer()
        [7, 6, 2, 5]
    """
    
    def __init__(self):
        """This is the default constructor of this class. |br| 
        It creates a null list and initialises the value of head and tail to null.
        """
        self.head = None
        self.tail = None
    
    def insert(self, data):
        """This function is used to insert elements in the linked list.

        :param data: This is the value to be inserted in the linked list.
        :type data: pbject
        """
        node = DoublyLinkedListNode(data) # new node
        if not self.head: # no head
            self.head = node
        else:
            self.tail.next = node # add behind tail
            node.prev = self.tail
        self.tail = node # move tail
    
    def printer(self, sep = ', '):
        """This function is used to print the linked list.

        :param sep: This is the string variable used to seperate the elements of the linked list., defaults to ', '
        :type sep: str, optional
        """
        ptr = self.head
        print('[', end = '')
        while ptr != None:
            print(ptr, end = '')
            ptr = ptr.next
            if ptr != None:
                print(sep, end = '')
        print(']')
    
    def reverse(self):
        """This function is used to reverse the orientation of the linked list.
        """
        head = self.head # head pointer
        prev = None # previous pointer
        while head != None: # new node left
            newHead = head.next # save pointer to next node (cut forward link)
            if newHead != None: # check if next node has a reverse link
                newHead.prev = head # save pointer to previous node (cut reverse link)
            head.next = prev # reverse the forward link
            head.prev = newHead # reverse the reverse link
            prev = head # move pointer to previous element
            head = newHead # use saved pointer to move head
        self.tail = self.head
        self.head = prev

# -------------------------- Binary Search Tree ------------------------------


class BSTNode:
    """This class is used to create nodes of the Binary Search tree. |br| 
    The member functions are: |br| 
    1. __init__ |br| 
    2. __str__ |br| 

    :Example: |br| 

        >>> from DSA import *
        >>> b = BSTNode(5)
        >>> print(type(b))
        <class 'DSA.BSTNode'>
        >>> b1 = b.__str__()
        >>> print(type(b1))
        <class 'str'>
        >>> print(b1)
        5
    """
    def __init__(self, info):
        """This is the default constructor for this class. |br| 
        Initialises the current node to the given value.

        :param info: Contains the value to which the current node is to be initialised to.
        :type info: object
        """
        self.info = info
        self.left = None
        self.right = None
        self.level = None
    
    def __str__(self):
        """This function converts the type of data element to string.

        :return: Returns the string of data element.
        :rtype: str
        """
        return str(self.info)

class BinarySearchTree:
    """This class is used to create a Binary Search Tree. |br| 
    Member functions: |br| 
    1. __init__ |br| 
    2. insert |br| 
    3. traverse |br| 
    4. height |br| 

    :Example: |br| 

        >>> from DSA import *
        >>> b = BinarySearchTree()
        >>> print(type(b))
        <class 'DSA.BinarySearchTree'>
        >>> b.insert(5)
        >>> b.insert(2)
        >>> b.insert(6)
        >>> b.insert(3)
        >>> b.traverse("PRE")
        5 2 3 6 
        >>> b.traverse("IN")
        2 3 5 6 
        >>> b.traverse("POST")
        3 2 6 5 
        >>> b.height(b.root)
        2
    """
    
    def __init__(self):
        """This is the default constructor of this  class. |br| 
        Initialises the value of root poiter to null.
        """
        self.root = None
    
    def insert(self, val):
        """This function is used to insert elements in the BST.

        :param val: The value to be inserted in BST.
        :type val: object
        """
        if self.root == None:
            self.root = BSTNode(val)
        else:
            current = self.root
            while True:
                if val < current.info: # move to left sub-tree
                    if current.left:
                        current = current.left # root moved
                    else:
                        current.left = BSTNode(val) # left init
                        break
                elif val > current.info: # move to right sub-tree
                    if current.right:
                        current = current.right # root moved
                    else:
                        current.right = BSTNode(val) # right init
                        break
                else:
                    break # value exists
    
    def traverse(self, order):
        """This function is used to traverse the given tree in the specified order.

        :param order: This is the specified order in which the tree is traversed. The order can be PRE, IN and POST.
        :type order: str
        """
        def preOrder(root):
            """This functions computes the preorder traversal of the BST.

            :param root: This is the root of the tree.
            :type root: pointer
            """
            print(root.info, end = ' ')
            if root.left != None:
                preOrder(root.left)
            if root.right != None:
                preOrder(root.right)
        def inOrder(root):
            """This functions computes the inorder traversal of the BST.

            :param root: This is the root of the tree.
            :type root: pointer
            """
            if root.left != None:
                inOrder(root.left)
            print(root.info, end = ' ')
            if root.right != None:
                inOrder(root.right)
        def postOrder(root):
            """This functions computes the postorder traversal of the BST.

            :param root: This is the root of the tree.
            :type root: pointer
            """
            if root.left != None:
                postOrder(root.left)
            if root.right != None:
                postOrder(root.right)
            print(root.info, end = ' ')
        if order == "PRE":
            preOrder(self.root)
            print()
        elif order == "IN":
            inOrder(self.root)
            print()
        elif order == "POST":
            postOrder(self.root)
            print()
    
    def height(self, root):
        """This computes the height of the tree.

        :param root: The tree of which height is to be computed.
        :type root: Pointer
        :return: Returns the height of the tree.
        :rtype: int
        """
        if root.left == None and root.right == None:
            return 0
        elif root.right == None:
            return 1 + self.height(root.left)
        elif root.left == None:
            return 1 + self.height(root.right)
        else:
            return 1 + max(self.height(root.left),self.height(root.right))

# --------------------------------- Suffix Trie --------------------------------

class Trie:
    """This class is used to make a Suffix Trie. |br| 
    Member functions: |br| 
    1. __init__ |br| 
    2. find |br| 
    3. insert |br| 
    4. checkPrefix |br| 
    5. countPrefix |br| 

    :Example: |br| 

        >>> from DSA import *
        >>> t = Trie()
        >>> print(type(t))
        <class 'DSA.Trie'>
        >>> t.insert("abcd")
        >>> t.insert("adce")
        >>> t.insert("acde")
        >>> t.find(t.T,"a")
        True
        >>> t.checkPrefix("ab")
        True
        >>> t.checkPrefix("abc")
        True
        >>> t.checkPrefix("ad")
        True
        >>> t.checkPrefix("ae")
        False
        >>> t.countPrefix("a")
        3
        >>> t.countPrefix("ab")
        1
    """
    
    def __init__(self):
        """This is the default constructor of this class.
        """
        self.T = {}
    
    def find(self, root, c):
        """Function to find an element in the tire.

        :param root: This is the trie tree in which we are finding elements.
        :type root: pointer
        :param c: This is the element being found.
        :type c: char
        :return: Returns true if found else returns false.
        :rtype: bool
        """
        return (c in root)
    
    def insert(self, s):
        """Function to insert string in the trie.

        :param s: This is the string being inserted in the trie.
        :type s: char
        """
        root = self.T
        for c in s:
            if not self.find(root,c):
                root[c] = {}
            root = root[c]
            root.setdefault('#',0)
            root['#'] += 1
    
    def checkPrefix(self, s):
        """This function is used to check if the passed argument is a prefix of the text from which trie is constructed.

        :param s: We are checking if this parameter is a prefix.
        :type s: char
        :return: Returns true if prefix exists else returns false.
        :rtype: bool
        """
        root = self.T
        for idx, char in enumerate(s):
            if char not in root:
                if idx == len(s) - 1:    
                    root[char] = '#'
                else:
                    root[char] = {}
            elif root[char] == '#' or idx == len(s) - 1:
                return True
            root = root[char]
        return False
    
    def countPrefix(self, s):
        """Couts the number of suffixes which have the guven string as a prefix.

        :param s: We are checking if the given string is a prefix.
        :type s: _char
        :return: Returns the number of suffixes which s as prefix.
        :rtype: int
        """
        found = True
        root = self.T
        for c in s:
            if self.find(root,c):
                root = root[c]
            else:
                found = False
                break
        if found:
            return root['#']
        return 0

class Heap:   
    """This class is used to implement the heap data structure.
    Member functions are parent(self, i), left(self, i), right(self, i), insert(self, val), min(self), Heapify(self, root), deleteMin(self)cd 21010

    :Example: |br| 

        >>> from DSA import *
        >>> h = Heap(10)
        >>> h.insert(5)
        >>> h.insert(3)
        >>> h.insert(2)
        >>> h.insert(6)
        >>> h.insert(7)
        >>> h.parent(1)
        0
        >>> h.left(1)
        3
        >>> h.right(1)
        4
        >>> h.min()
        2
        >>> h.deleteMin()
        >>> h.Heapify(0)
    """
    def __init__(self, cap):
        """This is the default constructor of this class.

        :param cap: This is used to initialise the maximum size of the heap.
        :type cap: int
        """
        self.H = []
        self.n = 0
        self.M = cap
    
    def parent(self, i):
        """This returns the parent of the current node.

        :param i: This is the location of current node.
        :type i: int
        :return: It returns the loaction of the parent.
        :rtype: int
        """
        if i > 0:
            return (i - 1) // 2
    
    def left(self, i):
        """This returns the left child of the current node.

        :param i: This is the location of the current node.
        :type i: int
        :return: Returns the location of left child.
        :rtype: int
        """
        return (2 * i) + 1
    
    def right(self, i):
        """This returns the right child of the current node.

        :param i: This is the location of the current node.
        :type i: int
        :return: This is the location of the right child.
        :rtype: int
        """
        return 2 * (i + 1)
    
    def insert(self, val):
        """This function is used to insert element in heap.

        :param val: This is the value of the element to be inserted.
        :type val: object
        """
        if self.n != self.M:
            self.H.append(val)
            i = self.n
            self.n += 1
            while i != 0 and self.H[self.parent(i)] > self.H[i]:
                self.H[i], self.H[self.parent(i)] = self.H[self.parent(i)], self.H[i]
                i = self.parent(i)
    
    def min(self):
        """This function is used to find the minimum value in the heap.

        :return: Returns the minimum value of heap.
        :rtype: object
        """
        if (self.n != 0):
            return self.H[0]
        return -1
    
    def Heapify(self, root):
        """This function is used to implement heapify algorithm on the heap.

        :param root: This is the node on which we perform heapify.
        :type root: object
        """
        l = self.left(root)
        r = self.right(root)
        s = root
        if (l < self.n and self.H[l] < self.H[root]):
            s = l
        if (r < self.n and self.H[r] < self.H[s]):
            s = r
        if s != root:
            self.H[root], self.H[s] = self.H[s], self.H[root]
            self.Heapify(s)
    
    def deleteMin(self):
        """This function is used to delete the minimum value in the heap.
        """
        if self.n > 0:
            if self.n == 1:
                self.H = []
                self.n = 0
            else:
                self.n -= 1
                self.H[0] = self.H[self.n]
                self.Heapify(0)