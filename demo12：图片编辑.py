# POST https://api.openai.com/v1/images/edits
# 注意：该功能的api使用成本很高的
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Image.create_edit(
    # 要编辑的图像。必须是有效的PNG文件，小于4MB，并且是正方形的。如果未提供蒙版，图像必须具有透明度，这将用作蒙版。
    image=open('images/winter.png','rb'),
    # 一个附加图像，其全透明区域（例如alpha为零）指示应编辑图像的位置。必须是有效的PNG文件，小于4MB，并且具有与图像相同的尺寸。
    mask = open('images/earth.png','rb'),
    # 所需图像的文本描述。最大长度为1000个字符。没有效果，图片不对
    prompt="冬天雪地的高空悬挂一个小球",
    n = 2,
    size='512x512'
)
print(response.data)