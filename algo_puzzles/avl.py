#AVL Tree Written by Zachary Rougeau

#/**************************************************the AVL Tree's tree node************************************************/
class TreeNode:
   def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#/*******************************************************************AVL Tree Class ***************************************/
class AVL_Tree:
    def __init__(self):
        self.root=None

    def insert(self,value):
        if(self.root is None):
            self.root=TreeNode();
            self.root.val=value
        else:
            self.root=self.insertIntoTree(self.root, value)

            if (self.height(self.root.left) - self.height(self.root.right) > 1):
                if (self.height(self.root.left.right)-self.height(self.root.left.left)>0):
                    self.root = self.leftRightRotation(self.root)
                else:
                    self.root=self.rotateRight(self.root)

            elif (self.height(self.root.right) - self.height(self.root.left) > 1):
                if (self.height(self.root.right.left)-self.height(self.root.right.right)>0):
                    self.root = self.rightLeftRotation(self.root)
                else:
                    self.root = self.rotateLeft(self.root)


    def insertIntoTree(self,node,value):
        newRoot = None
        if(node.left is None and value <=node.val):
            newNode=TreeNode()
            node.left=newNode
            node.left.val=value
            return node

        elif (node.right is None and value > node.val):
            newNode = TreeNode()
            node.right = newNode
            node.right.val=value
            return node
        else:
            if(value<=node.val):
                node.left=self.insertIntoTree(node.left,value)
                if (self.height(node.left) - self.height(node.right) > 1):
                    if (self.height(node.left.right)-self.height(node.left.left)>0):
                        return self.leftRightRotation(node)
                    else:
                        return self.rotateRight(node)


                elif (self.height(node.right) - self.height(node.left) > 1):
                    if (self.height(node.right.left)-self.height(node.right.right) > 0):
                        return self.rightLeftRotation(node)
                    else:
                        return self.rotateLeft(node)
                return node;
            else:
                node.right=self.insertIntoTree(node.right, value)
                if (self.height(node.right) - self.height(node.left) > 1):

                    if (self.height(node.right.left)-self.height(node.right.right) > 0):
                        return self.rightLeftRotation(node)
                    else:
                        return self.rotateLeft(node)
                elif (self.height(node.left) - self.height(node.right) > 1):
                    if (self.height(node.left.right) - self.height(node.left.left) > 0):
                        return self.leftRightRotation(node)
                    else:
                        return self.rotateRight(node)
                return node;

    def print(self):
        self.printTree(self.root)

    def printTree(self,node):

        print(node.val)

        if(node.left is not None):
            self.printTree(node.left)

        if(node.right is not None):
            self.printTree(node.right)

#Get's the height of the tree
    def getHeight(self,node):

        if(node.left is None and node.right is None):
            return 1;
        else:
            if(node.left is not None and node.right is not None):
                return max(self.getHeight(node.left),self.getHeight(node.right))+1
            if(node.left is not None):
                return self.getHeight(node.left)+1
            if (node.right is not None):
                return self.getHeight(node.right)+1

#Call Height Method from outside of the class
    def height(self,node):
        if(node is None):
            return 0
        else:
            return self.getHeight(node)


#/********************************AVL TREE: Rotations********************************************/

    def rotateRight(self,p_node):

        a_node=p_node.left
        p_node.left=a_node.right
        a_node.right=p_node

        return a_node

    def rotateLeft(self,p_node):

        a_node=p_node.right
        p_node.right=a_node.left
        a_node.left=p_node

        return a_node

    def testRotateLeft(self,node):

        self.root=self.rotateLeft(node)

    #https://www.tutorialspoint.com/data_structures_algorithms/avl_tree_algorithm.htm
    #https://www.guru99.com/avl-tree.html
    #https://www.youtube.com/watch?v=kdfxT8ed4Ww
    def leftRightRotation(self,c_node):

        #Step 1: assign a and b nodes to c node
        a_node=c_node.left
        b_node=c_node.left.right

        #Step 2: Connect the trees
        c_node.left=b_node
        a_node.right=b_node.left
        b_node.left=a_node

        #Step 3: Perform a right rotation
        newRootNode=self.rotateRight(c_node)

        return newRootNode



        return a_node

    #https://www.tutorialspoint.com/data_structures_algorithms/avl_tree_algorithm.htm
    #https://www.guru99.com/avl-tree.html
    def rightLeftRotation(self,a_node):

        #Step 1: assign b and c nodes to a node
        c_node=a_node.right
        b_node=a_node.right.left

        #Step 2: Connect the trees
        a_node.right=b_node
        c_node.left=b_node.right
        b_node.right=c_node

        #Step 3: Perform a right rotation
        newRootNode=self.rotateLeft(a_node)
        return newRootNode



        return a_node

#/****************************************************** Test Cases ****************************************/

if __name__ == '__main__':
    print("Main")

    tree=AVL_Tree();


    #Tree example 1:

    #tree.insert(70)
    #tree.insert(40)
    #tree.insert(20)

    #tree.insert(60)
    #tree.insert(80)
    #tree.insert(55)
    #tree.insert(85)
    #tree.insert(10)
    #tree.insert(15)
    #tree.insert(5)

    # Tree example 2:
    #tree.insert(4)
    #tree.insert(2)
    #tree.insert(10)

    #tree.insert(12)
    #tree.insert(8)
    #tree.insert(9)

    #Tree example 3:

    #tree.insert(13)
    #tree.insert(10)
    #tree.insert(15)
    #tree.insert(5)
    #tree.insert(11)
    #tree.insert(16)
    #tree.insert(4)
    #tree.insert(8)
    #insert 3
    #tree.insert(3)

    #Tree Example 4:
    #tree.insert(30)
    #tree.insert(5)
    #tree.insert(35)
    #tree.insert(32)
    #tree.insert(40)
    #insert 45
    #tree.insert(45)

    #Tree Example 5:

    #tree.insert(13)
    #tree.insert(10)
    #tree.insert(15)
    #tree.insert(5)
    #tree.insert(11)
    #tree.insert(16)
    #tree.insert(4)
    #tree.insert(6)
    #insert 7
    #tree.insert(7)

    #Tree Example 6:

    tree.insert(5)
    tree.insert(2)
    tree.insert(7)
    tree.insert(1)
    tree.insert(4)
    tree.insert(6)
    tree.insert(9)
    tree.insert(3)
    tree.insert(16)
    #insert 15
    tree.insert(15)

    tree.print();
