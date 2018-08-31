#_*_coding:utf-8_*_
#作者        ：wangmf
#创建时间    ：2018/8/21 20:33
#修改时间    ：2018/8/21 
#文件        ：Run_Alltest.py

# coding:utf-8
import unittest
import os
import HTMLTestRunner
from Public import ParseRepository
#待执行用例的目录
def allcase():
    pp = ParseRepository.ParseRepositoryConfig('Config/config.ini')
    case_dir = pp.getOptionValue('测试用例路径','用例路径')
    testcase = unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(case_dir,pattern='*.py',top_level_dir=None)
    # testcase.addTest(discover)
    #discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            #添加用例到testcase
            testcase.addTest(test_case)
    return testcase
if __name__=="__main__":
    runner = unittest.TextTestRunner()
    runner.run(allcase())
    report_path = r'D:\yl1674\Documents\GitHub\VC_Group\VC_Mobil\report\report.html'
    fp = open(report_path,mode="wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="自动化测试unittest测试框架报告",description="用例执行情况：")
    runner.run(allcase())
    fp.close()