import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')


# text 参数是要翻译的文本，target_language 是目标语言的缩写
def translate_text(text, target_language):
    prompt = f"将下列文本翻译成 {target_language}: \n{text}\n\n译文:"
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.2,
    )

    translation = response.choices[0].text.strip()
    return translation


text = input("要翻译的内容：").strip()
"""
中文 (zh)
英语 (en)
西班牙语 (es)
法语 (fr)
德语 (de)
意大利语 (it)
日语 (ja)
韩语 (ko)
葡萄牙语 (pt)
俄语 (ru)
"""
target_language = input("翻译为(填缩写):").strip()

context = translate_text(text=text, target_language=target_language)
print(context)
