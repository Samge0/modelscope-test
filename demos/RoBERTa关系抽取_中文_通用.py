#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-07-24 17:33
# describe： RoBERTa关系抽取-中文-通用-base
import configs
from demos.demo_base import DemoBase
import timeutils


class Demo(DemoBase):
    
    def get_test_texts(self) -> list:
        return [
            '高捷，祖籍江苏，本科毕业于东南大学。',
        ]
    
    def get_models() -> list:
        return []
        
    @timeutils.monitor
    def load_model(self, model_name=None):
        from modelscope.pipelines import pipeline
        from modelscope.utils.constant import Tasks
        ner_pipeline = pipeline(Tasks.information_extraction, 'damo/nlp_bert_relation-extraction_chinese-base', device=configs.DEVICE)
        return ner_pipeline

    @timeutils.monitor
    def gen_result(self, model_obj, input_text):
        results = model_obj(input_text)
        txt = ''
        for result in results:
            for i in result:
                txt += f'{i[0]} -> {i[1]} -> {i[2]}\n'
        return txt


def do_task():
    demo = Demo()
    demo.do_task()
    

if __name__ == "__main__":
    do_task()
