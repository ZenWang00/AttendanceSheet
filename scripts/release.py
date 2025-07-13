#!/usr/bin/env python3
"""
版本发布脚本

用于创建新版本标签和触发CI构建
"""

import subprocess
import sys
import re
import os

def run_command(cmd, description=""):
    """运行命令并显示结果"""
    if description:
        print(f"\n{description}")
    print(f"执行: {cmd}")
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.stdout:
            print("输出:", result.stdout)
        if result.stderr:
            print("错误:", result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"执行失败: {e}")
        return False

def get_current_version():
    """获取当前版本号"""
    # 从git标签中获取最新版本
    result = subprocess.run("git tag --sort=-version:refname | head -1", 
                          shell=True, capture_output=True, text=True)
    if result.returncode == 0 and result.stdout.strip():
        return result.stdout.strip()
    return "v0.0.0"

def increment_version(version, increment_type):
    """增加版本号"""
    # 移除v前缀
    version = version.lstrip('v')
    parts = version.split('.')
    
    if len(parts) != 3:
        print("错误：版本号格式不正确，应为 x.y.z")
        return None
    
    major, minor, patch = map(int, parts)
    
    if increment_type == 'major':
        major += 1
        minor = 0
        patch = 0
    elif increment_type == 'minor':
        minor += 1
        patch = 0
    elif increment_type == 'patch':
        patch += 1
    else:
        print("错误：增量类型必须是 major, minor, 或 patch")
        return None
    
    return f"v{major}.{minor}.{patch}"

def create_release(version, message=""):
    """创建发布"""
    print(f"\n创建版本 {version}")
    
    # 检查是否有未提交的更改
    if not run_command("git diff --quiet", "检查工作目录状态"):
        print("WARNING 警告：有未提交的更改")
        response = input("是否继续？(y/N): ")
        if response.lower() != 'y':
            return False
    
    # 创建标签
    tag_message = f"Release {version}\n\n{message}" if message else f"Release {version}"
    if not run_command(f'git tag -a {version} -m "{tag_message}"', "创建版本标签"):
        return False
    
    # 推送标签
    if not run_command(f"git push origin {version}", "推送标签到远程仓库"):
        return False
    
    print(f"\nSUCCESS 版本 {version} 创建成功！")
    print("CI将自动构建Windows exe文件")
    return True

def main():
    """主函数"""
    print("考勤统计表生成工具 - 版本发布脚本")
    print("="*50)
    
    if len(sys.argv) < 2:
        print("使用方法:")
        print("  python scripts/release.py major   # 主版本更新")
        print("  python scripts/release.py minor   # 次版本更新")
        print("  python scripts/release.py patch   # 补丁版本更新")
        print("  python scripts/release.py custom <version>  # 自定义版本")
        return
    
    increment_type = sys.argv[1]
    
    if increment_type == "custom":
        if len(sys.argv) < 3:
            print("错误：自定义版本需要指定版本号")
            return
        new_version = sys.argv[2]
        if not new_version.startswith('v'):
            new_version = f"v{new_version}"
    else:
        current_version = get_current_version()
        print(f"当前版本: {current_version}")
        
        new_version = increment_version(current_version, increment_type)
        if not new_version:
            return
    
    print(f"新版本: {new_version}")
    
    # 获取发布说明
    message = input("发布说明 (可选): ")
    
    # 创建发布
    if create_release(new_version, message):
        print(f"\nSUCCESS 发布 {new_version} 成功！")
        print("请等待几分钟，CI将自动构建exe文件")
        print("完成后可在GitHub Releases页面下载")

if __name__ == "__main__":
    main() 