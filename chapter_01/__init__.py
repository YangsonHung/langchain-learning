from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

# 必须加载环境变量
load_dotenv()

def run():
    model = init_chat_model("deepseek-v4-pro", base_url="https://api.deepseek.com")
    messages = [
        SystemMessage(content="帮我翻译成中文"),
        HumanMessage(content="what can I do for you?"),
    ]
    result = model.invoke(messages)
    print(result.content)

if __name__ == "__main__":
    run()