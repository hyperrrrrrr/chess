class Square:

    def __init__(self, row, col, piece = None):
        self.row = row
        self.col = col
        self.piece = piece

    #equals method
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col



    def has_piece(self):
        return self.piece != None

    def is_empty(self):
        return not self.has_piece()
    
    def has_team_piece(self, color):
        return self.has_piece() and self.piece.color == color

    def has_enemy_piece(self, color):
        return self.has_piece() and self.piece.color != color

    def isempty_or_enemy(self, color):
        return self.is_empty() or self.has_enemy_piece(color)

    #can resive as many args as needed (call be called with class instance))
    @staticmethod
    def in_range(*args):
        for arg in args:
            if arg < 0 or arg > 7:
                return False
        return True
    

    