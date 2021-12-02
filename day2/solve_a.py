NICE_OUTPUT = False

def nice_print(str):
    if NICE_OUTPUT:
        print(str)

def solve_example():
    fn = "example.txt"
    with open(fn) as input:
        print(f"Input: {fn}")
        find_final_position(input)

def solve_task():
    fn = "input.txt"
    with open(fn) as input:
        print(f"Input: {fn}")
        find_final_position(input)

def find_final_position(input_raw):
    cmd_strings = [x.strip() for x in input_raw.readlines()]
    cmds = [x.split(' ') for x in cmd_strings]
    cmds = [[x[0],int(x[1])]  for x in cmds]
    # up -> - depth, down -> + depth, forward -> + horiz
    horizontal = depth = 0
    for cmd in cmds:
        if cmd[0] == 'up':
            depth -= cmd[1]
        elif cmd[0] == 'down':
            depth += cmd[1]
        elif cmd[0] == 'forward':
            horizontal += cmd[1]
        else:
            raise ValueError(f"Invalid direction found: {cmd[0]}")
        nice_print(f"Command: {cmd} -> New Position: Horizontal {horizontal} Depth {depth}")
    print(f"Final position: Depth {depth}, Horizonal: {horizontal}")
    print(f"Result: {horizontal * depth}")

solve_example()
solve_task()