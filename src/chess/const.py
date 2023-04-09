WINDOW_WIDTH = 1050
WINDOW_HEIGHT = 800

#board
WIDTH = 800
HEIGHT = 800

#board 
ROWS = 8
COLS = 8

#squares
SQU_SIZE = WIDTH // COLS

#engine settings
FIND_TIME = 1250 #milliseconds
THREADS = 4 # < number of logical processors
HASH = 1024 #amount of allowed memory stockfish can use 

#more processing power for analysis
ANALISYS_THREADS = 16
ANALISYS_HASH = 16384

EVALUATION_SHALLOW_FIND_TIME = 35 #milliseconds
EVALUATION_DEEP_FIND_TIME = 55    #milliseconds