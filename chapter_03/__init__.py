from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_deepseek import ChatDeepSeek

# 必须加载环境变量
load_dotenv()

def run():
    model = ChatDeepSeek(model="deepseek-v4-pro")
    messages = [
        HumanMessage(content="你是什么模型，你能做什么？")
    ]
    result = model.invoke(messages)
    print(result.content)

if __name__ == "__main__":
    run()