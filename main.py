#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-07-24 10:23
# describe：测试主入口


import configs

# 终端提示文本
terminal_tip = f"""请选择要执行的任务：

{configs.terminal_tip}
exit -> 退出

如果需要退出，请输入 exit 或按 Ctrl + C
："""


# 执行任务
def do_task():
    input_text = input(terminal_tip)
    if input_text == 'exit':
        return
    
    obj = configs.COMMAND_MAP.get(input_text)
    if obj is None:
        print("输入错误，自动退出")
        return
    
    obj.do_task()


if __name__ == "__main__":
    do_task()




