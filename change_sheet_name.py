from openpyxl import load_workbook


def chane_name():
    filename = 'C:/Users/ThinkPad/Desktop/��ѯ�鸴�б���Ϣ.xlsx'
    wb = load_workbook(filename)
    ws = wb['hello']
    ws.title = '�ƻ�'
    wb.save(filename)  # ������
    wb.close()


import os


def file_name():
    file_dir = 'C:/Users/ThinkPad/Downloads/hello'
    for root, dirs, files in os.walk(file_dir):
        print(root)  # ��ǰĿ¼·��
        print(dirs)  # ��ǰ·����������Ŀ¼
        print(files)  # ��ǰ·�������з�Ŀ¼���ļ�


if __name__ == "__main__":
    file_name()
