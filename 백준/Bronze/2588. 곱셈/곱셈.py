first = []
second = []
first_line = input()
for i in first_line:
  first.append(i)
second_line= input()
for i in second_line:
  second.append(i)

print(int(second[2]) * int(first_line))
print(int(second[1]) * int(first_line))
print(int(second[0]) * int(first_line))
print(int(first_line) * int(second_line))  