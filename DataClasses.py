class Btree: 
    def __init__ (self, value, left=None, right=None):
        self.v = value  # change labels, I don't like this being called self.node; make it self.v
        self.l = left
        self.r = right

    def __repr__ (self):
        return " %s l: { %s }  r: [ %s ] " % (self.v, self.l, self.r)


#    def span(tree):
#        if nul tree: 
    def locate (self, location):
        if location == []:
            print("A")
            if self == None:
                print("AA")
                return "end node"
            else:
                print("AB", self.v)
                return self.v
        elif self == None:
            print("Z")
            return "out of tree"
        elif location[0]==0:
            print("B")
            (self.l).locate (location[1:])
        elif location[0]==1:
            print("C")
            (self.r).locate (location[1:])
        else: 
            print("uh, trouble?:" , tree, location)


   # def addNode(self, location, tree):
        #if 


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



        #want to have left and right be of type/class btree or bnode. 

node1 = Btree(1)
node2 = Btree(2)
Tree1 = Btree(0, node1, node2) 
Tree2 = Btree(-1, Tree1, Tree1)
print(Tree2)
print(Tree2.locate([]) ) 
print(Tree2.locate([0]) )
print(Tree2.locate([1]) )
print(Tree2.locate([0,1]) )
print(Tree2.locate([1,0]) )
# note to self: python isn't immutable. 
# furthermore: modifying Tree1's children modifies node1 / node 2, not just Tree1. 
# OKAY. so. Radd and Ladd change the tree. 
# I do want them to be that way, but This way they don't return anything, 
# and if I want to make a Tree that is a modified version of another tree then
# I can't use the add functions because they modify the tree.
# wtfffff?????F?F?F?
# ok  I guess I'll have to part with the "having a Method that changes the tree" idea?
# or I could just... no... omfg... making a tree based off another three willmean modifying that tree will modify the other tree... I'm not giving up on the idea of THAT. 
# ok so I need to clarify what the problem is. or rather what my goal is. i want to make binary trees because they give a nice way to store data in that you can access it with a bunch of ls and rs, and giving it extra structure will make it even nicer. 
# first it needs the basic properties of a data struct. repr, "append", :, map, head, tail, !!, 
# I think for now I'm just gonna try to make it so that I can add the contents of a tree to another without modifications in the first tree affecting the second one. also want a proper representation. The method I have in mind is with recursion. 



