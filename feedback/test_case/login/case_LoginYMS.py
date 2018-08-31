#_*_coding:utf-8_*_
#作者        ：wangmf
#创建时间    ：2018/8/21 17:37
#修改时间    ：2018/8/21 
#文件        ：case_LoginYMS.py
#
from Public import OpenApp
import unittest
from Public import LoginPage,ParseRepository,Logout
from Config import Globalvar
from Util import ObjectMap


class LoginYMS(unittest.TestCase):
    def setUp(self):
        self.driver = OpenApp.OpenVCM.Open1(self)
        print('执行test用例')
    def tearDown(self):
        pass
    def test_LoginYMS(self):
        l = LoginPage.Login_start(self.driver,Globalvar.config_path)

        #step1 登录内网Outbound账号================================================
        l.login_YMS(Globalvar.YMS_account,Globalvar.YMS_password,Globalvar.YMS_server,Globalvar.YMS_outbound)
        pp = ParseRepository.ParseRepositoryConfig(Globalvar.config_path)
        # self.driver.implicitly_wait(5)
        #点击展开设置页，验证账号信息
        ObjectMap.getElement(self.driver,'id',pp.getOptionValue('设置页相关','账号头像')).click()
        obj = ObjectMap.getElement(self.driver,"id",pp.getOptionValue('设置页相关','账号信息'))
        assert getattr(obj,'text')==Globalvar.YMS_account,('账号显示错误'+(getattr(obj,'text')))
        #退出账号
        out = Logout.Logout(self.driver)
        out.logout()

        #step2 登录外网Outbound账号================================================
        l.login_YMS(Globalvar.YMS_account, Globalvar.YMS_password, Globalvar.YMS_server, outbound='183.251.103.228')
        pp = ParseRepository.ParseRepositoryConfig(Globalvar.config_path)
        # self.driver.implicitly_wait(5)
        # 点击展开设置页，验证账号信息
        ObjectMap.getElement(self.driver, 'id', pp.getOptionValue('设置页相关', '账号头像')).click()
        obj = ObjectMap.getElement(self.driver, "id", pp.getOptionValue('设置页相关', '账号信息'))
        assert getattr(obj, 'text') == Globalvar.YMS_account, ('账号显示错误' + (getattr(obj, 'text')))
        # 退出账号
        out = Logout.Logout(self.driver)
        out.logout()

        #step3 登录无Outbound账号==================================================
        l.login_YMS(Globalvar.YMS_account, Globalvar.YMS_password, Globalvar.YMS_server, outbound=' ')
        pp = ParseRepository.ParseRepositoryConfig(Globalvar.config_path)
        # self.driver.implicitly_wait(5)
        # 点击展开设置页，验证账号信息
        ObjectMap.getElement(self.driver, 'id', pp.getOptionValue('设置页相关', '账号头像')).click()
        obj = ObjectMap.getElement(self.driver, "id", pp.getOptionValue('设置页相关', '账号信息'))
        assert getattr(obj, 'text') == Globalvar.YMS_account, ('账号显示错误' + (getattr(obj, 'text')))
        # 退出账号
        out = Logout.Logout(self.driver)
        out.logout()



if __name__=="__main__":
    unittest.main()