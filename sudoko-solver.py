new_board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]

hard_board = [[".",".","9","7","4","8",".",".","."],
             ["7",".",".",".",".",".",".",".","."],
             [".","2",".","1",".","9",".",".","."],
             [".",".","7",".",".",".","2","4","."],
             [".","6","4",".","1",".","5","9","."],
             [".","9","8",".",".",".","3",".","."],
             [".",".",".","8",".","3",".","2","."],
             [".",".",".",".",".",".",".",".","6"],
             [".",".",".","2","7","5","9",".","."]]

def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0:
            print("_____________________")
        new_row = "|"
        for j in range(len(board[i])):
            new_row += board[i][j]
            new_row += " "
            if j % 3 == 2:
                new_row += "|"

        print(new_row)


def setAllowed(board, allowed):
    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                allowed[i][j] = []
            else:
                # remove same row
                for k in range(9):
                    try:
                        allowed[i][j].remove(int(board[i][k]))
                    except ValueError:
                        pass

                # remove same column
                for k in range(9):
                    try:
                        allowed[i][j].remove(int(board[k][j]))
                    except ValueError:
                        pass

                # remove same square
                current_square = getSquare(i, j, board)
                for k in range(len(current_square)):
                    try:
                        allowed[i][j].remove(int(current_square[k]))
                    except ValueError:
                        pass


def getSquare(i, j, board):
    current_square = []
    if i < 3 and j < 3:
        for i in range(0, 3):
            for j in range(0, 3):
                current_square.append(board[i][j])
    elif i < 3 and j < 6:
        for i in range(0, 3):
            for j in range(3, 6):
                current_square.append(board[i][j])
    elif i < 3 and j < 9:
        for i in range(0, 3):
            for j in range(6, 9):
                current_square.append(board[i][j])
    elif i < 6 and j < 3:
        for i in range(3, 6):
            for j in range(0, 3):
                current_square.append(board[i][j])
    elif i < 6 and j < 6:
        for i in range(3, 6):
            for j in range(3, 6):
                current_square.append(board[i][j])
    elif i < 6 and j < 9:
        for i in range(3, 6):
            for j in range(6, 9):
                current_square.append(board[i][j])
    elif i < 9 and j < 3:
        for i in range(6, 9):
            for j in range(0, 3):
                current_square.append(board[i][j])
    elif i < 9 and j < 6:
        for i in range(6, 9):
            for j in range(3, 6):
                current_square.append(board[i][j])
    elif i < 9 and j < 9:
        for i in range(6, 9):
            for j in range(6, 9):
                current_square.append(board[i][j])

    return current_square


def checkAllowed(allowed):
    # checks if there is an allowed list with length 1
    for i in range(9):
        for j in range(9):
            if len(allowed[i][j]) == 1:
                return True
    return False


def isSolved(board):
    # check rows
    for i in range(9):
        all_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
            try:
                all_nums.remove(int(board[i][j]))
            except ValueError:
                pass

        if len(all_nums) != 0:
            return False

    # check columns
    for j in range(9):
        all_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(9):
            try:
                all_nums.remove(int(board[i][j]))
            except ValueError:
                pass

        if len(all_nums) != 0:
            return False

    # check squares
    ranges = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    for pair in ranges:
        current_square = getSquare(pair[0], pair[1], board)

        all_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(9):
            try:
                all_nums.remove(int(current_square[i]))
            except ValueError:
                pass

        if len(all_nums) != 0:
            return False

    return True


def isValid(board):
    # checks for duplicates

    # check rows
    for i in range(9):
        all_nums = []
        for j in range(9):
            if board[i][j] != ".":
                all_nums.append(board[i][j])

        if len(all_nums) != len(set(all_nums)):
            return False

    # check columns
    for j in range(9):
        all_nums = []
        for i in range(9):
            if board[i][j] != ".":
                all_nums.append(board[i][j])

        if len(all_nums) != len(set(all_nums)):
            return False

    # check squares
    ranges = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    for pair in ranges:
        current_square = getSquare(pair[0], pair[1], board)

        all_nums = []
        for i in range(9):
            if current_square[i] != ".":
                all_nums.append(current_square[i])

        if len(all_nums) != len(set(all_nums)):
            return False

    return True


def fillBoard(board, allowed):
    setAllowed(board, allowed)
    while checkAllowed(allowed):
        for i in range(9):
            for j in range(9):
                if len(allowed[i][j]) == 1:
                    board[i][j] = str(allowed[i][j][0])

        setAllowed(board, allowed)


def makeBoard(board):
    # copy a board to avoid inplace shallow copies
    new_board = []
    for i in range(9):
        new_row = []
        for j in range(9):
            new_row.append(board[i][j])

        new_board.append(new_row)

    return new_board


def makeAllowed(allowed):
    # copy allowed to avoid inplace shallow copies
    new_allowed = []
    for i in range(9):
        new_row = []
        for j in range(9):
            new_list = []
            for k in range(len(allowed[i][j])):
                new_list.append(allowed[i][j][k])
            new_row.append(new_list)
        new_allowed.append(new_row)
    return new_allowed


def getAllowed(allowed):
    # gets the shortest list of allowed numbers
    # returns the list plus its (i,j)
    # if sllowed is empty, returns empty list (-1,-1)
    min_length = 10
    ind_i = -1
    ind_j = -1
    allowed_list = []

    for i in range(9):
        for j in range(9):
            if len(allowed[i][j]) > 1 and len(allowed[i][j]) < min_length:
                min_length = len(allowed[i][j])
                allowed_list = allowed[i][j]
                ind_i = i
                ind_j = j

    return {"allowed_list": allowed_list, "pos": (ind_i, ind_j)}

def solveSudoko(board, allowed):
    if isSolved(board):
        printBoard(board)
    elif not isValid(board):
        return # don't continue bad boards
    else:
        # loop over possible numbers in a cell
        next_allowed = getAllowed(allowed)
        for guess in next_allowed["allowed_list"]:

            # make copies for next recursive calls
            new_board = makeBoard(board)
            new_allowed = makeAllowed(allowed)

            # make guess
            new_board[next_allowed["pos"][0]][next_allowed["pos"][1]] = str(guess)

            # update board and allowed
            fillBoard(new_board, new_allowed)

            # try it all again
            solveSudoko(new_board, new_allowed)

if __name__ == "__main__":
    # reset allowed
    allowed = []
    for i in range(9):
        new_row = []
        for j in range(9):
            new_row.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
        allowed.append(new_row)

    fillBoard(hard_board, allowed)
    solveSudoko(hard_board, allowed)