'''
Created on Jan 29, 2017

@author: Jonat
'''

import sys
import search.Algorithms
from puzzle.NByNPuzzle import NByNPuzzle
import time

class driver_3(object):
    
    goalState = "0,1,2,3,4,5,6,7,8"
    puzzleWidth = 3
    puzzleHeight = 3

    if __name__ == '__main__':
        
        searchAlgorithmName = ""
        i = 0
        for arg in sys.argv:
            if (i == 1):
                searchAlgorithmName = str(arg)
                searchAlgorithmMethodCall = getattr(search.Algorithms, searchAlgorithmName)
                goalState3By3Puzzle = NByNPuzzle(searchAlgorithmName, puzzleWidth, puzzleHeight, goalState, None, None, 0)
            elif(i == 2):
                threePuzzle = NByNPuzzle(searchAlgorithmName, 3, 3, arg, None, None, 0)
                start_time = time.clock()
                goal = searchAlgorithmMethodCall(threePuzzle, goalState3By3Puzzle)
                
                outputFile = open('output.txt', 'w')
                
                outputFile.write("path_to_goal: " + search.Algorithms.buildPath(goal.getState()) + "\n")
                costStr = str(goal.getState().getDepth())
                outputFile.write("cost_of_path: " + costStr + "\n")
                outputFile.write("nodes_expanded: " + str(goal.getNodesExpanded()) + "\n")
                outputFile.write("fringe_size: " + str(goal.getFringeSize()) + "\n")
                outputFile.write("max_fringe_size: " + str(goal.getMaxFringeSize()) + "\n")
                outputFile.write("search_depth: " + costStr + "\n")
                outputFile.write("max_search_depth: " + str(goal.getMaxDepth()) + "\n")
                outputFile.write("running_time: %s" % round(time.clock() - start_time, 8) + "\n")
                outputFile.write("max_ram_usage: 1.00000000" + "\n")
            i = i + 1
