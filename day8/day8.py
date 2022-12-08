import numpy as np

def solve(input):
    with open(input) as f:
        data = [list(map(int,x)) for x in f.read().split('\n')]
        del data[-1]
        data = np.array(data)
    inner_visible = 0
    scores = []
    for i in range(1,len(data)-1):
        for j in range(1,len(data[0])-1):
            inner_visible += is_visible(data,i,j)
            scores.append(scenic_score(data,i,j))
    total_visible = 2*len(data) + 2*len(data[0]) - 4 + inner_visible
    return total_visible, max(scores)

def is_visible(arr,i,j):
    size = arr[i,j]
    top = arr[0:i,j] #from top
    left = arr[i,0:j] #from left
    right = arr[i,j+1:len(arr)]
    bottom = arr[i+1:len(arr),j]
    if all(top<size) or all(left<size) or all(right<size) or all(bottom<size):
        return 1
    return 0

def scenic_score(arr,i,j):
    scores = []
    size = arr[i,j]
    top = arr[0:i,j]<size ; top = top[::-1]
    left = arr[i,0:j]<size ; left = left[::-1]
    right = arr[i,j+1:len(arr)]<size
    bottom = arr[i+1:len(arr),j]<size
    tree_list = [top,left,right,bottom]
    for l in tree_list:
        s_line = [i for i, x in enumerate(l) if not x]
        if len(s_line) == 0: #all true
            sc = len(l)
        else:
            sc = s_line[0]+1
        scores.append(sc)
    return np.prod(scores)

if __name__ == '__main__':
    print(solve('input.txt'))