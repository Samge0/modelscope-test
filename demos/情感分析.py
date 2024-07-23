#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-07-24 10:29
# describe：情感分析
import configs
import timeutils


# 加载模型
@timeutils.monitor
def load_model():
    from modelscope.pipelines import pipeline
    from modelscope.utils.constant import Tasks
    semantic_cls = pipeline(Tasks.text_classification, 'damo/nlp_structbert_emotion-classification_chinese-tiny', model_revision='v1.0.0', device=configs.DEVICE)
    return semantic_cls


# 使用模型跟提示文本，生成结果并返回
@timeutils.monitor
def gen_result(model_obj, input_text):
    result = model_obj(input=input_text)
    max_index = result['scores'].index(max(result['scores']))
    most_accurate_label = result['labels'][max_index]
    return most_accurate_label


# 执行任务
def do_task():
    print("正在加载模型...")
    model_obj = load_model()
    if configs.TERMINAL_MODEL:
        while True:
            input_text = input("请输入文本：")
            result = gen_result(model_obj, input_text)
            print(result)
    else:
        test_texts = [
            '这家店的菜真好吃！',
            '差评，跟宣传的不符合，也不给退货',
            '这是我买到过最实惠的产品了！',
            '这个产品太差了，买不起！',
        ]
        for input_text in test_texts:
             result = gen_result(model_obj, input_text)
             msg = f"【{result}】{input_text}"
             print(msg)


if __name__ == "__main__":
    do_task()
