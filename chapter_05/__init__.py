from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# 必须加载环境变量
load_dotenv()

def run():
    model = ChatOpenAI(model="doubao-seed-2.0-pro",
                       base_url="https://ark.cn-beijing.volces.com/api/coding/v3")
    messages = [
        SystemMessage(content="你是一个中英翻译助手，帮助用户将中文翻译成英文，或者将英文翻译成中文。"),
        HumanMessage(content="how are you?"),
    ]
    # result = model.invoke(messages)
    # print(result.content)
    # 流失输出
    stream = model.stream(messages)
    for chunk in stream:
        print(chunk.text, end="\n")

if __name__ == "__main__":
    run()