#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-07-24 09:59
# describe：配置文件

import torch


# 是否使用终端交互模式
TERMINAL_MODEL = True


# 模型运行所在的设备
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'