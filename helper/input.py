from io import TextIOWrapper
from typing import List
import os


class Input:

    filepath: str
    source: TextIOWrapper

    def __init__(self, currentdir: str, filename: str):
        self.filepath = os.path.join(currentdir, filename)

    def get_lines(self) -> List[str]:
        with open(self.filepath) as input:
            return [x.strip() for x in input]

    def get_2d_ints(self) -> List[List[int]]:
        with open(self.filepath) as input:
            return [[int(y) for y in x.strip()] for x in input]

    def get_1d_ints_from_list(self) -> List[int]:
        with open(self.filepath) as input:
            return [int(x.strip()) for x in input]

    def __repr__(self):
        return f"Filename: {self.filepath}"
