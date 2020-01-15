import shutil

filename = "67158479_p0.jpg"
src = "D:/Documents/Programming Projects/pixiv script/pictures/" + filename
dst = "D:/Documents/Programming Projects/pixiv script/new/" + filename

shutil.move(src, dst)