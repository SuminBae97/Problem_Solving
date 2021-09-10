
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

moves = [val-1 for val in moves]

# for i in range(len(board)):
#     for j in range(len(board[i])):
#         print(board[j][i])

new_board = list(map(list,zip(*board)))
stack =[]

total_count = 0
#
for index in moves:
    vals = new_board[index]
    for i in range(len(vals)):

        if vals[i]==0:
            pass


        else:
            added_value = vals[i]
            if len(stack)==0:
                stack.append(added_value)

            else:
                if stack[-1]==added_value:
                    total_count+=2
                    stack.pop()
                else:
                    stack.append(added_value)

            vals[i]=0
            break








