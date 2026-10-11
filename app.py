from fastmcp import FastMCP
import matplotlib.pyplot as plt
import io
from fastmcp.utilities.types import Image
app=FastMCP("MY MCP Server")
#提供一個加法的工具
@app.tool
#@ 是裝飾器語法，它的意思是「把下面這個函式交給 app.tool 處理」 靠速人家要提供工具
def add(n1: int, n2: int) -> int:
    """加法工具"""
    return n1 + n2
#提供一個繪製圓餅圖的工具
@app.tool
def draw_pie_chart(numbers:list[int])->Image:
    """繪製圓餅圖工具"""
    plt.pie(numbers)
    buffer=io.BytesIO() #savefig() 就是規定「你要給我一個地方寫進去」
    #io.BytesIO() 就是騙過它：給它一個長得像檔案、其實在記憶體裡的容器
    plt.savefig(buffer,format="png")
    return Image(data=buffer.getvalue(), format="png")