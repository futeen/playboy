'''
从python-unrar开源项目官网得知了Python下的unrar还依赖RAR官方的库。

Win：

1. 先到RARLab官方下载库文件，http://www.rarlab.com/rar/UnRARDLL.exe ，然后安装；

2. 安装最好选择默认路径，一般在 C:\Program Files (x86)\UnrarDLL\ 目录下；

3. 然后重要的一步，就是添加环境变量，此电脑（我的电脑）右键，属性，找到 高级系统设置，高级 选项卡下点击 环境变量，
在系统变量（注意不是用户变量）中 新建，变量名输入 UNRAR_LIB_PATH ，必须一模一样，变量值要特别注意！如果你是64位
系统，就输入 C:\Program Files (x86)\UnrarDLL\x64\UnRAR64.dll，如果是32位系统就输入 C:\Program Files (x86)
\UnrarDLL\UnRAR.dll ，这个从unrar安装目录的内容也能看出来它是区分64和32位的。

4. 确定保存环境变量后，重启你的PyCharm，代码不变，再运行就不会出错了。这个时候依赖库已经添加到系统环境中。
'''

from unrar import rarfile

tf = rarfile.RarFile('/Users/futeen/desktop/shenyang.rar')
tf.extractall(path=r'/Users/futeen/desktop/hello')

