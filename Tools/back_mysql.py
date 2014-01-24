#!/usr/bin/python
# -*- coding:utf-8 -*-
# Filename: 'back_mysql.py'

"""MySQL备份脚本

按照如下格式打包：
[BASE_FOLDER]/[host]/[database]/[年月日]/[sql压缩包+日志]
例如：
/data/back_mysql/
└── 127.0.0.1
    ├── test
    │   └── 20140103
    │       ├── 20140103151001.log
    │       └── 20140103151001.zip
    └── mysql
        └── 20140103
            ├── 20140103151001.log
            └── 20140103151001.zip


配合linux的[crontab] 或 windows的[计划任务]使用

"""

import os
import subprocess
from datetime import datetime


# 备份根路径
BASE_FOLDER = r"/data/back_mysql"

# 备份结果是否使用zip打包压缩
USR_ZIP = True

# 配置待备份的MySQL数据源
MYSQL_SOURCES = (
    {
        "host": "127.0.0.1",
        "port": 3306,
        "database": "mysql",
        "user": "root",
        "password": "123456"
    },
    {
        "host": "127.0.0.1",
        "port": 3306,
        "database": "test",
        "user": "root",
        "password": "12345"
    },

)

_CMD_BACKUP = "mysqldump -h {host} -P {port} {database} -u {user} -p{password} --single-transaction > "
_CMD_TAR = "zip -jmq {destination} {source}"

_START_TIME = datetime.now()
_LOG_PATH = ""
_CURRENT_DB = ""


def execute(cmd):
    return subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )


def log_out(info):
    with open(_LOG_PATH, "a") as log:
        log.write("*" * 80 + "\n")
        log.write("Datetime: %s\n" % _START_TIME)
        log.write("Database: %s\n" % _CURRENT_DB)
        for line in info.stdout.readlines():
            log.write(line)
        log.write("-" * 80 + "\n\n")


def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def create_folder(source):
    folder = os.path.join(
        BASE_FOLDER,
        source["host"],
        source["database"],
        _START_TIME.strftime("%Y%m%d")
    )

    if not os.path.exists(folder):
        os.makedirs(folder)

    global _LOG_PATH
    _LOG_PATH = os.path.join(
        folder,
        _START_TIME.strftime("%Y%m%d%H%M%S") + ".log"
    )
    return folder


def backup(source):
    global _CURRENT_DB
    _CURRENT_DB = source["database"]

    folder = create_folder(source)

    file_name = _START_TIME.strftime("%Y%m%d%H%M%S")
    sql_file = os.path.join(folder, file_name + ".sql")
    backup_script = (_CMD_BACKUP + sql_file).format(**source)
    result = execute(backup_script)
    result.wait()
    log_out(result)

    if USR_ZIP:
        tar_script = _CMD_TAR.format(
            destination=os.path.join(folder, file_name + ".zip"),
            source=sql_file
        )
        execute(tar_script).wait()


def main():
    for source in MYSQL_SOURCES:
        start_time = datetime.now()
        backup(source)
        finished_time = datetime.now()
        print("spent: {0} backup: {1}".format(
            finished_time - start_time, source))

    print("all finished!")


if __name__ == "__main__":
    main()
    pass
