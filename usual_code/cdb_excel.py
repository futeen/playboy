import pandas as pd


def deal_data():
    df = pd.read_excel("C:/Users/ThinkPad/Desktop/测试资料包-国开行/1、薪资发放明细表/在职1.xls")
    df2 = pd.read_excel("C:/Users/ThinkPad/Desktop/测试资料包-国开行/3、薪资发放明细表-合并.xls")
    num = df.pop("房租补").values.tolist()  # 拿出标题头的数据
    num2 = df.pop("专项附加扣除合计").values.tolist()
    data = map(lambda x, y: x + y, num, num2)
    data = pd.DataFrame(data)
    df2["本期免税收入"] = data
    df2.to_excel("C:/Users/ThinkPad/Desktopa.xlsx")

    # df.to_excel("C:/Users/ThinkPad/Desktop/a.xlsx")

    '''
    df.insert(0, 'hello', num, allow_duplicates=True)
    print(df)
    '''


if __name__ == "__main__":
    deal_data()

