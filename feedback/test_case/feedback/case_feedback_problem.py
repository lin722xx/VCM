#_*_coding:utf-8_*_

import os,sys,json,re
from Util import ObjectMap
from Public import ParseRepository
from Config import Globalvar
import datetime

#意见反馈操作-程序问题
class feedback:
    def setUp(self):
        self.driver = OpenApp.OpenVCM.Open1(self)
    def __init__(self,driver):
        self.driver = driver
    def feedback(self,time,err_info):
        #**注意：由于网页限制显示10个字符，所以缩短时间的显示，time必须为格式：time_now = datetime.datetime.now().strftime("%M%S")，err_info也精简突出问题**
        #进入意见反馈界面
        ObjectMap.getElement(self.driver,'id',pp.getOptionValue('设置页相关','账号头像')).click()
        ObjectMap.getElement(self.driver,'id',pp.getOptionValue('设置页相关','关于')).click()
        ObjectMap.getElement(self.driver,'id',pp.getOptionValue('关于','意见反馈')).click()
        #获取当前时间
        # print(time_now)
        #填写当前时间+问题信息，提交反馈
        ObjectMap.getElement(self.driver,'id',pp.getOptionValue('关于', '程序问题')).click()
        ObjectMap.getElement(self.driver,'id',pp.getOptionValue('关于','问题描述')).send_keys(time+err_info)
        ObjectMap.getElement(self.driver,'id',pp.getOptionValue('关于','提交')).click()

        #提交成功之后，返回主界面
        ObjectMap.getElement(self.driver,'id',pp.getOptionValue('关于','帮助'))
        ObjectMap.getElement(self.driver,'id',pp.getOptionValue('返回','返回')).click()
        operate = screen_operate(self.driver)
        operate.swipLeft(1000)

