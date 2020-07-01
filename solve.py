def solve(board):
    found = find_empty(board)
    if not found:
        return True
    row, col = found
    for i in range(1, 10):
        if(valid(board, i, found)):
            board[row][col] = i
            if(solve(board) == True):
                return True
            board[row][col] = 0
    return False
    
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] == 0):
                return [i, j]
    return None

def valid(board, number, position):
    for i in range(len(board[0])):
        if board[position[0]][i] == number and i != position[1]:
            return False
    for i in range(len(board)):
        if board[i][position[1]] == number and i != position[0]:
            return False
    
    BoxPositionX = position[1] // 3
    BoxPositionY = position[0] // 3
    for i in range(3):
        for j in range(3):
            if board[BoxPositionY*3 + i][BoxPositionX*3 + j] == number and BoxPositionX*3 + i != position[1] and BoxPositionY*3 + j != position[0]:
                return False
    return True

# def print_board(board):
#     for i in range(len(board)):
#         if i % 3 == 0 and i != 0:
#             print("- - - - - - - - - - - - ")
#         for j in range(len(board[0])):
#             if j % 3 == 0 and j != 0:
#                 print(" | ", end="")
#             if j == 8:
#                 print(board[i][j])
#             else:
#                 print(str(board[i][j]) + " ", end="")

# board = [
#     [7,8,0,4,0,0,1,2,0],
#     [6,0,0,0,7,5,0,0,9],
#     [0,0,0,6,0,1,0,7,8],
#     [0,0,7,0,4,0,2,6,0],
#     [0,0,1,0,5,0,9,3,0],
#     [9,0,4,0,6,0,0,0,5],
#     [0,7,0,3,0,0,0,1,2],
#     [1,2,0,0,0,7,4,0,0],
#     [0,4,9,2,0,6,0,0,7]
# ]

board = [
    [
        [
            [7,8,0],[4,0,0],[1,2,0]
        ]
        ,
        [
            [6,0,0],[0,7,5],[0,0,9]
        ]
        ,
        [
            [0,0,0],[6,0,1],[0,7,8]
        ]
    ],[
        [
            [0,0,7],[0,4,0],[2,6,0]
        ]
        ,
        [
            [0,0,1],[0,5,0],[9,3,0]
        ]
        ,
        [
            [9,0,4],[0,6,0],[0,0,5]
        ]
    ],[
        [
            [0,7,0],[3,0,0],[0,1,2]
        ]
        ,
        [
            [1,2,0],[0,0,7],[4,0,0]
        ]
        ,
        [
            [0,4,9],[2,0,6],[0,0,7]
        ]        
    ]
]

# print_board(board)
# print()
# solve(board)
# print_board(board)