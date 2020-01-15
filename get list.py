import os

path = "D:/Documents/Programming Projects/pixiv script/New folder"
dirs = os.listdir(path)

f = open("D:/Documents/Programming Projects/pixiv script/filenames.txt", "w")

for i in range(len(dirs)):
    f.write(dirs[i] + "\n")

f.close()
print("Done")
