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

def parse_data (data):
    diagram = []
    columns = []
    moves = []
    in_diagram = True
    for row in data:
        if columns == []:
            for i in range(0,len(row),4):
                columns.append(LifoQueue(maxsize=2000))
        if not row:
            in_diagram = False
        else:
            if in_diagram and '[' in row:
                diagram.append(row)
            else:
                if not in_diagram:
                    moves.append(row)
    for i in range(len(diagram)):
        row = diagram.pop()
        for i in range(0,round(len(row)/4)):
            if row[(i*4)+1] != ' ':
                columns[i].put(row[(i*4)+1])            
    return columns, moves
    

def step_1 (data):
    result = ''
    columns, moves = parse_data(data)
    for move in moves:
        elements = move.split(' ')
        qty = int(elements[1])
        source = int(elements[3])
        target = int(elements[5])
        for i in range(0,qty):
            val = columns[source-1].get(False)
            columns[target-1].put(val)
    for column in columns:
        result = result + column.get(False)    
    return result

def step_2 (data):   
    result = ''
    columns, moves = parse_data(data)
    for move in moves:
        elements = move.split(' ')
        qty = int(elements[1])
        source = int(elements[3])
        target = int(elements[5])
        tempstack = LifoQueue(maxsize=2000)
        for i in range(0,qty):
            val = columns[source-1].get(False)
            tempstack.put(val)
        for i in range(0,qty):
            val = tempstack.get(False)
            columns[target-1].put(val)            
    for column in columns:
        result = result + column.get(False)    
    return result

if __name__ == '__main__':
    data = read_data(sys.argv[1], False, False)
    results = ''
    if sys.argv[2] == '1':
        results = step_1(data)
    else:
        results = step_2(data)
    print(results) 
