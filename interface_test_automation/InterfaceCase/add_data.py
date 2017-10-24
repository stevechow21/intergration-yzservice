#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'steve'

import sys
sys.path.append("..")
from interface_test_automation.initialization import ParametrizedTestCase

#### 后台操作-创建测试数据（登录、机构、套餐、检查项）
class addData(ParametrizedTestCase):

    def addData(self):
        #### 根据被测接口的实际情况，合理的添加HTTP头
        header = {'Host': '172.16.10.100:17010',
                  'Accept': 'application/json, text/javascript, */*; q=0.01',
                  'Accept-Encoding': 'gzip, deflate',
                  'Content-Type': 'application/json; charset=utf8',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                  'X-Requested-With': 'XMLHttpRequest'}
        self.http.set_header(header)
        response = self.http.post(self.test_data.request_url,  self.test_data.request_param)
        print (response)

        self.UpdateRecordWithoutResponse(response)
        self.BaseDataAssert(response)
        self.UpdateRecordWithResponse()