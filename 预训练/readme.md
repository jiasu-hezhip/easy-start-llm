# 简介
预训练一般开发者都不会涉及，一般只需要微调就好，这里只介绍如何训练千问1的基座模型，千问2也已经集成到了transformers，但是导入需要cuda11，所以这里不介绍

这里会给出千问1的训练代码

1.修改[generate_data.py](generate_data.py)生成训练数据

2.修改[generate_data.py](generate_data.py)中的数据路径

3.train.sh pretrain.py
