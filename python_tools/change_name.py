mport os
import pprint

'''
path为文件的文件夹所在路径，
会提示输入已输出的文件路径，
会提示输入需要修改的文件的名称
'''


def change_name(path):
    a = 0
    folder = {}
    for dir, file, root in os.walk(path):
        for x in root:
            folder[str(a)] = x
            a += 1

    pprint.pprint(folder)
    num = input("Please enter the file num to change : \n")
    name = input("Please enter the file name to change : \n")
    os.rename(path + folder[str(num)], path + str(name))
    folder[str(num)] = name
    print("Name has changed.")
    print(folder)


if __name__ == "__main__":
    change_name(path="")

