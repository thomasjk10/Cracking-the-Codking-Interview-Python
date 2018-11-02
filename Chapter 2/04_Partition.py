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

    def partition(self,val):
        current_node = self.first
        les_nodes = mynode()
        grt_nodes = mynode()
        count = 0
        while current_node:
            if current_node.data < val:
                if les_nodes.data == None:
                    les_nodes = mynode(current_node.data)
                else:
                    nxt_lesnode = mynode(current_node.data)
                    cur_lesnode = les_nodes
                    while cur_lesnode.nextptr != None:
                        cur_lesnode = cur_lesnode.nextptr
                    cur_lesnode.nextptr = nxt_lesnode

            else:
                if grt_nodes.data == None:
                    grt_nodes = mynode(current_node.data)
                else:
                    nxt_grtnode = mynode(current_node.data)
                    cur_grtnode = grt_nodes
                    while cur_grtnode.nextptr != None:
                        cur_grtnode = cur_grtnode.nextptr
                    cur_grtnode.nextptr = nxt_grtnode
            current_node = current_node.nextptr

        comb_node = les_nodes
        new_list = []
        while comb_node.nextptr != None:
            comb_node = comb_node.nextptr
        comb_node.nextptr = grt_nodes
        current_node = les_nodes
        while current_node.nextptr != None:
            current_node = current_node.nextptr
            new_list.append(current_node.data)
        return new_list


myllist = MyLinkList()
myllist.adddata_end(3)
myllist.adddata_end(5)
myllist.adddata_end(8)
myllist.adddata_end(5)
myllist.adddata_end(10)
myllist.adddata_end(2)
myllist.adddata_end(1)
myllist.displist()
print (myllist.partition(5))
