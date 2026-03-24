def add(a, b):
    return a + b

# 新加这几行，让它能互动
if __name__ == "__main__":
    x = 10
    y = 5
    print(f"你好！我是你的计算器：{x} + {y} 的结果是 {add(x, y)}")
