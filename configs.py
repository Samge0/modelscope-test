#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-07-24 09:59
# describe：配置文件

import torch

from demos import 情感分析, 命名实体识别_中文通用


# 是否使用终端交互模式
TERMINAL_MODEL = True


# 模型运行所在的设备
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'


# 命令映射字典
COMMAND_MAP = {
    '0': 情感分析,
    '1': 命名实体识别_中文通用,
}

# 命令提示文本
terminal_tip = "\n".join([f"{idx} -> {cmd.__name__}" for idx, cmd in COMMAND_MAP.items()])