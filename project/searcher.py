#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: 
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###

    def __init__(self, depth_limit):
         """constructs a new Searcher object by initializing the 
         following attributes: an attribute states for the Searcher‘s
         list of untested states; it should be initialized to an empty list
         an attribute num_tested that will keep track of how many states the
         Searcher tests; it should be initialized to 0, an attribute
         depth_limit that specifies how deep in the state-space
         search tree the Searcher will go; it should be initialized 
         to the value specified by the parameter depth_limit. 
         (A depth_limit of -1 will be used to indicate that 
          the Searcher does not use a depth limit.) """
         self.states = []
         self.num_tested = 0
         self.depth_limit = depth_limit


    def add_state(self, new_state):
        """takes a single State object called new_state and adds it to 
        the Searcher‘s list of untested stXates. This method should
        only require one line of code! It should not return a value. """
        self.states.append(new_state)
        #append() its the same thing as +=
        
    def should_add(self, state):
        """takes a State object called state and returns True if the
        called Searcher should add state to its list of untested states, 
        and False otherwise. """
        if self.depth_limit != -1 and state.num_moves > self.depth_limit:
            return False
        
        elif state.creates_cycle() == True:
            return False 
        else:
            return True
        
        
    def  add_states(self, new_states):
        """takes a list State objects called new_states, and that processes 
        the elements of new_states one at a time as follows: If a given state 
        s should be added to the Searcher‘s list of untested states (because s 
        would not cause a cycle and is not beyond the Searcher‘s depth limit), 
        the method should use the Searcher‘s add_state() method to add s to 
        the list of states. If a given state s should not be added to the 
        Searcher object’s list of states, the method should ignore the state.
        This method should not return a value."""
        for x in new_states:
            if self.should_add(x) == True:
                self.add_state(x)

    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s        


    def find_solution(self, init_state):
        """performs a full state-space search that begins at the specified
        initial state init_state and ends when the goal state is found or when
        the Searcher runs out of untested states. The searcher should begin
        by adding init_state to its list of states. Make sure to use
        the existing add_state() method to do so. If the searcher finds a
        goal state, it should return it. If the searcher runs out of
        untested states before finding a goal state, it should return
        the special keyword None. (Note that there should not be any
        quotes around None, because it is not a string.) The method should 
        increment the Searcher object’s num_tested attribute every time that
        it tests a state to see if it is the goal."""
        self.add_state(init_state)
        while len(self.states) != 0:
            self.num_tested += 1
            s = self.next_state()
            if s.is_goal() == True:
                return s
            else:
                x = s.generate_successors()
                self.add_states(x)

        return None

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s


### Add your BFSeacher and DFSearcher class definitions below. ###

class BFSearcher(Searcher):
    """or searcher objects that perform breadth-first search (BFS) instead
    of random search. As discussed in lecture, BFS involves always choosing
    one the untested states that has the smallest depth (i.e., the smallest
    number of moves from the initial state)."""

    def next_state(self):
        """overrides (i.e., replaces) the next_state method that is
        inherited from Searcher. Rather than choosing at random from the list
        of untested states, this version of next_state should follow FIFO
        (first-in first-out) ordering – choosing the state that has been
        in the list the longest.  """
        p = self.states[0]
        self.states.remove(p)
        return p    
                
class DFSearcher(Searcher):
    """for searcher objects that perform depth-first search (DFS) instead of
    random search. As discussed in lecture, DFS involves always choosing
    one the untested states that has the largest depth (i.e., the largest
    number of moves from the initial state).DFS, the next state to be tested
    should be one of the ones that has the largest depth in the state-space
    search tree."""
    
    def next_state(self):
        """follows LIFO (last-in first-out) ordering – choosing the state
        that was most recently added to the list. """
        q = self.states[-1]
        self.states.remove(q)
        return q    

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0


    ### Add your other heuristic functions here. ###
def h1(state):
    """ a heuristic function that returns the number of misplaced tiles"""
    return state.board.num_misplaced()

def h2(state):
    """this heurisgic function doees basically this h2 = (# of tiles in wrong row) + (# of tiles in wrong column) to determine priority"""
    


class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###

    def  __init__(self, heuristic):
        """constructs a new GreedySearcher object. The constructor should begin
        by calling the constructor inherited from the superclass; this will 
        allow that superclass constructor to initialize the inherited attributes.
        Use the super() function to access the __init__ method in the superclass 
        (as we did in the constructor for the Holiday class from lecture), 
        and pass in a value of -1 to indicate that GreedySearcher objects 
        will not use a depth limit."""
        super().__init__ (-1)
        self.heuristic = heuristic
        
        
        
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)


    def add_state(self, state):
         """overrides (i.e., replaces) the add_state method that is inherited
         from Searcher. Rather than simply adding the specified state to the
         list of untested states, the method should add a sublist that is a
         [priority, state] pair, where priority is the priority of state
         that is determined by calling the priority method. Pairing each
         state with its priority will allow a GreedySearcher to choose its
         next state based on the priorities of the states. """
         x = [[self.priority(state), state]]   
         self.states += x 
              
     
    def next_state(self):
         """overrides (i.e., replaces) the next_state method that is inherited
         from Searcher. This version of next_state should choose one of the
         states with the highest priority. """
         c = max(self.states)
         self.states.remove(c)
         return c[1]

         

        
    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s


### Add your AStarSeacher class definition below. ###



class AStarSearcher(Searcher):
    """for searcher objects that perform A* search. Like greedy search, A*
    is an informed search algorithm that assigns a priority to each state 
    based on a heuristic function, and that selects the next state based 
    on those priorities. However, when A* assigns a priority to a state, it
    also takes into account the cost that has already been expended to get 
    to that state (i.e. the number of moves to that state). More specifically,
    the priority of a state is computed using the following pseudocode: """
    
    def  __init__(self, heuristic):
        """assigns a priority to a state, it also takes into account the
        cost that has already been expended to get to that state (i.e.
        the number of moves to that state). """
        self.heuristic = heuristic
        #state = State(board, None, 'init')
        return (self.heuristic(state) + state.num_moves) * -1
#i thnk theres something wrong with my num moves














