'''
Created on Feb 1, 2017

@author: Jonat
'''

class Neighbor(object):

    def __init__(self, newNode, direction):
        self.newNode = newNode
        self.direction = direction

    def getNewNode(self):
        return self.newNode
    
    def getDirection(self):
        return self.direction