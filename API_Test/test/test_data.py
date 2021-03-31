import unittest,ddt,time,os
import warnings
from HTMLTestRunner import HTMLTestRunner

from API_Test.HwTestReport.HwTestReport import HTMLTestReport



from API_Test.get_test_case.read_excel import ExcelUtil
from API_Test.script.api_script import CaseScript


excel = ExcelUtil("G:\LocalGit\github仓库\API_Test\Demo\jiekou.xlsx", 'Sheet1')
@ddt.ddt
class DataTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # warnings.simplefilter('ignore',ResourceWarning)
        print('接口测试开始...')
    @classmethod
    def tearDownClass(cls):
        print('...接口测试结束')
    @ddt.data(*excel.next())
    def test01(self,data):
        # 每次遍历后将字典置为空
        body_data = {}
        ReqMethod=data['请求方式']
        url2 = data['接口地址']
        test_data = data['参数']
        Except1 = data['响应码']
        Except2=data['预期结果']
        li = test_data.split('\n')
        for j in li:
            key= j.split('=')[0]
            value= j.split('=')[1]
            body_data[key] = value
        #选择请求方式
        if ReqMethod =='post':
            Result01 = CaseScript().post_api(url=url2,data=body_data)
            self.assertEqual(Except1, str(Result01[0]))
            self.assertIn(Except2,Result01[1])

        if ReqMethod =='get':
            Result02 = CaseScript().get_api(url=url2)
            self.assertEqual(Except1, str(Result02[0]))
            self.assertIn(Except2,Result02[1])




if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DataTest)
    now = time.strftime("%m%d%H%M")
    file_name = "G:\LocalGit\github仓库\API_Test\HwTestReport\HtmlTestReport\TestReport.html"

    with open(file_name, 'wb') as file:
        HTMLTestReport(stream=file, verbosity=3, title='接口测试报告').run(suite)





