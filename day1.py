# Day 1 

# Example
# example_listA = [3, 4, 2, 1, 3, 3]
# example_listB = [4, 3, 5, 3, 9, 3]




# Read from .txt file lists
listA = []
listB = []

with open("input_day1.txt", "r") as file:
    for line in file:
        num1, num2 = map(int, line.split())  # Divide y convierte a entero
        listA.append(num1)
        listB.append(num2)

# print("List A:", listA)
# print("List B:", listB)

# Part 1
# Calculate the total distance between the two lists
def total_distance(listA, listB):
    total = 0
    listA.sort()
    listB.sort()
    for i in range(len(listA)):
        total += abs(listA[i] - listB[i])
    return total

print("Total distance: ", total_distance(listA, listB)) # 2904518

# Part 2
# Calculate similarity score between the two lists

def similarity_score(listA, listB):
    score = 0
    for i in range(len(listA)):
        if listA[i] in(listB):
            count = listB.count(listA[i])
            score += listA[i] * count

    return score

print("Similarity score: ", similarity_score(listA, listB)) # 31