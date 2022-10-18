#
# state.py (Final project)
#
# A State class for the Eight Puzzle
#
# name: 
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

from board import *

# the list of possible moves, each of which corresponds to
# moving the blank cell in the specified direction
MOVES = ['up', 'down', 'left', 'right']

class State:
    """ A class for objects that represent a state in the state-space 
        search tree of an Eight Puzzle.
    """
    ### Add your method definitions here. ###
        

    def __repr__(self):
        """ returns a string representation of the State object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = self.board.digit_string() + '-'
        s += self.move + '-'
        s += str(self.num_moves)
        return s
    
    def creates_cycle(self):
        """ returns True if this State object (the one referred to
            by self) would create a cycle in the current sequence of moves,
            and False otherwise.
        """
        # You should *NOT* change this method.
        state = self.predecessor
        while state != None:
            if state.board == self.board:
               return True
            state = state.predecessor
        return False

    def __gt__(self, other):
        """ implements a > operator for State objects
            that always returns True. This will be needed to break
            ties when we use max() on a list of [priority, state] pairs.
            If we don't have a > operator for State objects,
            max() will fail with an error when it tries to compare
            two [priority, state] pairs with the same priority.
        """
        # You should *NOT* change this method.
        return True
    
    
    
    
    
    def __init__(self, board, predecessor, move):
        """ constructs a new State object by initializing the following four
        fields/attributes:an attribute board that stores a reference to the
        Board object associated with this state, as specified by the
        parameter board an attribute predecessor that stores a reference
        to the State object that comes before this state in the current
        sequence of moves, as specified by the parameter predecessor, an 
        attribute move that stores a string representing the move that was
        needed to transition from the predecessor state to this state, 
        as specified by the parameter move
        an attribute num_moves that stores an integer representing
        the number of moves that were needed to get from the initial
        state (the state at the root of the tree) to this state. 
        If predecessor is None–which means that this new state is 
        the initial state–then num_moves should be initialized to 0. 
        Otherwise, it should be assigned a value that is one more
        that the number of moves for the predecessor state."""
        
        self.num_moves = 0 
        self.board  = board
        self.move = move
        self.predecessor = predecessor
        if self.predecessor != None:
            self.num_moves += self.predecessor.num_moves + 1
        else:
            self.num_moves = 0
    


    def is_goal(self):
        """ returns True if the called State object is a goal
        state, and False otherwise."""
        if self.board.num_misplaced() == 0:
            return True 
        else:
            return False
    
    
    def generate_successors(self):
        """creates and returns a list of State objects for all successor
        states of the called State object. We discussed the concept of
        successor states in lecture."""
        successors = []    
        for x in MOVES:
            the_copy = self.board.copy()
            the_move = the_copy.move_blank(x)
            #look over this 
            if the_move:
                y = State(the_copy, self, x)
                successors += [y] 
        return successors

    def print_moves_to(self):
        """prints the sequence of moves that lead from the initial state to
        the called State object (i.e., to self). """
        if self.predecessor == None:
            print('initial state:')
            print(self.board)
           
        else:
            self.predecessor.print_moves_to()
            print('move the blank ' + str(self.move) + ':')
            print(self.board)
            
    def helper(self):
        """a helper method that will be used for h2"""
        for x in range(len(self.board)):
            for y in range(len(self.board[0])):
                
                #use % to find colm
                #use // to find row 
  
    
  
#print self.move
    
    
    
    
    
    
