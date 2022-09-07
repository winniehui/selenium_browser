import pytest

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")
