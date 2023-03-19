from src.game.const import *
from stockfish import Stockfish
stockfish = Stockfish(path=r"src\computer\engine.exe")

class Computer:
    def __init__(self):
        pass

    def best_move(self, fen):
        '''
        Returns a uci-style move using stockfish 15.1.3 (ex. 'e2e4')
        '''
        #uses stockfish 15.1.3 to calc best move - board fen needed
        stockfish.set_fen_position(fen)
        return stockfish.get_best_move_time(FIND_TIME)
    

    