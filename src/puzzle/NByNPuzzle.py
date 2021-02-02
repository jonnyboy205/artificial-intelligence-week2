'''
Created on Jan 29, 2017

@author: Jonat
'''

from puzzle import Neighbor

class NByNPuzzle():

    def buildUpNeighbor(self, indexOfZero):
        UpElementIndex = indexOfZero + self.Up
        if UpElementIndex >= 0:
            newNodeArrayUp = self.nodeArray + []
            newNodeArrayUp[indexOfZero] = self.nodeArray[UpElementIndex]
            newNodeArrayUp[UpElementIndex] = 0
            newStateUp = ""
            for newNodeUp in newNodeArrayUp:
                newStateUp += str(newNodeUp) + ","
            
            newStateUp = list(newStateUp)
            newStateUp.pop()
            newStateUp = ''.join(newStateUp)
            self._neighborsArray.append(Neighbor.Neighbor(newStateUp, "Up"))


    def buildDownNeighbor(self, indexUpperBound, indexOfZero):
        DownElementIndex = indexOfZero + self.Down
        if (DownElementIndex <= indexUpperBound):
            newNodeArrayDown = self.nodeArray + []
            newNodeArrayDown[indexOfZero] = self.nodeArray[DownElementIndex]
            newNodeArrayDown[DownElementIndex] = 0
            newStateDown = ""
            for newNodeDown in newNodeArrayDown:
                newStateDown += str(newNodeDown) + ","
            
            newStateDown = list(newStateDown)
            newStateDown.pop()
            newStateDown = ''.join(newStateDown)
            self._neighborsArray.append(Neighbor.Neighbor(newStateDown, "Down"))


    def buildLeftNeighbor(self, indexOfZero):
        LeftElementIndex = indexOfZero - 1
        if (LeftElementIndex >= (indexOfZero - (indexOfZero % self.w))):
            newNodeArrayLeft = self.nodeArray + []
            newNodeArrayLeft[indexOfZero] = self.nodeArray[LeftElementIndex]
            newNodeArrayLeft[LeftElementIndex] = 0
            newStateLeft = ""
            for newNodeLeft in newNodeArrayLeft:
                newStateLeft += str(newNodeLeft) + ","
            
            newStateLeft = list(newStateLeft)
            newStateLeft.pop()
            newStateLeft = ''.join(newStateLeft)
            self._neighborsArray.append(Neighbor.Neighbor(newStateLeft, "Left"))


    def buildRightNeighbor(self, indexOfZero):
        RightElementIndex = indexOfZero + 1
        if (RightElementIndex <= (indexOfZero - (indexOfZero % self.w) + self.w - 1)):
            newNodeArrayRight = self.nodeArray + []
            newNodeArrayRight[indexOfZero] = self.nodeArray[RightElementIndex]
            newNodeArrayRight[RightElementIndex] = 0
            newStateRight = ""
            for newNodeRight in newNodeArrayRight:
                newStateRight += str(newNodeRight) + ","
            
            newStateRight = list(newStateRight)
            newStateRight.pop()
            newStateRight = ''.join(newStateRight)
            self._neighborsArray.append(Neighbor.Neighbor(newStateRight, "Right"))

    def __init__(self, searchAlgorithm, w, h, state, parent, parentDirection, depth):
        self.w, self.h = w, h
        self.state = state
        self.parent = parent
        self.parentDirection = parentDirection
        self.depth = depth 
        
        self.Up = w * -1;
        self.Down = w; 
        self.nodeArray = state.split(",");
        self._neighborsArray = []
        indexUpperBound = self.h * self.w - 1
        
        index = 0
        indexOfZero = -1
        for nod2 in self.nodeArray:
            if (int(nod2) == 0):
                indexOfZero = index
                break
            index = index + 1
        
        orderOfVisitsPush = []
        if(searchAlgorithm == "dfs"):
            orderOfVisitsPush = ["Right", "Left", "Down", "Up"]
        else:  # bfs, ast, ida
            orderOfVisitsPush = ["Up", "Down", "Left", "Right"]
        
        for direction in orderOfVisitsPush:
            if ("Up" == direction):
                self.buildUpNeighbor(indexOfZero)
            elif("Down" == direction):
                self.buildDownNeighbor(indexUpperBound, indexOfZero)
            elif("Left" == direction):
                self.buildLeftNeighbor(indexOfZero)
            elif("Right" == direction):
                self.buildRightNeighbor(indexOfZero)
        
    def neighbors(self):
        return self._neighborsArray
    
    def __str__(self):
        return self.state
    
    def __eq__(self, other):
        return self.state == other.state
    
    def __ne__(self, other):
        return self.state != other.state
    
    def __hash__(self):
        return hash(self.state)
    
    def getParent(self):
        return self.parent
    
    def getParentDirection(self):
        return self.parentDirection
    
    def getDepth(self):
        return self.depth
    
    def getNodeArray(self):
        return self.nodeArray
    
    def getWidth(self):
        return self.w
    
    def getHeight(self):
        return self.h
