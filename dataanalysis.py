import re
import numpy as np
import matplotlib.pyplot as plt

# X射线衍射图谱数据分析
def XRDAnalysis(filePath: str) -> None:
    # 打开文件并将内容读入content
    with open(filePath, 'r') as txt:
        content = txt.readlines()
        txt.close()
    
    invar, devar = [], []   # 自变量和因变量

    timeMarker = content[0]
    time = re.findall(r"(\d+)\/(\d+)\/(\d+)\s(\d+)\:(\d+)\:(\d+)", timeMarker)
    print(time)

    # 遍历每一行，读取行中信息，并筛选出有用的信息对
    for line in content:
        # 正则表达式匹配
        # 这里的正则表达式可以筛选掉分析机器自动生成的特征标识码而只获取数据对
        isMatch = re.match(r"([+-]?\d+\.\d+|\d+)\s\s([+-]?\d+\.\d+|\d+)", line)   
        if isMatch:
            x, y = list(map(float, line.split()))
            invar.append(x)
            devar.append(y)
        else:
            continue

    plt.plot(invar, devar)
    plt.xlabel("2 Theta (degree)")
    plt.ylabel("Intensity (a.u.)")
    plt.title("XRD Analysis")
    plt.show()

# 测试用，正常情况下模块不会作为主模块被调用
if __name__ == "__main__":
    XRDAnalysis("E:/QQFiles/Tencent Files/1729820749/FileRecv/Z1.txt")
