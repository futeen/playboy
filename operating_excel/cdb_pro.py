# 编译日期：2019-05-09 13:46:21
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

'''
def test():
    df = pd.read_excel("C:/Users/Administrator/Desktop/测试资料包-国开行/1、薪资发放明细表/在职1.xls")
    df2 = pd.read_excel("C:/Users/Administrator/Desktop/测试资料包-国开行/3、薪资发放明细表-合并.xls")
    num = df.pop("房租补").values.tolist()  # 拿出标题头的数据
    num2 = df.pop("专项附加扣除合计").values.tolist()
    data = list(map(lambda x, y: x + y, num, num2))

    data = pd.DataFrame(data)
    print(data)

    df2["本期免税收入"] = data
    df2.to_excel("C:/Users/Administrator/Desktop/a.xlsx")
    

def judge_num():
    num = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='b1')
    num = len(num)
    print(num)
    return num

# 获取在职7 数据
def get_data_one():
    # 在职 7
    name = ['b']
    card_id = ['e']
    cur_income = ['w', 'am', 'ad', 'ae']
    cur_notax = ['u', 'n', 'ao', 'an']
    old_fee = ['y']
    health_fee = ['aa', 'ab']
    losejob_fee = ['z']
    house_fee = ['x', 'ag']
    year_fee = ['ac']
    tax_fee = ['ai']
    start_point = ['h']
    special_discount = ['i']
    
    current_income = [name, card_id, cur_income, cur_notax, old_fee, health_fee, losejob_fee, house_fee, year_fee, tax_fee, start_point, special_discount]
    print(current_income)
    # get all data
    name_data, card_id_data, cur_income_data, cur_notax_data, old_fee_data, health_fee_data, losejob_fee_data, house_fee_data, year_fee_data, tax_fee_data, start_point_data, special_discount_data = [],[],[],[],[],[],[],[],[],[],[],[]
    
    integrete_data = []
    for x in current_income:
        if x == name:
            for h in x:
                cell_eight = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（终-删林森）7.xls',cell='{0}7'.format(h))
                cell_eight = cell_eight[:-3]
                name_data.append(cell_eight)
            integrete_data.append(name_data)
            
        if x == card_id:
            for i in x:
                cell_nine = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（终-删林森）7.xls',cell='{0}7'.format(i))
                cell_nine = cell_nine[:-3]
                card_id_data.append(cell_nine)
            integrete_data.append(card_id_data)
            
            
        if x == cur_income:
            print('this is cur_income')
            for a in x:
                cell_one = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（终-删林森）7.xls',cell='{0}7'.format(a))
                cell_one = cell_one[:-3]
                cur_income_data.append(cell_one)
            integrete_data.append(cur_income_data)
            
            
        if x == cur_notax:
            for b in x:
                cell_two = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（终-删林森）7.xls',cell='{0}7'.format(b))
                cell_two = cell_two[:-3]
                cur_notax_data.append(cell_two)
            integrete_data.append(cur_notax_data)
                
        if x == old_fee:
            for c in x:
                cell_three = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（终-删林森）7.xls',cell='{0}7'.format(c))
                cell_three = cell_three[:-3]
                old_fee_data.append(cell_three)
            integrete_data.append(old_fee_data)
                
        if x == health_fee:
            for d in x:
                cell_four = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（终-删林森）7.xls',cell='{0}7'.format(d))
                cell_four = cell_four[:-3]
                health_fee_data.append(cell_four)
            integrete_data.append(health_fee_data)
                
        if x == losejob_fee:
            for e in x:
                cell_five = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（终-删林森）7.xls',cell='{0}7'.format(e))
                cell_five = cell_five[:-3]
                losejob_fee_data.append(cell_five)
            integrete_data.append(losejob_fee_data)
        
        if x == house_fee:
            for f in x:
                cell_six = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（终-删林森）7.xls',cell='{0}7'.format(f))
                cell_six = cell_six[:-3]
                house_fee_data.append(cell_six)
            integrete_data.append(house_fee_data)
                
        if x == year_fee:
            for g in x:
                cell_seven = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（终-删林森）7.xls',cell='{0}7'.format(g))
                cell_seven = cell_seven[:-3]
                year_fee_data.append(cell_seven)
            integrete_data.append(year_fee_data)
        
        if x == tax_fee:
            for j in x:
                cell_ten = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（终-删林森）7.xls',cell='{0}7'.format(j))
                cell_ten = cell_ten[:-3]
                tax_fee_data.append(cell_ten)
            integrete_data.append(tax_fee_data)
        
        if x == start_point:
            for k in x:
                cell_eleven = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（终-删林森）7.xls',cell='{0}7'.format(k))
                cell_eleven = cell_eleven[:-3]
                start_point_data.append(cell_eleven)
            integrete_data.append(start_point_data)
        
        if x == special_discount:
            for l in x:
                cell_twelve = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（终-删林森）7.xls',cell='{0}7'.format(l))
                cell_twelve = cell_twelve[:-3]
                special_discount_data.append(cell_twelve)
            integrete_data.append(special_discount_data)
    return integrete_data



def ready_data_one():
    # 在职 7，数据整理
    # name, card_id, cur_income, cur_notax, old_fee, health_fee, losejob_fee, house_fee, year_fee
    data = get_data_one()
    print(len(data)) 
    print('---------------------------------')
    name, card_id, cur_income, cur_notax, old_fee, health_fee, losejob_fee, house_fee, year_fee, tax_fee, start_point, special_discount = data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11]
    all_data = [name, card_id, cur_income, cur_notax, old_fee, health_fee, losejob_fee, house_fee, year_fee, tax_fee, start_point, special_discount]
    for x in all_data:
        for y in x:
            for z in range(len(y)):
                if y[z] == '':
                    y[z] = 0
                
    # 在职7数据准备
    data = all_data
    name_final, card_id_final, cur_income_final, cur_notax_final, old_fee_final, health_fee_final, losejob_fee_final, house_fee_final, year_fee_final, tax_fee_final, start_point_final, special_discount_final=[],[],[],[],[],[],[],[],[],[],[],[]
    print(len(tax_fee[0]), len(start_point[0]), len(special_discount[0]))
    for x in range(len(cur_income[0])):
        # 姓名
        result_name = name[0][x]
        name_final.append(result_name)
        # 身份证号
        result_cardid = card_id[0][x]
        card_id_final.append(result_cardid)
        # 本期收入
        result_curincome = cur_income[0][x]+cur_income[1][x]-cur_income[2][x]-cur_income[3][x]
        cur_income_final.append(result_curincome)
        # 本期免税收入
        result_curnotax = cur_notax[0][x]+cur_notax[1][x]+cur_notax[2][x]-cur_notax[3][x]
        cur_notax_final.append(result_curnotax)
        # 基本养老保险
        result_oldfee = old_fee[0][x]
        old_fee_final.append(result_oldfee)
        # 基本医疗保险
        result_healthfee = health_fee[0][x]+health_fee[1][x]
        health_fee_final.append(result_healthfee)
        # 失业保险费
        result_losejobfee = losejob_fee[0][x]
        losejob_fee_final.append(result_losejobfee)
        # 住房公积金
        result_housefee = house_fee[0][x]+house_fee[1][x]
        house_fee_final.append(result_housefee)
        # 企业年金
        result_yearfee = year_fee[0][x]
        year_fee_final.append(result_yearfee)
        # 累计补退税额
        result_taxfee = tax_fee[0][x]
        tax_fee_final.append(result_taxfee)
        # 起征点
        result_startpoint = start_point[0][x]
        start_point_final.append(result_startpoint)
        # 专项抵扣
        result_specialdiscount = special_discount[0][x]
        special_discount_final.append(result_specialdiscount)
        
    sheet_one = [name_final, card_id_final, cur_income_final, cur_notax_final, old_fee_final, health_fee_final, losejob_fee_final, house_fee_final, year_fee_final, tax_fee_final, start_point_final, special_discount_final]
    return sheet_one

    
def write_one():
    data = ready_data_one()
    length = len(data[0])
    num = judge_num() + 1
    # 写数据
    for x in range(length):
        # 姓名
        print('writing names')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='b{0}'.format(str(num+x)),text=data[0][x])
        # 身份证号
        print('writing card_id')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='d{0}'.format(str(num+x)),text=data[1][x])
        # 本期收入
        print('writing cur_income')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='e{0}'.format(str(num+x)),text=data[2][x])
        # 本期免税收入
        print('writing cur_notax')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='f{0}'.format(str(num+x)),text=data[3][x])
        # 基本养老保险
        print('writing old_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='g{0}'.format(str(num+x)),text=data[4][x])
        # 基本医疗保险
        print('writing health_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='h{0}'.format(str(num+x)),text=data[5][x])
        # 失业保险
        print('writing losejob_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='i{0}'.format(str(num+x)),text=data[6][x])
        # 住房公积金
        print('writing house_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='j{0}'.format(str(num+x)),text=data[7][x])
        # 企业年金
        print('writing year_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='p{0}'.format(str(num+x)),text=data[8][x])
        # 累计补退税额
        print('writing tax_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='w{0}'.format(str(num+x)),text=data[9][x])
        # 起征点
        print('writing year_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='x{0}'.format(str(num+x)),text=data[10][x])
        # 专项抵扣
        print('writing year_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='y{0}'.format(str(num+x)),text=data[11][x])



# --------------------------------------------------------------------------------------------------处理表格，在职6


# 获取在职6 数据
def get_data_two():
    # 在职 6
    name = ['b']
    card_id = ['e']
    cur_income = ['v', 'ak', 'ac', 'ad']
    cur_notax = ['t', 'n', 'am', 'ac']
    old_fee = ['x']
    health_fee = ['z', 'aa']
    losejob_fee = ['y']
    house_fee = ['w', 'af']
    year_fee = ['ab']
    tax_fee = ['ai']
    start_point = ['h']
    special_discount = ['i']
    
    current_income = [name, card_id, cur_income, cur_notax, old_fee, health_fee, losejob_fee, house_fee, year_fee, tax_fee, start_point, special_discount]
    print(current_income)
    # get all data
    name_data, card_id_data, cur_income_data, cur_notax_data, old_fee_data, health_fee_data, losejob_fee_data, house_fee_data, year_fee_data, tax_fee_data, start_point_data, special_discount_data = [],[],[],[],[],[],[],[],[],[],[],[]
    
    integrete_data = []
    for x in current_income:
        if x == name:
            for h in x:
                cell_eight = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（交流干部）6.xls',cell='{0}7'.format(h))
                cell_eight = cell_eight[:-3]
                name_data.append(cell_eight)
            integrete_data.append(name_data)
            
        if x == card_id:
            for i in x:
                cell_nine = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（交流干部）6.xls',cell='{0}7'.format(i))
                cell_nine = cell_nine[:-3]
                card_id_data.append(cell_nine)
            integrete_data.append(card_id_data)
            
            
        if x == cur_income:
            print('this is cur_income')
            for a in x:
                cell_one = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（交流干部）6.xls',cell='{0}7'.format(a))
                cell_one = cell_one[:-3]
                cur_income_data.append(cell_one)
            integrete_data.append(cur_income_data)
            
            
        if x == cur_notax:
            for b in x:
                cell_two = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（交流干部）6.xls',cell='{0}7'.format(b))
                cell_two = cell_two[:-3]
                cur_notax_data.append(cell_two)
            integrete_data.append(cur_notax_data)
                
        if x == old_fee:
            for c in x:
                cell_three = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（交流干部）6.xls',cell='{0}7'.format(c))
                cell_three = cell_three[:-3]
                old_fee_data.append(cell_three)
            integrete_data.append(old_fee_data)
                
        if x == health_fee:
            for d in x:
                cell_four = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（交流干部）6.xls',cell='{0}7'.format(d))
                cell_four = cell_four[:-3]
                health_fee_data.append(cell_four)
            integrete_data.append(health_fee_data)
                
        if x == losejob_fee:
            for e in x:
                cell_five = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（交流干部）6.xls',cell='{0}7'.format(e))
                cell_five = cell_five[:-3]
                losejob_fee_data.append(cell_five)
            integrete_data.append(losejob_fee_data)
        
        if x == house_fee:
            for f in x:
                cell_six = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（交流干部）6.xls',cell='{0}7'.format(f))
                cell_six = cell_six[:-3]
                house_fee_data.append(cell_six)
            integrete_data.append(house_fee_data)
                
        if x == year_fee:
            for g in x:
                cell_seven = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（交流干部）6.xls',cell='{0}7'.format(g))
                cell_seven = cell_seven[:-3]
                year_fee_data.append(cell_seven)
            integrete_data.append(year_fee_data)
        
        if x == tax_fee:
            for j in x:
                cell_ten = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（交流干部）6.xls',cell='{0}7'.format(j))
                cell_ten = cell_ten[:-3]
                tax_fee_data.append(cell_ten)
            integrete_data.append(tax_fee_data)
        
        if x == start_point:
            for k in x:
                cell_eleven = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（交流干部）6.xls',cell='{0}7'.format(k))
                cell_eleven = cell_eleven[:-3]
                start_point_data.append(cell_eleven)
            integrete_data.append(start_point_data)
        
        if x == special_discount:
            for l in x:
                cell_twelve = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（交流干部）6.xls',cell='{0}7'.format(l))
                cell_twelve = cell_twelve[:-3]
                special_discount_data.append(cell_twelve)
            integrete_data.append(special_discount_data)
    return integrete_data



def ready_data_two():
    # 在职 6，数据整理
    # name, card_id, cur_income, cur_notax, old_fee, health_fee, losejob_fee, house_fee, year_fee
    data = get_data_two()
    print(len(data)) 
    print('---------------------------------')
    name, card_id, cur_income, cur_notax, old_fee, health_fee, losejob_fee, house_fee, year_fee, tax_fee, start_point, special_discount = data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11]
    all_data = [name, card_id, cur_income, cur_notax, old_fee, health_fee, losejob_fee, house_fee, year_fee, tax_fee, start_point, special_discount]
    for x in all_data:
        for y in x:
            for z in range(len(y)):
                if y[z] == '':
                    y[z] = 0
                
    # 在职6数据准备
    data = all_data
    name_final, card_id_final, cur_income_final, cur_notax_final, old_fee_final, health_fee_final, losejob_fee_final, house_fee_final, year_fee_final, tax_fee_final, start_point_final, special_discount_final=[],[],[],[],[],[],[],[],[],[],[],[]
    print(len(tax_fee[0]), len(start_point[0]), len(special_discount[0]))
    for x in range(len(cur_income[0])):
        # 姓名
        result_name = name[0][x]
        name_final.append(result_name)
        # 身份证号
        result_cardid = card_id[0][x]
        card_id_final.append(result_cardid)
        # 本期收入
        result_curincome = cur_income[0][x]+cur_income[1][x]-cur_income[2][x]-cur_income[3][x]
        cur_income_final.append(result_curincome)
        # 本期免税收入
        result_curnotax = cur_notax[0][x]+cur_notax[1][x]+cur_notax[2][x]-cur_notax[3][x]
        cur_notax_final.append(result_curnotax)
        # 基本养老保险
        result_oldfee = old_fee[0][x]
        old_fee_final.append(result_oldfee)
        # 基本医疗保险
        result_healthfee = health_fee[0][x]+health_fee[1][x]
        health_fee_final.append(result_healthfee)
        # 失业保险费
        result_losejobfee = losejob_fee[0][x]
        losejob_fee_final.append(result_losejobfee)
        # 住房公积金
        result_housefee = house_fee[0][x]+house_fee[1][x]
        house_fee_final.append(result_housefee)
        # 企业年金
        result_yearfee = year_fee[0][x]
        year_fee_final.append(result_yearfee)
        # 累计补退税额
        result_taxfee = tax_fee[0][x]
        tax_fee_final.append(result_taxfee)
        # 起征点
        result_startpoint = start_point[0][x]
        start_point_final.append(result_startpoint)
        # 专项抵扣
        result_specialdiscount = special_discount[0][x]
        special_discount_final.append(result_specialdiscount)
        
    sheet_one = [name_final, card_id_final, cur_income_final, cur_notax_final, old_fee_final, health_fee_final, losejob_fee_final, house_fee_final, year_fee_final, tax_fee_final, start_point_final, special_discount_final]
    return sheet_one

    
def write_two():
    data = ready_data_one()
    length = len(data[0])
    num = judge_num() + 1
    # 写数据
    for x in range(length):
        # 姓名
        print('writing names')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='b{0}'.format(str(num+x)),text=data[0][x])
        # 身份证号
        print('writing card_id')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='d{0}'.format(str(num+x)),text=data[1][x])
        # 本期收入
        print('writing cur_income')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='e{0}'.format(str(num+x)),text=data[2][x])
        # 本期免税收入
        print('writing cur_notax')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='f{0}'.format(str(num+x)),text=data[3][x])
        # 基本养老保险
        print('writing old_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='g{0}'.format(str(num+x)),text=data[4][x])
        # 基本医疗保险
        print('writing health_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='h{0}'.format(str(num+x)),text=data[5][x])
        # 失业保险
        print('writing losejob_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='i{0}'.format(str(num+x)),text=data[6][x])
        # 住房公积金
        print('writing house_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='j{0}'.format(str(num+x)),text=data[7][x])
        # 企业年金
        print('writing year_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='p{0}'.format(str(num+x)),text=data[8][x])
        # 累计补退税额
        print('writing tax_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='w{0}'.format(str(num+x)),text=data[9][x])
        # 起征点
        print('writing year_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='x{0}'.format(str(num+x)),text=data[10][x])
        # 专项抵扣
        print('writing year_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='y{0}'.format(str(num+x)),text=data[11][x])



# --------------------------------------------------------------------------------------------------处理表格，莫斯科代表

# 获取莫斯科 数据
def get_data_three():
    # 莫斯科
    name = ['b']
    card_id = ['e']
    cur_income = ['s']
    cur_notax = ['l', 'x', 'aa']
    tax_fee = ['u']
    start_point = ['h']
    special_discount = ['i']
    
    current_income = [name, card_id, cur_income, cur_notax, tax_fee, start_point, special_discount]
    print(current_income)
    # get all data
    name_data, card_id_data, cur_income_data, cur_notax_data, tax_fee_data, start_point_data, special_discount_data = [],[],[],[],[],[],[]
    
    integrete_data = []
    for x in current_income:
        if x == name:
            for h in x:
                cell_eight = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/莫斯科代表处4.xls',cell='{0}7'.format(h))
                cell_eight = cell_eight[:-3]
                name_data.append(cell_eight)
            integrete_data.append(name_data)
            
        if x == card_id:
            for i in x:
                cell_nine = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/莫斯科代表处4.xls',cell='{0}7'.format(i))
                cell_nine = cell_nine[:-3]
                card_id_data.append(cell_nine)
            integrete_data.append(card_id_data)
            
            
        if x == cur_income:
            print('this is cur_income')
            for a in x:
                cell_one = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/莫斯科代表处4.xls',cell='{0}7'.format(a))
                cell_one = cell_one[:-3]
                cur_income_data.append(cell_one)
            integrete_data.append(cur_income_data)
            
            
        if x == cur_notax:
            for b in x:
                cell_two = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/莫斯科代表处4.xls',cell='{0}7'.format(b))
                cell_two = cell_two[:-3]
                cur_notax_data.append(cell_two)
            integrete_data.append(cur_notax_data)
                
        
        if x == tax_fee:
            for j in x:
                cell_ten = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/莫斯科代表处4.xls',cell='{0}7'.format(j))
                cell_ten = cell_ten[:-3]
                tax_fee_data.append(cell_ten)
            integrete_data.append(tax_fee_data)
        
        if x == start_point:
            for k in x:
                cell_eleven = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/莫斯科代表处4.xls',cell='{0}7'.format(k))
                cell_eleven = cell_eleven[:-3]
                start_point_data.append(cell_eleven)
            integrete_data.append(start_point_data)
        
        if x == special_discount:
            for l in x:
                cell_twelve = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/莫斯科代表处4.xls',cell='{0}7'.format(l))
                cell_twelve = cell_twelve[:-3]
                special_discount_data.append(cell_twelve)
            integrete_data.append(special_discount_data)
    return integrete_data



def ready_data_three():
    # 莫斯科，数据整理
    # name, card_id, cur_income, cur_notax,tax_fee, start_point, special_discount
    data = get_data_three()
    print(len(data)) 
    print('---------------------------------')
    name, card_id, cur_income, cur_notax, tax_fee, start_point, special_discount = data[0], data[1], data[2], data[3], data[4], data[5], data[6]
    all_data = [name, card_id, cur_income, cur_notax, tax_fee, start_point, special_discount]
    for x in all_data:
        for y in x:
            for z in range(len(y)):
                if y[z] == '':
                    y[z] = 0
                
    # 莫斯科数据准备
    data = all_data
    name_final, card_id_final, cur_income_final, cur_notax_final, tax_fee_final, start_point_final, special_discount_final=[],[],[],[],[],[],[]
    print(len(tax_fee[0]), len(start_point[0]), len(special_discount[0]))
    for x in range(len(cur_income[0])):
        # 姓名
        result_name = name[0][x]
        name_final.append(result_name)
        # 身份证号
        result_cardid = card_id[0][x]
        card_id_final.append(result_cardid)
        # 本期收入
        result_curincome = cur_income[0][x]
        cur_income_final.append(result_curincome)
        # 本期免税收入
        result_curnotax = cur_notax[0][x]+cur_notax[1][x]-cur_notax[2][x]
        cur_notax_final.append(result_curnotax)
        # 累计补退税额
        result_taxfee = tax_fee[0][x]
        tax_fee_final.append(result_taxfee)
        # 起征点
        result_startpoint = start_point[0][x]
        start_point_final.append(result_startpoint)
        # 专项抵扣
        result_specialdiscount = special_discount[0][x]
        special_discount_final.append(result_specialdiscount)
        
    sheet_one = [name_final, card_id_final, cur_income_final, cur_notax_final, tax_fee_final, start_point_final, special_discount_final]
    return sheet_one

    
def write_three():
    data = ready_data_three()
    length = len(data[0])
    num = judge_num() + 1
    # 写数据
    for x in range(length):
        # 姓名
        print('writing names')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='b{0}'.format(str(num+x)),text=data[0][x])
        # 身份证号
        print('writing card_id')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='d{0}'.format(str(num+x)),text=data[1][x])
        # 本期收入
        print('writing cur_income')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='e{0}'.format(str(num+x)),text=data[2][x])
        # 本期免税收入
        print('writing cur_notax')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='f{0}'.format(str(num+x)),text=data[3][x])
        # 累计补退税额
        print('writing tax_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='w{0}'.format(str(num+x)),text=data[4][x])
        # 起征点
        print('writing year_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='x{0}'.format(str(num+x)),text=data[5][x])
        # 专项抵扣
        print('writing year_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='y{0}'.format(str(num+x)),text=data[6][x])


# ------------------------------------------------------------------------------------------------------------处理表格，高管

# 高管 数据
def get_data_four():
    # 高管
    name = ['b']
    card_id = ['e']
    cur_income = ['m', 't']
    cur_notax = ['x']
    old_fee = ['o']
    health_fee = ['q', 'r']
    losejob_fee = ['p']
    house_fee = ['n']
    year_fee = ['s']
    tax_fee = ['u']
    start_point = ['h']
    special_discount = ['i']
    
    current_income = [name, card_id, cur_income, cur_notax, old_fee, health_fee, losejob_fee, house_fee, year_fee, tax_fee, start_point, special_discount]
    print(current_income)
    # get all data
    name_data, card_id_data, cur_income_data, cur_notax_data, old_fee_data, health_fee_data, losejob_fee_data, house_fee_data, year_fee_data, tax_fee_data, start_point_data, special_discount_data = [],[],[],[],[],[],[],[],[],[],[],[]
    
    integrete_data = []
    for x in current_income:
        if x == name:
            for h in x:
                cell_eight = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/高管1.xls',cell='{0}7'.format(h))
                cell_eight = cell_eight[:-3]
                name_data.append(cell_eight)
            integrete_data.append(name_data)
            
        if x == card_id:
            for i in x:
                cell_nine = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/高管1.xls',cell='{0}7'.format(i))
                cell_nine = cell_nine[:-3]
                card_id_data.append(cell_nine)
            integrete_data.append(card_id_data)
            
            
        if x == cur_income:
            print('this is cur_income')
            for a in x:
                cell_one = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/高管1.xls',cell='{0}7'.format(a))
                cell_one = cell_one[:-3]
                cur_income_data.append(cell_one)
            integrete_data.append(cur_income_data)
            
            
        if x == cur_notax:
            for b in x:
                cell_two = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/高管1.xls',cell='{0}7'.format(b))
                cell_two = cell_two[:-3]
                cur_notax_data.append(cell_two)
            integrete_data.append(cur_notax_data)
                
        if x == old_fee:
            for c in x:
                cell_three = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/高管1.xls',cell='{0}7'.format(c))
                cell_three = cell_three[:-3]
                old_fee_data.append(cell_three)
            integrete_data.append(old_fee_data)
                
        if x == health_fee:
            for d in x:
                cell_four = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/高管1.xls',cell='{0}7'.format(d))
                cell_four = cell_four[:-3]
                health_fee_data.append(cell_four)
            integrete_data.append(health_fee_data)
                
        if x == losejob_fee:
            for e in x:
                cell_five = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/高管1.xls',cell='{0}7'.format(e))
                cell_five = cell_five[:-3]
                losejob_fee_data.append(cell_five)
            integrete_data.append(losejob_fee_data)
        
        if x == house_fee:
            for f in x:
                cell_six = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/高管1.xls',cell='{0}7'.format(f))
                cell_six = cell_six[:-3]
                house_fee_data.append(cell_six)
            integrete_data.append(house_fee_data)
                
        if x == year_fee:
            for g in x:
                cell_seven = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/高管1.xls',cell='{0}7'.format(g))
                cell_seven = cell_seven[:-3]
                year_fee_data.append(cell_seven)
            integrete_data.append(year_fee_data)
        
        if x == tax_fee:
            for j in x:
                cell_ten = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/高管1.xls',cell='{0}7'.format(j))
                cell_ten = cell_ten[:-3]
                tax_fee_data.append(cell_ten)
            integrete_data.append(tax_fee_data)
        
        if x == start_point:
            for k in x:
                cell_eleven = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/高管1.xls',cell='{0}7'.format(k))
                cell_eleven = cell_eleven[:-3]
                start_point_data.append(cell_eleven)
            integrete_data.append(start_point_data)
        
        if x == special_discount:
            for l in x:
                cell_twelve = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/高管1.xls',cell='{0}7'.format(l))
                cell_twelve = cell_twelve[:-3]
                special_discount_data.append(cell_twelve)
            integrete_data.append(special_discount_data)
    return integrete_data



def ready_data_four():
    # 高管，数据整理
    # name, card_id, cur_income, cur_notax, old_fee, health_fee, losejob_fee, house_fee, year_fee
    data = get_data_four()
    print(len(data)) 
    print('---------------------------------')
    name, card_id, cur_income, cur_notax, old_fee, health_fee, losejob_fee, house_fee, year_fee, tax_fee, start_point, special_discount = data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11]
    all_data = [name, card_id, cur_income, cur_notax, old_fee, health_fee, losejob_fee, house_fee, year_fee, tax_fee, start_point, special_discount]
    for x in all_data:
        for y in x:
            for z in range(len(y)):
                if y[z] == '':
                    y[z] = 0
                
    # 高管数据准备
    data = all_data
    name_final, card_id_final, cur_income_final, cur_notax_final, old_fee_final, health_fee_final, losejob_fee_final, house_fee_final, year_fee_final, tax_fee_final, start_point_final, special_discount_final=[],[],[],[],[],[],[],[],[],[],[],[]
    print(len(tax_fee[0]), len(start_point[0]), len(special_discount[0]))
    for x in range(len(cur_income[0])):
        # 姓名
        result_name = name[0][x]
        name_final.append(result_name)
        # 身份证号
        result_cardid = card_id[0][x]
        card_id_final.append(result_cardid)
        # 本期收入
        result_curincome = cur_income[0][x]-cur_income[1][x]
        cur_income_final.append(result_curincome)
        # 本期免税收入
        result_curnotax = cur_notax[0][x]
        cur_notax_final.append(result_curnotax)
        # 基本养老保险
        result_oldfee = old_fee[0][x]
        old_fee_final.append(result_oldfee)
        # 基本医疗保险
        result_healthfee = health_fee[0][x]+health_fee[1][x]
        health_fee_final.append(result_healthfee)
        # 失业保险费
        result_losejobfee = losejob_fee[0][x]
        losejob_fee_final.append(result_losejobfee)
        # 住房公积金
        result_housefee = house_fee[0][x]
        house_fee_final.append(result_housefee)
        # 企业年金
        result_yearfee = year_fee[0][x]
        year_fee_final.append(result_yearfee)
        # 累计补退税额
        result_taxfee = tax_fee[0][x]
        tax_fee_final.append(result_taxfee)
        # 起征点
        result_startpoint = start_point[0][x]
        start_point_final.append(result_startpoint)
        # 专项抵扣
        result_specialdiscount = special_discount[0][x]
        special_discount_final.append(result_specialdiscount)
        
    sheet_one = [name_final, card_id_final, cur_income_final, cur_notax_final, old_fee_final, health_fee_final, losejob_fee_final, house_fee_final, year_fee_final, tax_fee_final, start_point_final, special_discount_final]
    return sheet_one

    
def write_four():
    data = ready_data_four()
    length = len(data[0])
    num = judge_num() + 1
    # 写数据
    for x in range(length):
        # 姓名
        print('writing names')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='b{0}'.format(str(num+x)),text=data[0][x])
        # 身份证号
        print('writing card_id')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='d{0}'.format(str(num+x)),text=data[1][x])
        # 本期收入
        print('writing cur_income')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='e{0}'.format(str(num+x)),text=data[2][x])
        # 本期免税收入
        print('writing cur_notax')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='f{0}'.format(str(num+x)),text=data[3][x])
        # 基本养老保险
        print('writing old_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='g{0}'.format(str(num+x)),text=data[4][x])
        # 基本医疗保险
        print('writing health_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='h{0}'.format(str(num+x)),text=data[5][x])
        # 失业保险
        print('writing losejob_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='i{0}'.format(str(num+x)),text=data[6][x])
        # 住房公积金
        print('writing house_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='j{0}'.format(str(num+x)),text=data[7][x])
        # 企业年金
        print('writing year_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='p{0}'.format(str(num+x)),text=data[8][x])
        # 累计补退税额
        print('writing tax_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='w{0}'.format(str(num+x)),text=data[9][x])
        # 起征点
        print('writing year_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='x{0}'.format(str(num+x)),text=data[10][x])
        # 专项抵扣
        print('writing year_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='y{0}'.format(str(num+x)),text=data[11][x])


# ----------------------------------------------------------------------------------------------------------处理表格，内退
    
# 内退 数据
def get_data_five():
    # 内退
    name = ['b']
    card_id = ['e']
    cur_income = ['p']
    cur_notax = ['l', 'aa']
    tax_fee = ['w']
    start_point = ['h']
    special_discount = ['i']
    
    current_income = [name, card_id, cur_income, cur_notax, tax_fee, start_point, special_discount]
    print(current_income)
    # get all data
    name_data, card_id_data, cur_income_data, cur_notax_data, tax_fee_data, start_point_data, special_discount_data = [],[],[],[],[],[],[]
    
    integrete_data = []
    for x in current_income:
        if x == name:
            for h in x:
                cell_eight = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/内退3.xls',cell='{0}7'.format(h))
                cell_eight = cell_eight[:-3]
                name_data.append(cell_eight)
            integrete_data.append(name_data)
            
        if x == card_id:
            for i in x:
                cell_nine = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/内退3.xls',cell='{0}7'.format(i))
                cell_nine = cell_nine[:-3]
                card_id_data.append(cell_nine)
            integrete_data.append(card_id_data)
            
            
        if x == cur_income:
            print('this is cur_income')
            for a in x:
                cell_one = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/内退3.xls',cell='{0}7'.format(a))
                cell_one = cell_one[:-3]
                cur_income_data.append(cell_one)
            integrete_data.append(cur_income_data)
            
            
        if x == cur_notax:
            for b in x:
                cell_two = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/内退3.xls',cell='{0}7'.format(b))
                cell_two = cell_two[:-3]
                cur_notax_data.append(cell_two)
            integrete_data.append(cur_notax_data)
                
        
        if x == tax_fee:
            for j in x:
                cell_ten = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/内退3.xls',cell='{0}7'.format(j))
                cell_ten = cell_ten[:-3]
                tax_fee_data.append(cell_ten)
            integrete_data.append(tax_fee_data)
        
        if x == start_point:
            for k in x:
                cell_eleven = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/内退3.xls',cell='{0}7'.format(k))
                cell_eleven = cell_eleven[:-3]
                start_point_data.append(cell_eleven)
            integrete_data.append(start_point_data)
        
        if x == special_discount:
            for l in x:
                cell_twelve = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/内退3.xls',cell='{0}7'.format(l))
                cell_twelve = cell_twelve[:-3]
                special_discount_data.append(cell_twelve)
            integrete_data.append(special_discount_data)
    return integrete_data



def ready_data_five():
    # 内退，数据整理
    # name, card_id, cur_income, cur_notax,tax_fee, start_point, special_discount
    data = get_data_five()
    print(len(data)) 
    print('---------------------------------')
    name, card_id, cur_income, cur_notax, tax_fee, start_point, special_discount = data[0], data[1], data[2], data[3], data[4], data[5], data[6]
    all_data = [name, card_id, cur_income, cur_notax, tax_fee, start_point, special_discount]
    for x in all_data:
        for y in x:
            for z in range(len(y)):
                if y[z] == '':
                    y[z] = 0
                
    # 内退数据准备
    data = all_data
    name_final, card_id_final, cur_income_final, cur_notax_final, tax_fee_final, start_point_final, special_discount_final=[],[],[],[],[],[],[]
    print(len(tax_fee[0]), len(start_point[0]), len(special_discount[0]))
    for x in range(len(cur_income[0])):
        # 姓名
        result_name = name[0][x]
        name_final.append(result_name)
        # 身份证号
        result_cardid = card_id[0][x]
        card_id_final.append(result_cardid)
        # 本期收入
        result_curincome = cur_income[0][x]
        cur_income_final.append(result_curincome)
        # 本期免税收入
        result_curnotax = cur_notax[0][x]-cur_notax[1][x]
        cur_notax_final.append(result_curnotax)
        # 累计补退税额
        result_taxfee = tax_fee[0][x]
        tax_fee_final.append(result_taxfee)
        # 起征点
        result_startpoint = start_point[0][x]
        start_point_final.append(result_startpoint)
        # 专项抵扣
        result_specialdiscount = special_discount[0][x]
        special_discount_final.append(result_specialdiscount)
        
    sheet_one = [name_final, card_id_final, cur_income_final, cur_notax_final, tax_fee_final, start_point_final, special_discount_final]
    return sheet_one

    
def write_five():
    data = ready_data_five()
    length = len(data[0])
    num = judge_num() + 1
    # 写数据
    for x in range(length):
        # 姓名
        print('writing names')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='b{0}'.format(str(num+x)),text=data[0][x])
        # 身份证号
        print('writing card_id')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='d{0}'.format(str(num+x)),text=data[1][x])
        # 本期收入
        print('writing cur_income')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='e{0}'.format(str(num+x)),text=data[2][x])
        # 本期免税收入
        print('writing cur_notax')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='f{0}'.format(str(num+x)),text=data[3][x])
        # 累计补退税额
        print('writing tax_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='w{0}'.format(str(num+x)),text=data[4][x])
        # 起征点
        print('writing year_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='x{0}'.format(str(num+x)),text=data[5][x])
        # 专项抵扣
        print('writing year_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='y{0}'.format(str(num+x)),text=data[6][x])


# ----------------------------------------------------------------------------------------------------------处理表格，离退休
    
# 离退休 数据
def get_data_six():
    # 离退休
    name = ['b']
    card_id = ['e']
    cur_income = ['r']
    cur_notax = ['o', 'ab']
    tax_fee = ['af']
    start_point = ['h']
    special_discount = ['i']
    
    current_income = [name, card_id, cur_income, cur_notax, tax_fee, start_point, special_discount]
    print(current_income)
    # get all data
    name_data, card_id_data, cur_income_data, cur_notax_data, tax_fee_data, start_point_data, special_discount_data = [],[],[],[],[],[],[]
    
    integrete_data = []
    for x in current_income:
        if x == name:
            for h in x:
                cell_eight = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/离退休5.xls',cell='{0}7'.format(h))
                cell_eight = cell_eight[:-3]
                name_data.append(cell_eight)
            integrete_data.append(name_data)
            
        if x == card_id:
            for i in x:
                cell_nine = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/离退休5.xls',cell='{0}7'.format(i))
                cell_nine = cell_nine[:-3]
                card_id_data.append(cell_nine)
            integrete_data.append(card_id_data)
            
            
        if x == cur_income:
            print('this is cur_income')
            for a in x:
                cell_one = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/离退休5.xls',cell='{0}7'.format(a))
                cell_one = cell_one[:-3]
                cur_income_data.append(cell_one)
            integrete_data.append(cur_income_data)
            
            
        if x == cur_notax:
            for b in x:
                cell_two = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/离退休5.xls',cell='{0}7'.format(b))
                cell_two = cell_two[:-3]
                cur_notax_data.append(cell_two)
            integrete_data.append(cur_notax_data)
                
        
        if x == tax_fee:
            for j in x:
                cell_ten = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/离退休5.xls',cell='{0}7'.format(j))
                cell_ten = cell_ten[:-3]
                tax_fee_data.append(cell_ten)
            integrete_data.append(tax_fee_data)
        
        if x == start_point:
            for k in x:
                cell_eleven = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/离退休5.xls',cell='{0}7'.format(k))
                cell_eleven = cell_eleven[:-3]
                start_point_data.append(cell_eleven)
            integrete_data.append(start_point_data)
        
        if x == special_discount:
            for l in x:
                cell_twelve = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/离退休5.xls',cell='{0}7'.format(l))
                cell_twelve = cell_twelve[:-3]
                special_discount_data.append(cell_twelve)
            integrete_data.append(special_discount_data)
    return integrete_data



def ready_data_six():
    # 离退休，数据整理
    # name, card_id, cur_income, cur_notax,tax_fee, start_point, special_discount
    data = get_data_six()
    print(len(data)) 
    print('---------------------------------')
    name, card_id, cur_income, cur_notax, tax_fee, start_point, special_discount = data[0], data[1], data[2], data[3], data[4], data[5], data[6]
    all_data = [name, card_id, cur_income, cur_notax, tax_fee, start_point, special_discount]
    for x in all_data:
        for y in x:
            for z in range(len(y)):
                if y[z] == '':
                    y[z] = 0
                
    # 离退休数据准备
    data = all_data
    name_final, card_id_final, cur_income_final, cur_notax_final, tax_fee_final, start_point_final, special_discount_final=[],[],[],[],[],[],[]
    print(len(tax_fee[0]), len(start_point[0]), len(special_discount[0]))
    for x in range(len(cur_income[0])):
        # 姓名
        result_name = name[0][x]
        name_final.append(result_name)
        # 身份证号
        result_cardid = card_id[0][x]
        card_id_final.append(result_cardid)
        # 本期收入
        result_curincome = cur_income[0][x]
        cur_income_final.append(result_curincome)
        # 本期免税收入
        result_curnotax = cur_notax[0][x]-cur_notax[1][x]
        cur_notax_final.append(result_curnotax)
        # 累计补退税额
        result_taxfee = tax_fee[0][x]
        tax_fee_final.append(result_taxfee)
        # 起征点
        result_startpoint = start_point[0][x]
        start_point_final.append(result_startpoint)
        # 专项抵扣
        result_specialdiscount = special_discount[0][x]
        special_discount_final.append(result_specialdiscount)
        
    sheet_one = [name_final, card_id_final, cur_income_final, cur_notax_final, tax_fee_final, start_point_final, special_discount_final]
    return sheet_one

    
def write_six():
    data = ready_data_six()
    length = len(data[0])
    num = judge_num() + 1
    # 写数据
    for x in range(length):
        # 姓名
        print('writing names')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='b{0}'.format(str(num+x)),text=data[0][x])
        # 身份证号
        print('writing card_id')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='d{0}'.format(str(num+x)),text=data[1][x])
        # 本期收入
        print('writing cur_income')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='e{0}'.format(str(num+x)),text=data[2][x])
        # 本期免税收入
        print('writing cur_notax')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='f{0}'.format(str(num+x)),text=data[3][x])
        # 累计补退税额
        print('writing tax_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='w{0}'.format(str(num+x)),text=data[4][x])
        # 起征点
        print('writing year_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='x{0}'.format(str(num+x)),text=data[5][x])
        # 专项抵扣
        print('writing year_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='y{0}'.format(str(num+x)),text=data[6][x])


# ------------------------------------------------------------------------------------------------------------------------董秘，首席，总监


# 董秘，首席，总监 数据
def get_data_seven():
    # 董秘，首席，总监
    name = ['b']
    card_id = ['e']
    cur_income = ['r']
    cur_notax = ['l', 'aa']
    old_fee = ['t']
    health_fee = ['v', 'w']
    losejob_fee = ['u']
    house_fee = ['s']
    year_fee = ['x']
    tax_fee = ['y']
    start_point = ['h']
    special_discount = ['i']
    
    current_income = [name, card_id, cur_income, cur_notax, old_fee, health_fee, losejob_fee, house_fee, year_fee, tax_fee, start_point, special_discount]
    print(current_income)
    # get all data
    name_data, card_id_data, cur_income_data, cur_notax_data, old_fee_data, health_fee_data, losejob_fee_data, house_fee_data, year_fee_data, tax_fee_data, start_point_data, special_discount_data = [],[],[],[],[],[],[],[],[],[],[],[]
    
    integrete_data = []
    for x in current_income:
        if x == name:
            for h in x:
                cell_eight = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/董秘、总监、首席2.xls',cell='{0}7'.format(h))
                cell_eight = cell_eight[:-3]
                name_data.append(cell_eight)
            integrete_data.append(name_data)
            
        if x == card_id:
            for i in x:
                cell_nine = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/董秘、总监、首席2.xls',cell='{0}7'.format(i))
                cell_nine = cell_nine[:-3]
                card_id_data.append(cell_nine)
            integrete_data.append(card_id_data)
            
            
        if x == cur_income:
            print('this is cur_income')
            for a in x:
                cell_one = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/董秘、总监、首席2.xls',cell='{0}7'.format(a))
                cell_one = cell_one[:-3]
                cur_income_data.append(cell_one)
            integrete_data.append(cur_income_data)
            
            
        if x == cur_notax:
            for b in x:
                cell_two = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/董秘、总监、首席2.xls',cell='{0}7'.format(b))
                cell_two = cell_two[:-3]
                cur_notax_data.append(cell_two)
            integrete_data.append(cur_notax_data)
                
        if x == old_fee:
            for c in x:
                cell_three = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/董秘、总监、首席2.xls',cell='{0}7'.format(c))
                cell_three = cell_three[:-3]
                old_fee_data.append(cell_three)
            integrete_data.append(old_fee_data)
                
        if x == health_fee:
            for d in x:
                cell_four = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/董秘、总监、首席2.xls',cell='{0}7'.format(d))
                cell_four = cell_four[:-3]
                health_fee_data.append(cell_four)
            integrete_data.append(health_fee_data)
                
        if x == losejob_fee:
            for e in x:
                cell_five = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/董秘、总监、首席2.xls',cell='{0}7'.format(e))
                cell_five = cell_five[:-3]
                losejob_fee_data.append(cell_five)
            integrete_data.append(losejob_fee_data)
        
        if x == house_fee:
            for f in x:
                cell_six = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/董秘、总监、首席2.xls',cell='{0}7'.format(f))
                cell_six = cell_six[:-3]
                house_fee_data.append(cell_six)
            integrete_data.append(house_fee_data)
                
        if x == year_fee:
            for g in x:
                cell_seven = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/董秘、总监、首席2.xls',cell='{0}7'.format(g))
                cell_seven = cell_seven[:-3]
                year_fee_data.append(cell_seven)
            integrete_data.append(year_fee_data)
        
        if x == tax_fee:
            for j in x:
                cell_ten = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/董秘、总监、首席2.xls',cell='{0}7'.format(j))
                cell_ten = cell_ten[:-3]
                tax_fee_data.append(cell_ten)
            integrete_data.append(tax_fee_data)
        
        if x == start_point:
            for k in x:
                cell_eleven = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/董秘、总监、首席2.xls',cell='{0}7'.format(k))
                cell_eleven = cell_eleven[:-3]
                start_point_data.append(cell_eleven)
            integrete_data.append(start_point_data)
        
        if x == special_discount:
            for l in x:
                cell_twelve = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/董秘、总监、首席2.xls',cell='{0}7'.format(l))
                cell_twelve = cell_twelve[:-3]
                special_discount_data.append(cell_twelve)
            integrete_data.append(special_discount_data)
    return integrete_data



def ready_data_seven():
    # 董秘，首席，总监，数据整理
    # name, card_id, cur_income, cur_notax, old_fee, health_fee, losejob_fee, house_fee, year_fee
    data = get_data_seven()
    print(len(data)) 
    print('---------------------------------')
    name, card_id, cur_income, cur_notax, old_fee, health_fee, losejob_fee, house_fee, year_fee, tax_fee, start_point, special_discount = data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11]
    all_data = [name, card_id, cur_income, cur_notax, old_fee, health_fee, losejob_fee, house_fee, year_fee, tax_fee, start_point, special_discount]
    for x in all_data:
        for y in x:
            for z in range(len(y)):
                if y[z] == '':
                    y[z] = 0
                
    # 董秘，首席，总监,数据准备
    data = all_data
    name_final, card_id_final, cur_income_final, cur_notax_final, old_fee_final, health_fee_final, losejob_fee_final, house_fee_final, year_fee_final, tax_fee_final, start_point_final, special_discount_final=[],[],[],[],[],[],[],[],[],[],[],[]
    print(len(tax_fee[0]), len(start_point[0]), len(special_discount[0]))
    for x in range(len(cur_income[0])):
        # 姓名
        result_name = name[0][x]
        name_final.append(result_name)
        # 身份证号
        result_cardid = card_id[0][x]
        card_id_final.append(result_cardid)
        # 本期收入
        result_curincome = cur_income[0][x]
        cur_income_final.append(result_curincome)
        # 本期免税收入
        result_curnotax = cur_notax[0][x]+cur_notax[1][x]
        cur_notax_final.append(result_curnotax)
        # 基本养老保险
        result_oldfee = old_fee[0][x]
        old_fee_final.append(result_oldfee)
        # 基本医疗保险
        result_healthfee = health_fee[0][x]+health_fee[1][x]
        health_fee_final.append(result_healthfee)
        # 失业保险费
        result_losejobfee = losejob_fee[0][x]
        losejob_fee_final.append(result_losejobfee)
        # 住房公积金
        result_housefee = house_fee[0][x]
        house_fee_final.append(result_housefee)
        # 企业年金
        result_yearfee = year_fee[0][x]
        year_fee_final.append(result_yearfee)
        # 累计补退税额
        result_taxfee = tax_fee[0][x]
        tax_fee_final.append(result_taxfee)
        # 起征点
        result_startpoint = start_point[0][x]
        start_point_final.append(result_startpoint)
        # 专项抵扣
        result_specialdiscount = special_discount[0][x]
        special_discount_final.append(result_specialdiscount)
        
    sheet_one = [name_final, card_id_final, cur_income_final, cur_notax_final, old_fee_final, health_fee_final, losejob_fee_final, house_fee_final, year_fee_final, tax_fee_final, start_point_final, special_discount_final]
    return sheet_one

    
def write_seven():
    data = ready_data_seven()
    length = len(data[0])
    num = judge_num() + 1
    # 写数据
    for x in range(length):
        # 姓名
        print('writing names')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='b{0}'.format(str(num+x)),text=data[0][x])
        # 身份证号
        print('writing card_id')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='d{0}'.format(str(num+x)),text=data[1][x])
        # 本期收入
        print('writing cur_income')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='e{0}'.format(str(num+x)),text=data[2][x])
        # 本期免税收入
        print('writing cur_notax')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='f{0}'.format(str(num+x)),text=data[3][x])
        # 基本养老保险
        print('writing old_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='g{0}'.format(str(num+x)),text=data[4][x])
        # 基本医疗保险
        print('writing health_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='h{0}'.format(str(num+x)),text=data[5][x])
        # 失业保险
        print('writing losejob_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='i{0}'.format(str(num+x)),text=data[6][x])
        # 住房公积金
        print('writing house_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='j{0}'.format(str(num+x)),text=data[7][x])
        # 企业年金
        print('writing year_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='p{0}'.format(str(num+x)),text=data[8][x])
        # 累计补退税额
        print('writing tax_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='w{0}'.format(str(num+x)),text=data[9][x])
        # 起征点
        print('writing year_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='x{0}'.format(str(num+x)),text=data[10][x])
        # 专项抵扣
        print('writing year_fee')
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='y{0}'.format(str(num+x)),text=data[11][x])



# ------------------------------------------------------------------------------------------------------------------------- 补发内容


# 4月补发 数据
def get_data_eight():
    # 4月补发
    name = ['b']
    card_id = ['e']
    cur_income = ['w']
    cur_notax = ['t', 'o', 'an']
    tax_fee = ['aj']
    start_point = ['h']
    special_discount = ['i']
    
    current_income = [name, card_id, cur_income, cur_notax, tax_fee, start_point, special_discount]
    print(current_income)
    # get all data
    name_data, card_id_data, cur_income_data, cur_notax_data, tax_fee_data, start_point_data, special_discount_data = [],[],[],[],[],[],[]
    
    integrete_data = []
    for x in current_income:
        if x == name:
            for h in x:
                cell_eight = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/4月补发（定）.xls',cell='{0}7'.format(h))
                cell_eight = cell_eight[:-3]
                name_data.append(cell_eight)
            integrete_data.append(name_data)
            
        if x == card_id:
            for i in x:
                cell_nine = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/4月补发（定）.xls',cell='{0}7'.format(i))
                cell_nine = cell_nine[:-3]
                card_id_data.append(cell_nine)
            integrete_data.append(card_id_data)
            
            
        if x == cur_income:
            print('this is cur_income')
            for a in x:
                cell_one = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/4月补发（定）.xls',cell='{0}7'.format(a))
                cell_one = cell_one[:-3]
                cur_income_data.append(cell_one)
            integrete_data.append(cur_income_data)
            
            
        if x == cur_notax:
            for b in x:
                cell_two = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/4月补发（定）.xls',cell='{0}7'.format(b))
                cell_two = cell_two[:-3]
                cur_notax_data.append(cell_two)
            integrete_data.append(cur_notax_data)
                
        
        if x == tax_fee:
            for j in x:
                cell_ten = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/4月补发（定）.xls',cell='{0}7'.format(j))
                cell_ten = cell_ten[:-3]
                tax_fee_data.append(cell_ten)
            integrete_data.append(tax_fee_data)
        
        if x == start_point:
            for k in x:
                cell_eleven = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/4月补发（定）.xls',cell='{0}7'.format(k))
                cell_eleven = cell_eleven[:-3]
                start_point_data.append(cell_eleven)
            integrete_data.append(start_point_data)
        
        if x == special_discount:
            for l in x:
                cell_twelve = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/4月补发（定）.xls',cell='{0}7'.format(l))
                cell_twelve = cell_twelve[:-3]
                special_discount_data.append(cell_twelve)
            integrete_data.append(special_discount_data)
    return integrete_data



def ready_data_eight():
    # 4月补发，数据整理
    # name, card_id, cur_income, cur_notax,tax_fee, start_point, special_discount
    data = get_data_eight()
    print(len(data)) 
    print('---------------------------------')
    name, card_id, cur_income, cur_notax, tax_fee, start_point, special_discount = data[0], data[1], data[2], data[3], data[4], data[5], data[6]
    all_data = [name, card_id, cur_income, cur_notax, tax_fee, start_point, special_discount]
    for x in all_data:
        for y in x:
            for z in range(len(y)):
                if y[z] == '':
                    y[z] = 0
                
    # 4月补发数据准备
    data = all_data
    name_final, card_id_final, cur_income_final, cur_notax_final, tax_fee_final, start_point_final, special_discount_final=[],[],[],[],[],[],[]
    print(len(tax_fee[0]), len(start_point[0]), len(special_discount[0]))
    for x in range(len(cur_income[0])):
        # 姓名
        result_name = name[0][x]
        name_final.append(result_name)
        # 身份证号
        result_cardid = card_id[0][x]
        card_id_final.append(result_cardid)
        # 本期收入
        result_curincome = cur_income[0][x]
        cur_income_final.append(result_curincome)
        # 本期免税收入
        result_curnotax = cur_notax[0][x]+cur_notax[1][x]+cur_notax[2][x]
        cur_notax_final.append(result_curnotax)
        # 累计补退税额
        result_taxfee = tax_fee[0][x]
        tax_fee_final.append(result_taxfee)
        # 起征点
        result_startpoint = start_point[0][x]
        start_point_final.append(result_startpoint)
        # 专项抵扣
        result_specialdiscount = special_discount[0][x]
        special_discount_final.append(result_specialdiscount)
        
    sheet_one = [name_final, card_id_final, cur_income_final, cur_notax_final, tax_fee_final, start_point_final, special_discount_final]
    return sheet_one


def write_addition():
    data = ready_data_eight()
    print(data)
    
    position = []
    a = 0
    aim_id = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='d2')
    for x in range(len(data[1])):
        for y in range(len(aim_id)):
            if data[1][x] == aim_id[y]:
                print(x , y)
                position.append(y)
    print(position)
    
    # write cur_income
    source_data_one, source_data_two, source_data_three = [],[],[]
    for x in position:
        b = iexcel.read_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='e{0}'.format(x+2))
        source_data_one.append(b)
        c = iexcel.read_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='f{0}'.format(x+2))
        source_data_two.append(c)
        d = iexcel.read_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='x{0}'.format(x+2))
        source_data_three.append(d)
    
    print(len(source_data_one))
    
    pre_data_one, pre_data_two, pre_data_three = data[2], data[3], data[4]
    
    
    writing_data_one = list(map(lambda x,y:x+y, pre_data_one, source_data_one))
    writing_data_two = list(map(lambda x,y:x+y, pre_data_two, source_data_two))
    writing_data_three = list(map(lambda x,y:x+y, pre_data_three, source_data_three))

    
    count = 0
    for y in position:
        print("writing cur_income_data")
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='e{0}'.format(str(y+2)),text=writing_data_one[count])
        print("cur_notax_data")
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='f{0}'.format(str(y+2)),text=writing_data_two[count])
        print("tax_fee_data")
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='x{0}'.format(str(y+2)),text=writing_data_three[count])
        count += 1 
    
    
    
    
# -------------------------------------------------------------------------------------- 处理其他工资绩效差额


# 其他工资绩效差额 数据
def get_data_nine():
    #其他工资绩效差额
    name = ['b']
    card_id = ['e']
    cur_income = ['l']
    tax_fee = ['m']
    start_point = ['h']
    special_discount = ['i']
    
    current_income = [name, card_id, cur_income, tax_fee, start_point, special_discount]
    print(current_income)
    # get all data
    name_data, card_id_data, cur_income_data, tax_fee_data, start_point_data, special_discount_data = [],[],[],[],[],[]
    
    integrete_data = []
    for x in current_income:
        if x == name:
            for h in x:
                cell_eight = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（其他工资绩效奖金差额）8.xls',cell='{0}7'.format(h))
                cell_eight = cell_eight[:-3]
                name_data.append(cell_eight)
            integrete_data.append(name_data)
            
        if x == card_id:
            for i in x:
                cell_nine = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（其他工资绩效奖金差额）8.xls',cell='{0}7'.format(i))
                cell_nine = cell_nine[:-3]
                card_id_data.append(cell_nine)
            integrete_data.append(card_id_data)
            
            
        if x == cur_income:
            print('this is cur_income')
            for a in x:
                cell_one = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（其他工资绩效奖金差额）8.xls',cell='{0}7'.format(a))
                cell_one = cell_one[:-3]
                cur_income_data.append(cell_one)
            integrete_data.append(cur_income_data)
            
        
        if x == tax_fee:
            for j in x:
                cell_ten = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（其他工资绩效奖金差额）8.xls',cell='{0}7'.format(j))
                cell_ten = cell_ten[:-3]
                tax_fee_data.append(cell_ten)
            integrete_data.append(tax_fee_data)
        
        if x == start_point:
            for k in x:
                cell_eleven = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（其他工资绩效奖金差额）8.xls',cell='{0}7'.format(k))
                cell_eleven = cell_eleven[:-3]
                start_point_data.append(cell_eleven)
            integrete_data.append(start_point_data)
        
        if x == special_discount:
            for l in x:
                cell_twelve = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/4月个税/在职（其他工资绩效奖金差额）8.xls',cell='{0}7'.format(l))
                cell_twelve = cell_twelve[:-3]
                special_discount_data.append(cell_twelve)
            integrete_data.append(special_discount_data)
    return integrete_data



def ready_data_nine():
    # 其他工资绩效差额，数据整理
    # name, card_id, cur_income, cur_notax,tax_fee, start_point, special_discount
    data = get_data_nine()
    print(len(data)) 
    print('---------------------------------')
    name, card_id, cur_income, tax_fee, start_point, special_discount = data[0], data[1], data[2], data[3], data[4], data[5]
    all_data = [name, card_id, cur_income, tax_fee, start_point, special_discount]
    for x in all_data:
        for y in x:
            for z in range(len(y)):
                if y[z] == '':
                    y[z] = 0
                
    # 其他工资绩效差额数据准备
    data = all_data
    name_final, card_id_final, cur_income_final, tax_fee_final, start_point_final, special_discount_final=[],[],[],[],[],[]
    print(len(tax_fee[0]), len(start_point[0]), len(special_discount[0]))
    for x in range(len(cur_income[0])):
        # 姓名
        result_name = name[0][x]
        name_final.append(result_name)
        # 身份证号
        result_cardid = card_id[0][x]
        card_id_final.append(result_cardid)
        # 本期收入
        result_curincome = cur_income[0][x]
        cur_income_final.append(result_curincome)

        # 累计补退税额
        result_taxfee = tax_fee[0][x]
        tax_fee_final.append(result_taxfee)
        # 起征点
        result_startpoint = start_point[0][x]
        start_point_final.append(result_startpoint)
        # 专项抵扣
        result_specialdiscount = special_discount[0][x]
        special_discount_final.append(result_specialdiscount)
        
    sheet_one = [name_final, card_id_final, cur_income_final, tax_fee_final, start_point_final, special_discount_final]
    return sheet_one


def write_addition_two():
    data = ready_data_nine()
    
    position = []
    a = 0
    aim_id = iexcel.read_col(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='d2')
    for x in range(len(data[1])):
        for y in range(len(aim_id)):
            if data[1][x] == aim_id[y]:
                print(x , y)
                position.append(y)

    print(len(position))
    
    
    # write data
    source_data_one, source_data_two = [],[]
    for x in position:
        b = iexcel.read_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='e{0}'.format(x+2))
        source_data_one.append(b)
        c = iexcel.read_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='x{0}'.format(x+2))
        source_data_two.append(c)

    
    print(len(source_data_one))
    
    pre_data_one, pre_data_two = data[2], data[3]
    for x in pre_data_two:
        print(type(x))
        

    writing_data_one = list(map(lambda x,y:x+y, pre_data_one, source_data_one))
    writing_data_two = list(map(lambda x,y:x+y, pre_data_two, source_data_two))
   
    
    count = 0
    for y in position:
        print("writing cur_income_data")
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='e{0}'.format(str(y+2)),text=writing_data_one[count])
        print("cur_notax_data")
        iexcel.write_cell(path='C:/Users/Administrator/Desktop/4月个税/正常工资薪金所得模板.xls',cell='x{0}'.format(str(y+2)),text=writing_data_two[count])
        count += 1
    

'''

# --------------------------------------------------------------------------------------------- 表格信息对比

def compare():
    df_on = pd.read_excel("D:/个税申报/201904/差异统计/汇总表.xls")
    df_tw = pd.read_excel("D:/个税申报/201904/差异统计/201904_税款计算_工资薪金所得.xls")
    df_on = df_on.sort_values(by=["*证照号码"])
    df_tw = df_tw.sort_values(by=["证照号码"])
    df_on.to_excel("D:/个税申报/201904/差异统计/汇总表.xls")
    df_tw.to_excel("D:/个税申报/201904/差异统计/201904_税款计算_工资薪金所得.xls")

    df_on = pd.read_excel("D:/个税申报/201904/差异统计/汇总表.xls")
    df_tw = pd.read_excel("D:/个税申报/201904/差异统计/201904_税款计算_工资薪金所得.xls")

    df_three = pd.read_excel("D:/个税申报/201904/差异统计/201903_税款计算_工资薪金所得.xls")
    '''
    df_on = pd.read_excel("D:/个税申报/201904/差异统计/汇总表.xls")
    df_tw = pd.read_excel("D:/个税申报/201904/差异统计/201904_税款计算_工资薪金所得.xls")
    
    
    '''
    df = pd.DataFrame()
    df["姓名"] = df_tw["姓名"]
    df["身份证号"] = df_tw["证照号码"]
    df["税额差额"] = df_tw["累计应补(退)税额"] - df_on["累计应补(退)税额"]
    df["累计费用-申报金额"] = df_tw["累计减除费用"]
    df["累计费用-实扣金额"] = df_on["累计减除费用"]
    df["累计费用差额"] = df_tw["累计减除费用"] - df_on["累计减除费用"]
    df["累计专扣-申报金额"] = df_tw["累计子女教育支出扣除"]+df_tw["累计赡养老人支出扣除"]+df_tw["累计继续教育支出扣除"]+df_tw["累计住房贷款利息支出扣除"]+df_tw["累计住房租金支出扣除"]
    df["累计专扣-实扣金额"] = df_on["累计专项附加扣除"]
    df["累计专扣差额"] = df_tw["累计子女教育支出扣除"]+df_tw["累计赡养老人支出扣除"]+df_tw["累计继续教育支出扣除"]+df_tw["累计住房贷款利息支出扣除"]+df_tw["累计住房租金支出扣除"]- df_on["累计专项附加扣除"]
    df["子女教育N-1月"] = df_three["累计子女教育支出扣除"]
    df["子女教育N月"] = df_tw["累计子女教育支出扣除"]
    df["继续教育N-1月"] = df_three["累计继续教育支出扣除"]
    df["继续教育N月"] = df_tw["累计继续教育支出扣除"]
    df["住房租金N-1月"] = df_three["累计住房租金支出扣除"]
    df["住房租金N月"] = df_tw["累计住房租金支出扣除"]
    df["住房贷款N-1月"] = df_three["累计住房贷款利息支出扣除"]
    df["住房贷款N月"] = df_tw["累计住房贷款利息支出扣除"]
    df["赡养老人N-1月"] = df_three["累计赡养老人支出扣除"]
    df["赡养老人N月"] = df_tw["累计赡养老人支出扣除"]

    # 多条件筛选
    # outfile = df1[(df1[u'设计井别']=='11') & (df1[u'投产井别']=='11') &(df1[u'目前井别']=='11')]

    df = df.loc[(df['税额差额'] != 0) | (df['累计费用差额'] != 0) | (df['累计专扣差额'] != 0)]


    df.to_excel("D:/个税申报/201904/差异统计/差异统计表.xlsx")
    
def words():
    df = pd.read_excel("D:/个税申报/201904/差异统计/差异统计表.xlsx")
    data = df.iloc[0].values.tolist()
    print(data)
    detail = " {0}您好，根据本月个税申报结果，您本月申报税额与实际扣除税额存在{1}元差异。" \
             "起征点申报金额{2}元，实际扣除{3}元，差额{4}元；" \
             "专项附加扣除申报金额{5}元，实际扣除{6}元，差额{7}元。" \
             "请您尽快核实差异原因："\
            "1、起征点存在差异的请立刻联系“3990”告知实际入职时间，我们将代为修改；"\
            "2、专项附加扣除存在差异的："\
            "①如以申报金额为准，请在共享系统中修正（可能原因包括：需要填写补扣金额、专项附加扣除表格信息有误需要修改并重新上传、住房租金表格上传后未手动选择城市规模）；"\
            "②如以实际扣除金额为准，请立刻联系“3990”进行修改。"

    c = detail.format(data[0], data[2], data[3], data[4], data[5], data[6], data[7], data[8])
    print(c)
    return c
    

    
# ---------------------------------------------------------------------------------- deal with excels fastest version

path_addition = "D:/个税申报/201904/薪资明细/4月补发（定）.xls"                       # compare
path_offie = "D:/个税申报/201904/薪资明细/4月发放3月办公厅值班费（定）.xls"           # compare
path_vip = "D:/个税申报/201904/薪资明细/董秘、总监、首席2.xls"
path_ceo = "D:/个税申报/201904/薪资明细/高管1.xls"
path_retire = "D:/个税申报/201904/薪资明细/离退休5.xls"
path_mosco = "D:/个税申报/201904/薪资明细/莫斯科代表处4.xls"
path_quit = "D:/个税申报/201904/薪资明细/内退3.xls"
path_comofficer = "D:/个税申报/201904/薪资明细/在职（交流干部）6.xls"
path_salarydiff = "D:/个税申报/201904/薪资明细/在职（其他工资绩效奖金差额）8.xls"     # compare
path_onpositon = "D:/个税申报/201904/薪资明细/在职（终-删林森）7.xls"

path = "D:/个税申报/201904/final_result.xlsx"


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
    # df_final.to_excel(path)
    return df_final
    


# get result from two different sheets
def compare_result(df, path_b):
    df_a = df
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
    # df.to_excel("C:/Users/Administrator/Desktop/a.xlsx")
    return df
    
    

def get_result():
    df = write_result()
    df = compare_result(df, path_addition)
    df = compare_result(df, path_offie)
    df = compare_result(df, path_salarydiff)
    df.to_excel(path)
    

    
    
def delete_lines():
    path = "D:/个税申报/201904/薪资明细"
    for roots, dirs, files in os.walk(path):
        file = files
    print(file)

    for x in file:
        aim = path + "\\" + x
        df = pd.read_excel(aim)[3:]
        df.fillna(0)
        df.to_excel(aim, header=False, index=False)


def delete_file():
    path = "D:/个税申报/201904/薪资明细"
    for roots, dirs, files in os.walk(path):
        file = files
    print(file)
    try:
        os.remove("D:/个税申报/201904/个税申报.zip")
        for x in file:
            aim = path + "/" + x
            os.remove(aim)
    except Exception as e:
        print(e)
