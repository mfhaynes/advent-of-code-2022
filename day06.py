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
    
def step_1 (data):
    result = 0
    signal=data[0]
    for i in range(len(signal)-4):
        if len(set([char for char in signal[i:i+4]])) == 4:
            result = i+4
            break     
    return result
    
def step_2 (data):
    result = 0
    signal=data[0]
    for i in range(len(signal)-14):
        if len(set([char for char in signal[i:i+14]])) == 14:
            result = i+14
            break     
    return result

if __name__ == '__main__':
    data = read_data(sys.argv[1], False, False)
    results = ''
    if sys.argv[2] == '1':
        results = step_1(data)
    else:
        results = step_2(data)
    print(results) 
