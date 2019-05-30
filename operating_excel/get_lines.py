def get_lines():
    id_list_nine = []
    id_list_result = []
    df_result = pd.read_excel("C:/Users/ThinkPad/Desktop/result.xlsx")
    df_nine = pd.read_excel("C:/Users/ThinkPad/Desktop/b.xls")
    id = df_nine["*证照号码"].values.tolist()
    print(id)
    for x in id:
        id_nine = df_nine.loc[df_nine["*证照号码"] == x]
        id_list_nine.append(id_nine)
        id_result = df_result.loc[df_result["*证照号码"] == "{0}".format(x)]
        id_list_result.append(id_result)
    print(b)
