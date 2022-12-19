import sys
import math
import datetime

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
    
def compare_arrays(left, right, index):
    for i in range(len(left)):
        leftval = left[i]
        try:
            rightval = right[i]
        except IndexError:
            return False
        if type(leftval) is int and type(rightval) is int:
            if rightval < leftval:
                return False
            elif rightval > leftval:
                return True
        else:
            if type(leftval) is int:
                leftval = [leftval]
            if type(rightval) is int:           
                rightval = [rightval]            
            if compare_arrays(leftval, rightval, index) is False:
                return False
            elif leftval != [] or rightval != []:
                return True
    return True
    
def step_1 (data):
    indexsum = 0
    for i in range(math.ceil(len(data)/3)):
        left_array = eval(data[i*3])
        right_array = eval(data[(i*3)+1])        
        if type(left_array) is int:
            left_array = [left_array]
        if type(right_array) is int:
            right_array = [right_array]            
        if compare_arrays(left_array, right_array, i+1):
            indexsum += (i+1)  
    return indexsum

def canonicalize_row(row_array):
    res = []
    for element in row_array:
        if type(element) is list:
            if element == []:
                res = res + [-1]
            else:
                res = res + canonicalize_row(element)
        else:
            res.append(element)
    return res        
    
def step_2 (data):
    before_packet1 = 0
    before_packet2 = 0  
    leaders = {}    
    for row in data:
        if row != '':
            try:
                leader = canonicalize_row(eval(row))[0]
            except IndexError:
                leader = 0
            try:
                leaders[leader] += 1
            except KeyError:
                leaders[leader] = 1
    runtot = 0
    runtots = []            
    for key in sorted(leaders.keys()):
        runtot += leaders[key]
        runtots.append(runtot)               
    return (runtots[2]+1) * (runtots[6]+2)

if __name__ == '__main__':
    data = read_data(sys.argv[1], False, False)
    results = ''
    if sys.argv[2] == '1':
        results = step_1(data)
    else:
        results = step_2(data)
    print(results) 