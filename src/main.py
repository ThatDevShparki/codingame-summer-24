# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

from __future__ import annotations

import sys
from enum import Enum
from typing import Any

MAX_PLAYERS = 3


def debug(*args: Any, **kwargs: Any):
    print(*args, **kwargs, file=sys.stderr)


class Scores:
    scores: list[int] | None = None

    def __init__(self, scores: list[int]):
        self.scores = scores

    @classmethod
    def read(cls) -> Scores:
        _scores = []
        for _ in range(MAX_PLAYERS):
            _values = input().split()
            _scores.append([int(s) for s in _values])
        return Scores(_scores)


class GameRegister:
    gpu: str | None = None
    registers: list[int] | None = None

    def __init__(self, gpu: str, registers: list[int]):
        self.gpu = gpu
        self.registers = registers

    @classmethod
    def read(cls) -> GameRegister:
        inputs = input().split()
        _gpu = inputs[0]
        _registers = [int(s) for s in inputs[1:]]
        return GameRegister(_gpu, _registers)


class GameState:
    player_idx: int | None = None
    nb_games: int | None = None

    scores: Scores | None = None
    registers: list[GameRegister] | None = None

    def __init__(self, player_idx: int, nb_games: int):
        self.player_idx = player_idx
        self.nb_games = nb_games

    def tick(self):
        self.scores = Scores.read()
        self.registers = (
            [GameRegister.read() for _ in range(self.nb_games)] if self.nb_games else []
        )

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
