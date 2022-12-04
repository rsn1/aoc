def solve1(input):
    tot_sum = 0
    with open(input) as f:
        data = [y.split('-') for x in f.read().split('\n') for y in x.split(',')]
        del data[-1]
    for i in range(0,len(data)-1,2):
        r1s = int(data[i][0]) ; r1e = int(data[i][-1])
        r2s = int(data[i+1][0]) ; r2e = int(data[i+1][-1])
        if is_fully_contained(r1s,r1e,r2s,r2e):
            tot_sum += 1
    return tot_sum

def solve2(input):
    tot_sum = 0
    with open(input) as f:
        data = [y.split('-') for x in f.read().split('\n') for y in x.split(',')]
        del data[-1]
    for i in range(0,len(data)-1,2):
        r1s = int(data[i][0]) ; r1e = int(data[i][-1])
        r2s = int(data[i+1][0]) ; r2e = int(data[i+1][-1])
        if overlap(r1s,r1e,r2s,r2e):
            tot_sum += 1
    return tot_sum

def is_fully_contained(r1s,r1e,r2s,r2e):
    if (r2s >= r1s and r2e <= r1e) or (r1s >= r2s and r1e <= r2e):
        return True
    return False

def overlap(r1s,r1e,r2s,r2e):
    if r2s > r1e or r2e < r1s:
        return False
    return True

if __name__ == '__main__':
    print(solve1('input.txt'))
    print(solve2('input.txt'))