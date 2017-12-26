import subprocess as s
import re


def myData():
    """查询当前链接的设备信息"""
    cmd_devices = "adb devices"
    devices = s.getoutput(cmd_devices)  # adb命令获取devices的原始信息

    if "List" is devices:
        print("无设备连接")
    else:
        dev = devices.replace("\t", " ").replace("\n", " ").split(" ")[-3]  # 将原始信息中的转义符号，替换为空格, 切片字符串中的空格

    cmd_version = "adb shell getprop ro.build.version.release"
    devices = s.getoutput(cmd_version).replace("\t", " ").replace("\n", " ").split(" ")[0]

    android_version = devices
    deviceName = dev  # 设备名字
    packages = 'com.fintech.xbuse'  # 测试包名
    appActivity = 'com.fintech.xbuse.ui.activity.StartActivity'

    return android_version, deviceName, packages, appActivity

def devices_ip():
    netcfg = "adb shell netcfg"
    ip = s.getoutput(netcfg)
    text = re.findall("wlan0(.+?)UP(.+?)/", ip)[0][1]

    return text[-13:]

print(myData())