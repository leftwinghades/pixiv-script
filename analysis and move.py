import codecs
import ast
import shutil

f = codecs.open("D:/Documents/Programming Projects/pixiv script/tagged.txt", "r", encoding="utf-8")
dictionary_list = f.readlines()
f.close()

for line in dictionary_list:
    line = ast.literal_eval(line)
    for k, v in line.items():
        if "_tag_here_" in v: # name of the tag
            filename = k
            src = "D:/Pictures/" + filename
            dst = "D:/Documents/Programming Projects/pixiv script/Moved/" + filename

            try:
                shutil.move(src, dst)
                print(k)
            except OSError as e:
                print(e)

print("Done")