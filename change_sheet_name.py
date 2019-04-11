from openpyxl import load_workbook


def chane_name():
    filename = 'C:/Users/ThinkPad/Desktop/查询查复列表信息.xlsx'
    wb = load_workbook(filename)
    ws = wb['hello']
    ws.title = '计划'
    wb.save(filename)  # 保存变更
    wb.close()


import os


def file_name():
    file_dir = 'C:/Users/ThinkPad/Downloads/hello'
    for root, dirs, files in os.walk(file_dir):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件


if __name__ == "__main__":
    file_name()
