class Btree: 
    def __init__ (self, value, left=None, right=None):
        self.node = value
        self.l = left
        self.r = right

    def __repr__ (self):
        return " %s  l: { %s }  r: [ %s ] " % (self.node, self.l, self.r)


'''
    def Ladd(self, tree):
        if not isinstance(tree, Btree):
            return "can only add trees"
        elif self.l != None:
            return "Node is full"
        else:
            self.l = tree
    
    def Radd(self, tree):
        if not isinstance(tree, Btree):
            return "can only add trees"
        elif self.r != None:
            return "Node is full"
        else:
            self.r = tree
'''


        #want to have left and right be of type/class btree or bnode. 

node1 = Btree(1)
node2 = Btree(2)
Tree1 = Btree(0, node1, node2) 
# note to self: python isn't immutable. 
# furthermore: modifying Tree1's children modifies node1 / node 2, not just Tree1. 
# OKAY. so. Radd and Ladd change the tree. 
# I do want them to be that way, but This way they don't return anything, 
# and if I want to make a Tree that is a modified version of another tree then
# I can't use the add functions because they modify the tree.
# wtfffff?????F?F?F?
# ok  I guess I'll have to part with the "having a Method that changes the tree" idea?
# or I could just... no... omfg... making a tree based off another three willmean modifying that tree will modify the other tree... I'm not giving up on the idea of THAT. 

