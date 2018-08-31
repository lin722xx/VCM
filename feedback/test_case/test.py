#_*_coding:utf-8_*_
#作者        ：wangmf
#创建时间    ：2018/8/29 15:14
#修改时间    ：2018/8/29 
#文件        ：test.py

from Public import Operate_Function,OpenApp
from Util import ObjectMap
import datetime,unittest,time

# time_now = datetime.datetime.now()
# print(time_now.strftime("%m%d%H%M%S"))

class test1(unittest.TestCase):
    def setUp(self):
        self.dr = OpenApp.OpenVCM.Open_skip(self)
    def test_1(self):
        # self.dr.implicitly_wait(10)
        # ObjectMap.getElement(self.dr, 'id', 'com.yealink.videophone:id/skip').click()
        # ObjectMap.getElement(self.dr,'id','com.yealink.videophone:id/btn_meeting_now')
        # test = Operate_Function.feedback(self.dr)
        # test.feedback('测试意见反馈')
        # touch_tab = Operate_Function.screen_operate(self.dr)
        # touch_tab.touch_Tab(3, 0)
        # touch_tab.swipLeft(1000)
        print('111')
        # x=self.dr.get_window_size()['width']
        # y=self.dr.get_window_size()['height']
        # print(x,y)

if __name__ == '__main__':
    unittest.main()