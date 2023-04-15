# GET https://api.openai.com/v1/models

import os
import openai

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
model_data_json = openai.Model.list().data
print(model_data_json)
# 获得的json文件中筛选出所有模型
model_lists = []
for model_data in model_data_json:
    model = model_data.id
    model_lists.append(model)

# 转换为元组
model_tuple = [(x,) for x in model_lists]
# 使用set去重
set_tuple = set(model_tuple)
# 转换回列表
model_list = [x[0] for x in set_tuple]

print("openai api中的所有模型：",len(model_list),'个，他们是',model_list)
