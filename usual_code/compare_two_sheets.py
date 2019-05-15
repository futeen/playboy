# find differences in two excel sheets
def inclusion():
    df_one = pd.read_excel("C:/Users/ThinkPad/Desktop/a.xlsx")
    df_two = pd.read_excel("C:/Users/ThinkPad/Desktop/b.xlsx")
    one, two = df_one["a"].values.tolist(), df_two["a"].values.tolist()
    a = [x for x in one if x not in two]
    b = [x for x in two if x not in one]

    df = pd.DataFrame()
    if a != [] or b != []:
        df = df_one.append(df_two)
        '''
        keep : {‘first’, ‘last’, False}, default ‘first’
        first : Drop duplicates except for the first occurrence.
        last : Drop duplicates except for the last occurrence.
        False : Drop all duplicates.
        inplace : boolean, default False
        Whether to drop duplicates in place or to return a copy
        '''
        df.drop_duplicates(keep=False,inplace=True)
        df.reset_index()
    print(df)


if __name__ == "__main__":
    inclusion()
