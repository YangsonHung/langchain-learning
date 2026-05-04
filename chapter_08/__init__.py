from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_redis import RedisChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# 必须加载环境变量
load_dotenv()

def run():
    prompt_template = ChatPromptTemplate.from_messages([
        ("user", "{text}")
    ])
    history = RedisChatMessageHistory(session_id="test", redis_url="redis://localhost:6379/0")
    model = ChatOpenAI(
        model="doubao-seed-2.0-pro",
        base_url="https://ark.cn-beijing.volces.com/api/coding/v3")
    parser = StrOutputParser()

    chain = prompt_template | model | parser

    runnable = RunnableWithMessageHistory(chain, get_session_history=lambda: history)

    # history.clear()

    runnable.invoke({"text": "用一个案例说明三者的语法区别"})


if __name__ == "__main__":
    run()