
#Binary Tree Data Structure
class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    #add branch to the tree
    def add_child(self, data):
        if self.data == data:
            return
        
        if data < self.data:
            #add data to the left
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)

        else:
            #add data to the right
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)
    
    #print the tree in order
    def InOrderTraversal(self):
        elements = []           

        #visit the left tree
        if self.left:
            elements += self.left.InOrderTraversal() 

        #visit base node
        elements.append(self.data)

        #visit the right tree
        if self.right:
            elements += self.right.InOrderTraversal() 

        return elements

    #print the tree in post order
    def PostOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.PostOrderTraversal()
        if self.right:
            elements += self.right.PostOrderTraversal()

        elements.append(self.data)

        return elements

    #print the tree in pre order
    def PreOrderTraversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.PreOrderTraversal()
        if self.right:
            elements += self.right.PreOrderTraversal()

        return elements

    #Find the Maximum Element in the tree
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    #Find the Minimum Element in the tree
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    #Calculate the summetion of the tree elements
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum    

    #Delete element from the tree
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete(min_value)
        
        return self                

    #Search for an element in the tree                
    def search(self, value):
        if self.data == value:
            return True
        
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
            
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False        



#Helping Function tobuild the binary tree
def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root
