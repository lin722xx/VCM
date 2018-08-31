#_*_coding:utf-8_*_
#作者        ：wangmf
#创建时间    ：2018/8/28 20:21
#修改时间    ：2018/8/28 
#文件        ：Logout.py

from Config import Globalvar
from Util import ObjectMap
from Public import ParseRepository,OpenApp
pp = ParseRepository.ParseRepositoryConfig(Globalvar.config_path)

class Logout:
    def __init__(self,driver):
        self.driver = driver
    def logout(self):
        #主界面退出账号
        ObjectMap.getElement(self.driver,'id',pp.getOptionValue('设置页相关','账号头像')).click()
        ObjectMap.getElement(self.driver,'id',pp.getOptionValue('设置页相关','云账号')).click()
        ObjectMap.getElement(self.driver,"id",pp.getOptionValue('云账号界面','注销')).click()
        ObjectMap.getElement(self.driver, "id", pp.getOptionValue('云账号界面', '确定退出')).click()


if __name__ == '__main__':
    op = OpenApp.OpenVCM()
    driver = op.Open1()
    lout = Logout(driver)
    lout.logout()

