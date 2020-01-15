import codecs
import ast

f = codecs.open("D:/Documents/Programming Projects/pixiv script/tagged.txt", "r", encoding="utf-8")
g = open("D:/Documents/Programming Projects/pixiv script/filenames.txt", "r")
h = codecs.open("D:/Documents/Programming Projects/pixiv script/remainder.txt", "w", encoding="utf-8")

dictionary_list = f.readlines()
files = g.read().split()

for line in dictionary_list:
    line = ast.literal_eval(line)
    for k, v in line.items():
        for i in files:
            if i in k:
                h.write(str(line) + "\n")

f.close()
g.close()
h.close()

print("Done")