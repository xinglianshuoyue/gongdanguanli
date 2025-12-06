import sys
import os
import openpyxl

# 1. 获取传入的三个参数（A列, B列, C列）
# 如果没有传参，防止报错给个默认空值
col_a = sys.argv[1] if len(sys.argv) > 1 else ""
col_b = sys.argv[2] if len(sys.argv) > 2 else ""
col_c = sys.argv[3] if len(sys.argv) > 3 else ""

file_path = 'data.xlsx'

print(f"准备写入内容: [{col_a}, {col_b}, {col_c}]")

# 2. 加载或新建 Excel 文件
if not os.path.exists(file_path):
    print("文件不存在，新建文件...")
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Column A", "Column B", "Column C"]) 
else:
    print("加载现有文件...")
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active

# 3. 追加一行内容
ws.append([col_a, col_b, col_c])

# 4. 保存文件
wb.save(file_path)
print("写入成功，保存完毕。")
