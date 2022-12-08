



















#dir d - directory d in current dir
#cd d - goes into d
#cd .. - up 1 lvl


#bug - same name different directories
def solve1(input):
    visited = set()
    dirsizes = {}
    dirs = ['/'] #dirs[-1] = current_dir
    with open(input) as f:
        data = f.read().split('\n')
        del data[-1]
        del data[0]
    #print(data)
    for idx,line in enumerate(data):
        split_line = line.split()
        #print(split_line)
        if split_line[0] == '$': #command
            if split_line[1] == 'cd':
                if split_line[2] == '..' and len(dirs) > 0:
                    dirs.pop()
                elif len(dirs) > 0: #go into dir
                    dirs.append(dirs[-1] + split_line[2])
            else: #ls
                dirsum = 0
                itidx = 1
                next_item = data[idx+itidx].split()
                while next_item[0] != '$':
                    if next_item[0].isdigit():
                        filepath = dirs[0] + '/'.join(dirs[1:]) + '/' + next_item[1]
                        if filepath not in visited: #file name
                              dirsum += int(next_item[0])
                              visited.add(filepath)
                    lend = len(data)
                    if idx+itidx+1 < lend:
                        itidx += 1
                        next_item = data[idx+itidx].split()
                    else:
                        break
                #all files accounted for, add to previous dirs
                for dir in dirs:
                    dirsizes[dir] = dirsizes.get(dir,0) + dirsum
    #solve tasks
    tot_sum = 0
    for k,v in dirsizes.items():
        if v <= 100000:
            tot_sum += v
    #print(visited)
    #
    unused = 70000000 - dirsizes[max(dirsizes)]
    space_needed = 30000000 - unused
    print(unused)
    print(space_needed)
    return tot_sum

if __name__ == '__main__':
    print(solve1('input.txt'))