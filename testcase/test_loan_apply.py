import time
import unittest
from Fintech_ua2.common.fintech_log import fintechLog
from Fintech_ua2.common.Myunit import Myunit
from Fintech_ua2.common.requests_code import user_code


class Test_login(Myunit):

    log = fintechLog()
    file = "D:\pp100\Fintech_ua2\conf\cfg\\"
    now = time.strftime("%Y-%m-%d %H_%M_%S")

    # def test_1(self):
    #     self.code_login('15984669732')
    #     self.out_login()

    # def test_2(self):
    #     self.password_login('15984669732', 'qwe123')
    #     self.out_login()

    def test_loan_apply(self):
        """正常借款流程"""
        mobile = "15984669732"
        my_loan_button = self.devices(textContains="我要借款")
        next_step = self.devices(textContains="下一步")
        select_use = self.devices(textContains="请选择用途")
        use_button = self.devices(textContains="完成")  # 医用
        get_code = self.devices(textContains="获取验证码")
        input_code = self.devices(textContains="请输入验证码")
        query_loan = self.devices(textContains="确认借款")

        self.password_login(mobile, 'qwe123')
        my_loan_button.click()               #
        next_step.click()                    #
        select_use.click()                   #
        use_button.click()                   #
        get_code.click()                     #
        input_code.set_text(user_code().select_sms_code(mobile))
        query_loan.click()
        time.sleep(5)
        self.out_login()


if __name__ == "__main__":
    unittest.main()
