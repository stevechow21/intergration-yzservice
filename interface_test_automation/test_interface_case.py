#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'steve'

import unittest
import urllib.parse
import json
import time
import sys
from initialization import ParametrizedTestCase
sys.path.append("..")
from InterfaceCase.add_data import addData
from InterfaceCase.edit_data import editData
from InterfaceCase.package_to_org import packageToOrg
from InterfaceCase.package_to_examine import packageToExamine
from InterfaceCase.release_package import releasePackage
from InterfaceCase.soldOut_package import soldOutPackage
from InterfaceCase.recommend_package import recommendPackage
from InterfaceCase.test_get_token import testGetToken
from InterfaceCase.test_get_province import testGetProvince
from InterfaceCase.test_get_city import testGetCity
from InterfaceCase.test_get_data_dictionary import testGetDataDictionary
from InterfaceCase.test_get_homepage import testGetHomepage
from InterfaceCase.test_get_package_list import testGetPackageList
from InterfaceCase.test_get_package_detail import testGetPackageDetail
from InterfaceCase.test_get_org_list import testGetOrgList
from InterfaceCase.test_get_package_price import testGetPackagePrice
from InterfaceCase.test_create_order import testCreateOrder
from InterfaceCase.test_cancel_order import testCancelOrder
from InterfaceCase.test_get_order_list import testGetOrderList
from InterfaceCase.test_order_detail import testOrderDetail
from InterfaceCase.test_edit_idcard import testEditIdCard
from InterfaceCase.test_edit_member import testEditMember
from InterfaceCase.test_view_member import testViewMember
from InterfaceCase.test_get_check_code import testGetCheckCode

class TestInterfaceCase(ParametrizedTestCase):

    def setUp(self):
        pass

    #### 后台操作-创建测试数据（登录、机构、套餐、检查项）
    def add_data(self):
        addData.addData(self)

    #### 后台操作-编辑测试数据（登录、机构、套餐、检查项）
    def edit_data(self):
        editData.editData(self)

    #### 套餐关联机构
    def package_to_org(self):
        packageToOrg.packageToOrg(self)

    #### 套餐添加检查项
    def package_to_examine(self):
        packageToExamine.packageToExamine(self)

    #### 上架套餐
    def release_package(self):
        releasePackage.releasePackage(self)

    #### 下架套餐
    def soldOut_package(self):
        soldOutPackage.soldOutPackage(self)

    #### 微信首页推荐套餐
    def recommend_package(self):
        recommendPackage.recommendPackage(self)

    ####分割线，以下为微信端#################################################################

    #### 获取token
    def test_get_token(self):
        testGetToken.testGetToken(self)

    #### 获取省份列表
    def test_get_province(self):
        testGetProvince.testGetProvince(self)

    #### 根据省份id获取城市列表
    def test_get_city(self):
        testGetCity.testGetCity(self)

    #### 根据父类code获取子类数据字典
    def test_get_data_dictionary(self):
        testGetDataDictionary.testGetDataDictionary(self)

    #### 根据城市获取推荐套餐列表
    def test_get_homepage(self):
        testGetHomepage.testGetHomepage(self)

    #### 根据城市和套餐类别查找体检套餐列表
    def test_get_package_list(self):
        testGetPackageList.testGetPackageList(self)

    #### 根据套餐id查找套餐详情
    def test_get_package_detail(self):
        testGetPackageDetail.testGetPackageDetail(self)

    #### 根据城市ID和套餐ID查询机构列表
    def test_get_org_list(self):
        testGetOrgList.testGetOrgList(self)

    #### 根据优惠码计算套餐价格
    def test_get_package_price(self):
        testGetPackagePrice.testGetPackagePrice(self)

    #### 创建订单
    def test_create_order(self):
        testCreateOrder.testCreateOrder(self)

    #### 取消订单
    def test_cancel_order(self):
        testCancelOrder.testCancelOrder(self)

    #### 查看订单列表
    def test_get_order_list(self):
        testGetOrderList.testGetOrderList(self)

    #### 订单详情
    def test_order_detail(self):
        testOrderDetail.testOrderDetail(self)

    #### 添加身份证
    def test_edit_idcard(self):
        testEditIdCard.testEditIdCard(self)

    #### 修改个人信息
    def test_edit_member(self):
        testEditMember.testEditMember(self)

    #### 查看个人信息
    def test_view_member(self):
        testViewMember.testViewMember(self)

    #### 获取下单时的Check Code
    def test_get_check_code(self):
        testGetCheckCode.testGetCheckCode(self)

    def tearDown(self):
        pass