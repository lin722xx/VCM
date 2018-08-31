#_*_coding:utf-8_*_
#作者        ：wangmf
#创建时间    ：2018/8/21 11:23
#修改时间    ：2018/8/21 
#文件        ：case_IPcall.py

from appium import webdriver
from Public import OpenApp,Operate_Function,ParseRepository,LoginPage
from Util import ObjectMap
from Config import Globalvar
import unittest,datetime


pp = ParseRepository.ParseRepositoryConfig(Globalvar.config_path)



class CallIP(unittest.TestCase):
    def setUp(self):
        self.dr =OpenApp.OpenVCM.Open_skip(self)
    def tearDown(self):
        self.dr.close_app()
    def test_CallIP(self):
        #实例化结束通话
        endcall = Operate_Function.end_call(self.dr)
        #step1启动App，进入拨号盘界面======================================
        # ObjectMap.getElement(self.dr,'id',pp.getOptionValue('启动页选项','跳过')).click()
        ObjectMap.getElement(self.dr,'id',pp.getOptionValue('会议界面','即时会议'))
        #点击跳转页签拨号盘界面
        touch_tab = Operate_Function.screen_operate(self.dr)
        touch_tab.touch_Tab(3,0)

        #step2呼出ip地址操作===============================================
        #以下点击拨号盘等操作
        try:
            obj=ObjectMap.getElement(self.dr,'id',pp.getOptionValue('拨号页面','编辑框'))
        except:
            touch_tab.touch_Tab(3, 0)
            obj=ObjectMap.getElement(self.dr,'id',pp.getOptionValue('拨号页面','编辑框'))

        obj.send_keys(Globalvar.CallIP)#输入ip地址
        ObjectMap.getElement(self.dr,'id',pp.getOptionValue('拨号页面','呼出')).click()

        #step3验证通话界面标题显示===========================================
        #判断通话界面的标题和number是否显示对应ip地址
        title = ObjectMap.getElement(self.dr,'id',pp.getOptionValue('通话界面','标题'))
        title_text = getattr(title,'text')
        assert title_text==Globalvar.CallIP,'标题显示为"' + title_text + '"与预期不符'

        number = ObjectMap.getElement(self.dr,'id',pp.getOptionValue('通话界面','号码'))
        number_text=getattr(number,'text')
        assert number_text==Globalvar.CallIP,'号码显示为"' + number_text + '"与预期不符'

        #step4验证通话统计界面===============================================
        #发送界面统计值
        ObjectMap.getElement(self.dr,'id',pp.getOptionValue('通话界面','通话统计')).click()
        send_values = ObjectMap.getElements(self.dr,'id',pp.getOptionValue('通话统计界面','value值'))
        for obj in send_values:
            obj_text = getattr(obj,'text')
            if obj_text=='0*0':
                # print('分辨率值异常')
                time_now = datetime.datetime.now().strftime("%M%S")
                ObjectMap.getElement(self.dr,'id',pp.getOptionValue('返回','返回')).click()
                endcall.end_call()
                #意见反馈
                fdb = Operate_Function.feedback(self.dr)
                fdb.feedback(time_now,'分辨率异常')
                break
        #接收界面统计值
        ObjectMap.getElement(self.dr,'xpath',pp.getOptionValue('通话统计界面','接收'))
        receive_values = ObjectMap.getElement(self.dr,'id',pp.getOptionValue('通话统计界面','value值'))
        for obj1 in receive_values:
            obj1_text = getattr(obj1,'text')
            if obj1_text=='0*0':

                time_now = datetime.datetime.now().strftime("%M%S")
                ObjectMap.getElement(self.dr, 'id', pp.getOptionValue('返回', '返回')).click()
                endcall.end_call()
                # 意见反馈
                fdb = Operate_Function.feedback(self.dr)
                fdb.feedback(time_now, '分辨率异常')
                break
        ObjectMap.getElement(self.dr,'id',pp.getOptionValue('返回','返回')).click()
        endcall.end_call()




if __name__ == "__main__":
    unittest.main()
    # suite = unittest.TestLoader().loadTestsFromTestCase(batchuncollectionmailTest)
    # unittest.TextTestRunner(verbosity=2).run(suite)