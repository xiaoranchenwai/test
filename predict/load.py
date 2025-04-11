from config.utils import config
from openai import OpenAI
# 获取大模型的输出
def get_model_output(text):
    base_url = config['base_url']
    model = config['llm_model_name']
    client = OpenAI(base_url=base_url, api_key=config['api_key'])
    completion = client.chat.completions.create(
        model = model,
        temperature = 0.0,
        messages = [
            {
                "role": "user",
                "content": text,
            }
        ],
    )

    return completion.choices[0].message.content