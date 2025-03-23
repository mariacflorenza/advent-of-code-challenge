# Day 3
import re

example_string = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

# Read from .txt file
string = ''
with open("input_day3.txt", "r") as file:
    string = file.read().strip()

# print("String: ", string)

# Part 1
def uncorrupted_mul(string):
    count = 0
    pattern = r'mul\((\d+),(\d+)\)'
    for match in re.finditer(pattern, string):
        count += int(match.group(1)) * int(match.group(2))
   
    return count

print("Uncorrupted mul: ", uncorrupted_mul(example_string)) # 0

# Part 2
example_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def uncorrupted_mul_do(string):
    
    events = re.findall(r"don't\(\)|do\(\)|mul\(\d+,\d+\)", string)
    
    sum = 0
    active = True 
    
    for event in events:
        if event == "don't()":
            active = False
        elif event == "do()":
            active = True
        else:
            if active:
                x, y = map(int, re.findall(r"\d+", event))
                sum += x * y
    
    return sum


print("Uncorrupted mul do:", uncorrupted_mul_do(string))