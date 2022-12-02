def get_total_calories(file):
    result = []
    with open(file) as f:
        #print([x.split('\n') for x in f.read().split('\n\n')])
        data = f.read().splitlines()
    i = 0
    sum = 0
    for j in range(len(data)):
        if data[j]:
            sum += int(data[j])
        else:
            result.append(sum)
            sum = 0
            i += 1
    return result



if __name__ == '__main__':
    tot_cal = get_total_calories('input.txt')
    sorted_cal = sorted(tot_cal,reverse=True)
    #task 1
    print(sorted_cal[0])
    #task 2
    print(sum(sorted_cal[0:3]))