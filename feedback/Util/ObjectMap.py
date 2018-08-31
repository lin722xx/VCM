#_*_coding:utf-8_*_
#作者        ：wangmf
#创建时间    ：2018/8/28 17:08
#修改时间    ：2018/8/28 
#文件        ：ObjectMap.py


from selenium.webdriver.support.ui import WebDriverWait


#获取单个元素，locateType值为xpath,或者ID，loacteExpression为对应的id或者xpath
def getElement(driver,locateType,locateExpression):
    try:
        element = WebDriverWait(driver,10).until(lambda x:x.find_element(by=locateType,value=locateExpression))
        return element
    except Exception as e:
        raise e


def getElements(driver,locateType,locateExpression):
    try:
        elements = WebDriverWait(driver, 10).until(lambda x: x.find_elements(by=locateType, value=locateExpression))
        return elements
    except Exception as e:
        raise e


if __name__ == '__main__':
    #测试代码
    from Public import ParseRepository
    from Public import OpenApp
    open = OpenApp.OpenVCM()
    driver = open.Open1()
    pp=ParseRepository.ParseRepositoryConfig('../Config/config.ini')

    search = getElement(driver,"id",pp.getOptionValue('启动页选项','YMS服务器'))
    search.click()
    search1 = getElement(driver,"id",pp.getOptionValue('YMS_Account','登录'))
    search1.send_keys("000055")
