from ctypes import *
from ctypes.wintypes import *

    
def imouse_drag(x1, y1, x2, y2,button='left',speed=10):  
    time.sleep(2)
    # (x1,y1)，(x2,y2)分别表示：鼠标移动的初末坐标点   
    try:
        dll = windll.LoadLibrary("../Com.Isearch.Func.AutoIt/AutoItX3.dll")         
    # 对象为：本地的一个动态链接库文件
        return dll.AU3_MouseClickDrag(button,x1,y1,x2,y2,speed)                     
    # 使用鼠标点击拖动方法
    except Exception as e:
        raise e
