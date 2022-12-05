import sys

def read_data (filename, cast_to_int):
    with open(filename) as f:
        if cast_to_int is True:
            data = [int(line.strip()) for line in f.readlines()]
        else:
            data = [line.strip() for line in f.readlines()]
    return data

def step_1 (data):
    totval = 0
    priority_dict={}
    for i in range(65,91):
        priority_dict[chr(i)] = i-38
    for i in range(97,123):
        priority_dict[chr(i)] = i-96        
    for row in data:
        midpoint = int(len(row)*.5)
        matches = [item for item in row[0:midpoint] if item in row[midpoint:]]
        totval += priority_dict[matches[0]]
    return totval

def step_2 (data):   
    totval = 0
    priority_dict={}
    for i in range(65,91):
        priority_dict[chr(i)] = i-38
    for i in range(97,123):
        priority_dict[chr(i)] = i-96     
    for i in range(0,len(data),3):
        matches = [item for item in data[i] if item in data[i+1] and item in data[i+2]]
        totval += priority_dict[matches[0]]  
    return totval     

if __name__ == '__main__':
    data = read_data(sys.argv[1], False)
    results = ''
    if sys.argv[2] == '1':
        results = step_1(data)
    else:
        results = step_2(data)
    print(results) 
