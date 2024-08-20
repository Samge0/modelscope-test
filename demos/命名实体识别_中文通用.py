#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-07-24 17:33
# describe： 命名实体识别_中文通用
import configs
from demos.demo_base import DemoBase
import timeutils


class Demo(DemoBase):
    
    def get_test_texts(self) -> list:
        return [
            '他继续与貝塞斯達遊戲工作室在接下来辐射4游戏。',
            '他与他家的猫漫步在飞亚达科技大厦前面的迈瑞大厦旁边的马路上。',
        ]
    
    def get_models() -> list:
        return [
            'damo/nlp_raner_named-entity-recognition_chinese-base-ecom-50cls',
            'damo/nlp_raner_named-entity-recognition_chinese-large-generic',
        ]
        
    @timeutils.monitor
    def load_model(self, model_name=None):
        from modelscope.pipelines import pipeline
        from modelscope.utils.constant import Tasks
        ner_pipeline = pipeline(Tasks.named_entity_recognition, 'damo/nlp_raner_named-entity-recognition_chinese-large-generic', device=configs.DEVICE)
        return ner_pipeline

    @timeutils.monitor
    def gen_result(self, model_obj, input_text):
        result = model_obj(input_text)
        return result.get('output')


def do_task():
    demo = Demo()
    demo.do_task()
    

if __name__ == "__main__":
    do_task()
