import codecs
import ast

f = codecs.open("D:/Documents/Programming Projects/pixiv script/remainder.txt", "r", encoding="utf-8")
dictionary_list = f.readlines()
f.close()

count = 0
freq = {}

for line in dictionary_list:
    line = ast.literal_eval(line)
    for k, v in line.items():
        for tag in v:
            if tag in freq:
                freq[tag] += 1
            else:
                freq[tag] = 1

freq = sorted(freq.items(), key=lambda x: x[1])

print(freq)