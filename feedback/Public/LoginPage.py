#_*_coding:utf-8_*_
#作者        ：wangmf
#创建时间    ：2018/8/27 18:35
#修改时间    ：2018/8/27 
#文件        ：LoginPaage.py


from Public import OpenApp
from Public import ParseRepository
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Config import Globalvar
from Util import ObjectMap

class Login_start:
    def __init__(self,driver,config_path):
        self.driver = driver
        self.pp = ParseRepository.ParseRepositoryConfig(config_path)
    def login_YMS(self,username,pwd,server,outbound):
        ObjectMap.getElement(self.driver,"id",self.pp.getOptionValue('启动页选项','YMS服务器')).click()
        #输入账号信息
        ObjectMap.getElement(self.driver,"id",self.pp.getOptionValue('YMS_Account','账号')).send_keys(username)
        ObjectMap.getElement(self.driver,"id",self.pp.getOptionValue('YMS_Account','密码')).send_keys(pwd)
        ObjectMap.getElement(self.driver,"id",self.pp.getOptionValue('YMS_Account','服务器')).send_keys(server)

        #判断Outbound是否为空，不为空时如果Outbound编辑框超时，点击高级设置，展开Outbound编辑框

        try:
            ObjectMap.getElement(self.driver,"id",self.pp.getOptionValue('YMS_Account','outbound')).send_keys(outbound)
        except Exception as e:
            # print(e)
            ObjectMap.getElement(self.driver,"id",self.pp.getOptionValue('YMS_Account','高级设置')).click()
            obj = ObjectMap.getElement(self.driver, "id", self.pp.getOptionValue('YMS_Account', 'outbound'))
            if outbound != ' ':
                obj.send_keys(outbound)
            else:
                obj.clear()
        #点击登录
        ObjectMap.getElement(self.driver,"id",self.pp.getOptionValue('YMS_Account','登录')).click()

    def login_Cloud(self,username,pwd,server):

        ObjectMap.getElement(self.driver, "id", self.pp.getOptionValue('启动页选项', 'Cloud服务器')).click()
        #点击账号登录页签
        ObjectMap.getElement(self.driver,"xpath",self.pp.getOptionValue('Cloud_Account', '账号登录')).click()
        #输入账号信息
        ObjectMap.getElement(self.driver, "id", self.pp.getOptionValue('Cloud_Account', '账号')).send_keys(username)
        ObjectMap.getElement(self.driver, "id", self.pp.getOptionValue('Cloud_Account', '密码')).send_keys(pwd)
        ObjectMap.getElement(self.driver, "id", self.pp.getOptionValue('Cloud_Account', '服务器')).send_keys(server)
        ObjectMap.getElement(self.driver, "id", self.pp.getOptionValue('YMS_Account', '登录')).click()



if __name__ == '__main__':
    open = OpenApp.OpenVCM()
    ls=Login_start(open.Open1(),'../Config/config.ini')
    ls.login_YMS(Globalvar.YMS_account,Globalvar.YMS_password,Globalvar.YMS_server,Globalvar.YMS_outbound)