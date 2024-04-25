# Linked list - Self Referential Objects 
# Linked list is a linear data structure where each element in the list in contained in a separate object called a node.
# A node models two pieces of information and individual item of the data we want to store and a reference to the next node in the list. 
# The first node in the linked list is called the head of the list while the last node called the tail. 

# Linked list often come in two forms - Singly linked list -> where each node stores a reference to the next node in the list or
# a doubly linked list where each node stores a reference to both the node before and after.

class Node: 
    """
    An object for storing a single node of a linked list. 
    Attributes:
    data: Data stored in node
    next_node: Reference to next node in linked list
    """
    data = None 
    next_node = None 

    def __init__(self, data):
        self.data = data 

    def __repr__(self):
        return "<Node data: %s>" % self.data 

class  LinkedList: 
    """
    Singly Linked list
    """

    def __init__(self):
        self.head = None 
    
    def is_empty(self):
        return self.head == None 


    def size(self):
        """
        Returns the number of nodes in the list Takes O(n) time
        """
        current = self.head 
        count = 0 

        while current: 
            count += 1 
            current = current.next_node 

        return count 


    def add(self, data):
        """ 
        Adds new Node containing data at the head of the list 
        Takes O(1) time 
        """
        new_node = Node(data)
        new_node.next_node = self.head 
        self.head = new_node 
    
    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Returns the node or `None` if not found
        Takes O(n) time
        """

        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """ Inserts a new Node containing data at index position 
        Insertion takes O(1) time but finding the node at the 
        insertion point take 0(n) time.

        Takes overall O(n) time 
        """
        if index == 0:
            self.add(data)
        
        if index > 0:
            new = Node(data)
            position = index
            current = self.head
            
            while position > 1:
                current = node.next_node 
                position -= 1 

            prev_node = current 
            next_node = current.next_node 

            prev.next_node = new 
            new.next_node =  next_node 
    
    def remove(self, key):
        """ 
        Removes Node containing data that matches the key
        Returns the node or None if key doesnt exist
        Takes O(n) time 
        """
        
        current = self.head
        previous = None 
        found = False 

        while current and not found:
            if current.data == key and current is self.head:
                found = True 
                self.head = current.next_node 
            elif current.data == key:
                found = True
                previous.next_node = current.next_node 
            else:
                previous = current 
                current = current.next_node 

        return current 



    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        current = self.head
        
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return  '-> '.join(nodes)
