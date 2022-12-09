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
    sign = lambda a: (a>0) - (a<0)
    hpos=[0,0]
    tpos=[0,0]
    tpos_places={'0,0': 1}
    moves={'R':(1,0), 'L':(-1,0), 'U':(0,1), 'D':(0,-1)}
    for move in data:
        dir, dist = move.split(' ')       
        for i in range(int(dist)):
            hpos = [sum(x) for x in zip(*[hpos,moves[dir]])]
            if abs(hpos[0]-tpos[0]) > 1 or abs(hpos[1]-tpos[1]) > 1:
                tpos[0] = tpos[0] + (1 * sign(hpos[0]-tpos[0]))
                tpos[1] = tpos[1] + (1 * sign(hpos[1]-tpos[1]))
                try:
                    tpos_places[','.join([str(pos) for pos in tpos])] += 1
                except KeyError:
                    tpos_places[','.join([str(pos) for pos in tpos])] = 1
    return len(tpos_places.keys())
    
def step_2 (data):
    sign = lambda a: (a>0) - (a<0)
    positions = [[0,0] for i in range(10)]
    tpos_places={'0,0': 1}
    moves={'R':(1,0), 'L':(-1,0), 'U':(0,1), 'D':(0,-1)}
    for move in data:
        dir, dist = move.split(' ')   
        for i in range(int(dist)):
            adjustment=moves[dir]  
            for j in range(len(positions)-1):
                positions[j] = [sum(x) for x in zip(*[positions[j],adjustment])]
                if abs(positions[j][0]-positions[j+1][0]) >1 or abs(positions[j][1]-positions[j+1][1]) > 1:
                    adjustment=[(1 * sign(positions[j][0]-positions[j+1][0])), (1 * sign(positions[j][1]-positions[j+1][1]))]
                else:
                    adjustment=[0,0]
                    break
            positions[9] = [sum(x) for x in zip(*[positions[9],adjustment])]     
            try:
                tpos_places[','.join([str(pos) for pos in positions[9]])] += 1
            except KeyError:
                tpos_places[','.join([str(pos) for pos in positions[9]])] = 1
    return len(tpos_places.keys())

if __name__ == '__main__':
    data = read_data(sys.argv[1], False, False)
    results = ''
    if sys.argv[2] == '1':
        results = step_1(data)
    else:
        results = step_2(data)
    print(results)
