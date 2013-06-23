#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:   Yan

"""有关Python中装饰器（Decorator）的示例
装饰器的用途有：引入日志、增加计时逻辑来检测性能、给函数加入事务的能力等
其实装饰器就是函数
```pyhton
@deco
def fun():
    pass
```
实际上就是这样一个复合函数：deco(fun())

装饰器作为函数也可以有自己的参数
```pyhton
@deco(arg)
def fun():
    pass
```
实际上等价于：deco(arg)(fun())

我觉得装饰器的本质就是数学中的符合函数，理解了符合函数，理解装饰器就差不多了

以下给出装饰器的几个例子，包括了有参装饰器、无参装饰器和有参函数、无参函数之间的相互组合
"""

from datetime import datetime

TESTER = "Yan"


# 1.无参装饰器包裹无参函数
def deco1(fun):
    print("[%s] %s() started" % (datetime.now(), fun.__name__))
    return fun


def deco2(fun):
    def wrapFun():
        print("[%s] %s() started" % (datetime.now(), fun.__name__))
        fun()
        print("[%s] %s() finished" % (datetime.now(), fun.__name__))
    return wrapFun

# # 删除注释执行
# @deco1      # @deco2
# def sayHi():
#     print("Hi~")
#
# sayHi()


# 2.无参装饰器包裹有参函数
def deco3(fun):
    def wrapFunArg(fun_arg):
        print("[%s] %s() started" % (datetime.now(), fun.__name__))
        fun(fun_arg)
        print("[%s] %s() finished" % (datetime.now(), fun.__name__))
    return wrapFunArg


# # 删除注释执行
# @deco3
# def sayName(name):
#     print("name is %s" % name)
#
# sayName("Apple")


# 3.有参装饰器包裹无参函数
def deco4(deco_arg):
    def wrapFun(fun):
        print("%s: [%s] %s() started" % (deco_arg, datetime.now(), fun.__name__))
        return fun
    return wrapFun


def deco5(deco_arg):
    def wrapFun(fun):
        def wrapFunInside():
            print("%s: [%s] %s() started" % (deco_arg, datetime.now(), fun.__name__))
            fun()
            print("%s: [%s] %s() finished" % (deco_arg, datetime.now(), fun.__name__))
        return wrapFunInside
    return wrapFun


# # 删除注释执行
# @deco4(TESTER)  # @deco5(TESTER)
# def sayHi():
#     print("Hi~")
#
# sayHi()


# 4.有参装饰器包裹有参函数
def deco6(deco_arg):
    def wrapFun(fun):
        def wrapFunArg(fun_arg):
            print("%s: [%s] %s() started" % (deco_arg, datetime.now(), fun.__name__))
            fun(fun_arg)
            print("%s: [%s] %s() finished" % (deco_arg, datetime.now(), fun.__name__))
        return wrapFunArg
    return wrapFun


# # 删除注释执行
# @deco6(TESTER)
# def sayName(name):
#     print("name is %s" % name)
#
# sayName("Apple")
