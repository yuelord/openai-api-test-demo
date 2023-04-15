# GET https://api.openai.com/v1/models/{model}

import os
import openai

openai.api_key = os.environ['OPENAI_API_KEY']
# 选择指定模型：有的模型不能用，特别是gpt-4、Moderation中的{text-moderation-latest、text-moderation-stable}
print(openai.Model.retrieve('gpt-3.5-turbo'))
