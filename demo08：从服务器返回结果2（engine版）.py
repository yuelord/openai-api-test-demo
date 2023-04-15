import os
import openai

openai.api_key = os.environ['OPENAI_API_KEY']

"""
选择指定模型：有的模型不能用，特别是gpt-3.5-turbo-0301、gpt-3.5-turbo、gpt-4、
            Moderation中的{text-moderation-latest、text-moderation-stable}
"""
response = openai.Completion.create(
    # 指定使用的 GPT-3.5 模型中，能用的最高版本text-davinci-003
    engine='text-davinci-003',
    # 发送的信息
    prompt='你好',
    # max_tokens 参数指定返回文本长度上限
    max_tokens=1024,
    # 用户名或ID
    user='用户1',
    # n 参数表示要求返回几个结果
    n=1,
    # stop 参数可以用于控制模型停止生成文本的条件
    stop=None,
    # temperature参数控制随机性和创造力程度，介于0和2之间,较高的值（如 0.8）_
    # 将使输出更加随机，而较低的值（如 0.2）,将使输出更加集中和确定。
    temperature=0
)

print(response.choices[0].text.strip())