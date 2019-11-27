# coding:utf-8
import unittest
import requests,json
import os, sys

cur_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, cur_path)
from db_fixture import test_data


class TestAddEvent(unittest.TestCase):
    """添加发布会"""

    def setUp(self):
        # self.base_url = "http://47.xx.xxx.xx:8000/api/add_event/"
        self.base_url = "https://sitcrmgw.vxlogisticproperties.com/gw/uncheck/api/login"

    def tearDown(self):
        print("")

    def test_add_event_all_null(self):
        """所有参数为空添加"""
        # payload = {"eid": "", "name": "", "limit2": "", "address": "", "start_time": ""}
        payload =  json.dumps({"password":"abc@1234","randomStr":726354,"userAccount":"yangx78"})
        headers = {"Content-Type": "application/json"}

        r = requests.post(self.base_url, data=payload, headers=headers)
        print("33333333333_______self.base_url  : " + str(self.base_url) + ",    payload :    " + str(payload) +" ,   r :  " + str(r))
        self.result = r.json()
        self.assertEqual(self.result["msg"], "操作成功")
        # self.assertEqual(self.result["message"], "parameter error")

    def test_add_event_eid_exist(self):
        """id已经存在"""
        payload = {"eid": 1, "name": "一加4发布会", "limit2": 2000, "address": "深圳宝体", "start_time": "2018-11-01 08:00:00"}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], 10022)
        self.assertEqual(self.result["message"], "event id already exists")

    def test_add_event_name_exists(self):
        """名称已经存在"""
        payload = {"eid": 88, "name": "红米Pro发布会", "limit2": 2000, "address": "深圳宝体",
                   "start_time": "2018-11-01 08:00:00"}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], 10023)
        self.assertEqual(self.result["message"], "event name already exists")

    def test_add_event_data_type_error(self):
        """日期格式错误"""
        payload = {"eid": 102, "name": "一加4发布会", "limit2": 2000, "address": "深圳宝体", "start_time": "2018"}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], 10024)

    def test_add_event_success(self):
        """添加成功"""
        payload = {"eid": 88, "name": "孙小二发布会", "limit2": 2000, "address": "深圳宝体", "start_time": "2018-11-01 08:00:00"}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        print(self.result)
        self.assertEqual(self.result["status"], 200)


if __name__ == '__main__':
    test_data.init_data()  # 初始化接口测试数据
    unittest.main()