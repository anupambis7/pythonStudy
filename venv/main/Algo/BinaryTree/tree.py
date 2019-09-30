
class Tree:
    def __init__(self,initial=None):
        self.value =initial
        if self.value:
            self.left_node = Tree()
            self.right_node = Tree()
        else:
            self.left_node = None
            self.right_node = None

    def isEmpty(self):
        return (self.value == None)

    def inOrder(self):
        if self.value == None:
            return([])
        else:
            return (self.left_node.inOrder() + [self.value] + self.right_node.inOrder())

    def insert(self,v):
        if self.isEmpty():
            self.value = v
            self.left_node =Tree()
            self.right_node = Tree()
        elif v > self.value :
            self.right_node.insert(v)
            return
        else:
            self.left_node.insert(v)
            return


    def find(self,v):
        if self.isEmpty():
            return("Not Found")
        elif self.value == v:
            return(True)
        elif  v > self.value :
            return(self.right_node.find(v))
        else:
            return(self.left_node.find(v))

    def findMinR(self):
         if self.left_node.isEmpty():
             return(self.value)
         else:
            return(self.left_node.findMinR())

    def findMaxR(self):
         if self.right_node.isEmpty():
             return(self.value)
         else:
            return(self.right_node.findMaxR())


    def findMinI(self):
        if self.isEmpty():
            return("Empty Tree")
        else:
            tempVal = self
            while (tempVal.left_node.isEmpty() != True):
                tempVal =tempVal.left_node
            return(tempVal.value)

########### DELETE VALUE ##############
    def delete(self,v):

        def isLeaf(self):
            if self.right_node.isEmpty() and self.left_node.isEmpty():
                return(True)
            else:
                return(False)
        def deleteNode(self):
            self.value = None
            self.right_node = None
            self.left_node = None


        if self.isEmpty():
            return
        elif v < self.value:
            return (self.left_node.delete(v))
        elif v > self.value:
            return (self.right_node.delete(v))
        else:
            if isLeaf(self):
                deleteNode(self)
            else:
                return

    def __str__(self):
        return (str(self.inOrder()))








t =Tree(9)
# Insert values
t.insert(8)
t.insert(2)
t.insert(5)
t.insert(10)
print(t)
# Find values
print(t.find(9))
print(t.find(10))
# Find Min values
print(t.findMinI())
print(t.findMinR())

# Find Max values
print(t.findMaxR())

t.delete(10)
print(t)