#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'steve'

import urllib.request
import http.cookiejar
import urllib.parse
import json
import configparser

# 配置类
class ConfigHttp:
    '''配置要测试接口服务器的ip、端口、域名等信息，封装http请求方法，http头设置'''

    def __init__(self, ini_file):
        config = configparser.ConfigParser()

        # 从配置文件中读取接口服务器IP、域名，端口
        config.read(ini_file)
        self.host = config['HTTP']['host']
        self.port = config['HTTP']['port']
        self.headers = {}  # http 头
        #install cookie
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        urllib.request.install_opener(opener)

    def set_host(self, host):
        self.host = host

    def get_host(self):
        return self.host

    def set_port(self, port):
        self.port = port

    def get_port(self):
        return self.port

    # 设置http头
    def set_header(self, headers):
        self.headers = headers

    # 封装HTTP GET请求方法
    def get(self, url, params):
        if params == '':
            url = 'http://' + self.host + ':' + str(self.port) + url
        elif params.find('.do') == -1:
            params = urllib.parse.urlencode(eval(params))  # 将参数转为url编码字符串
            url = 'http://' + self.host + ':' + str(self.port) + url + params
        else:
            url = 'http://' + self.host + ':' + str(self.port) + url + params
        print (url)
        request = urllib.request.Request(url, headers=self.headers)

        try:
            response = urllib.request.urlopen(request)
            response = response.read().decode('utf-8')  ## decode函数对获取的字节数据进行解码
            json_response = json.loads(response)  # 将返回数据转为json格式的数据
            return json_response
        except Exception as e:
            print('%s' % e)
            return {}

    # 封装HTTP POST请求方法
    def post(self, url, data, token=None):
        if url.find('yzhealth-portal') == -1:
            data_str = urllib.parse.urlencode(eval(data))  # 将参数转为url编码字符串
            if token is None:
                token = ''
            else:
                token = urllib.parse.urlencode(eval(token))
            # data = json.dumps(eval(data))
            # data = data.encode('utf-8')
            url = 'http://' + self.host + ':' + str(self.port) + url + data_str + '&' + token
        else:
            data = json.dumps(eval(data))
            data = data.encode('utf-8')
            url = 'http://' + self.host + ':' + str(self.port) + url
        print (url)
        try:
            request = urllib.request.Request(url, headers=self.headers)
            response = urllib.request.urlopen(request, data)
            response = response.read().decode('utf-8')
            json_response = json.loads(response)
            return json_response
        except Exception as e:
            print('%s' % e)
            return {}











    # 封装HTTP xxx请求方法
    # 自由扩展
    #
    ###     def get(self, url, params):
    ###        params = urllib.parse.urlencode(eval(params))  # 将参数转为url编码字符串
    ###       url = 'http://' + self.host + ':' + str(self.port) + url + params
    ###      request = urllib.request.Request(url, headers=self.headers)
    ###
    ###        try:
    ###          response = urllib.request.urlopen(request)
    ###         response = response.read().decode('utf-8')  ## decode函数对获取的字节数据进行解码
    ###             json_response = json.loads(response)  # 将返回数据转为json格式的数据
    ###             return json_response
    ###         except Exception as e:
    ###             print('%s' % e)
    ###         return {}

        # 封装HTTP POST请求方法
###        def post(self, url, data, token):
###            data = json.dumps(eval(data))
###            data = data.encode('utf-8')
###
###            token = urllib.parse.urlencode(eval(token))
###
###            url = 'http://' + self.host + ':' + str(self.port) + url + token
###            print (url)
###            try:
###                request = urllib.request.Request(url, headers=self.headers)
###                response = urllib.request.urlopen(request, data)
###                response = response.read().decode('utf-8')
###                json_response = json.loads(response)
###                return json_response
###            except Exception as e:
###                print('%s' % e)
###                return {}