import fileinput

input = [list(line.rstrip()) for line in list(fileinput.input())]
rows, cols = len(input), len(input[0])

# part 1
needle = "XMAS"
directions = [ # (dy, dx)
    (0, 1),   # Right
    (1, 0),   # Down
    (0, -1),  # Left
    (-1, 0),  # Up
    (1, 1),   # Down-right
    (-1, -1), # Up-left
    (1, -1),  # Down-left
    (-1, 1),  # Up-right
]
def check(y, x, dy, dx):
    for k in range(len(needle)):
        r, c = y + k * dy, x + k * dx
        if r < 0 or r >= rows or c < 0 or c >= cols or input[r][c] != needle[k]:
            return False
    return True
count = 0
for row in range(rows):
    for col in range(cols):
        for dx, dy in directions:
            if check(row, col, dy, dx):
                count += 1
print(count)

# part 2
count = 0
needle = {"MAS", "SAM"}
for i in range(rows):
    for j in range(cols):
        d1, d2 = None, None
        if (0 <= i - 1 < rows and 0 <= j - 1 < cols and
            0 <= i + 1 < rows and 0 <= j + 1 < cols):
            d1 = input[i-1][j-1] + input[i][j] + input[i+1][j+1]
        if (0 <= i - 1 < rows and 0 <= j + 1 < cols and
            0 <= i + 1 < rows and 0 <= j - 1 < cols):
            d2 = input[i-1][j+1] + input[i][j] + input[i+1][j-1]
        if d1 in needle and d2 in needle:
            count += 1
print(count)

