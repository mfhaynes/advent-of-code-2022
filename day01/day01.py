import sys

def read_data (filename, cast_to_int):
    with open(filename) as f:
        if cast_to_int is True:
            data = [int(line.strip()) for line in f.readlines()]
        else:
            data = [line.strip() for line in f.readlines()]
    return data

def step_1 (data):
    maxcal = 0
    curcal = 0
    for row in data:
        if row == '':
            if curcal > maxcal:
                maxcal = curcal
            curcal = 0
        else:
            curcal = curcal + int(row)
    return maxcal

def step_2 (data):   
    calarray = []
    curcal = 0
    for row in data:
        if row == '':
            calarray.append(curcal)
            curcal = 0
        else:
            curcal = curcal + int(row)
    totcal = 0
    for val in sorted(calarray)[-3:]:
        totcal += val    
    return totcal     

if __name__ == '__main__':
    data = read_data(sys.argv[1], False)
    results = ''
    if sys.argv[2] == '1':
        results = step_1(data)
    else:
        results = step_2(data)
    print(results) 
