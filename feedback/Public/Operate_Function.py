#_*_coding:utf-8_*_
#作者        ：wangmf
#创建时间    ：2018/8/21 11:37
#修改时间    ：2018/8/21 
#文件        ：Operate_Function.py


import os,sys,json,re
from Util import ObjectMap
from Public import ParseRepository
from Config import Globalvar
import datetime

pp = ParseRepository.ParseRepositoryConfig(Globalvar.config_path)



class screen_operate:
    def __init__(self,driver):
        self.driver = driver

    def get_screen_size(self):
        # 获取屏幕宽度和高度
        size_str = os.popen('adb shell wm size').read()
        if not size_str:
            print('请安装 ADB 及驱动并配置环境变量')
            sys.exit()
        m = re.search(r'(\d+)x(\d+)', size_str)
        if m:
            return "{height}x{width}".format(height=m.group(2), width=m.group(1))

    def touch_Tab(self, tab_num, is_login=1):
        # 点击页签,tab_num为第几个页签，is_login为是否登录，分别计算，duration决定点击的速度
        size = self.get_screen_size()
        str = size.split('x')

        # 屏幕高和宽的值
        screen_height = str[0]
        screen_width = str[1]
        point_x = 0

        # 判断是否已登录情况下点击对应页签
        if is_login == 1:
            width_button = int(screen_width) / 4
            point_x = int((tab_num - 1) * width_button + int(screen_width) / 8)
        else:
            width_button = int(screen_width) / 3
            point_x = int((tab_num - 1) * width_button + int(screen_width) / 6)
        point_y = int(screen_height) - 62
        # return (point_x,point_y)
        self.driver.tap([(point_x, point_y), (point_x, point_y)])

    # 屏幕向上滑动
    def swipeUp(self,t):
        size = self.get_screen_size()
        l = size.split('x')
        x1 = int(l[1]) * 0.5  # x坐标
        y1 = int(l[0]) * 0.75  # 起始y坐标
        y2 = int(l[0]) * 0.25  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向下滑动
    def swipeDown(self,t):
        size = self.get_screen_size()
        l = size.split('x')
        x1 = int(l[1]) * 0.5  # x坐标
        y1 = int(l[0]) * 0.25  # 起始y坐标
        y2 = int(l[0]) * 0.75  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    # 屏幕向左滑动
    def swipLeft(self,t):
        size = self.get_screen_size()
        l = size.split('x')
        x1 = int(l[1]) * 0.75
        y1 = int(l[0]) * 0.5
        x2 = int(l[1]) * 0.05
        self.driver.swipe(x1, y1, x2, y1, t)

    # 屏幕向右滑动
    def swipRight(self,t):
        size = self.get_screen_size()
        l = size.split('x')
        x1 = int(l[1]) * 0.05
        y1 = int(l[0]) * 0.5
        x2 = int(l[1]) * 0.75
        self.driver.swipe(x1, y1, x2, y1, t)

#挂断通话、结束会议、离开会议、取消离开会议
class end_call:
    def __init__(self,driver):
        self.driver = driver

    def end_call(self):
        try:
            ObjectMap.getElement(self.driver,'id',pp.getOptionValue('通话界面','挂断')).click()
        except:
            ObjectMap.getElement(self.driver,'id',pp.getOptionValue('通话界面','标题')).click()
            ObjectMap.getElement(self.driver,'id',pp.getOptionValue('通话界面','挂断')).click()

    def end_meeting(self):
        self.end_call()
        # ObjectMap.getElement(self.driver,'id',pp.getOptionValue('通话界面','挂断')).click()
        ObjectMap.getElement(self.driver,'id',pp.getOptionValue('通话界面','结束会议')).click()
    def leave_meeting(self):
        self.end_call()
        ObjectMap.getElement(self.driver,'id',pp.getOptionValue('通话界面','离开会议')).click()

    def cancel_endcall(self):
        self.end_call()
        ObjectMap.getElement(self.driver,'id',pp.getOptionValue('通话界面','取消挂断')).click()


#意见反馈操作
class feedback:
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
        ObjectMap.getElement(self.driver,'id',pp.getOptionValue('关于','问题描述')).send_keys(time+err_info)
        ObjectMap.getElement(self.driver,'id',pp.getOptionValue('关于','提交')).click()

        #提交成功之后，返回主界面
        ObjectMap.getElement(self.driver,'id',pp.getOptionValue('关于','帮助'))
        ObjectMap.getElement(self.driver,'id',pp.getOptionValue('返回','返回')).click()
        operate = screen_operate(self.driver)
        operate.swipLeft(1000)





# if __name__ == '__main__':
#     unittest.main()