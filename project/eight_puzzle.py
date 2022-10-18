#
# eight_puzzle.py (Final project)
#
# driver/test code for state-space search on Eight Puzzles   
#
# name: 
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

from searcher import *
from timer import *

def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
## You will uncommment the following lines as you implement
## other algorithms.
    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
#what does try do?
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()
            
            
            
            
            
            
def process_file(filename, algorithm, param):
    """ It should take the following three inputs: a string filename specifying
     the name of a text file in which each line is a digit string for an eight
     puzzle. For example, here is a sample file containing 10 digit strings,
     each of which represents an eight puzzle that can be solved in 10 moves:
     10_moves.txt a string algorithm that specifies which state-space search
     algorithm should be used to solve the puzzles ('random', 'BFS', 'DFS', 
     'Greedy', or 'A*'), a third input param that allows you to specify a 
     parameter for the searcher – either a depth limit (for the uninformed 
     search algorithms) or a choice of heuristic function (for the informed 
     search algorithms).Your function should open the file with the specified 
     filename for reading, and it should use a loop to process the file one line 
     at a time. We discussed line-by-line file processing earlier in the semester.
     """
    file = open(filename, 'r')
    num_moves = 0
    num_states_tested = 0
    num_puzzles_solved = 0

       
  
    for x in file: 
        x = x[:-1]
        board = Board(x)
        searcher = create_searcher(algorithm,param)
        state = State(board, None, 'init')
        soln = None
        try:
            soln = searcher.find_solution(state)
        except KeyboardInterrupt:
            print('search terminated, ', end='')
        if soln == None:
            print(x + ':' + ' no solution')
        else:
            num_puzzles_solved += 1
            num_moves += state.num_moves 
            #if state.predecessor != None:
                #state.num_moves += state.predecessor.num_moves + 1
            #else:
                #state.num_moves = 0
            num_states_tested += searcher.num_tested
            print(x + ': ' + str(state.num_moves) + ' moves' + ', ' + str(searcher.num_tested) + ' states tested')
    if num_puzzles_solved != 0:    
        print()
        print('solved ' + str(num_puzzles_solved) + ' puzzles')
        print('averages: ' + str(num_moves/num_puzzles_solved) + ' moves, ' + str(num_states_tested/num_puzzles_solved) + ' states tested')
    else:
        print()
        print('solved 0 puzzles')
    
  
            
            
            
#use mod for the h2 
            
            
            
            
            
