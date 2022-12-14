import sys

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
    x = 1
    cyc = 0
    test = 0
    strtot = 0
    for row in data:
        if row[0:4] == 'noop':
            cyc += 1
            if cyc%40 == 20:
                test = 1
                strtot += (cyc*x)
        else:
            cyc += 2
            if cyc%40 in [20,21]:
                test = 1
                if cyc%40 == 20:
                    strtot += (cyc*x)
                else:
                    strtot += ((cyc-1)*x)
            x += int(row[5:])                    
        if test == 1:
            test = 0
    return strtot
    
def step_2 (data):
    x = 1
    cyc = 0
    test = 0
    strtot = 0
    chars = []
    for row in data:
        if row[0:4] == 'noop':
            if abs((x%40)-(cyc%40)) < 2:
                chars.append('#')
            else:
                chars.append('.')            
            cyc += 1
        else:
            if abs((x%40)-(cyc%40)) < 2:
                chars.append('#')
            else:
                chars.append('.')            
            cyc += 1
            if abs((x%40)-(cyc%40)) < 2:
                chars.append('#')
            else:
                chars.append('.')                      
            cyc += 1
            x += int(row[5:])
    for i in range(6):
        offset = i*40
        print(''.join(chars[0+offset:39+offset]))
    return strtot

if __name__ == '__main__':
    data = read_data(sys.argv[1], False, False)
    results = ''
    if sys.argv[2] == '1':
        results = step_1(data)
    else:
        results = step_2(data)
    print(results) 