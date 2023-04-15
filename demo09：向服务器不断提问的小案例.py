import os
import openai

openai.api_key = os.environ['OPENAI_API_KEY']


def generate_response(prompt):
    # 指定使用的 GPT-3 模型版本
    model_engine = "text-davinci-003"
    # openai.Completion.create() 方法则是通过向 OpenAI API 发送请求来获得模型生成结果
    response = openai.Completion.create(
        # 指定使用的 GPT-3 模型版本
        engine=model_engine,
        prompt=prompt,
        # max_tokens 参数指定返回文本长度上限
        max_tokens=2048,
        # n 参数表示要求返回几个结果
        n=1,
        # stop 参数可以用于控制模型停止生成文本的条件
        stop=None,
        # temperature参数控制随机性和创造力程度，介于0和2之间,较高的值（如 0.8）_
        # 将使输出更加随机，而较低的值（如 0.2）,将使输出更加集中和确定。
        temperature=1.2,
    )
    message = response.choices[0].text.strip()
    return message


while True:
    prompt = input("您： ").strip()
    print(prompt)
    response = generate_response(prompt)
    print("ChatGPT：", response)
