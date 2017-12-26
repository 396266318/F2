# coding:utf-8

import unittest
import subprocess as s
import os, re, time
import uiautomator2 as u2
from FintechDemo.common.fintech_log import fintechLog
from common.requests_code import user_code


PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
package = 'com.fintech.xbuse'
Activity = '.ui.activity.StartActivity'


class Myunit(unittest.TestCase):

    log = fintechLog()
    file = "D:\pp100\Fintech_ua2\conf\cfg\\"
    now = time.strftime("%Y-%m-%d %H_%M_%S")

    def devices_ip(self):
        netcfg = "adb shell netcfg"
        ip = s.getoutput(netcfg)
        text = re.findall("wlan0(.+?)UP(.+?)/", ip)[0][1]

        return text[-13:]

    def adb_install(self):
        """安装packages"""
        adb_install_package = "adb install -r {0}".format(
            PATH("../../FintechDemo/conf/config/app-debug.apk"))  # adb install
        s.getoutput(adb_install_package)

    def adb_uninstall(self):
        """卸载安装packages"""
        adb_uninstall = "adb uninstall {0}".format(package)  # adb uninstall 命令
        s.getoutput(adb_uninstall)

    def judgment_app(self):
        """判断测试设备中是否有 packages 有就不安装，没有就安装"""
        adb_pm_list = "adb shell pm list packages -3"  # adb 查询命令 查询已经安装的packages
        lists = s.getoutput(adb_pm_list).replace("\n", "").replace("\t", "")
        try:
            r = re.findall(package, lists)[0]
            if r in lists:
                self.log.info("存在packages: {0}".format(r))
            else:
                self.log.info("不存在packages: {0}".format(r))

        except Exception as e:
            self.log.info(e)
            self.adb_install()

    def setUp(self):
        """启动 uiautomator2 检查APP是否安装"""
        uiautomator_app_start = "python -m uiautomator2 init"
        s.getoutput(uiautomator_app_start)
        # self.devices = u2.connect("192.168.5.209")
        self.devices = u2.connect(self.devices_ip())
        self.devices.healthcheck()
        self.devices.screen_on()
        self.judgment_app()
        # time.sleep(5)
        self.log.info("启动APP")
        self.devices.app_start(package, Activity)  # 启动APP
        self.devices.set_fastinput_ime(True)  # 关闭(fastinput)输入法
        self.devices(text="允许").wait(timeout=1.5)
        for i in range(8):
            allow = self.devices(textContains="允许")
            total_allow = self.devices(textContains="始终允许")
            if allow.exists is True:
                self.devices.watcher("允许").when(text="允许").when(text="允许").click(text="允许")
            if total_allow.exists is True:
                self.devices.watcher("始终允许").when(text="始终允许").when(text="始终允许").click(text="始终允许")

    def tearDown(self):
        self.devices.set_fastinput_ime(False)  # 关闭(fastinput)输入法
        self.log.info("结束APP:{0}".format(package))
        self.devices.app_stop(package)

    def base_config(self):
        """配置测试环境"""
        toggle_debug = self.devices(textContains="调试")
        url_test = self.devices(textContains="测试")
        confirm = self.devices(textContains="确认")
        if toggle_debug.exists is True:
            toggle_debug.click()                        # 点击调试
            url_test.click()  # 点击测试连接
            confirm.click()  # 点击确认按钮

    def code_login(self, mobile):
        """验证码登录"""
        apply_button = self.devices(text="我的")                                      # 点击我的按钮
        user_code_button = self.devices(textContains="获取验证码")                     # 点击获取验证码
        user_inport = self.devices(resourceId="com.fintech.xbuse:id/login_phone_et")  # 输入用户名
        user_code_input = self.devices(resourceId="com.fintech.xbuse:id/login_code")  # 输入验证码
        login_button = self.devices(resourceId="com.fintech.xbuse:id/login_btn")      # 登录按钮
        Credit_score = self.devices(textContains="知道了")

        if Credit_score.exists is True:
            Credit_score.click()

        apply_button.click()                                  # 点击我的按钮
        if user_code_button.exists is True:
            user_inport.clear_text()                          # 清空用户名输入框
            user_inport.set_text(mobile)                      # 输入用户名
            user_code_button.click()
            user_code_input.clear_text()
            user_code_input.set_text(user_code().select_sms_code(mobile))
            login_button.click()

    def password_login(self, user, password):
        """登录"""
        # my_button = self.devices(text="我的")
        forget_password = self.devices(textContains="忘记密码")
        toggle_password = self.devices(textContains="使用密码登录")
        user_login = self.devices(resourceId="com.fintech.xbuse:id/login_phone_et")
        user_password = self.devices(resourceId="com.fintech.xbuse:id/login_pwd_et")
        login_button = self.devices(resourceId="com.fintech.xbuse:id/login_btn")
        credit_score = self.devices(textContains="知道了")

        try:
            if credit_score.exists is True:            # 用于 判断页面 借款申请拒单生成的信用评分 点击
                credit_score.click()
            if self.login_state() is True:             # 判断当前APP上是否有登录
                self.out_login()                       # 调用退出函数
        except Exception as e:
            self.log.info("退出App: {0}".format(e))
            self.out_login()
        finally:                                       # 密码登录流程
            self.base_config()
            toggle_password.click()                    # 切换使用密码登录
            if forget_password.exists is True:
                user_login.clear_text()                # 清空用户名输入框
                user_login.set_text(user)              # 输入用户名
                user_password.clear_text()             # 清空密码输入框
                self.devices.set_fastinput_ime(True)
                user_password.send_keys(password)      # 输入密码
                login_button.click()                   # 点击登录按钮
                self.devices.set_click_post_delay(2)

    def out_login(self):
        """退出"""
        my_button = self.devices(text="我的")
        more_button = self.devices(textContains="更多")
        safety_exit_button = self.devices(textContains="安全退出")
        try:
            my_button.click()
            if more_button.exists is True:
                more_button.click()
                safety_exit_button.click()
        except Exception as e:
            self.log.info(e)

    def login_state(self):
        """判断登录状态"""
        my_button = self.devices(text="我的")
        more_button = self.devices(textContains="更多")
        my_button.click()
        return more_button.exists

    # def test(self):
        # self.code_login('15984669732')
        # self.password_login('15984669732', 'qwe123')
        # time.sleep(3)
        # self.out_login()
        # pass


if __name__ == "__main__":
    unittest.main()
