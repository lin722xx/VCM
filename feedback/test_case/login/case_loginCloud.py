#_*_coding:utf-8_*_
#作者        ：wangmf
#创建时间    ：2018/8/29 10:10
#修改时间    ：2018/8/29 
#文件        ：case_loginCloud.py


from Public import OpenApp
import unittest
from Public import LoginPage,ParseRepository,Logout
from Config import Globalvar
from Util import ObjectMap


class LoginCloud(unittest.TestCase):
    def setUp(self):
        self.driver = OpenApp.OpenVCM.Open1(self)
        print('执行test用例')
    def tearDown(self):
        out = Logout.Logout(self.driver)
        out.logout()
    def test_LoginCloud(self):
        l = LoginPage.Login_start(self.driver,Globalvar.config_path)
        l.login_Cloud(Globalvar.Cloud_account,Globalvar.Cloud_password,Globalvar.Cloud_server)
        pp = ParseRepository.ParseRepositoryConfig(Globalvar.config_path)
        self.driver.implicitly_wait(5)
        ObjectMap.getElement(self.driver,'id',pp.getOptionValue('设置页相关','账号头像')).click()
        obj = ObjectMap.getElement(self.driver,"id",pp.getOptionValue('设置页相关','账号信息'))

        # print(getattr(obj,'text'))
        # print(is_loginsucess)
        # assert getattr(obj, 'text') == '1200', '账号显示错误'+getattr(obj,'text')
        assert getattr(obj,'text')==Globalvar.Cloud_account,('账号显示错误'+(getattr(obj,'text')))




if __name__=="__main__":
    unittest.main()