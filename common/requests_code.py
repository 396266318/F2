import json
import re
import requests


class user_code():
    base_url = 'http://uat-creditloan.pp100.net'
    session = requests.Session()

    def admin_login(self):
        """后端登录"""
        url = self.base_url + '/admin/login'
        querystring = {
            "userName": 'admin',
            "password": '123456'
        }

        response = self.session.post(url, params=querystring)
        text = json.loads(response.text)
        auth = 'A-Auth-Token'
        token = text.get("data").get("token")

        return auth, token

    # admin_login()


    def select_sms_code(self, mobile):
        '''查询短信信息,需要先登录到后台管理系统'''
        auth = self.admin_login()
        url = self.base_url + '/admin/sms/send/logs'
        headers = {
            "A-Auth-Token": auth[1]
        }
        querystring = {
            "currPage": "1",
            "mobile": mobile
        }
        response = self.session.post(url, headers=headers, params=querystring)
        text = json.loads(response.text)
        content = text.get('data').get('records')[0].get('content')
        code = re.search('\d+', str(content)).group()

        return code


# if __name__ == "":
    # main()