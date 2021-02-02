'''
Created on Jan 29, 2017

@author: Jonat
'''
import queue
from puzzle.NByNPuzzle import NByNPuzzle
from search.Result import Result
import time

def bfs(initialPuzzleNode, goalTest3by3):
    frontier = queue.Queue()
    frontierSet = set()
    frontier.put(initialPuzzleNode)
    frontierSet.add(initialPuzzleNode)
    maxFrontierSize = frontier._qsize()
    explored = set()
    nodesExpanded = 0
    maxDepth = 0
    while not frontier.empty():
        if (frontier._qsize() > maxFrontierSize):
            maxFrontierSize = frontier._qsize()
        state = frontier._get()
        explored.add(state)
        if state == goalTest3by3:
            return Result(state, nodesExpanded, frontier._qsize(), maxFrontierSize, maxDepth)
        else:
            nodesExpanded = nodesExpanded + 1
            if len(state.neighbors()) == 0:
                continue
            else:
                for neighbor in (state.neighbors()):
                    if len(str(neighbor)) == 0:
                        continue
                    else:
                        neighborDepth = state.getDepth() + 1
                        neighborNbyNPuzzle = NByNPuzzle("bfs", 3, 3, neighbor.getNewNode(), state, neighbor.getDirection(), neighborDepth)
                        if (neighborNbyNPuzzle not in explored) and (neighborNbyNPuzzle not in frontierSet) and (neighbor.getNewNode() is not None):
                            frontier.put(neighborNbyNPuzzle)
                            frontierSet.add(neighborNbyNPuzzle)
                            if (neighborDepth > maxDepth):
                                maxDepth = neighborDepth

def dfs(initialPuzzleNode, goalTest3by3):
    frontier = []
    frontierSet = set()
    frontier.append(initialPuzzleNode)
    frontierSet.add(initialPuzzleNode)
    maxFrontierSize = len(frontier)
    explored = set()
    nodesExpanded = 0
    maxDepth = 0
    while len(frontier) != 0:
        if (len(frontier) > maxFrontierSize):
            maxFrontierSize = len(frontier)
        state = frontier.pop()
        explored.add(state)
        if state == goalTest3by3:
            return Result(state, nodesExpanded, len(frontier), maxFrontierSize, maxDepth)
        else:
            nodesExpanded = nodesExpanded + 1
            if len(state.neighbors()) == 0:
                continue
            else:
                for neighbor in (state.neighbors()):
                    if len(str(neighbor)) == 0:
                        continue
                    else:
                        neighborDepth = state.getDepth() + 1
                        neighborNByNPuzzle = NByNPuzzle("dfs", 3, 3, neighbor.getNewNode(), state, neighbor.getDirection(), neighborDepth)
                        if (neighborNByNPuzzle not in explored) and (neighborNByNPuzzle not in frontierSet) and (neighbor.getNewNode() is not None):
                            frontier.append(neighborNByNPuzzle)
                            frontierSet.add(neighborNByNPuzzle)
                            if (neighborDepth > maxDepth):
                                maxDepth = neighborDepth

def calcManhattanDistance(initialPuzzleNode, goalTest3by3, number):
    '''get indexOfNumber in initialPuzzleNode'''
    index = 0
    indexOfNumber = -1
    for numberInIntialPuzzleNode in initialPuzzleNode.getNodeArray():
        if (numberInIntialPuzzleNode == number):
            indexOfNumber = index
            break
        else:
            index = index + 1
    indexGoal = 0
    indexOfNumberInGoal = -1
    for numberInGoalTest3by3 in goalTest3by3.getNodeArray():
        if (numberInGoalTest3by3 == number):
            indexOfNumberInGoal = indexGoal 
            break
        else:
            indexGoal = indexGoal + 1
    '''first figure out what row it's in'''
    '''then what column'''
    numberColumn = indexOfNumber % initialPuzzleNode.getWidth()
    numberRow = int((indexOfNumber - numberColumn)/initialPuzzleNode.getHeight())

    numberInGoalColumn = indexOfNumberInGoal % goalTest3by3.getWidth()
    numberInGoalRow = int((indexOfNumberInGoal - numberInGoalColumn)/goalTest3by3.getHeight())

    across = abs(numberColumn - numberInGoalColumn)
    long = abs(numberRow - numberInGoalRow)
    manhattanDistance = across + long
    
    return manhattanDistance

def aggregateManhattanDistance(initialPuzzleNode, goalTest3by3):
    manhattanDistanced = 0
    if len(initialPuzzleNode.getNodeArray()) != 0:
        for number in initialPuzzleNode.getNodeArray():
            manhattanDistanced = manhattanDistanced + calcManhattanDistance(initialPuzzleNode, goalTest3by3, number) 
    return manhattanDistanced

def priorityAst(neighborDepth, neighborNByNPuzzle, goalTest3by3, neighborDirection):
    priority = neighborDepth + aggregateManhattanDistance(neighborNByNPuzzle, goalTest3by3)
    neighborDirectionPriority = 5
    if (neighborDirection == "Up"):
        neighborDirectionPriority = 1
    elif(neighborDirection == "Down"):
        neighborDirectionPriority = 2
    elif(neighborDirection == "Left"):
        neighborDirectionPriority = 3
    elif(neighborDirection == "Right"):
        neighborDirectionPriority = 4
    priorityTriple = (priority, neighborDirectionPriority, time.time())
    return priorityTriple

def rebuildQueueByReplacingElement(priorityQueue, neighborPriorityNodeTUple):
    newPriorityQueue = queue.PriorityQueue()
    while not priorityQueue.empty():
        element = priorityQueue.get()
        if element[1] == neighborPriorityNodeTUple[1] and element[0] > neighborPriorityNodeTUple[0]:
            newPriorityQueue.put(neighborPriorityNodeTUple)
        else:
            newPriorityQueue.put(element)
    return newPriorityQueue

def ast(initialPuzzleNode, goalTest3by3):
    frontier = queue.PriorityQueue()
    frontierSet = set()
    frontier.put((aggregateManhattanDistance(initialPuzzleNode, goalTest3by3), initialPuzzleNode))
    frontierSet.add((aggregateManhattanDistance(initialPuzzleNode, goalTest3by3), initialPuzzleNode))
    maxFrontierSize = frontier._qsize()
    explored = set()
    nodesExpanded = 0
    maxDepth = 0
    while not frontier.empty():
        if (frontier._qsize() > maxFrontierSize):
            maxFrontierSize = frontier._qsize()
        state = frontier._get()            
        explored.add(state)
        stateValue = state[1]
        if stateValue == goalTest3by3:
            return Result(stateValue, nodesExpanded, frontier._qsize(), maxFrontierSize, maxDepth)
        else:
            nodesExpanded = nodesExpanded + 1
            if len(stateValue.neighbors()) == 0:
                continue
            else:
                for neighbor in (stateValue.neighbors()):
                    if len(str(neighbor)) == 0:
                        continue
                    else:
                        neighborDepth = stateValue.getDepth() + 1
                        neighborNByNPuzzle = NByNPuzzle("ast", 3, 3, neighbor.getNewNode(), stateValue, neighbor.getDirection(), neighborDepth)
                        priority = priorityAst(neighborDepth, neighborNByNPuzzle, goalTest3by3, neighbor.getDirection())
                        neighborPriorityNodeTUple = (priority, neighborNByNPuzzle)
                        if neighbor.getNewNode() is not None:
                            if (neighborNByNPuzzle not in explored) and (neighborNByNPuzzle not in frontierSet):
                                frontier.put(neighborPriorityNodeTUple)
                                frontierSet.add(neighborNByNPuzzle)
                                if (neighborDepth > maxDepth):
                                    maxDepth = neighborDepth
                            elif neighborNByNPuzzle in frontierSet:
                                frontier = rebuildQueueByReplacingElement(frontier, neighborPriorityNodeTUple)

def astDepthLimit(initialPuzzleNode, goalTest3by3, depthLimit):
    frontier = queue.PriorityQueue()
    frontierSet = set()
    frontier.put((aggregateManhattanDistance(initialPuzzleNode, goalTest3by3), initialPuzzleNode))
    frontierSet.add((aggregateManhattanDistance(initialPuzzleNode, goalTest3by3), initialPuzzleNode))
    maxFrontierSize = frontier._qsize()
    explored = set()
    nodesExpanded = 0
    maxDepth = 0
    while not frontier.empty():
        if (frontier._qsize() > maxFrontierSize):
            maxFrontierSize = frontier._qsize()
        state = frontier._get()            
        explored.add(state)
        stateValue = state[1]
        if stateValue == goalTest3by3:
            return Result(stateValue, nodesExpanded, frontier._qsize(), maxFrontierSize, maxDepth)
        else:
            nodesExpanded = nodesExpanded + 1
            if len(stateValue.neighbors()) == 0:
                continue
            else:
                for neighbor in (stateValue.neighbors()):
                    if len(str(neighbor)) == 0:
                        continue
                    else:
                        neighborDepth = stateValue.getDepth() + 1
                        neighborNByNPuzzle = NByNPuzzle("ida", 3, 3, neighbor.getNewNode(), stateValue, neighbor.getDirection(), neighborDepth)
                        priority = priorityAst(neighborDepth, neighborNByNPuzzle, goalTest3by3, neighbor.getDirection())
                        neighborPriorityNodeTUple = (priority, neighborNByNPuzzle)
                        if neighbor.getNewNode() is not None and neighborDepth <= depthLimit:
                            if (neighborNByNPuzzle not in explored) and (neighborNByNPuzzle not in frontierSet):
                                frontier.put(neighborPriorityNodeTUple)
                                frontierSet.add(neighborNByNPuzzle)
                                if (neighborDepth > maxDepth):
                                    maxDepth = neighborDepth
                            elif neighborNByNPuzzle in frontierSet:
                                frontier = rebuildQueueByReplacingElement(frontier, neighborPriorityNodeTUple)
    return None
    
def ida(initialPuzzleNode, goalTest3by3):
    depth = -1
    returnValue = None
    while True:
        depth = depth + 1
        returnValue = astDepthLimit(initialPuzzleNode, goalTest3by3, depth)
        if (returnValue is not None):
            break
    return returnValue

def buildPath(goal):
    backwardsPathToGoalArray = []
    currentNode = goal
    cost = 0
    while (not (currentNode is None)):
        if not(currentNode.getParentDirection() is None):
            backwardsPathToGoalArray.append(str(currentNode.getParentDirection()))
            cost = cost + 1
        currentNode = currentNode.getParent()
    pathToGoalArray = []
    backwardsPathToGoalArray.reverse()
    for backwardsNode in backwardsPathToGoalArray:
        pathToGoalArray.append(backwardsNode)
    backwardsPathToGoal = '\'' + '\', \''.join(pathToGoalArray) + '\''
    return "[" + backwardsPathToGoal + "]"
