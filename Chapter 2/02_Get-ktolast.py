''' Get the kth to last element from singly linked list'''
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

    def get_knode(self, k):
        curr_node = self.first
        prev_node = self.first
        if k <= self.listsize():
            for i in range(k):
                if curr_node.nextptr != None:
                    curr_node = curr_node.nextptr
            while curr_node.nextptr != None:
                curr_node = curr_node.nextptr
                prev_node = prev_node.nextptr
            return  prev_node.data

''' Test Cases - 1 1,2  1,2,3,4  1,2,3,4,5,6,7,0,1'''

myllist = MyLinkList()
myllist.adddata_end(1)
myllist.adddata_end(2)
myllist.displist()
print (myllist.get_knode(2))
