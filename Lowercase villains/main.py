string = input()

count = 0
for s in string:
    if s.islower():
        count += 1

print(count)