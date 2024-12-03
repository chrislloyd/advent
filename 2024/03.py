import re
import fileinput

input = "".join(fileinput.input())
mul_pattern = r"mul\((\d+),(\d+)\)"

# part 1
pattern = re.compile(mul_pattern)
matches = re.findall(pattern, input)
result = sum(int(x) * int(y) for x, y in matches)
print(result)

# part 2
pattern = re.compile(r"%s|do\(\)|don't\(\)" % mul_pattern)
mul_enabled = True
result = 0
for match in pattern.finditer(input):
    instruction  = match.group(0)
    if instruction == "do()":
        mul_enabled = True
    elif instruction == "don't()":
        mul_enabled = False
    elif mul_enabled:
        x, y = match.groups()
        result += int(x) * int(y)
print(result)
