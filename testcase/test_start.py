import time
import unittest
import subprocess as s
from Fintech_ua2.common.fintech_log import fintechLog
from Fintech_ua2.common.Myunit import Myunit


class slippage(Myunit):
    """滑动"""

    def size(self):
        adb = "adb shell wm size"
        str = s.getoutput(adb).replace("\n", "")
        l = str.split(": ")[1]
        size = l.split("x")
        return size

    def info_size(self):
        size = self.devices.info
        height = size.get("displayHeight")
        width = size.get('displayWidth')
        return height, width

    def up_swipe(self):
        width = self.info_size()[0]
        higt = self.info_size()[1]
        self.devices.swipe(width / 2, higt * 0.3, width / 2, higt * 0.5, 0.5)


    def test(self):
        # print(self.size())
        self.password_login('15984669732', 'qwe123')
        # self.devices(text="我要借款").click()
        # self.devices(text="下一步").click()
        # self.devices(resourceId='com.fintech.xbuse:id/loan_use').click()
        self.devices(resourceId="com.fintech.xbuse:id/loan_message_iv").click()
        self.up_swipe()
        self.devices(resourceId="com.fintech.xbuse:id/message_detail").click()
        self.out_login()


if __name__ == "__main__":
    unittest.main()