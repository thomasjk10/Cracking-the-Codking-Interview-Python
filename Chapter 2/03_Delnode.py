''' Remove a node from a linked list'''

class mynode:

    def __init__(self,data=None):
        self.data = data
        self.nextptr = None

class MyLinkList:

    def __init__(self):
        self.first = mynode()

    def displist(self):
        listall = []
        curr_node = self.first
        if curr_node.data == None:
            return print(listall)
        while curr_node:
            listall.append(curr_node.data)
            curr_node = curr_node.nextptr
        print (listall)

    def listsize(self):
        total = 0
        curr_node = self.first
        if curr_node.data == None:
            return total
        while curr_node.nextptr !=None:
            total = total +1
            curr_node = curr_node.nextptr
        return (total +1)

    def adddata_end(self,data):
        if self.first.data == None:
            self.first = mynode(data)
            curr_node = self.first
            new_node = curr_node.nextptr
        else:
            new_node = mynode(data)
            curr_node = self.first
        while curr_node.nextptr!= None:
            curr_node = curr_node.nextptr
        curr_node.nextptr = new_node

    def deldata_val(self,val):
        size = self.listsize()
        curr_node = self.first
        prev_node = self.first
        if curr_node.data == None:
            return (print("Linked list already empty. Cannot perform delete"))

        if size == 1:
            if curr_node.data == val:
                self.first = mynode()
                return (print("Removed 1 Item. Now Linked List has no data"))
            else:
                return (print("Data {} to be removed not found in list".format(val)))

        while True:
            if curr_node.data == val:
                prev_node.nextptr = curr_node.nextptr
                return (print("{} removed successfully".format(val)))
            prev_node = curr_node
            curr_node = curr_node.nextptr
            if curr_node.nextptr == None:
                return (print("Data {} to be removed not found in list".format(val)))

myllist = MyLinkList()
myllist.adddata_end(5)
myllist.adddata_end(4)
myllist.adddata_end(6)
myllist.adddata_end(3)
myllist.displist()
myllist.deldata_val(4)
myllist.displist()
