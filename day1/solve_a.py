NICE_OUTPUT = False

def nice_print(str):
    if NICE_OUTPUT:
        print(str)

def solve_example():
    fn = "example.txt"
    with open(fn) as input:
        print(f"Input: {fn}")
        count_depth_increase(input)

def solve_task():
    fn = "input.txt"
    with open(fn) as input:
        print(f"Input: {fn}")
        count_depth_increase(input)


def count_depth_increase(input):
    depths = [int(x) for x in input.readlines()]
    ctr = 0
    for i in range(0, len(depths)-1):
        depth_1, depth_2 = depths[i:i+2]
        if depth_2 > depth_1:
            ctr += 1
            nice_print(f"{i}:{depth_1} -> {i+1}:{depth_2} = ▲")
        else:
            nice_print(f"{i}:{depth_1} -> {i+1}:{depth_2} = ▼")
    print(f"Result: {ctr}")

solve_example()
solve_task()