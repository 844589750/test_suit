#!/usr/bin python
# coding=utf8
import requests
import json
import allure


@allure.feature('豆瓣接口城市参数校验')
def test_douban_city_cases(service, config):
    data = config["douban_city_test"]
    for case in data:
        with allure.step(case["des"]):
            try:
                result = get_request(service, case)
                allure.attach("返回结果", json.dumps(result))
                resp = result["title"]
                expect = case['expect'].encode('utf-8').decode('unicode_escape')[1:-1]
                assert check(expect in resp, "断言结果")
            except Exception:
                assert check(False, "断言结果出现异常")


@allure.feature('豆瓣接口返回数据量校验')
def test_douban_count_cases(service, config):
    data = config["douban_total_test"]
    for case in data:
        with allure.step(case["des"]):
            try:
                result = get_request(service, case)
                allure.attach("返回结果", json.dumps(result))
                count = int(case["count"])
                start = int(case["start"])
                total = int(result["total"])
                subjects = result["subjects"]
                expect = int(case['expect'])
                if total > start + count:
                    assert check(len(subjects) == expect, "断言结果")
                else:
                    assert check(len(subjects) < expect, "断言结果")
            except Exception:
                assert check(False, "断言结果出现异常")


def get_request(service, data):
    for key in data:
        data[key] = json.dumps(data[key])
    if service["method"] == "post":
        rep = requests.post(service["host"] + service["url"], params=data)
    else:
        rep = requests.get(service["host"] + service["url"], params=data)
    return rep.json()


def check(flag, des):
    with allure.step(des):
        if flag:
            allure.attach("实际结果", "成功")
            return True
        else:
            allure.attach("实际结果", "成功")
            return False
