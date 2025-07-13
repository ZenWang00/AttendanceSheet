#!/usr/bin/env python3
"""
考勤统计表生成工具 - 使用示例

这个脚本展示了如何使用考勤统计表生成工具的各种功能。
"""

import subprocess
import sys
import os

def run_command(cmd, description):
    """运行命令并显示结果"""
    print(f"\n{'='*50}")
    print(f"执行: {description}")
    print(f"命令: {cmd}")
    print('='*50)
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print("输出:")
        print(result.stdout)
        if result.stderr:
            print("错误:")
            print(result.stderr)
        print(f"返回码: {result.returncode}")
        return result.returncode == 0
    except Exception as e:
        print(f"执行失败: {e}")
        return False

def main():
    """主函数 - 演示各种使用方法"""
    print("考勤统计表生成工具 - 使用示例")
    print("="*50)
    
    # 检查主脚本是否存在
    if not os.path.exists("create_new_attendance_sheet.py"):
        print("错误: 找不到 create_new_attendance_sheet.py 文件")
        return
    
    # 示例1: 显示帮助信息
    run_command("python create_new_attendance_sheet.py --help", 
                "显示帮助信息")
    
    # 示例2: 运行测试
    run_command("python create_new_attendance_sheet.py --test", 
                "运行时间计算测试")
    
    # 示例3: 检查数据源文件
    data_files = [f for f in os.listdir('.') if f.startswith('考勤表-上下班工时统计表') and f.endswith('.xlsx')]
    if data_files:
        print(f"\n找到数据源文件: {data_files[0]}")
        
        # 示例4: 基本使用（自动查找数据源）
        run_command("python create_new_attendance_sheet.py", 
                    "基本使用 - 自动查找数据源文件")
        
        # 示例5: 指定输出文件
        run_command(f"python create_new_attendance_sheet.py --output '示例输出.xlsx'", 
                    "指定输出文件名")
        
    else:
        print("\n未找到数据源文件，跳过实际处理示例")
        print("请确保当前目录下有符合格式的数据源文件：")
        print("考勤表-上下班工时统计表YYYY年M月.xlsx")
    
    print("\n" + "="*50)
    print("示例演示完成！")
    print("更多使用方法请参考 README.md 文件")

if __name__ == "__main__":
    main() 