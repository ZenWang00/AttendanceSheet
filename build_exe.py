#!/usr/bin/env python3
"""
考勤统计表生成工具 - exe打包脚本

这个脚本用于将Python程序打包成Windows可执行文件。
"""

import subprocess
import sys
import os
import shutil

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

def check_dependencies():
    """检查依赖包"""
    print("检查依赖包...")
    
    # 检查PyInstaller
    try:
        import PyInstaller
        print("✓ PyInstaller 已安装")
    except ImportError:
        print("✗ PyInstaller 未安装，正在安装...")
        if not run_command("pip install pyinstaller", "安装PyInstaller"):
            print("安装PyInstaller失败！")
            return False
    
    # 检查主程序文件
    if not os.path.exists("create_new_attendance_sheet.py"):
        print("✗ 找不到主程序文件 create_new_attendance_sheet.py")
        return False
    
    print("✓ 主程序文件存在")
    return True

def build_exe():
    """构建可执行文件"""
    print("\n开始构建可执行文件...")
    
    # 检测操作系统
    import platform
    system = platform.system()
    print(f"当前操作系统: {system}")
    
    if system == "Windows":
        exe_name = "考勤统计表生成工具.exe"
        exe_path = f"dist/{exe_name}"
    elif system == "Darwin":  # macOS
        exe_name = "考勤统计表生成工具"
        exe_path = f"dist/{exe_name}"
        print("⚠️  注意：在macOS上构建的是macOS可执行文件，不是Windows exe文件")
        print("   要在Windows上运行，请在Windows系统上重新构建")
    else:  # Linux
        exe_name = "考勤统计表生成工具"
        exe_path = f"dist/{exe_name}"
        print("⚠️  注意：在Linux上构建的是Linux可执行文件，不是Windows exe文件")
        print("   要在Windows上运行，请在Windows系统上重新构建")
    
    # 清理之前的构建文件
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    if os.path.exists("build"):
        shutil.rmtree("build")
    if os.path.exists(f"{exe_name}.spec"):
        os.remove(f"{exe_name}.spec")
    
    # 构建可执行文件
    cmd = f'pyinstaller --onefile --name "{exe_name}" --clean create_new_attendance_sheet.py'
    if not run_command(cmd, "构建可执行文件"):
        print("构建失败！")
        return False
    
    # 检查生成的文件
    if os.path.exists(exe_path):
        print(f"\n✅ 构建成功！可执行文件位置: {exe_path}")
        
        # 显示文件大小
        size = os.path.getsize(exe_path)
        size_mb = size / (1024 * 1024)
        print(f"文件大小: {size_mb:.1f} MB")
        
        return True
    else:
        print(f"✗ 构建失败，未找到生成的可执行文件: {exe_path}")
        return False

def create_release_package():
    """创建发布包"""
    print("\n创建发布包...")
    
    # 检测操作系统
    import platform
    system = platform.system()
    
    if system == "Windows":
        exe_name = "考勤统计表生成工具.exe"
    elif system == "Darwin":  # macOS
        exe_name = "考勤统计表生成工具"
    else:  # Linux
        exe_name = "考勤统计表生成工具"
    
    # 创建发布目录
    release_dir = "release"
    if os.path.exists(release_dir):
        shutil.rmtree(release_dir)
    os.makedirs(release_dir)
    
    # 复制可执行文件
    exe_source = f"dist/{exe_name}"
    exe_dest = f"{release_dir}/{exe_name}"
    
    if os.path.exists(exe_source):
        shutil.copy2(exe_source, exe_dest)
        print(f"✓ 复制可执行文件到: {exe_dest}")
    else:
        print(f"✗ 找不到可执行文件: {exe_source}")
        return False
    
    # 复制README文件
    if os.path.exists("README.md"):
        shutil.copy2("README.md", f"{release_dir}/README.md")
        print("✓ 复制README文件")
    
    # 复制示例数据源文件（如果存在）
    data_files = [f for f in os.listdir('.') if f.startswith('考勤表-上下班工时统计表') and f.endswith('.xlsx')]
    if data_files:
        shutil.copy2(data_files[0], f"{release_dir}/{data_files[0]}")
        print(f"✓ 复制示例数据源文件: {data_files[0]}")
    
    print(f"\n✅ 发布包创建完成！位置: {release_dir}/")
    return True

def main():
    """主函数"""
    print("考勤统计表生成工具 - exe打包脚本")
    print("="*50)
    
    # 检查依赖
    if not check_dependencies():
        print("\n❌ 依赖检查失败，无法继续构建")
        return
    
    # 构建exe文件
    if not build_exe():
        print("\n❌ 构建失败")
        return
    
    # 创建发布包
    if not create_release_package():
        print("\n❌ 创建发布包失败")
        return
    
    print("\n" + "="*50)
    print("🎉 构建完成！")
    
    # 检测操作系统
    import platform
    system = platform.system()
    
    if system == "Windows":
        print("\n发布包包含:")
        print("- 考勤统计表生成工具.exe (Windows可执行文件)")
        print("- README.md (使用说明)")
        print("- 示例数据源文件 (如果存在)")
        print("\n使用方法:")
        print("1. 将exe文件和数据源文件放在同一目录")
        print("2. 双击exe文件或通过命令行运行")
        print("3. 查看README.md了解详细使用方法")
    else:
        print(f"\n⚠️  注意：当前在{system}系统上构建，生成的是{system}可执行文件")
        print("要在Windows上运行，请在Windows系统上重新构建")
        print("\n发布包包含:")
        print(f"- 考勤统计表生成工具 ({system}可执行文件)")
        print("- README.md (使用说明)")
        print("- 示例数据源文件 (如果存在)")

if __name__ == "__main__":
    main() 