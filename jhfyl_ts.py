# -*- coding:utf-8 -*-

#泰山地图刷经验的脚本

import time
import os
import sys
from aip import AipOcr
from urllib3.exceptions import MaxRetryError

reload(sys)
sys.setdefaultencoding('utf-8')


config = {
    'appId': '14825626',
    'apiKey': 'Z6dl0mYhGSFocDYwpLY6Xi0c',
    'secretKey': '3uP2HZxSaU9UetwzoXPOGT7NVDmIqGRx'
}

client = AipOcr(**config)

imagepath = "/Users/zf/jhfyl/sc.png"

def get_file_content(file):
    with open(file, 'rb') as fp:
        return fp.read()


def img_to_str(image_path):
    image = get_file_content(image_path)

    result = ''
    try:
        result = client.basicGeneral(image)

    except MaxRetryError as e:
        print('网络异常:'+ e)

    finally:
        if 'words_result' in result:
            return ' '.join([w['words'] for w in result['words_result']])
        else:
            return result


def screencap():
    command = 'adb exec-out screencap -p > /Users/zf/jhfyl/sc.png'
    os.system(command)
    time.sleep(1)

def moveDown():
    command = 'adb shell input tap 481 1320'
    os.system(command)
    time.sleep(0.5)

def moveUp():
    command = 'adb shell input tap 1031 682'
    os.system(command)
    time.sleep(0.5)

def isfight(words):
    if words is None:
        return False
    else:
        result = False
        try:
            result = words.find("江秋萍") >= 0
        except Exception as e:
            print("words 不是 string")
        finally:
            return result

def overfight(words):

    if words is None:

        return False
    else:
        result = False
        try:
            result = words.find("关闭") >= 0
        except Exception as e:
            print("words 不是 string")
        finally:
            return result


def touchfightover():
    command = 'adb shell input tap 560 1567'
    os.system(command)
    time.sleep(1)

def cleanpng():
    if os.path.exists(imagepath):
        os.remove(imagepath)


#泰山脚本
def autoJB():

    #1: 需要向上移动  2 需要向下移动
    flag = 1
    while True:
        cleanpng()

        if flag == 1:
            moveUp()
            moveUp()
            moveUp()
            moveUp()
            moveUp()

            moveUp()
            moveUp()
            moveUp()
            moveUp()
            moveUp()

            moveUp()

            flag = 2

        elif flag == 2:
             moveDown()
             moveDown()
             moveDown()
             moveDown()
             moveDown()

             moveDown()
             moveDown()
             moveDown()
             moveDown()
             moveDown()

             moveDown()

             flag = 1

        time.sleep(2.5)

        screencap()
        words = img_to_str(imagepath)
        print(type(words))
        print('1 \n')

        if isfight(words):
            time.sleep(10





                       )
            cleanpng()
            screencap()
            nwords = img_to_str(imagepath)
            print(type(nwords))
            print('2 \n')
            if overfight(nwords):
                touchfightover()
                time.sleep(3)
            continue

        if overfight(words):
            touchfightover()
            time.sleep(3)
            continue


if __name__ == '__main__':

    autoJB()