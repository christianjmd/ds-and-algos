import copy

# =================================================

def grid_from_file(file_name):

    matrix = []
    fileID = open(file_name)
    for line in fileID:
        line = line.strip("\n").split(",")
        matrix.append(line)

    return matrix

# =================================================


def valid_entry(grid, num, r, c):

    # begin by checking if there's any 1's in the row.
    for i in range(len(grid) - 1):  # check value in the row.
        if num == grid[r][i]:
            return False

    # then check every value in the column if it's alright.
    for j in range(len(grid) - 1):
        if grid[j][c] == num:
            return False

    # get values from the sub-grid
    check = []
    n = int(len(grid) ** (0.5))
    row = (r // n) * n
    column = (c // n) * n
    for i in range(row, row + n):
        for j in range(column, column + n):
            check.append(grid[i][j])

    if num in check:
        return False
    else:
        return True


# # ===============================================


def grids_augmented_in_row(grid, num, row):

    output = []


    if num in grid[row]:
        return grid

    else:

        # this is to check each value in the sub-grid.
        for x in range(len(grid)):

            if grid[row][x] == 'x':

                counter = 0

                # if possibility we can change, check each value in the column
                for q in range(len(grid)):
                    if grid[q][x] != num:
                        counter += 1

                # only check the sub-grid if it's not contained in the column.
                if counter == len(grid):
                    # last condition is to check the sub-grid if it contains the value.
                    check = []
                    n = int(len(grid) ** (0.5))
                    ro = (row // n) * n
                    col = (x // n) * n
                    for i in range(ro, ro + n):
                        for j in range(col, col + n):
                            check.append(grid[i][j])

                    if num not in check:
                        change = copy.deepcopy(grid)
                        change[row][x] = num
                        output += [change]

        return output


# =================================================

def grids_augmented_with_number(grid, num):

    ret = []
    worthyChecker = 0
    rowsWithoutNum = []
    b = 0

    for a in range(len(grid)):
        if num not in grid[a]:
            rowsWithoutNum.append(a)

    if len(rowsWithoutNum) == 0:        # return original grid because num is already in every position.
        return grid

    else:

        while b < len(grid):

            m = 0

            if (grid[rowsWithoutNum[m]][b] == 'x') and (b < len(grid)):

                newList = copy.deepcopy(grid)
                c = b

                while m < len(rowsWithoutNum) and c < len(grid): # m refers to the row in which we're trying to replace 'x' with num.

                    if grid[rowsWithoutNum[m]][c] == 'x':  # we found a position we could POSSIBLY append to. Therefore, check.

                        # COLUMN CHECK   // everything from here to the bottom, HAS TO BE EXECUTED. because it NEEDS to be found.
                        columnCounter = 0
                        d = 0
                        while d < len(grid):
                            if newList[d][c] != num:
                                columnCounter += 1
                            d += 1

                        # SUB-GRID CHECK
                        if columnCounter == len(grid):
                            subgrid = []
                            n = int(len(grid) ** (0.5))
                            newRow = (rowsWithoutNum[m] // n) * n
                            newColumn = (c // n) * n
                            for nr in range(newRow, newRow + n):
                                for nc in range(newColumn, newColumn + n):
                                    subgrid.append(grid[nr][nc])
                            # CHECK IF WE SHOULD ALTER THE OLD TABLE
                            if num not in subgrid:
                                changeRow = rowsWithoutNum[m]
                                changeColumn = c
                                newList[changeRow][changeColumn] = num

                                c = -1
                                m += 1  # we've found where to put num, therefore, go to the next row yay
                                worthyChecker = 0

                        # if we've reached the end of the list, increase the row,
                        if c == len(grid) - 1:
                            m += 1
                            c = 0               # reset the start of the loop again.
                        else:
                            c += 1

                    else:
                        c += 1

                # we check if newList should be added to ret.
                for z in range(len(grid)):
                    if num in newList[z]:
                        worthyChecker += 1
                if worthyChecker == len(grid):
                    ret += [newList]
                    for findIndex in range(len(grid)):
                        if (newList[rowsWithoutNum[0]][findIndex] == num):
                            b = findIndex + 1
                else:
                    b += 1

            else:
                b += 1


        if len(ret) > 0:
            return ret
        else:
            return []



# =================================================

def sudoku_solver(file_name):

    # opens given file
    grid = []
    fileID = open(file_name)
    for line in fileID:
        line = line.strip("\n").split(",")
        grid.append(line)


    start = 1   # this refers to the value we're going to input.
    worthyChecker = 0
    b = 0       # goes through each value of the first row without num.
    newList = copy.deepcopy(grid)   # place here because we're only going to be using one this whole time.

    while b < len(grid) and start != len(grid) + 1:

        m = 0
        num = str(start)
        rowsWithoutNum = []

        for a in range(len(grid)):
            if num not in grid[a]:
                rowsWithoutNum.append(a)

        if (grid[rowsWithoutNum[m]][b] == 'x') and (b < len(grid)):

            c = b

            while m < len(rowsWithoutNum) and c < len(grid):  # m refers to the row in which we're trying to replace 'x' with num.

                if grid[rowsWithoutNum[m]][c] == 'x':  # we found a position we could POSSIBLY append to. Therefore, check.

                    # COLUMN CHECK   // everything from here to the bottom, HAS TO BE EXECUTED. because it NEEDS to be found.
                    columnCounter = 0
                    d = 0
                    while d < len(grid):
                        if newList[d][c] != num:
                            columnCounter += 1
                        d += 1

                    # SUB-GRID CHECK
                    if columnCounter == len(grid):
                        subgrid = []
                        n = int(len(grid) ** (0.5))
                        newRow = (rowsWithoutNum[m] // n) * n
                        newColumn = (c // n) * n
                        for nr in range(newRow, newRow + n):
                            for nc in range(newColumn, newColumn + n):
                                subgrid.append(grid[nr][nc])
                        # CHECK IF WE SHOULD ALTER THE OLD TABLE
                        if num not in subgrid:
                            changeRow = rowsWithoutNum[m]
                            changeColumn = c
                            newList[changeRow][changeColumn] = num
                            c = -1
                            m += 1  # we've found where to put num, therefore, go to the next row
                            worthyChecker = 0

                    # if we've reached the end of the list, increase the row,
                    if c == len(grid) - 1:
                        m += 1
                        c = 0  # reset the start of the loop again.
                    else:
                        c += 1

                else:
                    c += 1

            # check if we should append num into the grid because it may not be there for each row.
            for z in range(len(grid)):
                if num in newList[z]:
                    worthyChecker += 1

            if worthyChecker == len(grid):
                grid = copy.deepcopy(newList)
                start += 1
                b = 0
            else:
                b += 1  # we increment by one because we wish to go the next value in the first list that doesnt contain num.
                newList = copy.deepcopy(grid)   # reset the grid.

        else:
            b += 1

    return grid








