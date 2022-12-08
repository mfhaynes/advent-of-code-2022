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
    dataheight = len(data)
    datawidth = len(data[0])
    invisible = 0
    for rownum in range(1,dataheight-1):
        for colnum in range(1,datawidth-1):
            left_tree_heights = [val for val in data[rownum][0:colnum]]
            right_tree_heights = [val for val in data[rownum][colnum+1:]]
            up_tree_heights = [val[colnum] for val in data[0:rownum]]
            down_tree_heights = [val[colnum] for val in data[rownum+1:]]           
            if (data[rownum][colnum] > max(left_tree_heights) or 
                data[rownum][colnum] > max(right_tree_heights) or
                data[rownum][colnum] > max(up_tree_heights) or
                data[rownum][colnum] > max(down_tree_heights)):
                   pass
            else:
               invisible += 1
    return (dataheight*datawidth) - invisible

def find_vision_distance(heights, myheight):
    counter = 0
    for height in heights:
        counter += 1
        if height >= myheight:
            break
    return counter
    
def step_2 (data):
    dataheight = len(data)
    datawidth = len(data[0])
    maxscore = 0
    for rownum in range(1,dataheight-1):
        for colnum in range(1,datawidth-1):
            left = find_vision_distance(reversed([val for val in data[rownum][0:colnum]]), data[rownum][colnum])
            right = find_vision_distance([val for val in data[rownum][colnum+1:]], data[rownum][colnum])
            up = find_vision_distance(reversed([val[colnum] for val in data[0:rownum]]), data[rownum][colnum])
            down = find_vision_distance([val[colnum] for val in data[rownum+1:]], data[rownum][colnum])
            if left*right*up*down > maxscore:
                maxscore = left*right*up*down
    return maxscore

if __name__ == '__main__':
    data = read_data(sys.argv[1], False, False)
    results = ''
    if sys.argv[2] == '1':
        results = step_1(data)
    else:
        results = step_2(data)
    print(results) 
