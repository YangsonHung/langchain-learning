from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# 必须加载环境变量
load_dotenv()

def run():
    # 使用 ChatOpenAI 来调用 deepseek-v4-pro 模型
    model = ChatOpenAI(model="deepseek-v4-pro", base_url="https://api.deepseek.com")
    messages = [
        SystemMessage(content="帮我翻译成中文"),
        HumanMessage(content="how are you?"),
    ]
    result = model.invoke(messages)
    print(result.content)

if __name__ == "__main__":
    run()