#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'steve'

import unittest
import urllib.parse
import json

class Assert1(unittest.TestCase):

    def __init__(self, methodName='runTest', test_data=None, http=None, db1_cursor=None, db2_cursor=None):
        super(Assert1, self).__init__(methodName)
        self.test_data = test_data
        self.http = http
        self.db1_cursor = db1_cursor
        self.db2_cursor = db2_cursor

class Assert2(Assert1):
    def setUp(self):
        pass

    def assertion(self, response, expected_1='', expected_2='', expected_3=''):
        if response == {}:
            self.test_data.result = 'Error'
            try:
                # 更新结果表中的用例运行结果
                self.db1_cursor.execute('UPDATE test_result SET result = %s WHERE case_id = %s',
                                        (self.test_data.result, self.test_data.case_id))
                self.db1_cursor.execute('commit')
            except Exception as e:
                print('%s' % e)
                self.db1_cursor.execute('rollback')
            return

        try:
            ####连接数据库，读取数据库相关值，用于和接口请求返回结果做比较
            # self.db1_cursor.execute('SELECT expected_1, expected_2 FROM expected_result WHERE case_id = %s', (self.test_data.case_id,))
            # expected_result = self.db1_cursor.fetchone()
            # expected_status = expected_result[0]
            # expected_code = expected_result[1]
            self.assertEqual(response['status'], expected_1, msg='返回status不等于' + expected_1)
            if expected_2 != '':
                self.assertEqual(response['code'], expected_2, msg='返回code不等于' + expected_2)
            if expected_3 != '':
                self.assertEqual(response['data'], expected_3, msg='返回data不等于' + expected_3)
            self.test_data.result = 'Pass'

            if response["data"] == "None":
                pass
            else:
                self.code = response["data"]
                self.test_data.result = 'Pass'
                try:
                    self.db1_cursor.execute('UPDATE stored_cache SET verification_code = %s where tid = %s', (self.code, '1'))
                    self.db1_cursor.execute('UPDATE stored_cache SET phone_number = %s where tid = %s', (self.phoneNumber, '1'))
                    self.db1_cursor.execute('commit')

                except Exception as e:
                    # 回滚
                    print('%s' % e)
                    self.db1_cursor.execute('rollback')
        except AssertionError as e:
            print ('%s' % e)
            self.test_data.result = 'Fail'
            self.test_data.reason = '%s' % e  #### 记录失败原因
        #### 更新结果表中的用例运行结果
        try:
            self.db1_cursor.execute('UPDATE test_result SET result = %s WHERE case_id = %s',
                                    (self.test_data.result, self.test_data.case_id))
            self.db1_cursor.execute('UPDATE test_result SET reason = %s WHERE case_id = %s',
                                    (self.test_data.reason, self.test_data.case_id))
            self.db1_cursor.execute('commit')
        except Exception as e:
            print('%s' % e)
            self.db1_cursor.execute('rollback')