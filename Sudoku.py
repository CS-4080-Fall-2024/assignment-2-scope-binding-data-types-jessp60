# Solving a Sudoku Puzzle Using Backtracking 
# Reference: https://youtu.be/lLixGoGuClc?si=Nrn0LDhHDezgtj6i
def solveSudoku(board):
    # Use a list of objects to store the board values
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    # Create a copy of the copy of the board row, column, and box values 
    for i in range(9):
        for j in range(9):
            # Parse througe the table and save used values 
            if board[i][j] != ".":
                num = int(board[i][j])
                rows[i].add(num)
                cols[j].add(num)
                
                # Calculate box id and save number
                boxId = i//3 * 3 + j // 3
                boxes[boxId].add(num)


    # Create a function to backtrack through the values and check for validity 
    def backTrack(i, j):
        # Since there is no global variable called solved, we use the keyword 'nonlocal' to look at one layer outside the function 
        nonlocal solved
        # If we are moving past the final row (index 8), then the board has been solved 
        if i == 9: 
            solved = True
            return 

        # If at the end of the row, move onto the next
        newRowIndex = i + 1 if j == 8 else i
        # Set the column to the beginning if moving to the next row 
        newColIndex = 0 if j == 8 else j+1

        # If the current index has a value, move on 
        if board[i][j] != '.':
            backTrack(newRowIndex, newColIndex)
        else: 
            # Otherwise, check what numbers can be put in this spot
            for num in range(1, 10): # Python's range function only enumerates through start to end-1
                boxId = i//3 * 3 + j // 3
                if num not in rows[i] and num not in cols[j] and num not in boxes[boxId]:
                    # If the number is a valid choice, add the values to corresponding lists 
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[boxId].add(num)
                    # This will help keep track of what values are avialable for the empty spaces 


                    # Update the board 
                    board[i][j] = str(num)
                    # Continue to the next space on the board 
                    backTrack(newRowIndex, newColIndex)
                    
                    # Once the backtracking has been done, we need to reset the row and column availability for the next value
                    if not solved: 
                        rows[i].remove(num)
                        cols[j].remove(num)
                        boxes[boxId].remove(num)
                        board[i][j] = "."
    
    # Before backtracking, reset the flag to false
    solved = False

    # Call the backtracking function from the first row and column of the board
    backTrack(0,0)


def main(): 
  board = [["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]
  solveSudoku(board)
  for line in board:
    print(line)
main()