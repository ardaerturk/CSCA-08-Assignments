'''
I hear-by decree that all work contained in this file is solely my own
and that I received no help in the creation of this code.
I have read and understood the University of Toronto academic code of
behaviour with regards to plagiarism, and the seriousness of the
penalties that could be levied as a result of committing plagiarism
on an assignment.

Name: Arda Erturk
MarkUs Login: erturkar
'''

PUZZLE1 = '''
tlkutqyu
hyrreiht
inokdcne
eaccaayu
riainpaf
rrpnairb
ybybnick
ujvaynak
'''

PUZZLE2 = '''
fgbkizpyjohwsunxqafy
hvanyacknssdlmziwjom
xcvfhsrriasdvexlgrng
lcimqnyichwkmizfujqm
ctsersavkaynxvumoaoe
ciuridromuzojjefsnzw
bmjtuuwgxsdfrrdaiaan
fwrtqtuzoxykwekbtdyb
wmyzglfolqmvafehktdz
shyyrreihtpictelmyvb
vrhvysciipnqbznvxyvy
zsmolxwxnvankucofmph
txqwkcinaedahkyilpct
zlqikfoiijmibhsceohd
enkpqldarperngfavqxd
jqbbcgtnbgqbirifkcin
kfqroocutrhucajtasam
ploibcvsropzkoduuznx
kkkalaubpyikbinxtsyb
vjenqpjwccaupjqhdoaw
'''


def rotate_puzzle(puzzle):
    '''(str) -> str
    Return the puzzle rotated 90 degrees to the left.
    '''

    raw_rows = puzzle.split('\n')
    rows = []
    # if blank lines or trailing spaces are present, remove them
    for row in raw_rows:
        row = row.strip()
        if row:
            rows.append(row)

    # calculate number of rows and columns in original puzzle
    num_rows = len(rows)
    num_cols = len(rows[0])

    # an empty row in the rotated puzzle
    empty_row = [''] * num_rows

    # create blank puzzle to store the rotation
    rotated = []
    for row in range(num_cols):
        rotated.append(empty_row[:])
    for x in range(num_rows):
        for y in range(num_cols):
            rotated[y][x] = rows[x][num_cols - y - 1]

    # construct new rows from the lists of rotated
    new_rows = []
    for rotated_row in rotated:
        new_rows.append(''.join(rotated_row))

    rotated_puzzle = '\n'.join(new_rows)

    return rotated_puzzle


def lr_occurrences(puzzle, word):
    '''(str, str) -> int
    Return the number of times word is found in puzzle in the
    left-to-right direction only.

    >>> lr_occurrences('xaxy\nyaaa', 'xy')
    1
    '''
    return puzzle.count(word)


def total_occurrences(puzzle, word):
    '''(str, str) -> int
    Return total occurrences of word in puzzle.
    All four directions are counted as occurrences:
    left-to-right, top-to-bottom, right-to-left, and bottom-to-top.    
    >>> total_occurrences('PUZZLE2' , 'nick')
    4
    >>> total_occurrences(PUZZLE2, 'brian')
    3
    >>> total_occurrences(PUZZLE2, 'paco')
    1
    >>> total_occurrences(PUZZLE2, 'thierry')
    1
    >>> total_occurrences(PUZZLE1, 'thierry')
    2
    >>> total_occurrences(PUZZLE1, 'paco')
    1
    >>> total_occurrences(PUZZLE1, 'brian')
    2
    >>> total_occurrences(PUZZLE1, 'nick')
    2    
    '''
    # your code here   
    num = 0
    num = num + puzzle.count(word)
    num = num + lr_occurrences(rotate_puzzle(puzzle), word)
    num = num + lr_occurrences(rotate_puzzle(rotate_puzzle(puzzle)), word)
    num = num + lr_occurrences(rotate_puzzle(rotate_puzzle(rotate_puzzle(puzzle))), word)

    return num


def in_puzzle_horizontal(puzzle, word):
    '''(str, str) -> bool
   Return true iff the given word can be found in puzzle in one or both horizontal directions.    
   >>> in_puzzle_horizontal(PUZZLE1, 'brian')
   True
   >>> in_puzzle_horizontal(PUZZLE1, 'thierry')
   True
   >>> in_puzzle_horizontal(PUZZLE1, 'nick')
   True
   >>> in_puzzle_horizontal(PUZZLE1, 'paco')
   False
   >>> in_puzzle_horizontal(PUZZLE2, 'paco')
   False
   >>> in_puzzle_horizontal(PUZZLE2, 'brian')
   False
   >>> in_puzzle_horizontal(PUZZLE2, 'thierry')
   True
   >>> in_puzzle_horizontal(PUZZLE2, 'nick')
   True
    '''   
#    check the word's occurrence on left-to-right and right-to-left directions
    check1 = (word in puzzle) or ( word in rotate_puzzle(rotate_puzzle(puzzle)))    
    return check1


def in_puzzle_vertical(puzzle, word):
    '''(str, str) -> bool
    Return True iff the given word can be found in puzzle in one or both vertical directions.    
    >>> in_puzzle_vertical(PUZZLE1, 'brian')
    True
    >>> in_puzzle_vertical(PUZZLE1, 'thierry')
    True
    >>> in_puzzle_vertical(PUZZLE1, 'nick')
    True
    >>> in_puzzle_vertical(PUZZLE1, 'paco')
    True
    >>> in_puzzle_vertical(PUZZLE2, 'paco')
    True
    >>> in_puzzle_vertical(PUZZLE2, 'nick')
    True
    >>> in_puzzle_vertical(PUZZLE2, 'thierry')
    False
    >>> in_puzzle_vertical(PUZZLE2, 'brian')
    True
    >>> in_puzzle_vertical(PUZZLE2, 'arda')
    False    
    '''
#    check the word's occurrence on top-to-bottom and bottom-to-top directions
    check2 = (word in rotate_puzzle(puzzle)) or (word in rotate_puzzle(rotate_puzzle(rotate_puzzle(puzzle))))

    return check2


def in_puzzle(puzzle, word):
    ''' (str, str) -> bool
    Return True iff the given word can be found anywhere in puzzle.    
    >>> in_puzzle(PUZZLE2, 'brian')
    True
    >>> in_puzzle(PUZZLE2, 'thierry')
    True
    >>> in_puzzle(PUZZLE2, 'paco')
    True
    >>> in_puzzle(PUZZLE2, 'nick')
    True
    >>> in_puzzle(PUZZLE2, 'arda')
    False
    >>> in_puzzle(PUZZLE2, 'trump')
    False
    >>> in_puzzle(PUZZLE2, 'hillary')
    False
    >>> in_puzzle(PUZZLE1, 'brian')
    True
    >>> in_puzzle(PUZZLE1, 'thierry')
    True
    >>> in_puzzle(PUZZLE1, 'paco')
    True
    >>> in_puzzle(PUZZLE1, 'nick')
    True
    >>> in_puzzle(PUZZLE1, 'arda')
    False
    >>> in_puzzle(PUZZLE1, 'trump')
    False
    >>> in_puzzle(PUZZLE1, 'hillary')
    False


    '''
#    check all the directions
    check_all_puzzle = in_puzzle_vertical(puzzle, word) or in_puzzle_horizontal(puzzle, word)    
    return check_all_puzzle


def in_exactly_one_dimension(puzzle, word):
    ''' (str, str) -> bool
    Return True iff the given word can be found in exactly one of the two dimensions but not both.    
    >>> in_exactly_one_dimension(PUZZLE1, 'brian')
    False
    >>> in_exactly_one_dimension(PUZZLE1, 'nick')
    False
    >>> in_exactly_one_dimension(PUZZLE1, 'paco')
    False
    >>> in_exactly_one_dimension(PUZZLE1, 'thierry')
    False
    >>> in_exactly_one_dimension(PUZZLE1, 'trump')
    False
    >>> in_exactly_one_dimension(PUZZLE1, 'ybyb')
    True
    >>> in_exactly_one_dimension(PUZZLE2, 'thierry')
    True
    >>> in_exactly_one_dimension(PUZZLE2, 'paco')
    False
    >>> in_exactly_one_dimension(PUZZLE2, 'nick')
    False
    >>> in_exactly_one_dimension(PUZZLE2, 'brian')
    False
    '''  
#    check the horizontal directon and check for the word whether it's in the vertical direction or not.
    check_dimension1 = in_puzzle_horizontal(puzzle, word) and not in_puzzle_vertical(puzzle, word)    
    return check_dimension1


def all_horizontal(puzzle, word):
    ''' (str, str) -> bool
    Return true iff all occurrences of the supplied word are horizontal in the puzzle.    
    >>> all_horizontal(PUZZLE1, 'brian')
    True
    >>> all_horizontal(PUZZLE1, 'paco')
    False
    >>> all_horizontal(PUZZLE1, 'thierry')
    True
    >>> all_horizontal(PUZZLE1, 'nick')
    True
    >>> all_horizontal(PUZZLE2, 'nick')
    True
    >>> all_horizontal(PUZZLE2, 'thierry')
    True
    >>> all_horizontal(PUZZLE2, 'paco')
    False
    >>> all_horizontal(PUZZLE2, 'brian')
    False
    >>> all_horizontal(PUZZLE2, 'trump')
    True
    >>> all_horizontal(PUZZLE1, 'hillary')
    True

    '''
#    check the word in horizontal direction, the word whether it's in the puzzle or not and the vertical direction.
    check_occurrence = ((((in_puzzle_horizontal(puzzle, word) or (word in puzzle))))) or not in_puzzle_vertical(puzzle, word)
    return check_occurrence 


def at_most_one_vertical(puzzle, word):
    ''' (str, str) -> bool
    return True iff word occurs at most once in the puzzle and that occurrence is vertical.
    >>> at_most_one_vertical(PUZZLE1, 'brian')
    False
    >>> at_most_one_vertical(PUZZLE1, 'nick')
    False
    >>> at_most_one_vertical(PUZZLE1, 'paco')
    True
    >>> at_most_one_vertical(PUZZLE1, 'thierry')
    False
    >>> at_most_one_vertical(PUZZLE2, 'thierry')
    False
    >>> at_most_one_vertical(PUZZLE2, 'paco')
    True
    >>> at_most_one_vertical(PUZZLE2, 'nick')
    False
    >>> at_most_one_vertical(PUZZLE2, 'brian')
    False
    '''
#    check the vertical direction
    check_occurrence = in_puzzle_vertical(puzzle, word)
#    count the word for all directions
    rotated_puzzle_count1 = puzzle.count(word)
    rotated_puzzle_count2 = rotate_puzzle(puzzle).count(word)
    rotated_puzzle_count3 = rotate_puzzle(rotate_puzzle(puzzle)).count(word)
    rotated_puzzle_count4 = rotate_puzzle(rotate_puzzle(rotate_puzzle(puzzle))).count(word)
    return check_occurrence and ((rotated_puzzle_count2 + rotated_puzzle_count4 == 1) and (( rotated_puzzle_count1 + rotated_puzzle_count3 == 0)))


def do_tasks(puzzle, name):
    '''(str, str) -> NoneType
    puzzle is a word search puzzle and name is a word.
    Carry out the tasks specified here and in the handout.
    '''
    # *task* 1a: add a print call below the existing one to print
    # the number of times that name occurs in the puzzle left-to-right.
    # Hint: one of the two starter functions defined above will be useful.
#    the end='' just means "Don't start a newline, the next thing
    # that's printed should be on the same line as this text
    # *task* 1a: add a print call below the existing one to print
    # the number of times that name occurs in the puzzle left-to-right.
    # Hint: one of the two starter functions defined above will be useful.
    # the end='' just means "Don't start a newline, the next thing
    # that's printed should be on the same line as this text
    print('Number of times', name, 'occurs left-to-right: ', end='')
    # your print call here
    print(lr_occurrences(puzzle, name)) 
    # *task* 1b: add code that prints the number of times
    # that name occurs in the puzzle top-to-bottom.
    # (your format for all printing should be similar to
    # the print statements above)
    # Hint: both starter functions are going to be useful this time!
    print('Number of times', name, 'occurs top-to-bottom: ', end='')
    print (lr_occurrences(rotate_puzzle(puzzle), name))
    # *task* 1c: add code that prints the number of times
    # that name occurs in the puzzle right-to-left.
    print('Number of times', name, 'right-to-left: ', end='')
    print((lr_occurrences(rotate_puzzle(rotate_puzzle(puzzle)), name)))
    # *task* 1d: add code that prints the number of times
    # that name occurs in the puzzle bottom-to-top.
    print('Number of times', name, 'occurs bottom-to-top: ', end='')
    print(lr_occurrences(rotate_puzzle(rotate_puzzle(rotate_puzzle(puzzle))), name))        
    print (total_occurrences(puzzle, name))
    print (in_puzzle_horizontal(puzzle, name))
do_tasks(PUZZLE1, 'brian')
do_tasks(PUZZLE1, 'nick')
do_tasks(PUZZLE2, 'nick')
print(in_puzzle(PUZZLE1, 'nick'))
print (in_puzzle(PUZZLE2, 'thierry'))