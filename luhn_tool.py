"""
================================================================
项目名称：Luhn 算法生成器 (Luhn Algorithm Generator)
用途说明：本项目仅用于【算法学习】、【数学逻辑演示】及【开发测试】。
法律提示：严禁将生成的号码用于任何非法欺诈、撞库或绕过付费系统的行为。
          开发者不对任何第三方的违法行为承担法律责任。
================================================================
"""

import random

def generate_luhn_number(bin_prefix="411111"):
    """
    根据给定的前缀（BIN）生成一个符合 Luhn 算法的 16 位测试号码。
    """
    # 1. 填充随机数直到 15 位
    digits = [int(d) for d in str(bin_prefix)]
    while len(digits) < 15:
        digits.append(random.randint(0, 9))
    
    # 2. 计算校验位 (Luhn 算法核心逻辑)
    payload = digits[:]
    checksum = 0
    
    # 从右向左，偶数位数字乘以 2
    for i, count in enumerate(reversed(payload)):
        if i % 2 == 0: 
            doubled = count * 2
            if doubled > 9:
                doubled -= 9
            checksum += doubled
        else:
            checksum += count
            
    # 3. 计算出第 16 位校验码，使总和能被 10 整除
    check_digit = (10 - (checksum % 10)) % 10
    digits.append(check_digit)
    
    return "".join(map(str, digits))

# --- 程序执行入口 ---
if __name__ == "__main__":
    print("\n" + "="*50)
    print("   Luhn 算法本地生成工具 (仅供本地开发测试)   ")
    print("="*50)
    
    # 你可以修改这里的 test_bin 为你想要测试的 6 位前缀
    test_bin = "411111" 
    
    print(f"正在基于前缀 {test_bin} 生成测试数据...\n")
    
    # 演示生成 5 个号码并打印
    for i in range(5):
        result = generate_luhn_number(test_bin)
        print(f"测试号码 {i+1}: {result}")
        
    print("\n" + "="*50)
    print("提示：生成的号码无真实资金关联，仅具有数学校验性。")
    print("="*50 + "\n")
