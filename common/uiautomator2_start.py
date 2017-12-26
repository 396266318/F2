import subprocess as s
import os, re, time
import uiautomator2 as u2
from FintechDemo.common.fintech_log import fintechLog
# from common.appiumServer import appiumServer_start

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
package = 'com.fintech.xbuse'
Activity = '.ui.activity.StartActivity'
log = fintechLog()

def adb_install():
    """安装packages"""
    adb_install_package = "adb install -r {0}".format(PATH("../../FintechDemo/conf/config/app-debug.apk"))  # adb install
    s.getoutput(adb_install_package)

def adb_uninstall():
    """卸载安装packages"""
    adb_uninstall = "adb uninstall {0}".format(package)  # adb uninstall 命令
    s.getoutput(adb_uninstall)

def judgment_app():
    """判断测试设备中是否有 packages 有就不安装，没有就安装"""
    adb_pm_list = "adb shell pm list packages -3"  # adb 查询命令 查询已经安装的packages
    lists = s.getoutput(adb_pm_list).replace("\n", " ").replace("\t", " ")
    try:
        r = re.findall(package, lists)[0]
        if r in lists:
            log.info("存在packages: {0}".format(r))
        else:
            log.info("不存在packages: {0}".format(r))
    except Exception as e:
        log.info(e)
        adb_install()

def app_start():
    # devicesName = appiumServer_start().myData()
    d = u2.connect_usb()
    d.healthcheck()
    d.screen_on()
    judgment_app()
    # time.sleep(5)
    d.app_start(package, Activity)  # 启动APP
    d(text="允许").wait(timeout=5.0)
    for i in range(8):
        allow = d(text="允许")
        total_allow = d(text="始终允许")
        if allow.exists is True:
            d.watcher("允许").when(text="允许").when(text="允许").click(text="允许")
        if total_allow.exists is True:
            d.watcher("始终允许").when(text="始终允许").when(text="始终允许").click(text="始终允许")
    log.info("结束{0}APP".format(package))
    # time.sleep(3)
    d.app_stop(package)

# app_start()
