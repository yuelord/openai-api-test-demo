# POST https://api.openai.com/v1/chat/completions
import openai
import os


# 从win10电脑的环境变量中访问 OpenAI API 密钥
openai.api_key = os.getenv('OPENAI_API_KEY')

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "你好"}]
)
print(completion.choices)
# print(completion.choices[0].message.content.strip())
