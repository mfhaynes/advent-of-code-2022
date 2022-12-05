import sys

def read_data (filename, cast_to_int):
    with open(filename) as f:
        if cast_to_int is True:
            data = [int(line.strip()) for line in f.readlines()]
        else:
            data = [line.strip() for line in f.readlines()]
    return data

def step_1 (data):
    score = 0
    result_array = {'X': {'A': 4, 'B': 1, 'C': 7},
                    'Y': {'A': 8, 'B': 5, 'C': 2},
                    'Z': {'A': 3, 'B': 9, 'C': 6}}
    for row in data:
        hands = row.split(' ')
        score += result_array[hands[1]][hands[0]]
    return score

def step_2 (data):   
    score = 0
    result_array = {'X': {'A': 3, 'B': 1, 'C': 2},
                    'Y': {'A': 4, 'B': 5, 'C': 6},
                    'Z': {'A': 8, 'B': 9, 'C': 7}}
    for row in data:
        inputs = row.split(' ')
        score += result_array[inputs[1]][inputs[0]]
    return score     

if __name__ == '__main__':
    data = read_data(sys.argv[1], False)
    results = ''
    if sys.argv[2] == '1':
        results = step_1(data)
    else:
        results = step_2(data)
    print(results) 
