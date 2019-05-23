# 编译日期：2019-05-20 10:27:29
# 版权所有：www.i-search.com.cn
# coding=utf-8
import time
import pdb
from ubpa.ilog import ILog
from ubpa.base_img import *
import getopt
from sys import argv
import sys
import pandas as pd
import ubpa.iexcel as iexcel

path_addition = "D:/个税申报/201904/薪资明细/4月补发（定）.xls"
path_offie = "D:/个税申报/201904/薪资明细/4月发放3月办公厅值班费（定）.xls"
path_vip = "D:/个税申报/201904/薪资明细/董秘、总监、首席2.xls"
path_ceo = "D:/个税申报/201904/薪资明细/高管1.xls"
path_retire = "D:/个税申报/201904/薪资明细/离退休5.xls"
path_mosco = "D:/个税申报/201904/薪资明细/莫斯科代表处4.xls"
path_quit = "D:/个税申报/201904/薪资明细/内退3.xls"
path_comofficer = "D:/个税申报/201904/薪资明细/在职（交流干部）6.xls"
path_salarydiff = "D:/个税申报/201904/薪资明细/在职（其他工资绩效奖金差额）8.xls"
path_onpositon = "D:/个税申报/201904/薪资明细/在职（终-删林森）7.xls"


def integrete_data(file_path):
    '''
    header = {"工号":[""],"姓名":[""],"证件类型":[""],"*证照号码":[""],"*本期收入":[""],"本期免税收入":[""],
    "基本养老保险费":[""],"基本医疗保险费":[""],"失业保险费":[""],"住房公积金":[""], "累计子女教育":[""],
    "累计继续教育":[""],"累计住房贷款利息":[""],"累计住房租金":[""],"累计赡养老人":[""],"企业(职业)年金":[""],
    "商业健康保险":[""],"税延养老保险":[""],"其他":[""],"准予扣除的捐赠额":[""],"减免税额":[""],"备注":[""],
    "累计应补(退)税额":[""],"累计减除费用":[""],"累计专项附加扣除":[""],
    }
    '''
    df = pd.read_excel(file_path)[:-3]
    name = file_path[20:-4]
    print(name)
    # generate aim excel
    df_result = pd.DataFrame(columns=("工号","姓名","证件类型","*证照号码","*本期收入","本期免税收入",
    "基本养老保险费","基本医疗保险费","失业保险费","住房公积金", "累计子女教育", "累计继续教育",
    "累计住房贷款利息","累计住房租金","累计赡养老人","企业(职业)年金","商业健康保险","税延养老保险",
    "其他","准予扣除的捐赠额","减免税额","备注","累计应补(退)税额","累计减除费用","累计专项附加扣除"))
    
    # 在职（终-删林森）7.xls
    if name == "在职（终-删林森）7":
        df_result["姓名"] = df["人员姓名"]
        df_result["*证照号码"] = df["身份证号"]
        df_result["*本期收入"] = df["应发合计"]+df["公积金纳税部分"]-df["薪资扣款"]+df["扣款"]
        df_result["本期免税收入"] = df["托补"]+df["房租补"]+df["话费1"]+df["纳税基数抵扣"]
        df_result["基本养老保险费"] = df["扣养老"]
        df_result["基本医疗保险费"] = df["扣医疗"]+df["扣大额"]
        df_result["失业保险费"] = df["扣失业"]
        df_result["住房公积金"] = df["扣公积金"]+df["补扣公积金"]
        df_result["企业(职业)年金"] = df["扣企业年金"]
        df_result["累计应补(退)税额"] = df["本次代扣税"]
        df_result["累计减除费用"] = df["起征点"]
        df_result["累计专项附加扣除"] = df["专项附加扣除合计"]
    
    # 在职（其他工资绩效奖金差额）8.xls
    if name == "在职（其他工资绩效奖金差额）8":
        df_result["姓名"] = df["人员姓名"]
        df_result["*证照号码"] = df["身份证号"]
        df_result["*本期收入"] = df["应发合计"]
        df_result["累计应补(退)税额"] = df["本次代扣税"]
        df_result["累计减除费用"] = df["起征点"]
        df_result["累计专项附加扣除"] = df["专项附加扣除合计"]
    
    # 在职（交流干部）6.xls
    if name == "在职（交流干部）6":
        df_result["姓名"] = df["人员姓名"]
        df_result["*证照号码"] = df["身份证号"]
        df_result["*本期收入"] = df["应发合计"]+df["公积金纳税部分"]-df["薪资扣款"]+df["扣款"]
        df_result["本期免税收入"] = df["托补"]+df["房租补"]+df["话费1"]+df["纳税基数抵扣"]
        df_result["基本养老保险费"] = df["扣养老"]
        df_result["基本医疗保险费"] = df["扣医疗"]+df["扣大额"]
        df_result["失业保险费"] = df["扣失业"]
        df_result["住房公积金"] = df["扣公积金"]+df["补扣公积金"]
        df_result["企业(职业)年金"] = df["扣企业年金"]
        df_result["累计应补(退)税额"] = df["本次代扣税"]
        df_result["累计减除费用"] = df["起征点"]
        df_result["累计专项附加扣除"] = df["专项附加扣除合计"]
    
    # 莫斯科代表处4.xls
    if name == "莫斯科代表处4":
        df_result["姓名"] = df["人员姓名"]
        df_result["*证照号码"] = df["身份证号"]
        df_result["*本期收入"] = df["应发合计"]
        df_result["本期免税收入"] = df["房租补"]+df["话费"]+df["纳税基数抵扣"]
        df_result["累计应补(退)税额"] = df["本次代扣税"]
        df_result["累计减除费用"] = df["起征点"]
        df_result["累计专项附加扣除"] = df["专项附加扣除合计"]
    
    # 高管1.xls
    if name == "高管1":
        df_result["姓名"] = df["人员姓名"]
        df_result["*证照号码"] = df["身份证号"]
        df_result["*本期收入"] = df["应发合计"]+df["扣款"]
        df_result["本期免税收入"] = df["话费1"]
        df_result["基本养老保险费"] = df["扣养老"]
        df_result["基本医疗保险费"] = df["扣医疗"]+df["扣大额"]
        df_result["失业保险费"] = df["扣失业"]
        df_result["住房公积金"] = df["扣当月公积"]  # different name
        df_result["企业(职业)年金"] = df["扣企业年金"]
        df_result["累计应补(退)税额"] = df["本次代扣税"]
        df_result["累计减除费用"] = df["起征点"]
        df_result["累计专项附加扣除"] = df["专项附加扣除合计"]
    
    # 内退3.xls
    if name == "内退3":
        df_result["姓名"] = df["人员姓名"]
        df_result["*证照号码"] = df["身份证号"]
        df_result["*本期收入"] = df["应发合计"]
        df_result["本期免税收入"] = df["房租补"]
        df_result["累计应补(退)税额"] = df["本次代扣税"]
        df_result["累计减除费用"] = df["起征点"]
        df_result["累计专项附加扣除"] = df["专项附加扣除合计"]
        
    # 离退休5.xls
    if name == "离退休5":
        df_result["姓名"] = df["人员姓名"]
        df_result["*证照号码"] = df["身份证号"]
        df_result["*本期收入"] = df["应发合计"]
        df_result["本期免税收入"] = df["其他补"]-df["免税合计"]
        #df_result["累计应补(退)税额"] = df["本次代扣税"]  # need ensure the item
        df_result["累计减除费用"] = df["起征点"]
        df_result["累计专项附加扣除"] = df["专项附加扣除合计"]
        
    # 董秘、总监、首席2
    if name == "董秘、总监、首席2":
        df_result["姓名"] = df["人员姓名"]
        df_result["*证照号码"] = df["身份证号"]
        df_result["*本期收入"] = df["应发合计"]
        df_result["本期免税收入"] = df["房租补"]+df["话费1"]
        df_result["基本养老保险费"] = df["扣养老"]
        df_result["基本医疗保险费"] = df["扣医疗"]+df["扣大额"]
        df_result["失业保险费"] = df["扣失业"]
        df_result["住房公积金"] = df["扣当月公积"]
        df_result["企业(职业)年金"] = df["扣企业年金"]
        df_result["累计应补(退)税额"] = df["本次代扣税"]
        df_result["累计减除费用"] = df["起征点"]
        df_result["累计专项附加扣除"] = df["专项附加扣除合计"]
        
    # 4月发放3月办公厅值班费（定）
    if name == "4月发放3月办公厅值班费（定）":
        df_result["姓名"] = df["人员姓名"]
        df_result["*证照号码"] = df["身份证号"]
        df_result["*本期收入"] = df["应发合计"]
        df_result["累计应补(退)税额"] = df["本次代扣税"]  
        
    # 4月补发（定）
    if name == "4月补发（定）":
        df_result["姓名"] = df["人员姓名"]
        df_result["*证照号码"] = df["身份证号"]
        df_result["*本期收入"] = df["应发合计"]
        df_result["本期免税收入"] = df["托补"] + df["房租补"]
        df_result["累计应补(退)税额"] = df["本次代扣税"]  
        df_result["累计减除费用"] = df["起征点"]
        df_result["累计专项附加扣除"] = df["专项附加扣除合计"]
        
    return df_result
    
def write_result():
    # get data result 
    data_addition = integrete_data(path_addition)      # deal on single way  
    data_office = integrete_data(path_offie)           # deal on single way 
    data_vip = integrete_data(path_vip)
    data_ceo = integrete_data(path_ceo)
    data_retire = integrete_data(path_retire)
    data_mosco = integrete_data(path_mosco)
    data_quit = integrete_data(path_quit)
    data_comofficer = integrete_data(path_comofficer)
    data_salarydiff = integrete_data(path_salarydiff)  # deal on single way 
    data_onposition = integrete_data(path_onpositon)
    
    # integrete data into df_final sheet
    df_final = data_vip.append(data_ceo)
    df_final = df_final.append(data_retire)
    df_final = df_final.append(data_mosco)
    df_final = df_final.append(data_quit)
    df_final = df_final.append(data_comofficer)
    df_final = df_final.append(data_onposition)
    
    # deal with header
    df_final.reset_index(drop=True, inplace=True)
    df_final.index.name = "编号"
    
    # get result sheet
    print(df_final)
    return df_final
    #df_final.to_excel("C:/Users/Administrator/Desktop/a.xlsx")


# get result of different in two sheets
def get_diff(path_a, path_b):
    df_a = integrete_data(path_a)
    df_b = integrete_data(path_b)
    
    # find the same names 
    df_samea = df_a[df_a["*证照号码"].isin(df_b["*证照号码"])]
    df_sameb = df_b[df_b["*证照号码"].isin(df_a["*证照号码"])]
    df_samea.reset_index(drop=True, inplace=True)
    df_sameb.reset_index(drop=True, inplace=True)
    
    # get unique items in df_a
    df_uniquea = df_a.append(df_samea)
    df_uniquea.drop_duplicates(keep=False,inplace=True)
    df_uniquea.reset_index(drop=True, inplace=True)
    
    # get unique items in df_b
    df_uniqueb = df_b.append(df_sameb)
    df_uniqueb.drop_duplicates(keep=False,inplace=True)
    df_uniqueb.reset_index(drop=True, inplace=True)
    
    # compute samea and sameb
    df_samea = df_samea.sort_values(by=["*证照号码"])
    df_sameb = df_sameb.sort_values(by=["*证照号码"])
    df_samea["累计应补(退)税额"] = df_samea["累计应补(退)税额"] + df_sameb["累计应补(退)税额"]
    df_samea.reset_index(drop=True, inplace=True)
    
    df = df_samea.append(df_uniquea)
    df = df.append(df_uniqueb)
    df.reset_index(drop=True, inplace=True)
    print(df)
    return df
    
    

def test():
    '''
    data_onposition = integrete_data(path_onpositon)
    data_salarydiff = integrete_data(path_salarydiff) 
    '''
    get_diff(path_onpositon, path_salarydiff)
