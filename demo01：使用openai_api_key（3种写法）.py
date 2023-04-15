import os
import openai
"""
写代码前，要在win10的高级系统设置>>环境变量中，新建系统变量(不是用户变量)，如下：
变量名(N)：OPENAI_API_KEY
变量值(V)：sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
注意：先配置好环境变量，再启动 pycharm 编辑器，否则检测不到windows配置好的 "OPENAI_API_KEY"
"""

# 方法一：通过组织
# openai.organization = 'org-z3vz6DeWINdBScnYLsmlOCn3'
# openai.api_key = os.environ['OPENAI_API_KEY']



# 方法二：
openai.api_key = os.environ['OPENAI_API_KEY']



# 方法三：
openai.api_key = os.getenv('OPENAI_API_KEY')



print(type(openai.api_key),openai.api_key)