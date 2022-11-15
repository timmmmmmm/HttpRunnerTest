import logging
import time
from typing import List


# commented out function will be filtered
# def get_headers():
#     return {"User-Agent": "hrp"}


def get_user_agent():
    return "hrp/funppy"

def sleep(n_secs):
    time.sleep(n_secs)

def concatenate(*args: List[str]) -> str:
    result = ""
    for arg in args:
        result += str(arg)
    return result

def setup_hook_example(name):
    logging.warning("setup_hook_example")
    return f"setup_hook_example: {name}"

def teardown_hook_example(name):
    logging.warning("teardown_hook_example")
    return f"teardown_hook_example: {name}"

def add_2FA_code():
    code = 0
    return code

def print(input):
    print(input)