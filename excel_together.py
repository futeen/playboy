from win32com.client import Dispatch

path1 = 'File_path'
path2 = 'File_path'

xl = Dispatch("Excel.Application")
xl.Visible = True  # ��True�ĳ�false��������excel�Ĳ����ɼ���

wb1 = xl.Workbooks.Open(Filename=path1)
wb2 = xl.Workbooks.Open(Filename=path2)

ws1 = wb1.Worksheets(1)
ws1.Copy(Before=wb2.Worksheets(1))

wb2.Close(SaveChanges=True)
xl.Quit()