#!/usr/bin/python
# -*- coding:utf-8 -*-
# Filename: 'test_log_conf.py'

"""Documentation"""
import logging
import logging.config

LOG_CONF = "./logging.ini"

logging.config.fileConfig(LOG_CONF)

log_root = logging.getLogger("root")
log_fun = logging.getLogger("fun")

# 测试配置文件[logger_multiLevel]配置项qualname=level1.level2
# 符合qualname规则，记录的日志将被输出至文件
log_level_1_2 = logging.getLogger("level1.level2")
log_level_1_2_3 = logging.getLogger("level1.level2.level3")

# 不符合qualname规则，记录的日志不被输出至文件
log_level_1_1 = logging.getLogger("level1.level1")


def test():
    log_fun.debug("enter `test()`")

    # 不被记录至文件
    log_level_1_1.debug("enter `test()`")

    def get_item(ls, index):
        # 被记录至文件
        log_level_1_2_3.debug("enter `getItem()`")

        return ls[index]

    try:
        # 被记录至文件
        log_level_1_2.debug("will call `get_item()`")
        get_item([], 10)
        return True
    except IndexError as e:
        log_fun.exception(e)
        return False


if __name__ == "__main__":
    log_root.info("start test")

    if not test():
        log_root.warning("this something wrong when execute `test()`")

    log_root.info("finished all")
