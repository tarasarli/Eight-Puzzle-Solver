#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: 
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1
        
        

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
    
        
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                self.tiles[row][col] = digitstr[(3*row + col)]
                if self.tiles[row][col] == '0':
                    self.blank_r = row
                    self.blank_c = col
                
        
        
        
   
    ### Add your other method definitions below. ###
    
    def __repr__(self):
        """returns a string representation of a Board object."""
        new = ''
        
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
               if self.tiles[row][col] == self.tiles[self.blank_r][self.blank_c]:
                   new += '_ ' 
               else:
                  new += str(self.tiles[row][col]) + ' '
            new += '\n'
               
                
        return new

                   
    #go over how to use '\n' because imma forget


    def move_blank(self, direction):
        """takes as input a string direction that specifies the direction
        in which the blank should move, and that attempts to modify the 
        contents of the called Board object accordingly. Not all moves 
        are possible on a given Board; for example, it isn’t possible to 
        move the blank down if it is already in the bottom row. The method 
        should return True or False to indicate whether the requested move 
        was possible"""
        if direction not in ['up','down','left','right']:
            return False
        else:
            if direction == 'up' and self.blank_r == 0:
                return False
                
            elif direction == 'down' and self.blank_r == 2:
                return False
            
            elif direction == 'right' and self.blank_c == 2:
                return False
                
            elif direction == 'left' and self.blank_c == 0:
                return False
      
        
      #why does dierection not have self. infront of it? because its passed in ; not an attribute
      #is else only connected to last elif or wntier block     ; its connected to block


        
            if direction == 'up':
                keeper = self.blank_r - 1
                number = self.tiles[keeper][self.blank_c]
                self.tiles[self.blank_r][self.blank_c] = number 
                blank = '0'

                self.tiles[keeper][self.blank_c] = blank
                self.blank_r = keeper

            elif direction =='down':
                keeper = self.blank_r + 1
                number = self.tiles[keeper][self.blank_c]
                self.tiles[self.blank_r][self.blank_c] = number 
                blank = '0'
                self.tiles[keeper][self.blank_c] = blank
                self.blank_r = keeper
                
            elif direction =='left':
                keeper = self.blank_c - 1
                number = self.tiles[self.blank_r][keeper]
                self.tiles[self.blank_r][self.blank_c] = number 
                blank = '0'
                self.tiles[self.blank_r][keeper] = blank
                self.blank_c = keeper
                
            elif direction =='right':
                keeper = self.blank_c + 1
                number = self.tiles[self.blank_r][keeper]
                self.tiles[self.blank_r][self.blank_c] = number 
                blank = '0'
                self.tiles[self.blank_r][keeper] = blank
                self.blank_c = keeper
                
            return True
        
                  
    def digit_string(self):
        """creates and returns a string of digits that corresponds to the
        current contents of the called Board object’s tiles attribute. """
        new_str = ''
        
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                new_str += self.tiles[row][col]
        
        return new_str



    def copy(self):
        """returns a newly-constructed Board object that is a deep copy of
        the called object (i.e., of the object represented by self). This 
        method should use the Board constructor to create a new Board 
        object with the same configuration of tiles as self, and it 
        should return the newly created Board object. """
        
        copy_of_board = self.digit_string()
        x = Board(copy_of_board)
        return x
  

#does this produce a shallow copy or a deep copy?


#what do the directions mean when it says "This method should use the Board >>>
#constructor to create a new Board object with the same configuration >>>
# of tiles as self, and it should return the newly created Board object.

# why is it giving me > IndexError: list index out of range



    def num_misplaced(self):
        """counts and returns the number of tiles in the called Board object
        that are not where they should be in the goal state. You should not
        include the blank cell in this count, even if it’s not where it 
        should be in the goal state. """
        incorrect_order = 0
        
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                if self.tiles[row][col] != GOAL_TILES[row][col]:
                    if self.tiles[row][col] != '0':
                        incorrect_order += 1
        
        return incorrect_order
               

    
    
    
    def __eq__(self, other):
        """can be called when the == operator is used to compare two Board 
        objects. The method should return True if the called object (self) 
        and the argument (other) have the same values for the tiles attribute,
        and False otherwise. This method should be straightforward to
        implement because you can simply use the == operator to compare 
        self.tiles and other.tiles. You do not need to explicitly 
        compare the individual tiles yourself, because the == operator
        already compares the individual elements of 2-D lists."""
        x =  True
    
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                if self.tiles[row][col] != other.tiles[row][col]: 
                    x = False
                    
        return x





























                
                     
                 
            
        
        
        
        












