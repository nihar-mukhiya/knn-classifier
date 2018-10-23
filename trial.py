# author : NIHAR MUKHIYA
# date : 18/09/2018
# description : implementation of various operations of BST such as
#               insertion, deletion, max-min value, parent-of-a-node, inorder, preorder, postorder
#               in python


import  sys
class Node(object):
    def __init__(self, val):
        self.rc = None
        self.lc = None
        self.val = val

    def insert(self, val):
        if(self.val):
            if(val<self.val):
                if(self.lc is None):
                    self.lc = Node(val)
                else:
                    self.lc.insert(val)
            elif(val>self.val):
                if(self.rc is None):
                    self.rc = Node(val)
                else:
                    self.rc.insert(val)
            else:
                self.val = val

    def minValue(self, node):
        current = node
        while(current.lc is not None):
            current = current.lc
        return current

    def children_count(self):
        cnt = 0
        if self.lc:
            cnt += 1
        if self.rc:
            cnt += 1
        return cnt

    def findParent(self, val):
        parent = None
        while True:
            if(self.val is None):
                return (None, None)
            if(self.val == val):
                return (parent, self)
            if(self.val < val):
                parent, self = self, self.rc
            else:
                parent, self = self, self.lc

    def deleteNode(self):
        g = int(input("Enter the element you want to delete:\n"))
        parent, node = self.findParent(g)
        if node is not None:
            global children_count
            children_count = node.children_count()
        # if node has no children
        if children_count == 0:
            if parent:
                if parent.lc is node:
                    parent.lc = None
                else:
                    parent.rc = None
                del node
            else:
                self.val = None

        elif children_count == 1:
            if node.lc:
                g = node.lc
            else:
                g = node.rc
            if parent:
                if parent.lc is node:
                    parent.lc = g
                else:
                    parent.rc = g
                del node
            else:
                self.lc = g.lc
                self.rc = g.rc
                self.val = g.val

        else:
            parent = node
            successor = node.rc
            while successor.lc:
                parent = successor
                successor = successor.lc
            node.val = successor.val
            if parent.lc == successor:
                parent.lc = successor.rc

            else:
                parent.rc = successor.rc



    def inorder(self):
            if(self.lc):
                self.lc.inorder()
            print(self.val)
            if(self.rc):
                self.rc.inorder()


    def preorder(self):
        print(self.val)
        if (self.lc):
            self.lc.preorder()
        if (self.rc):
            self.rc.preorder()

    def postorder(self):
        if (self.lc):
            self.lc.postorder()
        if (self.rc):
            self.rc.postorder()
        print(self.val)



a = int(input("enter root"))
root = Node(a)



while(1):
    z = input("Enter your choice\n 1. Insert\n2.smallest element\n 3. Inorder\n 4. Preorder\n 5. Postorder\n 6.Delete\n7. Exit\n")
    if (z == '1'):
        b = int(input("enter the number of elements to be inserted"))
        while (b > 0):
            c = int(input("enter elements: "))
            root.insert(c)
            b -= 1

    elif(z == '2'):
        y = root.minValue(root)
        print("The smallest element in BST is: " +str(y)+ "/n")

    elif (z == '3'):
        print("INORDER is: ")
        root.inorder()

    elif(z== '4'):
        print("PREORDER is: ")
        root.preorder()

    elif(z=='5'):
        print("POSTORDER is: ")
        root.postorder()

    elif(z == '6'):
        v = root.deleteNode()
        root.inorder()


    elif(z=='7'):
        sys.exit()



    else:
        print("wrong input!!")

"""
OUTPUT:

enter root5
Enter your choice
 1. Insert
2.smallest element
 3. Inorder
 4. Preorder
 5. Postorder
 6.Delete
7. Exit
1
enter the number of elements to be inserted4
enter elements: 6
enter elements: 4
enter elements: 3
enter elements: 2

enter element to be deleted: 5

INORDER is: 
2
3
4


"""