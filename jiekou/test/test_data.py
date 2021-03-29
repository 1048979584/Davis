import unittest
import warnings
from HTMLTestRunner import HTMLTestRunner

import ddt
from SLEQ.jiekou.common.common import SL_EQ
from SLEQ.jiekou.read_excel.read_excel import ExcelUtil
excel = ExcelUtil("D:\\phthon\\SLEQ\\jiekou\\Demo\\jiekou.xlsx", 'Sheet1')
@ddt.ddt
class DataTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # warnings.simplefilter('ignore',ResourceWarning)
        print('接口测试开始...')
    @classmethod
    def tearDownClass(cls):
        print('...接口测试结束')
#         #遍历获取列表的数据#
    @ddt.data(*excel.next())
    def test01(self,data):
        #每次遍历后将字典置为空
        data1 = {}
        url = data['接口地址']
        test_data = data['参数']
        Except=data['预期结果']
        case=data['断言方式']
        li = test_data.split('\n')
        #将参数改为字典形式
        for j in li:
            key= j.split('=')[0]
            value= j.split('=')[1]
            #添加字典的键值对
            data1[key] = value
        result=SL_EQ().test(url,data1)
        print(result)
        if  case=="assertIn":
             # r=json.loads(result)["pageSize"]
             self.assertIn(Except,result)
        if  case=="assertEqual":
            self.assertEqual(Except,result)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DataTest)
    with open("D:\\phthon\\SLEQ\\jiekou\\Demo\\TestReport.html",'w',encoding='utf-8')as f:
        HTMLTestRunner(stream=f,verbosity=2).run(suite)





