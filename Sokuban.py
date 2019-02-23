class Box:
    def __init__(self,r,c,board):
        self.r = r
        self.c = c
        self.board = board

class Player:
    def __init__(self,r,c,board):
        self.r = r
        self.c = c
        self.board = board

    def move_up(self):
        self.try_and_move(-1,0)
    
    def move_down(self):
        self.try_and_move(1,0)
    
    def move_left(self):
        self.try_and_move(0,-1)
    
    def move_right(self):
        self.try_and_move(0,1)

    def try_and_move(self, dr, dc):
        if self.board.is_empty(self.r+dr,self.c+dc):
            self.r +=dr
            self.c +=dc
        else:
            box = self.board.get_box_at(self.r+dr,self.c+dc)
            if box: 
                self.r +=dr
                self.c +=dc
                box.r += dr
                box.c += dc
        
        
    
class Exit:
    def __init__(self,r,c,board):
        self.r = r
        self.c = c
        self.board = board

class Board:

    def __init__(self, board_lines):
        self.row_count = len(board_lines)
        self.col_count = len(board_lines[0])
        self.original_board_lines = board_lines
        
        self.boxes = []
        self.exits = []

        for r in range(self.row_count):
            for c in range(self.col_count):
                if (board_lines[r][c] == 'A') or (board_lines[r][c] == 'B'):
                    self.player = Player(r, c, self)

                if (board_lines[r][c] == '*') or (board_lines[r][c] == '0'):
                    e = Exit(r, c, self)
                    self.exits.append(e)

                if (board_lines[r][c] == 'O') or (board_lines[r][c] == '0'):
                    b = Box(r, c, self)
                    self.boxes.append(b)

    def show_board(self):
        rows = []
        for r in range(self.row_count):
            rstr = []
            for c in range(self.col_count):
                if self.original_board_lines[r][c] == '#':
                    rstr.append('#')
                else:
                    rstr.append('.')
            rows.append(rstr)

        rows[self.player.r][self.player.c] = 'A'
        for b in self.boxes:
            rows[b.r][b.c] = 'O'

        for e in self.exits:
            if rows[e.r][e.c] == 'A':
                rows[e.r][e.c] = 'B'
            elif rows[e.r][e.c] == 'O':
                rows[e.r][e.c] = '0'
            else:
                rows[e.r][e.c] = '*'

        for row in rows:
            print(''.join(row))

    def get_box_at(self, r, c):
        for b in self.boxes:
            if b.r == r and b.c == c:
                return b
        return None
    
    def is_empty(self, r, c):
        if self.get_box_at(r,c) != None:
            return False
        if self.original_board_lines[r][c] == '#':
            return False
        return True

    def is_over(self):
        if self.original_board_lines[r][c] == '*':
            return False

def main():
    board = Board(['..#####.',
                   '###...#.',
                   '#*AO..#.',
                   '###.O*#.',
                   '#*##O.#.',
                   '#.#.*.##',
                   '#O.0OO*#',
                   '#...*..#',
                   '########',])
    
    player = board.player
    step = 0
    
    while not board.is_over():
        step += 1
        print('Step:', step, 'Current board is:')
        
        board.show_board()
        
        print('Pick direction L,R,U,D')
        movement = input()
        if movement == 'U':
            player.move_up()
        elif movement == 'D':
            player.move_down()
        elif movement == 'L':
            player.move_left()
        elif movement == 'R':
            player.move_right()

    print('You use',step,'steps')


    
if __name__ == '__main__':
    main()