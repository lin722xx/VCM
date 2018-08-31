from appium import webdriver
import unittest,os,time
from Util import ObjectMap
from Public import ParseRepository
from Config import Globalvar

pp = ParseRepository.ParseRepositoryConfig(Globalvar.config_path)


class OpenVCM(unittest.TestCase):
    def Open1(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '7.0',
            'appPackage': 'com.yealink.videophone',
            'appActivity': 'WaitingActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'deviceName':'8452f49e0804'
        }
        self.driver2 = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver2.implicitly_wait(30) #隐性等待时间为30秒
        return self.driver2

    def Open_skip(self):
        driver = OpenVCM.Open1(self)
        ObjectMap.getElement(driver,'id',pp.getOptionValue('启动页选项','跳过')).click()
        return driver