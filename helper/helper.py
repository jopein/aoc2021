from io import TextIOWrapper
from typing import List

class Input:

    filename: str
    source: TextIOWrapper

    def __init__(self, currentdir: str, filename: str):
        print(currentdir, filename)
        self.filename = filename

    def get_lines(self) -> List[str]:
        with open(self.filename) as input:
            return [x.strip() for x in input]

    def get_2d_ints(self) -> List[List[int]]:
        with open(self.filename) as input:
            return [[int(y) for y in x.strip()] for x in input]

    def get_1d_ints_from_list(self) -> List[int]:
        with open(self.filename) as input:
            return [int(x) for x in input]

    def __repr__(self):
        return f"Filename: {self.filename}"

class Pretty:

    is_on: bool

    def __init__(self, is_on: bool):
        self.is_on = is_on

    @staticmethod
    def print(self, msg: str) -> None:
        if self.is_on:
            print(msg)
