#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-07-24 10:29
# describe：情感分析
import configs
from demos.demo_base import DemoBase
import timeutils


class Demo(DemoBase):
    
    def get_test_texts(self) -> list:
        return [
            '这家店的菜真好吃！',
            '差评，跟宣传的不符合，也不给退货',
            '这是我买到过最实惠的产品了！',
            '这个产品太差了，买不起！',
        ]
        
    @timeutils.monitor
    def load_model(self):
        from modelscope.pipelines import pipeline
        from modelscope.utils.constant import Tasks
        semantic_cls = pipeline(Tasks.text_classification, 'damo/nlp_structbert_emotion-classification_chinese-tiny', model_revision='v1.0.0', device=configs.DEVICE)
        return semantic_cls

    @timeutils.monitor
    def gen_result(self, model_obj, input_text):
        result = model_obj(input=input_text)
        max_index = result['scores'].index(max(result['scores']))
        most_accurate_label = result['labels'][max_index]
        return most_accurate_label


def do_task():
    demo = Demo()
    demo.do_task()
    

if __name__ == "__main__":
    do_task()
