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
    print(f"Executing: {description}")
    # Don't print command with Chinese characters to avoid encoding issues
    print('='*50)
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print("Output:")
        print(result.stdout)
        if result.stderr:
            print("Error:")
            print(result.stderr)
        print(f"Return code: {result.returncode}")
        return result.returncode == 0
    except Exception as e:
        print(f"Execution failed: {e}")
        return False

def check_dependencies():
    """检查依赖包"""
    print("Checking dependencies...")
    
    # 检查PyInstaller
    try:
        import PyInstaller
        print("OK PyInstaller installed")
    except ImportError:
        print("FAIL PyInstaller not installed, installing...")
        if not run_command("pip install pyinstaller", "Install PyInstaller"):
            print("Failed to install PyInstaller!")
            return False
    
    # 检查主程序文件
    if not os.path.exists("create_new_attendance_sheet.py"):
        print("FAIL Main program file not found: create_new_attendance_sheet.py")
        return False
    
    print("OK Main program file exists")
    return True

def build_exe():
    """构建可执行文件"""
    print("\nStarting executable build...")
    
    # 检测操作系统
    import platform
    system = platform.system()
    print(f"Current OS: {system}")
    
    if system == "Windows":
        exe_name = "AttendanceSheetTool.exe"
        exe_path = f"dist/{exe_name}"
    elif system == "Darwin":  # macOS
        exe_name = "AttendanceSheetTool"
        exe_path = f"dist/{exe_name}"
        print("Note: Building on macOS, generating macOS executable")
        print("To run on Windows, rebuild on Windows system")
    else:  # Linux
        exe_name = "AttendanceSheetTool"
        exe_path = f"dist/{exe_name}"
        print("Note: Building on Linux, generating Linux executable")
        print("To run on Windows, rebuild on Windows system")
    
    # 清理之前的构建文件
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    if os.path.exists("build"):
        shutil.rmtree("build")
    if os.path.exists(f"{exe_name}.spec"):
        os.remove(f"{exe_name}.spec")
    
    # 构建可执行文件
    cmd = f'pyinstaller --onefile --name "{exe_name}" --clean create_new_attendance_sheet.py'
    if not run_command(cmd, "Build executable"):
        print("Build failed!")
        return False
    
    # 检查生成的文件
    if os.path.exists(exe_path):
        print(f"\nSUCCESS Build successful! Executable location: {exe_path}")
        
        # 显示文件大小
        size = os.path.getsize(exe_path)
        size_mb = size / (1024 * 1024)
        print(f"File size: {size_mb:.1f} MB")
        
        return True
    else:
        print(f"FAIL Build failed, executable not found: {exe_path}")
        return False

def create_release_package():
    """创建发布包"""
    print("\nCreating release package...")
    
    # 检测操作系统
    import platform
    system = platform.system()
    
    if system == "Windows":
        exe_name = "AttendanceSheetTool.exe"
    elif system == "Darwin":  # macOS
        exe_name = "AttendanceSheetTool"
    else:  # Linux
        exe_name = "AttendanceSheetTool"
    
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
        print(f"OK Copied executable to: {exe_dest}")
    else:
        print(f"FAIL Executable not found: {exe_source}")
        return False
    
    # 复制README文件
    if os.path.exists("README.md"):
        shutil.copy2("README.md", f"{release_dir}/README.md")
        print("OK Copied README file")
    
    # 复制示例数据源文件（如果存在）
    data_files = [f for f in os.listdir('.') if f.startswith('考勤表-上下班工时统计表') and f.endswith('.xlsx')]
    if data_files:
        # Use English filename for release package
        shutil.copy2(data_files[0], f"{release_dir}/sample_data.xlsx")
        print(f"OK Copied sample data file: sample_data.xlsx")
    
    print(f"\nSUCCESS Release package created! Location: {release_dir}/")
    return True

def main():
    """主函数"""
    print("Attendance Sheet Tool - exe build script")
    print("="*50)
    
    # 检查依赖
    if not check_dependencies():
        print("\nERROR Dependency check failed, cannot continue build")
        return
    
    # 构建exe文件
    if not build_exe():
        print("\nERROR Build failed")
        return
    
    # 创建发布包
    if not create_release_package():
        print("\nERROR Failed to create release package")
        return
    
    print("\n" + "="*50)
    print("Build completed!")
    
    # 检测操作系统
    import platform
    system = platform.system()
    
    if system == "Windows":
        print("\nRelease package contains:")
        print("- AttendanceSheetTool.exe (Windows executable)")
        print("- README.md (usage instructions)")
        print("- Sample data source files (if exist)")
        print("\nUsage:")
        print("1. Place exe file and data source files in the same directory")
        print("2. Double-click exe file or run via command line")
        print("3. Check README.md for detailed usage")
    else:
        print(f"\nNote: Building on {system} system, generating {system} executable")
        print("To run on Windows, rebuild on Windows system")
        print("\nRelease package contains:")
        print(f"- AttendanceSheetTool ({system} executable)")
        print("- README.md (usage instructions)")
        print("- Sample data source files (if exist)")

if __name__ == "__main__":
    main() 