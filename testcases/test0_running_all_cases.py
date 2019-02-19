# -*- coding:utf-8 -*-
import unittest
import allure
import os

case_path = os.path.join(os.getcwd(), "ELN_test")
# 报告存放路径
report_path = os.path.join(os.getcwd(), "report")


def all_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
    print(discover)
    return discover


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(all_case())
# def all_case():
#     # 执行测试用例的目录
#     case_dir = r"C:\Users\Ms. Wang\Downloads\arxspan_automation_testing\testcases\ELN_test"
#     testcase = unittest.TestSuite()
#     discover = unittest.defaultTestLoader.discover(case_dir, pattern='test*.py', top_level_dir=None)
#     # discover方法筛选出来的用例，循环添加到测试套件中
#     for test_suit in discover:
#         for test_case in test_suit:
#             # 添加用例到testcase
#             testcase.addTest(test_case)
#     print(testcase)
#     return testcase
#
#
# if __name__ == "__m ain__" :
#     # 返回实例
#     runner = unittest.TextTestRunner()
#     # import HTMLTestRunner
#     #
#     # report_path = r"F:\MTbaby\report\result.html"  # 这里就是你创建result.html
#     # fp = open(report_path, 'wb')
#     # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'这是我的自动化测试报告', description=u'测试用例执行情况：')
#
#     # run所有用例
#     runner.run(all_case())
