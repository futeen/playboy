import os

# netsh wlan show profiles
# name=Hello World key=clear


def wifi_test():
    wifi = ('netsh wlan show profiles ')
    with os.popen(wifi) as f:
        wifiname_list = []
        for line in f:
            if "所有用户配置文件 :" in line:
                line = line.strip()
                wifiname = line.split(':')[1].strip()
                wifiname_list.append(wifiname)
        # print(wifiname_list)

    result = []
    for i in wifiname_list:
        try:
            get = 'netsh wlan show profiles name="{}" key=clear'.format(i)
            # print(get)
            with os.popen(get, mode="r") as r:
                for line in r:
                    if "关键内容" in line:
                        code = line.strip()
                        code = line.split(":")[1].strip()
                        txt = "wifi_name: " + str(i) + "   code: " + str(code)
                        result.append(txt)
        except Exception as e:
            pass
    with open("file_path", "w") as f:
        for code in result:
            f.writelines(code+"\n")


if __name__ == "__main__":
    wifi_test()

