#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'steve'

class ClearTestData:
    def __init__(self, cursor):
        self.cursor = cursor

    # 清除测试数据
    def clear_data(self):
        query = ('DELETE FROM test_result')
        self.cursor.execute(query)
        self.cursor.execute('commit')