#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-07-24 17:40
# describe：


from abc import abstractmethod
import inspect

import configs


class DemoBase:
    
    @abstractmethod
    def get_test_texts(self) -> list:
        raise NotImplementedError(f'{self.__class__.__name__}.{inspect.stack()[1][3]} method is not defined')
    
    @abstractmethod
    def load_model(self):
        raise NotImplementedError(f'{self.__class__.__name__}.{inspect.stack()[1][3]} method is not defined')
    
    @abstractmethod
    def gen_result(self, model_obj, input_text):
        raise NotImplementedError(f'{self.__class__.__name__}.{inspect.stack()[1][3]} method is not defined')
    
    # 执行任务
    def do_task(self):
        print("正在加载模型...")
        model_obj = self.load_model()
        if configs.TERMINAL_MODEL:
            while True:
                input_text = input("请输入文本：")
                if input_text == 'exit':
                    break
                print("正在推理...")
                result = self.gen_result(model_obj, input_text)
                print(result)
        else:
            print("正在推理...")
            test_texts = self.get_test_texts()
            for input_text in test_texts:
                result = self.gen_result(model_obj, input_text)
                msg = f"{input_text} => {result}"
                print(msg)
