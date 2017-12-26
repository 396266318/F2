import subprocess as s
import re

# adb_size = "adb shell wm size"
#
# s = s.getoutput(adb_size).replace("\n", "")
# l = s.split(": ")[1]
# ll = l.split("x")
#
# r = re.findall(": (.+)", s)
# r1 = r[0].split("x")

# width = int(r1[0])
# high = int(r1[1])
# print(width)
# print(high)
# up = (width / 2, high * 0.8, width / 2, high * 0.2)
# print(up)


def size():
    adb = "adb shell wm size"
    str = s.getoutput(adb).replace("\n", "")
    l = str.split(": ")[1]
    ll = l.split("x")
    width = int(ll[0])
    higt = int(ll[1])
    text = (width / 2, higt * 0.8, width / 2, higt * 0.5)
    print(text)
    print(width, higt)
    return width, higt

size()