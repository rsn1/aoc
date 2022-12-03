import string

lcase_map = {c:i+1 for i,c in enumerate(string.ascii_lowercase)}
ucase_map = {c:i+27 for i,c in enumerate(string.ascii_uppercase)}

def solve1(input):
    tot_prio = 0
    with open(input) as f:
        data = f.read().split('\n')
        del data[-1]
    for line in data:
        lhalf = set(line[:int(len(line)/2)])
        rhalf = set(line[int(len(line)/2):])
        citem = lhalf.intersection(rhalf).pop()
        if citem.isupper():
            tot_prio += ucase_map[citem]
        else:
            tot_prio += lcase_map[citem]
    return tot_prio

def solve2(input):
    tot_prio = 0
    with open(input) as f:
        data = f.read().split('\n')
        del data[-1]
    for i in range(0,len(data)-2,3):
        citem = set(data[i]).intersection(set(data[i+1])).intersection(set(data[i+2])).pop()
        if citem.isupper():
            tot_prio += ucase_map[citem]
        else:
            tot_prio += lcase_map[citem]
    return tot_prio

if __name__ == '__main__':
    print(solve1('input.txt'))
    print(solve2('input.txt'))

