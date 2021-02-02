'''
Created on Feb 6, 2017

@author: Jonat
'''

class Result(object):

    def __init__(self, state, nodesExpanded, fringeSize, maxFringeSize, maxDepth):
        self.state = state
        self.nodesExpanded = nodesExpanded
        self.fringeSize = fringeSize
        self.maxFringeSize = maxFringeSize
        self.maxDepth = maxDepth
    
    def getState(self):
        return self.state
    
    def getNodesExpanded(self):
        return self.nodesExpanded
    
    def getFringeSize(self):
        return self.fringeSize
    
    def getMaxFringeSize(self):
        return self.maxFringeSize

    def getMaxDepth(self):
        return self.maxDepth