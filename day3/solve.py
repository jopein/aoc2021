# import module from parent directory
import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from typing import List
import copy
from helper.input import Input
from helper.pretty import Pretty

pretty = Pretty(False)


def solve(fn: str):
    input_raw: Input = Input(currentdir, fn)
    print(input_raw)
    input: List[str] = input_raw.get_lines()
    # Task 1
    find_power_consumption(input)
    # Task 2
    find_life_support_rating(input)


def find_power_consumption(lines: List[str]) -> None:
    word_length = len(lines[0])
    # init lists with size(word_length)
    ctr_1 = [0] * word_length
    ctr_0 = [0] * word_length
    # count occurances of 0 / 1 in each position
    # this would be waaay faster with int(line, 2) and modulo.
    for line in lines:
        for pos in range(0, word_length):
            if line[pos] == "1":
                ctr_1[pos] += 1
            else:
                ctr_0[pos] += 1
    # build most / least common (inverted binary)
    # also, doing this in strings in slow.
    most_common = []
    least_common = []
    for pos in range(0, word_length):
        if ctr_1[pos] > ctr_0[pos]:
            most_common.append("1")
            least_common.append("0")
        else:
            most_common.append("0")
            least_common.append("1")
    # binary -> int
    epsilon_rate = int("".join(most_common), 2)
    gamma_rate = int("".join(least_common), 2)
    print(
        f"Most Common: {epsilon_rate}, Least Common: {gamma_rate}, Power Usage: {epsilon_rate*gamma_rate}"
    )


def find_life_support_rating(lines: List[str]) -> None:
    # we need to copys of the list, as the list is changed in the progress
    # recursion instead of iteration might also be a good idea
    oxy_lines = lines
    co2_lines = copy.deepcopy(lines)
    word_length = len(lines[0])
    # find oxy rating
    for i in range(0, word_length):
        oxy_lines = filter_list(i, oxy_lines, True)
        if len(oxy_lines) == 1:
            break
    # find co2 rating
    for i in range(0, word_length):
        co2_lines = filter_list(i, co2_lines, False)
        if len(co2_lines) == 1:
            break
    # binary -> int
    oxygen_generator_rating = int(oxy_lines[0], 2)
    co2_scrubbing_rating = int(co2_lines[0], 2)
    print(
        f"Oxygen rating: {oxygen_generator_rating}, CO2 rating: {co2_scrubbing_rating}, Life support rating: {oxygen_generator_rating*co2_scrubbing_rating}"
    )


def filter_list(pos: int, lines: List[str], isOxyMode: bool) -> List[str]:
    pretty.print(f"Filtering list at position: {pos} with mode {isOxyMode}")
    # count occurances
    cnt_1 = cnt_0 = 0
    for line in lines:
        if line[pos] == "1":
            cnt_1 += 1
        else:
            cnt_0 += 1

    # find criteria
    criteria = None
    # oxy
    if isOxyMode:
        if cnt_1 > cnt_0:
            criteria = "1"
        elif cnt_1 < cnt_0:
            criteria = "0"
        else:
            criteria = "1"
    # co2
    else:
        if cnt_1 < cnt_0:
            criteria = "1"
        elif cnt_1 > cnt_0:
            criteria = "0"
        else:
            criteria = "0"
    pretty.print(f"0s: {cnt_0}, 1s: {cnt_1}, Criteria is: {criteria}")

    # actual line filtering
    matching_lines = []
    for line in lines:
        if line[pos] == criteria:
            matching_lines.append(line)
    pretty.print(f"Current list: {matching_lines}")
    return matching_lines


solve("example.txt")
solve("input.txt")
