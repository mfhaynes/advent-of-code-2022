import sys
import datetime

def test_setup():
    data = [20,
            (2,18,-2,15),
            (9,16,10,16),
            (13,2,15,3),
            (12,14,10,16),
            (10,20,10,16),
            (14,17,10,16),
            (8,7,2,10),
            (2,0,2,10),
            (0,11,2,10),
            (20,14,25,17),
            (17,20,21,22),
            (16,7,15,3),
            (14,3,15,3),
            (20,1,15,3)]       
    return data            
    
def puzzle_setup():
    data = [4000000,
            (2692921,2988627,2453611,3029623),
            (1557973,1620482,1908435,2403457),
            (278431,3878878,-1050422,3218536),
            (1432037,3317707,2453611,3029623),
            (3191434,3564121,3420256,2939344),
            (3080887,2781756,3420256,2939344),
            (3543287,3060807,3420256,2939344),
            (2476158,3949016,2453611,3029623),
            (3999769,3985671,3420256,2939344),
            (2435331,2200565,1908435,2403457),
            (3970047,2036397,3691788,1874066),
            (2232167,2750817,2453611,3029623),
            (157988,333826,-1236383,477990),
            (1035254,2261267,1908435,2403457),
            (1154009,888885,1070922,-543463),
            (2704724,257848,3428489,-741777),
            (3672526,2651153,3420256,2939344),
            (2030614,2603134,1908435,2403457),
            (2550448,2781018,2453611,3029623),
            (3162759,2196461,3691788,1874066),
            (463834,1709480,-208427,2000000),
            (217427,2725325,-208427,2000000),
            (3903198,945190,3691788,1874066)]      
    return data        
    
    
def step_1 (data):
    boundaries = [val for val in data[1]]
    keyrowindex = data[0]
    keyrowbeacons = set([row[2] for row in data[1:] if row[3] == keyrowindex])
    invalidlocs = {}
    for row in data[1:]:
        boundaries = [min(boundaries[0], row[0], row[2]), min(boundaries[1], row[1], row[3]), max(boundaries[2], row[0], row[2]), max(boundaries[3], row[1], row[3])]
    keyrow = [0 for i in range(boundaries[0], boundaries[2]+1)]   
    for row in data[1:]: 
        dist = abs(row[0]-row[2]) + abs(row[1]-row[3])
        if keyrowindex > row[1]-dist and keyrowindex < row[1]+dist:
            minv = row[0]-(dist-abs(keyrowindex-row[1]))
            maxv = row[0]+(dist-abs(keyrowindex-row[1]))
            for i in range(minv,maxv+1):
                invalidlocs[i] = True
    return len(invalidlocs.keys())-len(keyrowbeacons)

def consolidate_array(current,addition):
    output = []
    if current == []:
        output.append(addition)
        return output
    for value in current:
        covered = 0
        disjoint = 0
        if addition[0] >= value[0] and addition[1] <= value[1]:
            covered += 1
        if addition[1] < value[0]-1 or addition[0] > value[1]+1:
            disjoint += 1      
    if covered == (len(current)):
        return current        
    if covered+disjoint == len(current):        
        current.append(addition)
        return current
    disjoint = 0    
    for value in current:
        if addition[0] <= value[0] and addition[1] >= value[1]:
            output.append(addition)
        elif addition[0] >= value[0] and addition[1] <= value[1]: 
            output.append(value)
        elif addition[1] < value[0]-1 or addition[0] > value[1]+1:
            output.append(value)
            disjoint += 1
        elif addition[0] < value[0]:
            output.append([addition[0], max(addition[1],value[1])])
        else:
            output.append([min(addition[0],value[0]), addition[1]])
    if disjoint == len(current):
        output.append(addition)    
    finalout = []
    for value in output:
        if value not in finalout:
            finalout.append(value)        
    return finalout  

def consolidator(input, stop_flag = False):
    output = []
    for array in input:
        output = consolidate_array(output, array)
    if len(output) < len(input):
        output = consolidator(output, stop_flag)
    else:
        if stop_flag is False:
            stop_flag = True
            output = consolidator(output, stop_flag)  
    return output        
    
def step_2 (data):
    boundaryval = data[0]
    keyrows = [[] for i in range(boundaryval+1)]
    for row in data[1:]:
        if row[3] > 0 and row[3] <= boundaryval and row[2] > 0 and row[2] <= boundaryval:
            keyrows[row[3]].append([row[2], row[2]])
    rowcount = 0     
    for row in data[1:]:
        rowcount += 1
        dist = abs(row[0]-row[2]) + abs(row[1]-row[3])
        j = 0
        if row[1] < dist:
            j += dist-row[1]
        for i in range(max(0,row[1]-dist), min(boundaryval+1,row[1]+dist+1)):
            keyrows[i].append([max(0, row[0]-j), min(boundaryval, row[0]+j)])
            if i < row[1]:
                j = j + 1
            else:
                j = j - 1   
    print(datetime.datetime.now())    
    for i in range(len(keyrows)):      
        results = consolidator(keyrows[i])
        if len(results) > 1:
            y = i
            x = results[0][1]+1
    return ((x*4000000)+y)

if __name__ == '__main__':
    results = ''
    if sys.argv[2] == '1':
        results = step_1(puzzle_setup())
    else:
        results = step_2(puzzle_setup())
    print(results) 