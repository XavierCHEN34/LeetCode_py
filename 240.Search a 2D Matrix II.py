def search(matrix,target):
    n_rows = len(matrix)
    if n_rows == 0:
        return False

    n_cols = len(matrix[0])
    if n_cols == 0:
        return False
    row_index = n_rows-1
    col_index = 0

    while(row_index >= 0 and col_index <= n_cols - 1):
        if(matrix[row_index][col_index]) == target:
            return True
        if(matrix[row_index][col_index]) > target:
            row_index -= 1
        if(matrix[row_index][col_index]) < target:
            col_index += 1

    return False