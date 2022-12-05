import sys

def read_data (filename, cast_to_int):
    with open(filename) as f:
        if cast_to_int is True:
            data = [int(line.strip()) for line in f.readlines()]
        else:
            data = [line.strip() for line in f.readlines()]
    return data

def step_1 (data):
    counter = 0   
    for row in data:
        assignments=[[int(val) for val in elfdata.split('-')] for elfdata in row.split(',')]
        if (assignments[0][0] >= assignments[1][0] and assignments[0][1] <= assignments[1][1]) or (assignments[1][0] >= assignments[0][0] and assignments[1][1] <= assignments[0][1]):
            counter += 1
    return counter

def step_2 (data):   
    counter = 0   
    for row in data:
        assignments=[[int(val) for val in elfdata.split('-')] for elfdata in row.split(',')]
        if assignments[0][0] in range(assignments[1][0], assignments[1][1]+1) or assignments[0][1] in range(assignments[1][0], assignments[1][1]+1) or assignments[1][0] in range(assignments[0][0], assignments[0][1]+1) or assignments[1][1] in range(assignments[0][0], assignments[0][1]+1):
            counter += 1
        else:
            print(assignments)        
    return counter

if __name__ == '__main__':
    data = read_data(sys.argv[1], False)
    results = ''
    if sys.argv[2] == '1':
        results = step_1(data)
    else:
        results = step_2(data)
    print(results) 
