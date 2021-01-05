number = [2, 4, 8, 2, 32, 7, 7, 5, 6, 10]
uniq = []

for numbers in number:
    if numbers not in uniq:
        uniq.append(numbers)
print(uniq)
