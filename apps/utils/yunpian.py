from djangoServer.myconfig import YUNPIAN_API_KEY
import requests
import json
import os
import sys

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+'/../../')


class YunPian(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = 'https://sms.yunpian.com/v2/sms/single_send.json'

    def single_send_sms(self, code, mobile):
        parmas = {
            'apikey': self.api_key,
            'mobile': mobile,
            'text': '【风长无从阻】您的验证码是{code}。如非本人操作，请忽略本短信'.format(code=code)
        }
        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        return re_dict


if __name__ == '__main__':
    yunpian = YunPian(YUNPIAN_API_KEY)
    print(YUNPIAN_API_KEY)
    # yunpian.single_send_sms('', '')
