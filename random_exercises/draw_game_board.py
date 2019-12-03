# Create a game board, from Ex. 24 practicepython.org

rows= int(input("How many rows for your board?"))
cols= int(input("How many columns for your board?"))


def draw_board(rows, cols): #Draws a game board with the number of squares specified by user
    row = " ---"
    row1 = " ---"
    empty_col = "    "
    empty_col1 = "    "
    col = "|   "
    col1 = "|   "
    l_row = " "
    l_col = "|"
    l_emp_col = " "
    draw_cols = rows
    while cols > 1:
        row1 += row
        cols -= 1
    row1 += l_row
    while rows > 1:
        col1 += col
        empty_col1 += empty_col
        rows -= 1
    col1 += l_col
    empty_col1 += l_emp_col
    while draw_cols > 0:
        print(row1)
        print(empty_col1)
        print(col1)
        print(empty_col1)
        draw_cols -= 1
    print(row1)

draw_board(rows, cols)