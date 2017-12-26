import subprocess as s

import re
import time
# netcfg = "adb shell netcfg"
# ip = s.getoutput(netcfg)
# # print(ip)
# t = re.findall("wlan0(.+?)UP(.+?)/", ip)[0][1]
# print(t)
# # a = t[0]
# # print(a[-13:])



def devices_ip():
    netcfg = "adb shell netcfg"
    ip = s.getoutput(netcfg)
    text = re.findall("wlan0(.+?)UP(.+?)/", ip)[0][1]
    return text[-13:]

print(devices_ip())

now = time.strftime("%Y-%m-%d %H_%M_%S")
print(now)