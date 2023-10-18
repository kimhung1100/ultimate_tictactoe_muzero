import os

os.environ["OMP_NUM_THREADS"] = "1"
from utilities import *
from network import *
import config
from typing import Dict, List, Optional
import math
import numpy as np
import torch
from torch.utils.data import Subset
import torch.multiprocessing as mp
import ray
import subprocess
import fnmatch
from tqdm import tqdm
import random

from utttpy.game.action import (
    Action,
)
from utttpy.game.ultimate_tic_tac_toe import UltimateTicTacToe

torch.manual_seed(1261)
random.seed(1261)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# MuZero training is split into two independent parts: Network training and
# self-play data generation.
def muzero():
    ray.init()
    replay_buffer = ReplayBuffer.remote()

    network, optimizer = load_model()
    network_id = ray.put(network.state_dict())
    storage = SharedStorage(network_id)
    for _ in range(os.cpu_count() - 2):
        run_selfplay.remote(network, storage, replay_buffer)

    while not ray.get(replay_buffer.ready.remote()):
        time.sleep(5)

    train_network(network, optimizer, storage, replay_buffer)
