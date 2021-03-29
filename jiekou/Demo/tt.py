
import json
import requests
class SL_EQ:
    def __init__(self):
        #通过登陆获取token
       r=requests.post(
                url='http://150.223.10.116:84/login',
                data={'username':'admin','password':111111},
                headers={'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'})
       self.token=r.json()['expand']['token']

    def test(self):
        url="http://150.223.10.116:86/sys/user/save"
        data={"parentId":178,"name":"语音通话","type":1,"url":"http://150.223.10.116:85/#/sysg/permission"}
        r2=requests.post(
                headers={"token":self.token},
        url=url,data=data)
        result=json.loads(r2.text)['msg']
        print( result)

if __name__ == '__main__':
    SL_EQ().test()




