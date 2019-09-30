
# Ref https://www.youtube.com/watch?v=mK7u8wf6pMs&list=PL3pGy4HtqwD02GVgM96-V0sq4_DSinqvf&index=39
class Node:
    def __init__(self,v = None):
        self.value = v
        self.next =None

    def __str__(self):
        tempList = self
        tempListVal = self.value
        while tempList.next != None:
            tempListVal = str(tempListVal) + "," + str(tempList.next.value)
            tempList = tempList.next
        return str(tempListVal)

        return str(self.value)

    def isEmpty(self):
        return (self.value == None)

    def append (self,v2):
        if self.isEmpty():
            self.value = v2
        elif self.next == None:
            newNode = Node(v2)
            self.next = newNode
        else:
            self.next.append(v2)
        return ()

    def appendi(self,v2):
        if self.isEmpty():
            self.value = v2

        tempList = self
        while tempList.next !=None:
            tempList = tempList.next

        newNode = Node(v2)
        tempList.next = newNode
        return ()


    def insert(self,v2):
        if self.isEmpty():
            self.value = v2
        else:
            newNode = Node(v2)
            newNode.next = self.next
            self.next = newNode
            (self.value,newNode.value) =(newNode.value,self.value)

    def deleteI(self,v2):
        if self.isEmpty():
            return ()
        elif self.value == v2:
            if self.next == None:
                self.value = None
            else:
                self.value = self.next.value
                self.next = self.next.next
        else:
            pointer = self
            while pointer.next != None:
                if (pointer.next.value == v2):
                    pointer.next = pointer.next.next
                    return ()
                else:
                    pointer = pointer.next

    def deleteR(self, v2):
        if self.isEmpty():
            return ()
        elif self.value == v2:
            if self.next == None:
                self.value = None
                return ()
            else:
                self.value = self.next.value
                self.next = self.next.next
                return ()
        else:
            if self.next.value == v2:
                self.next = self.next.next
                return ()
            else:
                self.next.deleteR(v2)





Lst1 = Node(1)
print(Lst1)
Lst1.append(2)
print(Lst1)
Lst1.append(3)
print(Lst1)
Lst1.append(4)
print(Lst1)
Lst1.appendi(5)
print(Lst1)
Lst1.insert(6)
print(Lst1)

Lst1.deleteI(3)
print(Lst1)

Lst1.deleteR(2)
print(Lst1)
Lst1.deleteR(5)
print(Lst1)