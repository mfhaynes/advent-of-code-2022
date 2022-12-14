import sys
import math
import datetime

def test_setup():
    data = [{'items': [79, 98], 'optype': 'multiply', 'opval': 19, 'test': 23, 'iftrue': 2, 'iffalse': 3},
            {'items': [54, 65, 75 ,74], 'optype': 'add', 'opval': 6, 'test': 19, 'iftrue': 2, 'iffalse': 0},
            {'items': [79, 60, 97], 'optype': 'multiplyself', 'test': 13, 'iftrue': 1, 'iffalse': 3},
            {'items': [74], 'optype': 'add', 'opval': 3, 'test': 17, 'iftrue': 0, 'iffalse': 1}]       
    return data            
    
def puzzle_setup():
    data = [{'items': [54, 89, 94], 'optype': 'multiply', 'opval': 7, 'test': 17, 'iftrue': 5, 'iffalse': 3},
            {'items': [66, 71], 'optype': 'add', 'opval': 4, 'test': 3, 'iftrue': 0, 'iffalse': 3},
            {'items': [76, 55, 80, 55, 55, 96, 78], 'optype': 'add', 'opval': 2, 'test': 5, 'iftrue': 7, 'iffalse': 4},
            {'items': [93, 69, 76, 66, 89, 54, 59, 94], 'optype': 'add', 'opval': 7, 'test': 7, 'iftrue': 5, 'iffalse': 2},
            {'items': [80, 54, 58, 75, 99], 'optype': 'multiply', 'opval': 17, 'test': 11, 'iftrue': 1, 'iffalse': 6},
            {'items': [69, 70, 85, 83], 'optype': 'add', 'opval': 8, 'test': 19, 'iftrue': 2, 'iffalse': 7},
            {'items': [89], 'optype': 'add', 'opval': 6, 'test': 2, 'iftrue': 0, 'iffalse': 1},            
            {'items': [62, 80, 58, 57, 93, 56], 'optype': 'multiplyself', 'test': 13, 'iftrue': 6, 'iffalse': 4}]       
    return data  
    
def step_1 (data):
    checkers=[0 for i in range(len(data))]
    for i in range(20):
        for j in range(len(data)):
            for item in data[j]['items']:
                checkers[j] += 1
                if data[j]['optype'] == 'add':
                    worry = item + data[j]['opval']
                else:
                    if data[j]['optype'] == 'multiplyself':
                        multiplier = item
                    else:
                        multiplier = data[j]['opval']
                    worry = item * multiplier
                worry = math.trunc(worry/3)
                if worry % data[j]['test'] == 0:
                    data[data[j]['iftrue']]['items'].append(worry)
                else:            
                    data[data[j]['iffalse']]['items'].append(worry)                
            data[j]['items'] = []  
        monkeys = sorted(checkers)[-2:]        
    return monkeys[0]*monkeys[1]
    
def step_2 (data):
    lcm = 1
    for row in data:
        lcm = lcm * row['test']
    checkers=[0 for i in range(len(data))]
    for i in range(10000):
        for j in range(len(data)):
            for item in data[j]['items']:
                checkers[j] += 1
                if data[j]['optype'] == 'add':
                    worry = item + data[j]['opval']
                else:
                    if data[j]['optype'] == 'multiplyself':
                        multiplier = item
                    else:
                        multiplier = data[j]['opval']
                    worry = item * multiplier
                    if worry > lcm:
                        worry = worry % lcm
                if worry % data[j]['test'] == 0:
                    data[data[j]['iftrue']]['items'].append(worry)
                else:            
                    data[data[j]['iffalse']]['items'].append(worry)                
            data[j]['items'] = []  
        monkeys = sorted(checkers)[-2:]        
    return monkeys[0]*monkeys[1]

if __name__ == '__main__':
    #data = read_data(sys.argv[1], False, False)
    results = ''
    if sys.argv[2] == '1':
        results = step_1(puzzle_setup())
    else:
        results = step_2(puzzle_setup())
    print(results) 