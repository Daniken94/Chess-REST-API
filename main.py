def show(chessboard):

    """Shows the chessboard in the console.

    DOES NOT WORK UNTIL ALL CLASES: Pawn, Knight, Queen, King, Rook, Bishop ARE CREATED!!!

    """

    WHITE = {
        Pawn: chr(9817),
        Knight: chr(9816),
        Queen: chr(9813),
        King: chr(9812),
        Rook: chr(9814),
        Bishop: chr(9815),
    }

    BLACK = {
        Pawn: chr(9823),
        Knight: chr(9818),
        Queen: chr(9819),
        King: chr(9812),
        Rook: chr(9820),
        Bishop: chr(9821),
    }

    for y in range(7, -1, -1):
        print(y, end='\t')
        for x in range(8):
            if chessboard.board[x][y] is not None:
                if chessboard.board[x][y].color == 'white':
                    print(WHITE[type(chessboard.board[x][y])], end='\t')
                else:
                    print(BLACK[type(chessboard.board[x][y])], end='\t')
            else:
                print('\t', end='')
        print('\n')
    print('\t', end='')

    for x in range(8):
        print(x, end='\t')
    print()

class Chessboard:
    def __init__(self):
        self.color = "white"
        self.board = [[None]*8 for i in range(8)]

    def setup(self):
        for x in range(8):
            for y in range(8):
                if y==0:
                    self.board[0][y] = Rook('white', 0, y)
                    self.board[7][y] = Rook('white', 7, y)
                    self.board[1][y] = Knight('white', 1, y)
                    self.board[6][y] = Knight('white', 6, y)
                    self.board[2][y] = Bishop('white', 2, y)
                    self.board[5][y] = Bishop('white', 5, y)
                    self.board[3][y] = Queen('white', 3, y)
                    self.board[4][y] = King('white', 4, y)
                if y == 1:
                    self.board[x][y] = Pawn('white', x, y)
                if y == 6:
                    self.board[x][y] = Pawn('black', x, y)
                if y == 7:
                    self.board[0][y] = Rook('black', 0, y)
                    self.board[7][y] = Rook('black', 7, y)
                    self.board[1][y] = Knight('black', 1, y)
                    self.board[6][y] = Knight('black', 6, y)
                    self.board[2][y] = Bishop('black', 2, y)
                    self.board[5][y] = Bishop('black', 5, y)
                    self.board[3][y] = Queen('black', 3, y)
                    self.board[4][y] = King('black', 4, y)

    def __getitem__(self, item):
        return self.board[item]

    def list_allowed_moves(self, x, y):
        figura = self.board[x][y]
        if not isinstance(figura, Figure):
            return None

        if figura.color != self.color:
            return None

        return figura.list_allowed_moves(self.board)

    def move(self, from_x, from_y, to_x, to_y):
        allowed_moves = self.list_allowed_moves(from_x, from_y)
        if allowed_moves is None:
            raise ValueError("not allowed move")

        if (to_x, to_y) in allowed_moves:
            figura = self.board[from_x][from_y]
            figura.move(to_x, to_y)
            self.board[to_x][to_y] = self.board[from_x][from_y]
            self.board[from_x][from_y] = None
            if self.color == "white":
                self.color = "black"
            else:
                self.color = "white"
        else:
            raise ValueError("not allowed move")

class Figure:
    def __init__(self, color, x ,y):
        self.color = color
        self.x = x
        self.y = y
    def move(self, x, y):
        self.x = x
        self.y = y

class Pawn(Figure):
    def __init__(self,color, x ,y):
        super().__init__(color, x ,y)
    def get_path_to_position(self, x, y):
        path = []
        if self.color == 'white':
            start_point = self.y+1
            end_point = y+1
            for path_y in range(start_point, end_point):
                path.append((x, path_y))
        else:
            start_point = self.y-1
            end_point = y-1
            for path_y in range(start_point, end_point, -1):
                path.append((x, path_y))
        return path
    def list_allowed_moves(self, chessboard):
        allowed_move = []
        if self.color == "white":
            if self.y < 7:
                if self.y ==1:
                    allowed_move.append((self.x, self.y + 1))
                    allowed_move.append((self.x, self.y+2))
                else:
                    allowed_move.append((self.x, self.y+1))
        else:
            if self.y >= 1:
                if self.y == 6:
                    allowed_move.append((self.x, self.y-1))
                    allowed_move.append((self.x, self.y-2))
                else:
                    allowed_move.append((self.x, self.y-1))
        new_allowed_move = []

        # at this point we got all possible allowed_move

        # check additional rules

        for move in allowed_move:

            # check if path are free (now figure are there)

            # skip the move if there is a figure in the path

            path_moves = self.get_path_to_position(move[0], move[1])
            if len(path_moves) > 0:
                for path_move in path_moves:
                    if chessboard[path_move[0]][path_move[1]] is not None and isinstance(chessboard[path_move[0]][path_move[1]], Figure):
                        continue
                new_allowed_move.append(path_move)
        if self.color == "white":
            possible_capture_moves =  [(self.x-1,self.y+1), (self.x+1,self.y+1)]
            for possible_capture_move in possible_capture_moves:
                if 0 <= possible_capture_move[0] <= 7 and  0 <= possible_capture_move[1] <= 7:
                    if isinstance(chessboard[possible_capture_move[0]][possible_capture_move[1]], Figure):
                        if chessboard[possible_capture_move[0]][possible_capture_move[1]].color == 'black':
                            new_allowed_move.append(possible_capture_move)
        if self.color == "black":
            possible_capture_moves =  [(self.x-1,self.y-1), (self.x+1,self.y-1)]
            for possible_capture_move in possible_capture_moves:
                if 0 <= possible_capture_move[0] <= 7 and 0 <= possible_capture_move[1] <= 7:
                    print("possible_capture_move", possible_capture_move)
                    if isinstance(chessboard[possible_capture_move[0]][possible_capture_move[1]], Figure):
                        if chessboard[possible_capture_move[0]][possible_capture_move[1]].color == 'white':
                            new_allowed_move.append(possible_capture_move)
        return new_allowed_move

class Knight(Figure):
    def __init__(self,color, x ,y):
        super().__init__(color, x ,y)
    def list_allowed_moves(self, chessboard):
        allowed_move = []
        X = [2, 1, -1, -2, -2, -1, 1, 2]
        Y = [1, 2, 2, 1, -1, -2, -2, -1]
        for i in range(8):
            x = self.x+ X[i]
            y = self.y + Y[i]
            if 0 <= x < 8 and 0 <= y < 8:
                allowed_move.append((x,y))
            return allowed_move

class Rook(Figure):
    def __init__(self,color, x ,y):
        super().__init__(color, x ,y)
    def list_allowed_moves(self, chessboard):
        allowed_move = []
        # move horizontal - x the same, y changed
        for Y in range(8):
            if self.y != Y:
                allowed_move.append((self.x, Y))
        # move vertical - x changed, y the same
        for X in range(8):
            if self.x != X:
                allowed_move.append((X, self.y))
        return allowed_move

class King(Figure):
    def __init__(self,color, x ,y):
        super().__init__(color, x ,y)

    def list_allowed_moves(self, chessboard):
        allowed_move = []
        X = [1, -1,0, 0, 1, -1, -1, 1]
        Y = [0, 0, 1, -1, 1, -1,  1, -1]

        for i in range(8):
            x = self.x+ X[i]
            y = self.y + Y[i]
            if 0 <= x < 8 and 0 <= y < 8:
                allowed_move.append((x,y))
        return allowed_move

class Bishop(Figure):
    def __init__(self,color, x ,y):
        super().__init__(color, x ,y)

    def list_allowed_moves(self, chessboard):
        allowed_move = set()

        for i in range(1,8):
            x = self.x+ i
            y = self.y + i
            if 0 <= x < 8 and 0 <= y < 8:
                allowed_move.add((x,y))

        for i in range(1,8):
            x = self.x - i
            y = self.y - i
            if 0 <= x < 8 and 0 <= y < 8:
                allowed_move.add((x,y))

        for i in range(1,8):
            x = self.x+ i
            y = self.y - i
            if 0 <= x < 8 and 0 <= y < 8:
                allowed_move.add((x,y))

        for i in range(1,8):
            x = self.x- i
            y = self.y + i
            if 0 <= x < 8 and 0 <= y < 8:
                allowed_move.add((x,y))

        return list(allowed_move)

class Queen(Figure):

    def __init__(self,color, x ,y):
        super().__init__(color, x ,y)

    def list_allowed_moves(self, chessboard):
        allowed_move = set()
        for i in range(1,8):
            x = self.x+ i
            y = self.y + i
            if 0 <= x < 8 and 0 <= y < 8:
                allowed_move.add((x,y))

        for i in range(1,8):
            x = self.x - i
            y = self.y - i
            if 0 <= x < 8 and 0 <= y < 8:
                allowed_move.add((x,y))

        for i in range(1,8):
            x = self.x+ i
            y = self.y - i
            if 0 <= x < 8 and 0 <= y < 8:
                allowed_move.add((x,y))

        for i in range(1,8):
            x = self.x- i
            y = self.y + i
            if 0 <= x < 8 and 0 <= y < 8:
                allowed_move.add((x,y))

        # move horizontal - x the same, y changed
        for Y in range(8):
            if self.y != Y:
                allowed_move.add((self.x, Y))

        # move vertical - x changed, y the same
        for X in range(8):
            if self.x != X:
                allowed_move.add((X, self.y))
        return list(allowed_move)