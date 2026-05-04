from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_redis import RedisChatMessageHistory

# 必须加载环境变量
load_dotenv()

def run():
    history = RedisChatMessageHistory(session_id="test",redis_url="redis://localhost:6379/0")
    # 第一轮
    history.add_user_message("简单你是谁，15字")
    model = ChatOpenAI(
        model="doubao-seed-2.0-pro",
        base_url="https://ark.cn-beijing.volces.com/api/coding/v3")
    ai_message = model.invoke(history.messages)
    print(ai_message.content)
    history.add_message(ai_message)

    # 第二轮
    history.add_user_message("请详细介绍下")
    ai_message_2 = model.invoke(history.messages)
    print("\n")
    print(ai_message_2.content)
    history.add_message(ai_message_2)


if __name__ == "__main__":
    run()