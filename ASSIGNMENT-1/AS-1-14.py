lst = [1, 2, 2, 3, 1, 4]
freq = {}
for item in lst:
    freq[item] = freq.get(item, 0) + 1
print("Frequencies:", freq)
