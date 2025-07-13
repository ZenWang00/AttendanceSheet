# 考勤统计表生成工具

这是一个用于生成员工考勤统计表的Python工具，可以自动处理打卡数据并生成格式化的Excel考勤表。

## 功能特性

- ✅ **自动数据源检测**：自动查找符合命名规范的数据源文件
- ✅ **智能时间计算**：支持同一天和跨天工作时长计算
- ✅ **闰年处理**：正确处理闰年2月的29天
- ✅ **数据缺失处理**：自动标记缺失的打卡数据
- ✅ **命令行支持**：支持多种命令行参数
- ✅ **测试功能**：内置时间计算逻辑测试

## 系统要求

- **Python版本**：Python 3.7+（仅开发环境需要）
- **运行环境**：Windows/macOS/Linux
- **exe版本**：仅支持Windows系统

## 安装方式

### 方式一：使用exe文件（推荐）

1. 下载最新版本的exe文件
2. 将exe文件放在包含数据源文件的目录中
3. 直接运行exe文件

### 方式二：使用Python脚本

```bash
# 安装依赖
pip install -r requirements.txt
```

## 数据源文件格式

### 文件命名规范
数据源文件必须按照以下格式命名：
```
考勤表-上下班工时统计表YYYY年M月.xlsx
```

例如：
- `考勤表-上下班工时统计表2025年6月.xlsx`
- `考勤表-上下班工时统计表2024年2月.xlsx`

### Excel文件结构
数据源Excel文件需要包含以下工作表：

1. **考勤统计** 工作表
   - 包含员工姓名和岗位信息
   - 表头在第5-6行

2. **打卡时间** 工作表
   - 包含每日打卡时间数据
   - 表头在第2-3行
   - 列格式：`('打卡时间', '1')`, `('打卡时间', '2')` 等

## 使用方法

### 基本用法

#### 使用exe文件（推荐）
```bash
# 自动查找数据源文件并生成考勤表
考勤统计表生成工具.exe

# 或者双击exe文件直接运行
```

#### 使用Python脚本
```bash
# 自动查找数据源文件并生成考勤表
python create_new_attendance_sheet.py
```

### 高级用法

#### 使用exe文件
```bash
# 指定数据源文件
考勤统计表生成工具.exe --input "考勤表-上下班工时统计表2025年6月.xlsx"

# 指定输出文件名
考勤统计表生成工具.exe --output "我的考勤表.xlsx"

# 指定年份和月份
考勤统计表生成工具.exe --year 2025 --month 6

# 运行测试用例
考勤统计表生成工具.exe --test

# 查看帮助信息
考勤统计表生成工具.exe --help
```

#### 使用Python脚本
```bash
# 指定数据源文件
python create_new_attendance_sheet.py --input "考勤表-上下班工时统计表2025年6月.xlsx"

# 指定输出文件名
python create_new_attendance_sheet.py --output "我的考勤表.xlsx"

# 指定年份和月份
python create_new_attendance_sheet.py --year 2025 --month 6

# 运行测试用例
python create_new_attendance_sheet.py --test

# 查看帮助信息
python create_new_attendance_sheet.py --help
```

### 命令行参数说明

| 参数 | 简写 | 说明 | 示例 |
|------|------|------|------|
| `--input` | `-i` | 数据源文件名（可选） | `--input "data.xlsx"` |
| `--output` | `-o` | 输出文件名（可选） | `--output "result.xlsx"` |
| `--year` | `-y` | 指定年份（可选） | `--year 2025` |
| `--month` | `-m` | 指定月份（可选） | `--month 6` |
| `--test` | `-t` | 运行测试用例 | `--test` |
| `--help` | `-h` | 显示帮助信息 | `--help` |

## 输出文件格式

生成的考勤统计表包含以下内容：

### 表头信息
- 标题：考勤表-上下班工时统计表
- 公司名称：武汉福福数通网络科技有限公司
- 时间段：显示具体的年月范围

### 数据列结构
- **员工姓名**：合并单元格显示员工姓名
- **岗位**：合并单元格显示岗位信息
- **每日数据**：每天两列
  - 签到签退列：显示签到和签退时间
  - 工作时长列：合并单元格显示当日工作时长
- **统计列**：
  - 累计时长：合并单元格显示总工作时长
  - 休息天数：显示休息天数
  - 备注：备注信息

### 时间计算逻辑

#### 同一天工作
- 签到时间 < 签退时间
- 计算公式：签退时间 - 签到时间
- 示例：08:30签到，18:30签退 → 10小时

#### 跨天工作
- 签到时间 > 签退时间
- 计算公式：(24:00 - 签到时间) + 签退时间
- 示例：22:00签到，06:00签退 → (24-22) + 6 = 8小时

## 使用示例

### 示例1：基本使用

#### 使用exe文件
```bash
# 将数据源文件放在exe文件同目录
# 双击运行或命令行执行
考勤统计表生成工具.exe

# 输出：2025年6月员工考勤统计表.xlsx
```

#### 使用Python脚本
```bash
# 将数据源文件放在当前目录
# 运行脚本
python create_new_attendance_sheet.py

# 输出：2025年6月员工考勤统计表.xlsx
```

### 示例2：指定参数

#### 使用exe文件
```bash
# 指定数据源和输出文件
考勤统计表生成工具.exe \
  --input "考勤表-上下班工时统计表2025年6月.xlsx" \
  --output "我的考勤表.xlsx"
```

#### 使用Python脚本
```bash
# 指定数据源和输出文件
python create_new_attendance_sheet.py \
  --input "考勤表-上下班工时统计表2025年6月.xlsx" \
  --output "我的考勤表.xlsx"
```

### 示例3：指定年月

#### 使用exe文件
```bash
# 手动指定年月（适用于文件名不符合规范的情况）
考勤统计表生成工具.exe \
  --year 2025 \
  --month 6 \
  --input "my_data.xlsx"
```

#### 使用Python脚本
```bash
# 手动指定年月（适用于文件名不符合规范的情况）
python create_new_attendance_sheet.py \
  --year 2025 \
  --month 6 \
  --input "my_data.xlsx"
```

## 错误处理

### 常见错误及解决方案

1. **找不到数据源文件**
   ```
   错误：未找到数据源文件！
   解决方案：确保文件名符合格式：考勤表-上下班工时统计表YYYY年M月.xlsx
   ```

2. **Excel文件读取失败**
   ```
   错误：读取Excel文件失败
   解决方案：检查Excel文件是否损坏，确保包含必要的"考勤统计"和"打卡时间"工作表
   ```

3. **参数错误**
   ```
   错误：月份必须在1-12之间
   解决方案：检查月份参数是否在有效范围内
   ```

## 测试功能

运行测试用例验证时间计算逻辑：

#### 使用exe文件
```bash
考勤统计表生成工具.exe --test
```

#### 使用Python脚本
```bash
python create_new_attendance_sheet.py --test
```

测试包括：
- 同一天正常工作时间
- 跨天夜班工作
- 边界情况处理
- 数据缺失情况

## 文件结构

### 开发版本
```
AttendanceSheet/
├── create_new_attendance_sheet.py  # 主程序
├── requirements.txt                 # 依赖包列表
├── README.md                       # 说明文档
├── example_usage.py                # 使用示例
├── 考勤表-上下班工时统计表2025年6月.xlsx  # 示例数据源
└── 2025年6月员工考勤统计表.xlsx         # 生成的输出文件
```

### 发布版本（exe）
```
发布目录/
├── 考勤统计表生成工具.exe              # 可执行文件
├── 考勤表-上下班工时统计表2025年6月.xlsx  # 数据源文件
└── 2025年6月员工考勤统计表.xlsx         # 生成的输出文件
```

## 依赖包

主要依赖包：
- `pandas`：数据处理
- `openpyxl`：Excel文件操作
- `numpy`：数值计算
- `argparse`：命令行参数解析

## exe版本使用说明

### 下载和安装
1. 从GitHub Releases页面下载最新版本的exe文件
2. 将exe文件放在包含数据源文件的目录中
3. 双击exe文件或通过命令行运行

### 注意事项
- exe文件仅支持Windows系统
- 确保数据源文件符合命名规范
- 如果遇到杀毒软件误报，请添加信任
- 建议将exe文件和数据源文件放在同一目录

### 常见问题
1. **exe文件无法运行**
   - 检查是否在Windows系统上运行
   - 确保有足够的权限
   - 尝试以管理员身份运行

2. **找不到数据源文件**
   - 确保数据源文件在exe文件同目录
   - 检查文件名是否符合规范

3. **输出文件无法生成**
   - 检查目录是否有写入权限
   - 确保磁盘空间充足

## 开发说明

### 代码结构
- `main()`：主函数，处理命令行参数
- `create_new_attendance_sheet()`：核心功能函数
- `calculate_work_hours()`：时间计算函数
- `test_time_calculation()`：测试函数
- `find_source_file()`：文件查找函数

### 扩展功能
如需添加新功能，可以：
1. 在 `create_new_attendance_sheet()` 中添加新的处理逻辑
2. 在 `main()` 中添加新的命令行参数
3. 在 `test_time_calculation()` 中添加新的测试用例

### 打包说明

#### 自动打包（推荐）
使用提供的打包脚本：
```bash
python build_exe.py
```

#### 手动打包
使用PyInstaller手动打包：
```bash
# 安装PyInstaller
pip install pyinstaller

# 打包为Windows exe文件（需要在Windows系统上执行）
pyinstaller --onefile --name "考勤统计表生成工具" create_new_attendance_sheet.py
```

#### 跨平台构建说明
- **Windows系统**：生成 `.exe` 文件，可直接在Windows上运行
- **macOS系统**：生成macOS可执行文件，不能直接在Windows上运行
- **Linux系统**：生成Linux可执行文件，不能直接在Windows上运行

**注意**：要在Windows上运行，必须在Windows系统上构建exe文件。

## 许可证

本项目仅供内部使用。

## 联系方式

如有问题或建议，请联系开发团队。 