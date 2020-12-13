class Node: 

    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

def maxHeight(node): 
    if node is None: 
        return 0 ;  
  
    else : 
  
        lHeight = maxHeight(node.left) 
        rHeight = maxHeight(node.right) 
  
        if (lHeight > rHeight): 
            return lHeight+1
        else: 
            return rHeight+1

root = Node(1);  
root.left = Node(2);  
root.right = Node(3);  
root.left.left = Node(4);  
root.right.left = Node(5);  
root.right.right = Node(6);  
root.right.right.right= Node(7);  
root.right.right.right.right = Node(8); 
  
  
print ("Lartësia: %d" %(maxHeight(root))) 