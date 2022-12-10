def solve(input):
    X_dict = {}
    cycle = 1
    X = 1
    X_dict[1] = X
    instruction_list = []
    with open(input) as f:
        data = [x.split() for x in f.read().split('\n')]
        del data[-1]
    while cycle < 240:
        if len(data) > 0:
            instruction = data.pop(0)
            if instruction[0] == 'noop':
                instruction_list.append(0)
            else: #addx
                to_add = int(instruction[-1])
                instruction_list.append(0) ; instruction_list.append(to_add)
        if len(instruction_list) > 0:
            X += instruction_list.pop(0)
        cycle += 1
        X_dict[cycle] = X
    return X_dict

def signal_strengths(X_dict):
    sum = 0
    for i in range(20,221,40):
        sum += X_dict[i]*i
    return sum

def crt(X_dict):
    str = ""
    cycle = 0
    for _,X in X_dict.items():
        xrange = [X-1,X,X+1]
        if cycle in xrange:
            str +='#'
        else:
            str +='.'
        cycle = (cycle+1)%40
        if cycle == 0:
            str += '\n'
    return str

if __name__ == '__main__':
    X_dict = solve('input.txt')
    print(signal_strengths(X_dict))
    print(crt(X_dict))
    
#X value = index of middle of '###'
#if cycle = X value +- 1 then draw