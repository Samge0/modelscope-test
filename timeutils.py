#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-07-24 10:38
# describe：
import time

# 计算函数耗时
def monitor(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 记录开始时间
        result = func(*args, **kwargs)  # 执行被装饰的函数
        end_time = time.time()  # 记录结束时间
        duration = end_time - start_time  # 计算耗时
        print(f"Function '{func.__name__}' took {duration:.2f} seconds to execute.")
        return result
    return wrapper