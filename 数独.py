import time 

def is_valid(board, row, col, num):
    # 检查行是否合法
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # 检查列是否合法
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # 检查小九宫格是否合法
    start_row, start_col = 3 * (row // 3), 3 * (col // 3) 
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  # 回溯
                return False
    return True

# 示例数独
example_sudoku = [
    [0, 0, 0, 4, 9, 8, 0, 0, 7],
    [0, 0, 6, 0, 0, 0, 2, 0, 0],
    [3, 0, 0, 2, 0, 0, 4, 1, 9],
    [9, 3, 1, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 7, 3],
    [5, 0, 0, 0, 0, 2, 9, 0, 0],
    [0, 2, 3, 8, 5, 0, 0, 9, 0],
    [0, 0, 5, 9, 0, 0, 0, 0, 4],
    [6, 4, 9, 0, 2, 0, 7, 0, 8],
]

print('程序开始运行')
T1 = time.time()
if solve_sudoku(example_sudoku):
    for row in example_sudoku:
        print(row)
    T2 = time.time()
    print('程序运行时间:%s毫秒' % ((T2 - T1)*1000))
else:
    print("No solution exists.")