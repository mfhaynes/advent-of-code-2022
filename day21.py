import sys
import time

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

def calculate(data, i=False):
    completed = {}
    incomplete = {}
    for row in data:
        name = row[0:4]
        operation = row[6:]
        try:
            operation = int(operation)
        except:
            incomplete[name] = operation
        else:
            completed[name] = operation
    if i is not False:
        completed['humn'] = i    
    while len(incomplete) > 0:
        round_completed = []
        for monkey in incomplete.keys():
            operation = incomplete[monkey]
            dependencies = (operation[0:4], operation[7:11])
            if dependencies[0] in completed.keys() and dependencies[1] in completed.keys():
                operation = operation.replace(operation[0:4], str(completed[dependencies[0]]))
                operation = operation.replace(operation[operation.find(' ')+3:], str(completed[dependencies[1]]))             
                result = int(eval(operation))
                completed[monkey] = result
                round_completed.append(monkey)
        for val in round_completed:
            del incomplete[val]        
    return completed
        
def step_1 (data):     
    return calculate(data)['root']

def sign (val1, val2):
    if val1 > val2:
        return 1
    else:
        return -1
    
def step_2 (data):
    for row in data:
        if row[0:4] == 'root':
            keyvals = (row[6:10], row[13:])
    lastval = 1
    inval = 1
    loop = True 
    results = calculate(data,inval)
    firstsign = sign(results[keyvals[0]], results[keyvals[1]])     
    while loop:
        results = calculate(data,inval)        
        if lastval > 1 and lastval == inval:         
            break
        if results[keyvals[0]] == results[keyvals[1]]:
            loop = False
        elif sign(results[keyvals[0]], results[keyvals[1]]) == firstsign:
            lastval = inval
            inval = inval * 2
        else:
            hold = inval
            inval = inval - abs(int(((inval-lastval)/2)))
            lastval = hold
    for i in range(inval-20,inval+20):
        results = calculate(data,i)
        if (results[keyvals[0]] == results[keyvals[1]]):
            break 
    return i

if __name__ == '__main__':
    data = read_data(sys.argv[1], False, False)
    results = ''
    if sys.argv[2] == '1':
        results = step_1(data)
    else:
        results = step_2(data)
    print(results) 
