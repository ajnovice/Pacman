# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    # problem.getStartState()
    # problem.isGoalState(problem.getStartState())
    # problem.getSuccessors(problem.getStartState())

    frontier = util.Stack()
    start_coord = problem.getStartState()
    start_action = [ ]    # actions should be a list
    start_cost = 0
    
    # List to hold coordinates of cells visited.
    visited_list = [ ]    
    frontier.push((start_coord, start_action, start_cost))
    
    # Depth First Search Algorithm
    while(not frontier.isEmpty( )):
        n_state, n_action_list, n_cumul_cost = frontier.pop( )       
        if problem.isGoalState(n_state):
            break      
        if (n_state not in visited_list):
            visited_list.append(n_state)

            for n_succ_state, n_succ_action, n_succ_cost in problem.getSuccessors(n_state):
                if (n_succ_state not in visited_list):
                    frontier.push((n_succ_state, n_action_list + [n_succ_action], n_cumul_cost + n_succ_cost))
    
    return n_action_list

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    start_coord = problem.getStartState()
    start_action = []  # actions should be a list
    start_cost = 0
    
    # List to hold coordinates of cells visited.
    visited_list = []
    frontier = util.Stack()
    frontier.push((start_coord, start_action, start_cost))
    
    # Breadth First Search Algorithm
    while(not frontier.isEmpty()):
        n_state, n_action_list, n_cumul_cost = frontier.pop()      
        # Goal-State must go here to pass AUTOGRADER
        if problem.isGoalState(n_state):
            # Break out of while loop, no need to continue.
            break
        
        if (n_state not in visited_list):
            visited_list.append(n_state)
            
            for n_succ_state, n_succ_action, n_succ_cost in problem.getSuccessors(n_state):                    
                if (n_succ_state not in visited_list):
                    frontier.push((n_succ_state, n_action_list + [n_succ_action], n_cumul_cost + n_succ_cost))
        
    return n_action_list
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    exploredState = []
    states = util.PriorityQueue()
    states.push((start, []) ,0)
    while not states.isEmpty():
        state, n_action_list = states.pop()
        if problem.isGoalState(state):
            return n_action_list
        if state not in exploredState:
            successors = problem.getSuccessors(state)
            for succ in successors:
                coordinates = succ[0]
                if coordinates not in exploredState:
                    directions = succ[1]
                    newCost = n_action_list + [directions]
                    states.push((coordinates, n_action_list + [directions]), problem.getCostOfActions(newCost))
        exploredState.append(state)
    return n_action_list
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    exploredState = []
    states = util.PriorityQueue()
    states.push((start, []), nullHeuristic(start, problem))
    nCost = 0
    while not states.isEmpty():
        state, n_action_list = states.pop()
        if problem.isGoalState(state):
            return n_action_list
        if state not in exploredState:
            successors = problem.getSuccessors(state)
            for succ in successors:
                coordinates = succ[0]
                if coordinates not in exploredState:
                    directions = succ[1]
                    nActions = n_action_list + [directions]
                    nCost = problem.getCostOfActions(nActions) + heuristic(coordinates, problem)
                    states.push((coordinates, n_action_list + [directions]), nCost)
        exploredState.append(state)
    return n_action_list
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
