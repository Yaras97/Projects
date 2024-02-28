class Knight:
    def __init__(self, horizontal, vertical, color):
        self.horizontal, self.vertical, self.color = horizontal, vertical, color
        self.board = [['.'] * 8 for _ in range(8)]

    def get_char(self):
        return 'N'

    def can_move(self, hor, ver):
        x1, y1 = '87654321'.index(str(self.vertical)), 'abcdefgh'.index(self.horizontal)
        x2, y2 = '87654321'.index(str(ver)), 'abcdefgh'.index(hor)
        return (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5

    def move_to(self, x, y):
        if self.can_move(x, y):
            self.horizontal, self.vertical = x, y

    def draw_board(self):
        x, y = '87654321'.index(str(self.vertical)), 'abcdefgh'.index(self.horizontal)
        for r in range(8):
            for c in range(8):
                if (x - r) ** 2 + (y - c) ** 2 == 5:
                    self.board[r][c] = '*'
        self.board[x][y] = 'N'
        for l in self.board:
            print(*l, sep='')
        self.board = [['.'] * 8 for _ in range(8)]


knight = Knight('c', 3, 'white')
knight.draw_board()