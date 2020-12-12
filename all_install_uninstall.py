import os
import re
import time



package = "com.astrill.astrillvpn"
install_url = "F:/aa/AstrillVPN-3.10.25.apk"


def get_deviceid():
    str_init = ' '
    all_info = os.popen('adb devices').readlines()
    # print('adb devices 输出的内容是：',all_info)

    for i in range(len(all_info)):
        str_init += all_info[i]
    devices_name = re.findall('\n(.+?)\t', str_init, re.S)

    print('所有设备名称：\n', devices_name)
    return devices_name


def installapk(deviceslist):
    print("------开始安装")
    for i in range(len(deviceslist)):
        cmd_put1 = f"adb -s {deviceslist[i]} install -r -d -t {install_url}"
        os.system(cmd_put1)

    return "安装完成"


def uninstall(deviceslist):
    print("------开始卸载")
    for i in range(len(deviceslist)):
        cmd_put2 = f"adb -s {deviceslist[i]} uninstall {package}"
        os.system(cmd_put2)

    return "卸载完成"


def run():
    try:
        data = get_deviceid()
        print()
        if not data:
            pass
        else:
            uninfo = uninstall(data)
            if uninfo == "卸载完成":
                time.sleep(2)
                installapk(data)
    except Exception as e:
        print("异常", e)

    os.system("java -cp ./alphafish.jar ")


if __name__ == '__main__':
    run()
