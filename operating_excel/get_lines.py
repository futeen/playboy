
rt pandas as pd
from codes.cdb import integrete_data


def get_lines():
    id_list_nine = []
    id_list_result = []
    df_result = pd.read_excel("C:/Users/ThinkPad/Desktop/result.xlsx")
    df_nine = pd.read_excel("C:/Users/ThinkPad/Desktop/b.xls")
    id = df_nine["*证照号码"].values.tolist()
    print(id)
    for x in id:
        id_nine = df_nine.loc[df_nine["*证照号码"] == x].values.tolist()[0][5:]
        id_list_nine.append(id_nine)
        id_result = df_result.loc[df_result["*证照号码"] == "{0}".format(x)].values.tolist()[0][5:]
        id_list_result.append(id_result)
    a = []
    b = []
    for x in id_list_nine:
        x = x[:2] + x[-3:-2]
        a.append(x)
    for x in id_list_result:
        x = x[:2] + x[-3:-2]
        b.append(x)
    print(a)
    print(b)



if __name__ == "__main__":
    get_lines()

