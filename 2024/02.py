import fileinput

def is_safe(levels: list[int]) -> bool:
    """
    >>> is_safe([1, 2, 3, 4, 5])
    True
    >>> is_safe([5, 4, 3, 2, 1])
    True
    >>> is_safe([1, 2, 3, 5, 4])
    False
    >>> is_safe([1, 2, 3, 4, 8])
    False
    """
    if len(levels) < 2:
        return True 
    delta = [levels[i+1] - levels[i] for i in range(len(levels) - 1)]
    increasing = all(d >= 0 for d in delta)
    decreasing = all(d < 0 for d in delta)
    gradual = all(1 <= abs(d) <= 3 for d in delta)
    return (increasing or decreasing) and gradual

def part1(reports: list[list[int]]) -> int:
    total = 0
    for levels in reports:
        if is_safe(levels):
            total += 1
    return total

def part2(reports: list[list[int]]) -> int:
    total = 0
    for levels in reports:
        if is_safe(levels):
            total += 1
            continue
        for i in range(len(levels)):
            new_levels = levels[:i] + levels[i+1:]
            if is_safe(new_levels):
                total += 1
                break
    return total

input = fileinput.input()
reports = [list(map(int, line.split())) for line in list(input)]

# sanity check
assert part1(reports) < part2(reports)

print(part1(reports))
print(part2(reports))
