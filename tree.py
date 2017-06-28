class tree:
    def __init__(self,value,left,right):
        self.l=left
        self.r=right
        self.v=value

treebeard=tree('stump',tree('leg','knee','foot'),tree('arm','hand','elbow'))
