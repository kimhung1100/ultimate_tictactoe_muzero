from muzero_baseline.muzero import MuZero
from tictactoe import *

# Initialize config
config = MuZeroConfig()
# Game object will be initialized in each thread separetly
mz = MuZero(TicTacToe, config)

mz.train()
