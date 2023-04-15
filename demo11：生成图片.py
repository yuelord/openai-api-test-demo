# POST https://api.openai.com/v1/images/generations

import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

response = openai.Image.create(
    prompt="男孩儿眉毛柔顺自然，眼睛大而明亮，鼻梁挺直，脸上却带着一丝坏笑",
    # 要生成的图片数，数值在[1,10]区间
    n=1,
    # 生成的图片尺寸，有3种规格选择：'256x256', '512x512', '1024x1024'
    size="512x512"
)
print(response)
# 打印第一张图片地址
print(response.data[0].url)