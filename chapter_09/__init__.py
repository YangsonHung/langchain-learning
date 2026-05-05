from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_core.tools import StructuredTool


def get_weather_tool(city: str) -> str:
    return f"城市{city}，今天的天气不错"


weatherTool = StructuredTool.from_function(
    func=get_weather_tool, description="获取某个城市的天气", name="get_weather_tool"
)


@tool("get_today_date_v2", description="获取今天是几月几号")
def get_today_date() -> str:
    """获取今天是几月几号"""
    from datetime import date

    return date.today().strftime("%Y年%m月%d日")


# 必须加载环境变量
load_dotenv()


def run():
    model = ChatOpenAI(
        model="glm-5.1", base_url="https://ark.cn-beijing.volces.com/api/coding/v3"
    )

    tools_map = {
        "get_today_date_v2": get_today_date,
        "get_weather_tool": weatherTool,
    }
    model_with_tools = model.bind_tools([get_today_date, weatherTool])

    response = model_with_tools.invoke("北京天气怎么样")

    messages = [{"role": "user", "content": "北京天气怎么样"}]
    while response.tool_calls:
        messages.append(response)
        for tool_call in response.tool_calls:
            print(f"Tool: {tool_call['name']}")
            print(f"Args: {tool_call['args']}")
            result = tools_map[tool_call["name"]].invoke(tool_call["args"])
            print(f"Result: {result}")

            from langchain_core.messages import ToolMessage

            tool_msg = ToolMessage(content=result, tool_call_id=tool_call["id"])
            messages.append(tool_msg)

        response = model_with_tools.invoke(messages)

    print(response.content)


if __name__ == "__main__":
    run()
