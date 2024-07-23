#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-07-24 10:23
# describe：测试主入口


from demos import 情感分析


# 终端提示文本
terminal_tip = """请选择要执行的任务：
0：情感分析

如果需要退出，请按 Ctrl + C
"""


# 执行任务
def do_task():
    input_text = input(terminal_tip)
    if input_text == '0':
        情感分析.do_task()
    else:
        print("输入错误，自动退出")


if __name__ == "__main__":
    do_task()




