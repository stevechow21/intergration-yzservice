#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'steve'

import unittest

class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, methodName='runTest', test_data=None, http=None, db1_cursor=None, db2_cursor=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.test_data = test_data
        self.http = http
        self.db1_cursor = db1_cursor
        self.db2_cursor = db2_cursor

    def UpdateRecordWithoutResponse(self, response):
        if {} == response:
            self.test_data.result = 'Error'
            try:
                #### 更新结果表中的用例运行结果
                self.db1_cursor.execute('UPDATE test_result SET result = %s WHERE case_id = %s',
                                        (self.test_data.result,
                                         self.test_data.case_id))
                self.db1_cursor.execute('commit')
            except Exception as e:
                print('%s' % e)
                self.db1_cursor.execute('rollback')
            return

    def BaseDataAssert(self, response):
        try:
            #### 断言
            self.assertNotEqual(str(response['code']), '-1', msg='返回code等于-1，创建失败')
            self.assertEqual(response['status'], 'success', msg='返回status不等于success')
            self.test_data.result = 'Pass'
        except AssertionError as e:
            print('%s' % e)
            self.test_data.result = 'Fail'
            self.test_data.reason = '%s' % e  #### 记录失败原因

    def UpdateRecordWithResponse(self):
        #### 更新结果表中的用例运行结果
        try:
            self.db1_cursor.execute('UPDATE test_result SET result = %s WHERE case_id = %s', (self.test_data.result,
                                                                                              self.test_data.case_id))
            self.db1_cursor.execute('UPDATE test_result SET reason = %s WHERE case_id = %s', (self.test_data.reason,
                                                                                              self.test_data.case_id))
            self.db1_cursor.execute('commit')
        except Exception as e:
            print('%s' % e)
            self.db1_cursor.execute('rollback')