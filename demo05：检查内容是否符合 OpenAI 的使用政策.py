import os
import openai

openai.api_key = os.environ['OPENAI_API_KEY']
openai.Model.retrieve('gpt-3.5-turbo')

message = input('you：').strip()

'''
本案例，主要用于检查内容是否符合 OpenAI 的使用政策

类别	描述
hate                基于种族、性别、民族、宗教、国籍、性取向、残疾状况或种姓表达、煽动或促进仇恨的内容。
hate/threatening	仇恨内容还包括对目标群体的暴力或严重伤害。
self-harm           提倡、鼓励或描述自残行为（例如自杀、割伤和饮食失调）的内容。
sexual              意在引起性兴奋的内容，例如对性活动的描述，或宣传性服务（不包括性教育和健康）的内容。
sexual/minors       包含 18 岁以下个人的色情内容。
violence            宣扬或美化暴力或颂扬他人的痛苦或屈辱的内容。
violence/graphic	以极端的画面细节描绘死亡、暴力或严重身体伤害的暴力内容。
'''
response = openai.Moderation.create(
    input=message
)

# print(response['results'])
output = response['results'][0]
print(output)