class Node: 
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

class BST: 
    def __init__(self):
        self.root = None

    def _insert_helper(self, root, value):
        
        if(root == None):
            return Node(value)

        if root.data == value:
            return root
        elif value < root.data:
            root.left = self._insert_helper(root.left, value)
        elif value > root.data:
            root.right =self._insert_helper(root.right, value)
        
        return root

    def insert(self, value):
        
        if(self.root == None):
            self.root = Node(value)
            return self.root
        
        self._insert_helper(self.root, value)
        
        

    def _inorder_traversal_helper(self, root):

        if root == None:
            return None

        self._inorder_traversal_helper(root.left)
        print(root.data, end=", ")
        self._inorder_traversal_helper(root.right)

        return None

    def inorder_traversal(self):

        if self.root == None:
            print("Tree is Empty") 
        else:
            self._inorder_traversal_helper(self.root)
        
        print("\n")

    def _search_helper(self, root, value):
        
        if root == None:
            return None
        if root.data == value:
            return root
        if root.data > value:
            return self._search_helper(root.left, value)

        if root.data < value:
            return self._search_helper(root.right, value)
        

    def search(self, value):
        if self.root == None:
            print("Tree is Empty")
            return None
        else: 
            found = self._search_helper(self.root, value)
            if found != None:
                print(f"Item Found {found.data}", end="\n")
            else:
                print(f"Item {value} Not Found in tree")
        
    def _only_search(self, value):
        if self.root == None:
            return None
        else: 
            return self._search_helper(self.root, value)
        

    def _get_successor(self, root):
        root = root.right
        while root != None and root.left != None:
            root = root.left
        return root 
    
    def _delete_helper(self, root, value):
        
        if root == None:
            return root
        elif root.data < value: 
            root.right = self._delete_helper(root.right, value)
        elif root.data > value:
            root.left = self._delete_helper(root.left, value)
        else: 
            # element found now delete
            if root.left == None: 
                return root.right
            elif root.right == None:
                return root.left 
            else:
                succ = self._get_successor(root)
                root.data = succ.data
                root.right = self._delete_helper(succ, succ.data)



    def delete_node(self, value):

        found_node = self._only_search(value)

        if found_node == None:
            # if element not found 
            print("Not Found")
        else:
            # if it is a last element of the tree or leaf node
             self._delete_helper(self.root, value)
        
        


# ----------------------------------------
bst1 = BST()

bst1.insert(30)
bst1.insert(20)
bst1.insert(40)
bst1.insert(10)
bst1.insert(25)
bst1.insert(5)
bst1.insert(7)
bst1.insert(50)


bst1.inorder_traversal()
# bst1.search(40)
# bst1.search(300)
# bst1.delete_node(40)
# bst1.delete_node(50)
bst1.delete_node(10)

bst1.inorder_traversal()

