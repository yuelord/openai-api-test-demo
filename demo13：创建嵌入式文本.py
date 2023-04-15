# POST https://api.openai.com/v1/embeddings
# pip install openai[datalib]
import os
import openai

embedding_messages = input('输入嵌入的文本：').strip()
openai.api_key = os.getenv('OPENAI_API_KEY')
res = openai.Embedding.create(
    model = 'text-embedding-ada-002',
    input= embedding_messages
)
print(res)

# 程序能跑动，代码也没有错。暂时不知道用来干嘛，应该嵌入大量的文字，且保存输入的原格式。