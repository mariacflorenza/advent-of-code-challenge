# Day 2

# Example
example_list = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]

# Read from .txt file lists
list = []
with open("input_day2.txt", "r") as file:
    for line in file:
        # each line is a sublist
        sublist = [int(num) for num in line.strip().split(' ')]
        list.append(sublist)


# Part 1
def is_safe(sublist):
    if sublist == sorted(sublist) or sublist == sorted(sublist, reverse=True):
        for i in range(len(sublist) - 1):
            if abs(sublist[i + 1] - sublist[i]) >= 4 or abs(sublist[i + 1] - sublist[i]) == 0:
            # if not (abs(sublist[i+1] - sublist[i]) > 0 and abs(sublist[i+1] - sublist[i]) < 4) :
                return False
        return True
    return False


def count_safe_reports(list):
    count = 0
    for report in list:
        if is_safe(report):
            count += 1
    return count

print("Safe reports: ", count_safe_reports(list)) # 5


# Part 2
def count_safe_reports_Dampener(list):
    count = 0
    for report in list:
        if is_safe(report):
            count += 1
        else:
            for i in range(len(report)):
                modified_report = report[:i] + report[i + 1:]
                if is_safe(modified_report):
                    count += 1
                    break
    return count

print("Safe reports with dampener: ", count_safe_reports_Dampener(list)) # 5