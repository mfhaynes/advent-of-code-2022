import sys
from queue import LifoQueue

def read_data (filename, cast_to_int, strip_whitespace):
    with open(filename) as f:
        if cast_to_int is True:
            data = [int(line.strip()) for line in f.readlines()]
        else:
            if strip_whitespace:
                data = [line.strip() for line in f.readlines()]
            else:
                data = [line[:-1] for line in f.readlines()]                
    return data
    
def parse_data(data):
    dirsizes = {}
    path=['/']
    for row in data:
        if row[0:1] == '$':
            if row[2:4] == 'cd':
                if row[5:7] == '..':
                    path.pop()
                else:
                    path.append('{}/'.format(row[5:]))
        else:
            if row[0:3] != 'dir':
                size=int(row.split(' ')[0])
                for i in range(len(path)):
                    try:
                        dirsizes[''.join(path[:i+1])] += size
                    except KeyError:
                        dirsizes[''.join(path[:i+1])] = size
    return dirsizes                    
    
def step_1 (data):
    dirsizes = parse_data(data)
    totsize = 0
    for dir in dirsizes.keys():
        if dirsizes[dir] < 100000:
            totsize += dirsizes[dir]        
    return totsize
    
def step_2 (data):
    dirsizes = parse_data(data)
    totdisk = 70000000
    needdisk = 30000000
    freedisk = totdisk - dirsizes['/']
    mindelete = needdisk-freedisk
    deletesize = totdisk
    for dir in dirsizes.keys():
        if dirsizes[dir] > mindelete and dirsizes[dir] < deletesize:
            deletesize = dirsizes[dir]        
    return deletesize

if __name__ == '__main__':
    data = read_data(sys.argv[1], False, False)
    results = ''
    if sys.argv[2] == '1':
        results = step_1(data)
    else:
        results = step_2(data)
    print(results) 
