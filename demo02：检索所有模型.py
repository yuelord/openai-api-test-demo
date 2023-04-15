# GET https://api.openai.com/v1/models

import os
import openai

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
print(openai.Model.list())