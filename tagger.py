import os
import urllib.request
import urllib.error
import codecs
import time
from bs4 import BeautifulSoup

f = open("D:/Documents/Programming Projects/pixiv script/filenames.txt", "r")
pictures_list = f.read().split()
f.close

output = codecs.open("D:/Documents/Programming Projects/pixiv script/tagged.txt", "w", encoding="utf-8")
r = open("D:/Documents/Programming Projects/pixiv script/removed.txt", "w")

count = 0

start_time = time.time()

print("========== BEGIN ==========")

for image in pictures_list:
    loop_time = time.time()

    pixiv_id = image[:image.index("_")]
    pixiv_url = "https://www.pixiv.net/member_illust.php?mode=medium&illust_id=" + pixiv_id

    try:
        source = urllib.request.urlopen(pixiv_url)
    except urllib.error.HTTPError as e:
        r.write(str(image + "\n"))
        count += 1

        print(str(count) + " - " + str(image))
        print('HTTPError: {}'.format(e.code))
        print(time.time() - loop_time)
    except urllib.error.URLError as e:
        r.write(str(image + "\n"))
        count += 1

        print(str(count) + " - " + str(image))
        print('URLError: {}'.format(e.reason))
        print(time.time() - loop_time)
    else:
        soup = BeautifulSoup(source, "html.parser")
        
        user = soup.find("h2", {"class": "name"}).string
        meta = soup.find("meta", {"name": "keywords"})
        tags = meta.attrs["content"].split(",")

        name_tags = [user] + tags

        pixiv_dict = {image: name_tags}

        output.write(str(pixiv_dict) + "\n")

        count += 1

        print(str(count) + " - " + str(image))
        print(time.time() - loop_time)

output.close()
r.close()

print("========== DONE ==========")
print("Average time: " + str((time.time() - start_time) / count))
print("Total elapsed time: " + str(time.time() - start_time))


# test_time = time.time()
# print(time.time() - test_time)