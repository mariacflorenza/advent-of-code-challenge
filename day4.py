# Day 4


example_words = [
    ['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'],
    ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'],
    ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'],
    ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'],
    ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'],
    ['X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'],
    ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'],
    ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'],
    ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'],
    ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X']
]


# Read from .txt
words = []

with open("input_day4.txt", "r") as file:
    for line in file:
        words.append(list(line.strip()))

# print(words)

# Part 1
def count_XMAS(words, word='XMAS'):
    row, column, length = len(words), len(words[0]), len(word)
    
    # Direcciones de búsqueda: (dx, dy)
    directions = [
        (0, 1), (0, -1),  # (→, ←)
        (1, 0), (-1, 0),  # (↓, ↑)
        (1, 1), (1, -1),  # ↓→, ↓←
        (-1, 1), (-1, -1) # ↑→, ↑←
    ]
    
    def in_range(x, y):
        return 0 <= x < row and 0 <= y < column

    def search_in_direction(x, y, dx, dy):
        for i in range(length):
            nx, ny = x + i * dx, y + i * dy
            if not in_range(nx, ny) or words[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for i in range(row):
        for j in range(column):
            if words[i][j] == word[0]:
                for dx, dy in directions:
                    if search_in_direction(i, j, dx, dy):
                        count += 1

    return count

print("Count XMAS:", count_XMAS(words))



# Part 2

# Example
example_words = [
    ['M', 'Y', 'M'],
    ['M', 'A', 'Y'],
    ['S', 'Y', 'S']
]
grid = [
    [".", "M", ".", "S", ".", ".", ".", ".", ".", "."],
    [".", ".", "A", ".", ".", "M", "S", "M", "S", "."],
    [".", "M", ".", "S", ".", "M", "A", "A", ".", "."],
    [".", ".", "A", ".", "A", "S", "M", "S", "M", "."],
    [".", "M", ".", "S", ".", "M", ".", "A", ".", "."],
    [".", ".", ".", ".", ".", ".", "S", ".", "S", "."],
    ["S", ".", "S", ".", "S", ".", "S", ".", "S", "."],
    [".", "A", ".", "A", ".", "A", ".", "A", ".", "."],
    ["M", ".", "M", ".", "M", ".", "M", ".", "M", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
]


def count_X_MAS(words):
    rows, cols = len(words), len(words[0])
    count = 0

    _set = {"M", "S"}

    
    for row in range(1, rows - 1):
        for column in range(1, cols - 1):
            if words[row][column] == "A":
                if {words[row - 1][column - 1], words[row + 1][column + 1]} == _set and {words[row - 1][column + 1], words[row + 1][column - 1]} == _set:
                    count += 1

    return count

print("Count X-MAS:", count_X_MAS(words)) 
