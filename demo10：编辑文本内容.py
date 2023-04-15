# POST https://api.openai.com/v1/edits
import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

response = openai.Edit.create(
    model='text-davinci-edit-001',
    # 要编辑的内容，比如，有错误的单词；要翻译的文字
    input='The input text to use as a starting point for the edit.',
    # 告诉AI，怎么修改
    instruction="翻译下内容"
)
print(response)
# 打印修改后的内容
print(response.choices[0].text)