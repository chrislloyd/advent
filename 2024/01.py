import fileinput

lines = list(fileinput.input())

left = []
right = []
for line in lines:
  a, b = map(int, line.split())
  left.append(a)
  right.append(b)

# part 1
left = sorted(left)
right = sorted(right)
total = 0
for i in range(len(lines)):
  distance = abs(left[i] - right[i])
  total += distance
print(total)

# part 2
counts = {}
for item in right:
  counts[item] = counts.get(item, 0) + 1
total = 0
for item in left:
  similarity = item * counts.get(item, 0)
  total += similarity
print(total)
