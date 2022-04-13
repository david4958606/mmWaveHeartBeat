import matplotlib
import sys

from more_itertools import first

sys.stdout = open('temp.txt', 'wt')

def read_output(file):
    """
    Reads the output of the program and returns a list of tuples.
    """
    with open(file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        t = tuple(map(str, line.split()))
        print(t)

def delFirstTowLines(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    with open(file, 'w') as f:
        for line in lines[2:]:
            f.write(line)

# 删除包含 End 的行
def delEndLine(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    with open(file, 'w') as f:
        for line in lines:
            if "End" not in line:
                f.write(line)

# 提取tuple的第n个元素
def get_nth_element(tuple, n):
    return tuple[n]

def get_first(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    
    firsts = []

    for line in lines:
        loc = locals()
        l = "t = " + line[:-1]
        exec(l)
        t = loc['t']
        firsts.append(t[0])

    with open('first.output', 'w') as f:
        for i in firsts:
            f.write(i)
            f.write('\n')

def get_nth_element(tuple, n):
    return tuple[n]

def get_second(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    
    firsts = []

    for line in lines:
        loc = locals()
        l = "t = " + line[:-1]
        exec(l)
        t = loc['t']
        firsts.append(t[1])

    with open('second.output', 'w') as f:
        for i in firsts:
            f.write(i)
            f.write('\n')

# 将第 3, 6 , 9 ... 行转化为十进制
def get_decimal(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    
    decimals = []

    for line in lines:
        loc = locals()
        l = "t = " + line[:-1]
        exec(l)
        t = loc['t']
        decimals.append(int(t[0], 16))

    with open('decimal.output', 'w') as f:
        for i in decimals:
            f.write(str(i))
            f.write('\n')

# 处理格式
read_output('output.txt')
delFirstTowLines('temp.txt')
delEndLine('temp.txt')

# 提取元素
get_first('temp.txt')
get_second('temp.txt')

get_decimal('temp.txt')
