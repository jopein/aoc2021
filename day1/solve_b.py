NICE_OUTPUT = True

def nice_print(str):
    if NICE_OUTPUT:
        print(str)

def solve_example():
    fn = "example.txt"
    with open(fn) as input:
        print(f"Input: {fn}")
        depths = parse_input(input)
        depth_windows = calc_windows_depths(depths)
        count_depth_increase(depth_windows)


def solve_task():
    fn = "input.txt"
    with open(fn) as input:
        print(f"Input: {fn}")
        depths = parse_input(input)
        depth_windows = calc_windows_depths(depths)
        count_depth_increase(depth_windows)

def parse_input(input_raw):
    return [int(x) for x in input_raw.readlines()]
    
def calc_windows_depths(depths):
    arr = []
    for i in range(0, len(depths)-2):
        sum = depths[i] + depths[i+1] +  depths[i+2]
        arr.append(sum)
        nice_print(f"{i}-{i+2} : [{depths[i]} + {depths[i+1]} + {depths[i+2]}] = {sum}")
    return arr

def count_depth_increase(depths):
    ctr = 0
    for i in range(0, len(depths)-1):
        depth_1, depth_2 = depths[i:i+2]
        if depth_2 > depth_1:
            ctr += 1
            nice_print(f"{i}-{i+2}:{depth_1} -> {i+1}-{i+3}:{depth_2} = ▲")
        else:
            nice_print(f"{i}-{i+2}:{depth_1} -> {i+1}-{i+3}:{depth_2} = ▼")
    print(f"Result: {ctr}")

solve_example()
solve_task()