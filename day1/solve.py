# import module from parent directory
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from typing import List
from helper.input import Input
from helper.pretty import Pretty

pretty = Pretty(False)

def solve(fn: str):
    input_raw: Input = Input(currentdir, fn)
    print(input_raw)
    input: List[int] = input_raw.get_1d_ints_from_list()
    # Task 1
    count_depth_increase(input)
    # Task 2
    windows: List[int] = calc_depth_windows(input)
    count_depth_increase(windows)
 
def calc_depth_windows(depths: List[int]):
    result: List[int] = []
    for i in range(0, len(depths)-2):
        sum = depths[i] + depths[i+1] +  depths[i+2]
        result.append(sum)
        pretty.print(f"{i}-{i+2} : [{depths[i]} + {depths[i+1]} + {depths[i+2]}] = {sum}")
    return result

def count_depth_increase(depths: List[int]) -> None:
    ctr = 0
    for i in range(0, len(depths)-1):
        depth_1, depth_2 = depths[i:i+2]
        if depth_2 > depth_1:
            ctr += 1
            pretty.print(f"{i}:{depth_1} -> {i+1}:{depth_2} = ▲")
        else:
            pretty.print(f"{i}:{depth_1} -> {i+1}:{depth_2} = ▼")
    print(f"Result: {ctr}")

solve("example.txt")
solve("input.txt")

