def is_safe(mat, row, col, num):
    for x in range(9):
        if mat[row][x] == num:
            return False
        
    for x in range(9):
        if mat[x][col] == num:
            return False
        
    startRow = row - (row % 3)
    startCol = col - (col % 3)

    for i in range(3):
        for j in range(3):
            if mat[i+startRow][j+startCol] == num:
                return False
    
    return True

def solve_sudoku_recursive(mat, row, col):
    if row == 8 and col == 9:
        return True

    if col == 9:
        row += 1
        col = 0

    if mat[row][col] != 0:
        return solve_sudoku_recursive(mat, row, col+1)
    
    for num in range(1, 10):
        if is_safe(mat, row, col, num):
            mat[row][col] = num

            if solve_sudoku_recursive(mat, row, col+1):
                return True
            mat[row][col] = 0
    
    return False

def solve_sudoku(mat):
    solve_sudoku_recursive(mat, 0, 0)

def main():
    mat = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]

    solve_sudoku(mat)

    for row in mat:
        print(" ".join(map(str, row)))
        
if __name__ == "__main__":
    main()
