#__getattr__, __getattribute__
#__getattr__ 就是在查找不到属性的时候调用
from datetime import date
class User:
    def __init__(self,info={}):
        self.info = info

    #在找不到属性的时候进入这个逻辑
    def __getattr__(self, item):
        return self.info[item]

    #比getattr高级，会无条件进入这个函数
    # def __getattribute__(self, item):
    #     return "bobby"

if __name__ == "__main__":
    user = User(info={"company_name":"imooc", "name":"bobby"})
    print(user.test)
