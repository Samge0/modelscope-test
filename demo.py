#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-07-24 10:22
# describe：魔塔社区模型最简demo

from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
semantic_cls = pipeline(Tasks.text_classification, 'damo/nlp_structbert_emotion-classification_chinese-tiny', model_revision='v1.0.0')
print(semantic_cls("这家店的菜真好吃！"))