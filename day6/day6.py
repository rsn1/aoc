def unique(window):
    windowset = set(window)
    return len(windowset) == len(window)

def solve1(file):
    with open(file) as f:
        data = f.read()
    for i in range(0,len(data)-3):
        window = data[i:i+4]
        is_unique = unique(window)
        if is_unique:
            return i+4

def solve2(file):
    with open(file) as f: 
        data = f.read()
    for i in range(0,len(data)-13):
        window = data[i:i+14]
        is_unique = unique(window)
        if is_unique:
            return i+14

if __name__ == '__main__':
    print(solve1('input.txt'))
    print(solve2('input.txt'))