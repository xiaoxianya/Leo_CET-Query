# -*- coding: utf-8 -*-

'''
0.2.1版本使用说明：
本脚本能且仅能在Python 3环境下运行
如果提示No modolued named 'requests'在CMD输入pip install requests即可解决
本代码版权归TJPU-Leo所有
禁止用于商业用途
'''

import requests
import random
import socket
import struct
import os

print ('本程序来自https://github.com/CNILeo/Leo_CET-Query')
print ('     版权归TJPU-Leo所有，严禁用于商业用途！      ')
print ('        如在使用本软件的过程中出现报错           ')
print ('            可加入QQ群362699550反馈              ')

HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Referer': 'http://www.chsi.com.cn/cet',
    'X-FORWARDED-FOR':'',
	'CLIENT-IP':''
}

param={
        'zkzh':'',
        'xm':''}

xxdm = 120040 #请自行修改学校代码
type = 1 #四级修改为1，六级修改为2
kc = 1 #考场默认从1开始，可以自行修改
zwh = 1 #座位号默认从1开始，可以自行修改
zwh_gd = 0 #确认座位号的请把0修改为1
zkzh = (((xxdm*1000 + 172)*10+ type)*1000 + kc) * 100 + zwh #切勿修改此处
param['zkzh']=zkzh
print (param['zkzh'])
param['xm']='天津工业大学' #单引号内修改为自己的姓名

while 1:
    IP = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    HEADERS['X-FORWARDED-FOR'] = IP
    HEADERS['CLIENT-IP'] = IP
    try:
        rsp = requests.get('http://www.chsi.com.cn/cet/query',params=param, headers=HEADERS)
    except requests.exceptions.ConnectionError:
        continue
    except requests.exceptions.HTTPError:
        continue
    if '写作和翻译' in rsp.text:
        print(param['zkzh'], '查询成功')
        break
    elif '验证码' in rsp.text:
        print('Error : 获取到验证码')
        continue
    else:
        print(param['zkzh'], '尝试失败')
        if zwh_gd:
            zkzh = zkzh + 100
        else:
            zkzh += 1
            temp = zkzh - 31
            if temp % 100 == 0:
                zkzh = zkzh + 70
        param['zkzh'] = zkzh
os.system('pause')