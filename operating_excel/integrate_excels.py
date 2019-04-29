from win32.com.client import Dispatch

path1 = 'filepath_a.xlsx'
path2 = 'filepath_b.xlsx'
path3 = 'filepath_c.xlsx'
path4 = 'filepath_d.xlsx'
path5 = 'filepath_e.xlsx'
path6 = 'filepath_f.xlsx'


# 打开容器excel功能
x1 = Diapatch("Excel.Application")
x1.Visible = True
x2 = Diapatch("Excel.Application")
x3 = Diapatch("Excel.Application")
x4 = Diapatch("Excel.Application")
x5 = Diapatch("Excel.Application")
x6 = Diapatch("Excel.Application")

# 打开表格
wb1 = x1.Workbooks.Open(path1)
wb2 = x2.Workbooks.Open(path2)
wb3 = x3.Workbooks.Open(path3)
wb4 = x4.Workbooks.Open(path4)
wb5 = x5.Workbooks.Open(path5)
wb6 = x6.Workbooks.Open(path6)

#确认操作sheet
ws1 = wb1.Worksheets(1)
ws2 = wb1.Worksheets(1)
ws3 = wb1.Worksheets(1)
ws4 = wb1.Worksheets(1)
ws5 = wb1.Worksheets(1)
ws6 = wb1.Worksheets(1)

# 将表格整合到file1
ws2.Copy(Before=wb1.Workbooks(1))
ws3.Copy(Before=wb1.Workbooks(1))
ws4.Copy(Before=wb1.Workbooks(1))
ws5.Copy(Before=wb1.Workbooks(1))
ws6.Copy(Before=wb1.Workbooks(1))

# 关闭excel
wb1.Close(SaveChanges=True)
wb2.Close(SaveChanges=True)
wb3.Close(SaveChanges=True)
wb4.Close(SaveChanges=True)
wb5.Close(SaveChanges=True)
wb6.Close(SaveChanges=True)

# 退出
x1.Quit()