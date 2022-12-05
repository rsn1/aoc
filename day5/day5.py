def solve(input,task2):
    with open(input) as f:
        stack,lines = f.read().split("\n\n")
    lines = lines.splitlines()
    stack_info = stack.splitlines()
    n_stacks = int(stack_info[-1][-2])
    stack_height = len(stack_info)-1
    stacks = [[] for _ in range(n_stacks)]
    for idx in range(len(stack_info)):
        stackidx = stack_info[-1].index(str(idx+1))
        for i in range(stack_height):
            if stack_info[i][stackidx] != " ":
                stacks[idx].insert(0,stack_info[i][stackidx])        
    #stacks now formatted
    for line in lines:
        nbr,frm,to = [int(s) for s in line.split(" ") if s.isdigit()]
        frm -= 1 ; to -= 1
        if task2:
            stack_to_move = stacks[frm][-nbr:]
            del stacks[frm][-nbr:]
            for st in stack_to_move:
                stacks[to].append(st)
        else:
            for _ in range(nbr):
                stacks[to].append(stacks[frm].pop())
    return "".join([x[-1] for x in stacks])
    
if __name__ == '__main__':
    print(solve('input.txt',False))
    print(solve('input.txt',True))