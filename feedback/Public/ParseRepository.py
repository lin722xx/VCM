#_*_coding:utf-8_*_
#作者        ：wangmf
#创建时间    ：2018/8/28 15:52
#修改时间    ：2018/8/28 
#文件        ：ParseRepository.py


from configparser import ConfigParser

#封装config信息获取

class ParseRepositoryConfig(object):
    def __init__(self,config_path):
        self.cf = ConfigParser()
        self.cf.read(config_path,encoding='utf-8')

    #获取section下所有的信息
    def getItemSection(self,sectionName):
        # print(self.cf.items(sectionName))
        return dict(self.cf.items(sectionName))

    #根据sectionName，和optionName获取对应的信息
    def getOptionValue(self,sectionName,optionName):
        # print(self.cf.get(sectionName,optionName))
        return self.cf.get(sectionName,optionName)


if __name__ == '__main__':
    pp = ParseRepositoryConfig('../Config/config.ini')
    print(pp.getItemSection('启动页选项'))
    print(pp.getOptionValue('启动页选项','YMS服务器'))
