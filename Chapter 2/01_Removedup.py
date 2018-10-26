''' Remove duplicates from unsorted linked list'''
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

    def remove_node(self,node):
        curr_node = self.first
        while (curr_node and curr_node.nextptr != node):
            curr_node = curr_node.nextptr
        if curr_node == None:
            self.first = self.first.nextptr
        else:
            curr_node.nextptr = node.nextptr

    def rem_dups(self):
        curr_node = self.first
        while curr_node:
            val = curr_node.data
            next_node = curr_node.nextptr
            while next_node:
                if next_node.data == val:
                    self.remove_node(next_node)
                next_node = next_node.nextptr
            curr_node = curr_node.nextptr

''' Test Cases - 1,4,4,1  5,5,5,3  1,2,3,4,5,6,7,0,1'''

myllist = MyLinkList()
myllist.adddata_end(1)
myllist.adddata_end(0)
myllist.adddata_end(2)
myllist.adddata_end(5)
myllist.adddata_end(6)
myllist.adddata_end(1)
myllist.adddata_end(2)
myllist.displist()
myllist.rem_dups()
myllist.displist()
