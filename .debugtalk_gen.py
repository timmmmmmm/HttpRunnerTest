# NOTE: Generated By hrp v4.3.0, DO NOT EDIT!

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from debugtalk import *


if __name__ == "__main__":
    import funppy
    funppy.register("get_user_agent", get_user_agent)
    funppy.register("sleep", sleep)
    funppy.register("concatenate", concatenate)
    funppy.register("setup_hook_example", setup_hook_example)
    funppy.register("teardown_hook_example", teardown_hook_example)
    funppy.register("add_2FA_code", add_2FA_code)
    funppy.register("print", print)
    funppy.serve()
