# 工单摘要提取算法

## 1、安装依赖

pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

## 2、启动服务

启动服务前，需要修改配置文件中的base_url和model_name，确保大模型服务可用
base_url为符合openai接口规范的大模型服务的地址，model_name为对应的模型名字

启动服务命令：

1、启动工单摘要服务：
python llm_summary_api.py

2、启动对话总结服务：
python conversation_summary_api.py

## 3、参数配置

配置文件在config/config.yaml中，可配置服务的端口号、大模型的服务地址和模型名

## 4、docker环境启动

打包镜像：

docker build -t llm_summary .

启动服务：

sudo docker run -itd -p 5020:5020 -p 5021:5021 -v ./summary_extract:/summary_extract --name llm_summary llm_summary

进入docker容器：

sudo docker exec -it llm_summary /bin/bash

启动工单摘要服务：

python llm_summary_api.py

启动对话总结服务：

python conversation_summary_api.py

## 相关文档

接口文档：

工单摘要接口文档：
https://alidocs.dingtalk.com/i/nodes/gvNG4YZ7JneM3nBvc2RE7w3nV2LD0oRE?utm_scene=team_space

对话总结接口文档：
https://alidocs.dingtalk.com/i/nodes/XPwkYGxZV3RX2GjkTqXXvn9zWAgozOKL?utm_scene=team_space

模型部署及运维文档：
https://alidocs.dingtalk.com/i/nodes/lyQod3RxJK3moqXKinPAjdDOJkb4Mw9r?utm_scene=team_space