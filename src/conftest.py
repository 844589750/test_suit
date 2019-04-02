# coding=utf8
import pytest
import yaml


@pytest.fixture(scope="session")
def config():
    conf_url = "config/case.yml"
    with open(conf_url, "r", encoding="utf-8") as file:
        conf = yaml.load(file)
    return conf


@pytest.fixture(scope="session")
def service():
    service_url = "config/service.yml"
    with open(service_url, "r", encoding="utf-8") as file:
        serv = yaml.load(file)
    return serv
