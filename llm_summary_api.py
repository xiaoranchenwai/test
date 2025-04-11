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

# 大模型提示词
prompt = '''
任务目标：对用户输入的内容进行总结
任务要求：
1、输出一段总结，不要换行或者分段
2、输出内容为反映什么位置存在什么问题，有什么后果，已移交哪个部门处理
3、若内容包含处理进展信息，则回答进展如何，否则，不要输出和处理进展相关的内容

内容如下：
##################
ADDRESS：
{}
##################
CONTENT_DESC：
{}
##################
UNDERTAKE_DEPT_NAME：
{}
##################
UNDERTAKE_OPINION：
{}
##################
REPLY_OPINION：
{}
##################
'''

# 定义输入格式
class Item(BaseModel):
    address: str
    content_desc: str
    undertake_dept_name: str
    undertake_opinion: str
    reply_opinion: str

# 定义输入格式
class Input(BaseModel):
    data: List[Item]
    

# 定义路由和处理函数
@app.post("/predict/summary")
async def create_item(request: Input):
    try:
        results = []
        for i in request.data:
            address = i.address
            content_desc = i.content_desc
            undertake_dept_name = i.undertake_dept_name
            undertake_opinion = i.undertake_opinion
            reply_opinion = i.reply_opinion
            
            text = prompt.format(address, content_desc, undertake_dept_name, undertake_opinion, reply_opinion)
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
    logger = get_logger('llm_summary_api')
    uvicorn.run(app, host=config['host'], port=int(config['llm_summary_port']), workers=config['workers'])
