class Btree: 
    def __init__ (self, value, left=None, right=None): 
        self.node = value
        self.l = left
        self.r = right

    def __repr__(self):
        return " %s  l: { %s }  r: [ %s ] " % (self.node, self.l, self.r)


