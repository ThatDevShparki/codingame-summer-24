# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

from __future__ import annotations

import sys
from enum import Enum
from typing import Any

MAX_PLAYERS = 3


def debug(*args: Any, **kwargs: Any):
    print(*args, **kwargs, file=sys.stderr)


class Score:
    total: int
    gold: int
    silver: int
    bronze: int

    def __init__(self, total: int, gold: int, silver: int, bronze: int):
        self.total = total
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    @classmethod
    def read(cls) -> Score:
        _values = [int(s) for s in input().split()]
        return Score(*_values)


class Register:
    gpu: str
    registers: list[int]

    def __init__(self, gpu: str, registers: list[int]):
        self.gpu = gpu
        self.registers = registers

    def get_pos_and_stun_for_player(self, player_idx: int) -> tuple[int, int]:
        # Returns position and stun timer
        return (self.registers[player_idx], self.registers[player_idx + MAX_PLAYERS])

    @classmethod
    def read(cls) -> Register:
        inputs = input().split()
        _gpu = inputs[0]
        _registers = [int(s) for s in inputs[1:]]
        return Register(_gpu, _registers)


class GameState:
    player_idx: int
    nb_games: int

    scores: list[Score]
    registers: list[Register]

    def get_player_score(self) -> Score:
        return self.scores[self.player_idx]

    def get_player_pos_stun_for_game(self, game_idx: int) -> tuple[int, int]:
        return self.registers[game_idx].get_pos_and_stun_for_player(self.player_idx)

    def __init__(self, player_idx: int, nb_games: int):
        self.player_idx = player_idx
        self.nb_games = nb_games

    def tick(self):
        self.scores = [Score.read() for _ in range(MAX_PLAYERS)]
        self.registers = [Register.read() for _ in range(self.nb_games)]

    @classmethod
    def read(cls) -> GameState:
        _player_idx = int(input())
        _nb_games = int(input())
        return GameState(_player_idx, _nb_games)


class Command(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    UP = "UP"
    DOWN = "DOWN"


class Game:
    state: GameState | None = None
    outputQueue: list[Command] = []

    def __init__(self, state: GameState):
        self.state = state

    def tick(self):
        if self.state is None:
            return

        self.state.tick()
        self.play()

        while self.outputQueue:
            print(self.outputQueue.pop(0).value)

    def do(self, command: Command):
        self.outputQueue.append(command)

    def play(self):
        self.do(Command.LEFT)

    @classmethod
    def read(cls) -> Game:
        _state = GameState.read()
        return Game(_state)


if __name__ == "__main__":
    game = Game.read()

    while True:
        game.tick()
