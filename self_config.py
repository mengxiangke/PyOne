#-*- coding=utf-8 -*-
import os

#限制调用域名
allow_site=[u'no-referrer']

#######源码目录
config_dir="/root/PyOne"
data_dir=os.path.join(config_dir,'data')

#下载链接过期时间
downloadUrl_timeout="300"

#后台密码设置
password="PyOne"

#网站名称
title="PyOne"

#自定义代码
tj_code=""""""
headCode=""""""
footCode=""""""
cssCode=""""""

#主题设置
theme="bst4"

#网站标题前缀
title_pre="index of "

#onedrive api设置
redirect_uri="https://auth.pyone.me/" #不要修改！
BaseAuthUrl='https://login.microsoftonline.com'
app_url=u'https://graph.microsoft.com/'

#aria2配置
ARIA2_HOST="localhost"
ARIA2_PORT="6800"
ARIA2_SECRET=""
ARIA2_SCHEME="http"


#搜索模式
show_secret="no"

#文件是否支持加密--no-文件夹加密的情况下，如果直接访问该文件夹下的文件链接，则会跳过密码
encrypt_file="no"


od_users={
    "A":{
        "client_id":"b164356c-ae8a-484d-a4d0-aa1a67f8c676",
        "client_secret":"yfYVT21||ireutYLYG962#*",
        "share_path":"/",
        "other_name":"网盘1区",
        "order":1
    },
    "B":{
        "client_id":"",
        "client_secret":"",
        "share_path":"/",
        "other_name":"网盘2区",
        "order":2
    },
    "C":{
        "client_id":"",
        "client_secret":"",
        "share_path":"/",
        "other_name":"网盘3区",
        "order":3
    }
}


