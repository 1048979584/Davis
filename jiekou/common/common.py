
import json
import requests
class SL_EQ:
    def __init__(self):
        #通过登陆获取token
       r=requests.post(
                url='http://150.223.10.116:86/login',
                data={'username':'admin','password':111111},
                headers={'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'})
       self.token=r.json()['expand']['token']
       print(self.token)
    def test(self,url,data):
        r2=requests.post(
        headers={"token":self.token},
        url=url,
        data=data)
        result=json.loads(r2.text)['msg']
        return result





if __name__ == '__main__':
    SL_EQ().test( url='http://150.223.10.116:84/sys/user/save',
                 data={"username":"Test_pl",
                    "name":"双流Test00p",
                    "password":"admin010",
                 "email":"1048979584@qq.com",
                     "roleIds":6,
                    "deptId":91,
                    "mobile":13628165081,
                    "status":1
                    })

