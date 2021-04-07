import unittest,ddt,time,os,json
import warnings
from API_Test.HwTestReport.HwTestReport import HTMLTestReport
from API_Test.Get_TestCase.read_excel import ExcelUtil
from API_Test.script.api_script import CaseScript


excel = ExcelUtil("G:\LocalGit\github\QiuW\API_Test\Test_Case\ApiCase.xlsx", '汇总')
@ddt.ddt
class DataTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # warnings.simplefilter('ignore',ResourceWarning)
        print('### 接口测试开始 ###')
    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        print('### 接口测试结束 ###')
    @ddt.data(*excel.next())
    def test01(self,data):
        body_data = {}  # 每次遍历后将字典置为空
        ReqMethod=data['请求方式']
        url2 = data['接口地址']
        Except1 = data['状态码']
        Except2=data['响应文本']

        if ReqMethod =='get':
            Result02 = CaseScript().get_api(url=url2)
            self.assertEqual(Except1, str(Result02[0]))
            self.assertIn(Except2,Result02[1])

        if ReqMethod =='post_session':
            test_data = eval((data['参数']))  # 还原数据类型
            Result01 = CaseScript().post_api_session(url=url2,data=test_data)
            self.assertEqual(Except1, str(Result01[0]))
            assert_data = Except2.split('\n')
            for i in assert_data:
                self.assertIn(i, Result01[1])

        if ReqMethod =='post':
            test_data = eval((data['参数']))
            Result01 = CaseScript().post_api(url=url2,data=test_data)
            self.assertEqual(Except1, str(Result01[0]))
            assert_data=Except2.split('\n')
            for i in assert_data:
                self.assertIn(i,Result01[1])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DataTest)
    #时间维度生成报告
    #now=time.strftime("%m_%d_%H_%M)", time.localtime())
    now = time.strftime("%m_%d_%H)", time.localtime())
    print(now)
    report_name="TestReport("+now+".html"
    file_name = "G:\LocalGit\github\QiuW\API_Test\Test_Report\%s"%(report_name)

    with open(file_name, 'wb') as file:
        HTMLTestReport(stream=file, verbosity=3, title='接口测试报告').run(suite)





