# import module from parent directory
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from typing import List, Tuple
from helper.input import Input
from helper.pretty import Pretty

pretty = Pretty(False)

def solve(fn: str):
    input_raw: Input = Input(currentdir, fn)
    print(input_raw)
    input: List[str] = input_raw.get_lines()
    cmds: Tuple[str, int] = parse_commands(input)
    # Task 1
    find_final_position_simple(cmds)
    # Task 2
    find_final_position_complex(cmds)
 

def parse_commands(lines: List[str]) -> Tuple[str, int]:
    # this could be a oneliner 
    cmds = [x.split(' ') for x in lines]
    cmds = [(x[0],int(x[1])) for x in cmds]
    return cmds

def find_final_position_simple(commands: Tuple[str, int]) -> None:
    # up -> - depth, down -> + depth, forward -> + horiz
    horizontal = depth = 0
    for cmd in commands:
        if cmd[0] == 'up':
            depth -= cmd[1]
        elif cmd[0] == 'down':
            depth += cmd[1]
        elif cmd[0] == 'forward':
            horizontal += cmd[1]
        else:
            raise ValueError(f"Invalid direction found: {cmd[0]}")
        pretty.print(f"Command: {cmd} -> New Position: Horizontal {horizontal} Depth {depth}")
    print(f"Final position: Depth {depth}, Horizonal: {horizontal}")
    print(f"Result: {horizontal * depth}")

def find_final_position_complex(commands: Tuple[str, int]) -> None:
    # up -> - depth, down -> + depth, forward -> + horiz
    horizontal = depth = aim = 0
    for cmd in commands:
        if cmd[0] == 'up':
            aim -= cmd[1]
        elif cmd[0] == 'down':
            aim += cmd[1]
        elif cmd[0] == 'forward':
            horizontal += cmd[1]
            depth += cmd[1] * aim 
        else:
            raise ValueError(f"Invalid direction found: {cmd[0]}")
        pretty.print(f"Command: {cmd} -> New Position: Horizontal: {horizontal} Depth: {depth} Aim: {aim}")
    print(f"Final position: Horizonal: {horizontal}, Depth {depth}, Aim: {aim}")
    print(f"Result: {horizontal * depth}")



solve("example.txt")
solve("input.txt")

