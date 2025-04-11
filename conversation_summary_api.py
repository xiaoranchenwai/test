import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from config.utils import config, get_logger
from predict.load import get_model_output

# 创建FastAPI应用实例
app = FastAPI()

# 跨域支持
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

prompt = '''任务目标：你是一名优秀的话务员，负责总结对话内容。
任务要求：
1、对客户反馈的主要内容进行描述，忽略次要或与主要内容无关的内容。
2、描述客户期待得到什么样的结果。
3、以一段话的方式生成总结。

对话内容如下：
{}

生成格式如下：
群众来电：'''

class Item(BaseModel):
    text: str

# 定义输入格式
class Input(BaseModel):
    data: List[Item]
    

# 定义路由和处理函数
@app.post("/predict/summary")
async def create_item(request: Input):
    try:
        results = []
        for i in request.data:
            text = i.text
            text = prompt.format(text)
            result = get_model_output(text)
            result = result.replace('\n', '')
            logger.info("大模型提取摘要为: {}".format(result))
            results.append(result)
    
        answer = {
            "data": [
                {
                "summary": results
                }
            ],
            "success": "true"

        }

    except Exception as e:
        logger.error("提取摘要出错: {}".format(e))
        answer = {
            "data": [
                {
                "summary": "提取摘要出错"
                }
            ],
            "success": "false"

        }
    
    return answer

# 运行Uvicorn服务器
if __name__ == '__main__':
    logger = get_logger('conversation_summary_api')
    uvicorn.run(app, host=config['host'], port=int(config['conversation_summary_api']), workers=config['workers'])
