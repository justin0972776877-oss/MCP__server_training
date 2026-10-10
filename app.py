from fastmcp import FastMCP
app=FastMCP("MY MCP Server")
#提供一個加法的工具
@app.tool
#@ 是裝飾器語法，它的意思是「把下面這個函式交給 app.tool 處理」
def add(n1: int, n2: int) -> int:
    """加法工具"""
    return n1 + n2


