# /// script
# dependencies = [
#     "fastmcp>=3.0.2",
# ]
#
# ///
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def weather(city: str) -> str:
    return f"The weather in {city} is sunny with a high of 25°C"

@mcp.prompt()
def weather_in_city(city_name: str) -> str:
    return f"How is the weather in {city_name}?"

if __name__ == "__main__":
    mcp.run()
