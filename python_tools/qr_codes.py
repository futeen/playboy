import qrcode
from PIL import Image
import os
from MyQR import myqr


def first_demo():
    # 存储字符串
    qr = qrcode.make("hello world")
    qr.get_image().show()


# 将二维码保存到本地
def second_demo():
    text = "www.baidu.com"
    img = qrcode.make(text)
    img.save('qr.png')
    img.show()


# 生成带有内嵌图片的二维码
def third_demo():
    qr = qrcode.QRCode(
        # 二维码size尺寸大小。官方称为version
        version=1,
        # 二维码错误处理级别，有四种方式，稍后给出解释
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        # 二维码图片的大小
        box_size=10,
        # 二维码白色边框的大小
        border=2
    )
    # 添加数据
    qr.add_data('小可爱你好，我是波多野结衣老湿')
    # 填充数据
    qr.make(fit=True)
    # 生成二维码图片        指定填充颜色        指定背景颜色
    img = qr.make_image(fill_color='black', back_color='white')

    # 得到生成的二维码图片的宽，高
    img_w, img_h = img.size

    # 添加图片到二维码中
    # 使用pillow的Image打开图片
    icon = Image.open('girl.jpg')

    # 设置icon的大小,为二维码图片大小的6分之一
    factor = 3
    size_w = img_w // factor
    size_h = img_h // factor

    # 得到icon图片的大小
    icon_w, icon_h = icon.size

    # 只有当我们icon图片的大小超过了二维码图片的3分之一的时候，才对icon图片大小重新定义大小。
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h

    # 重新设置icon的尺寸
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    # 得到在二维码中显示的位置，坐标。
    w = (img_w - icon_w) // 2
    h = (img_h - icon_h) // 2

    img.paste(icon, (w, h), mask=None)
    # girl.jpg 是内嵌的图片路径
    img.save('girl_imag.jpg')


# 生成带背景图片的二维码
def fourth_demo():
    words = 'i-search rpa'
    # 调用myqr.run方法，就能够生成图片了。返回三个值，二维码的version，纠错级别，二维码的完整路径
    version, level, qr_name = myqr.run(
        # 存放的数据
        words=words,
        # 二维码size
        version=10,
        # 选取的背景图片
        picture='girl.jpg',
        # 是否为彩色。如果为False，那么就是黑白的
        colorized=True,
        # 保存到本地的名字
        save_name='girl_img.png',
        # 保存二维码的目录,这里就是当前目录。默认就是这个
        save_dir=os.getcwd()
    )
    print(version, level, qr_name)


if __name__ == "__main__":
    second_demo()

