#!/bin/bash
output=`pytest --alluredir ./result main.py`
output=`allure generate ./result/ -o ./report/ --clean`
allure open -h 127.0.0.1 -p 8083 ./report/