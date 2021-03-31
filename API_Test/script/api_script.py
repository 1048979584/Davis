import json
import requests
class CaseScript:
    def __init__(self):
        #通过登陆获取token
        r=requests.get(
                url='https://test-web.wind56.com/wind56apis/auth/oauth/token',
                data={'username':'13910001000 ','password':123456},
                headers={'Content-Type':'application/json;charset=UTF-8'}).status_code
       # self.token=r.json()['expand']['token']
        self.token = r
        print(r)
    def get_api(self,url,params=None):
        get_status_code=requests.get(url).status_code
        get_text = requests.get(url).content.decode('utf-8')
        return get_status_code, get_text

    def post_api(self,url,data):
        post_result= requests.post(
            headers={"token": self.token},
            url=url,
            data=data)
        post_status_code = post_result.status_code
        post_text = post_result.text
        return post_status_code , post_text
        #result = json.loads(r2.text)['msg']

    def delete_api(self, url, data):
        pass
    def put_api(self, url, data):
        pass


if __name__ == '__main__':
    CaseScript().get_api(url='https://www.baidu.com/')

