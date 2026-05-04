from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 必须加载环境变量
load_dotenv()

def run():
    model = ChatOpenAI(model="doubao-seed-2.0-pro", base_url="https://ark.cn-beijing.volces.com/api/coding/v3")
    parser = StrOutputParser()

    # message = model.invoke("写一手对子")
    # content = parser.invoke(message)
    # print(content)


    stream = model.stream("写一副春联")
    for chunk in parser.transform(stream):
        print(chunk, end="", flush=True)


if __name__ == "__main__":
    run()