#!/usr/bin/python
# -*- coding:utf-8 -*-

"""Documentation"""

import os
from datetime import datetime

import logging

LOG_NAME = "test"


def init_log():
    file_name = "{0}_{1}.log".format(
        LOG_NAME,
        datetime.now().strftime("%Y%m%d%H%M%S")
    )

    logging.basicConfig(
        filename=os.path.join(os.getcwd(), file_name),
        filemode='w',
        format='%(asctime)s, %(levelname)s, %(message)s',
        level=logging.NOTSET
    )




if __name__ == "__main__":
    init_log()
    logging.info("log test")
    logging.error("this is error!!!")

    pass
