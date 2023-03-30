func isValidSudoku(board [][]byte) bool {
    cols := make([]map[byte]bool, 9)
    rows := make([]map[byte]bool, 9)
    squares := make([]map[byte]bool, 9)

    for i := 0; i < 9; i++ {
        cols[i] = make(map[byte]bool)
        rows[i] = make(map[byte]bool)
        squares[i] = make(map[byte]bool)
    }

    for r := 0; r < 9; r++ {
        for c := 0; c < 9; c++ {
            if board[r][c] == '.' {
                continue
            }
            // expression _, ok := map[key] is used to check if a value is present in the map
            if _, ok := rows[r][board[r][c]]; ok {
                return false
            }
            if _, ok := cols[c][board[r][c]]; ok {
                return false
            }
            if _, ok := squares[(r/3)*3+c/3][board[r][c]]; ok {
                return false
            }
            rows[r][board[r][c]] = true
            cols[c][board[r][c]] = true
            squares[(r/3)*3+c/3][board[r][c]] = true
        }
    }

    return true
}
