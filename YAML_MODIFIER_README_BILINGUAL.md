# YAMLModifier - YOLOv7 YAML Configuration File Modifier Tool
# YAMLModifier - YOLOv7 YAML配置修改工具

---

## Features / 功能說明

This is a YAML modification tool for YOLOv7 configuration files that can:
這是一個用於YOLOv7配置檔案的YAML修改工具，可以：

- 📖 Read YAML configuration files / 讀取YAML配置檔案
- ✏️ Modify `nc` (number of classes) parameter / 修改`nc`（類別數）參數
- 💾 Save to specified location / 保存到指定位置

## Installation / 安裝依賴

```bash
pip install pyyaml ruamel.yaml
```

**Note / 注意:**
- `ruamel.yaml`: Used to preserve comments and formatting in YAML files / 用於保留YAML檔案中的註解和格式
- `pyyaml`: Fallback library for basic YAML operations / YAML基本操作的備用庫

---

## Usage / 使用方法

### 1. Command Line Usage / 命令列使用

#### Basic Usage - Modify and Overwrite Original File / 基礎用法 - 修改並覆蓋原檔案

```bash
python yaml_modifier.py -i cfg/training/yolov7-tiny.yaml -nc 10
```

#### Modify and Save to New Location / 修改並保存到新位置

```bash
python yaml_modifier.py -i cfg/training/yolov7-tiny.yaml -o cfg/training/yolov7-tiny-custom.yaml -nc 5
```

#### View Current nc Value Only (No Modification) / 僅查看當前nc值（不修改）

```bash
python yaml_modifier.py -i cfg/training/yolov7-tiny.yaml --get-nc
```

### 2. Using in Python Code / 在Python代碼中使用

#### Method 1: Complete Processing Workflow / 方法1: 完整處理流程

```python
from yaml_modifier import YAMLModifier

# Create modifier instance / 創建修改器實例
modifier = YAMLModifier(
    input_path='cfg/training/yolov7-tiny.yaml',
    output_path='cfg/training/yolov7-tiny-custom.yaml'
)

# Complete in one step: Read -> Modify -> Save / 一次性完成：讀取 -> 修改 -> 保存
modifier.process(new_nc=10)
```

#### Method 2: Step-by-Step Operation / 方法2: 逐步操作

```python
from yaml_modifier import YAMLModifier

modifier = YAMLModifier(
    input_path='cfg/training/yolov7-tiny.yaml',
    output_path='cfg/training/yolov7-tiny-custom.yaml'
)

# Step 1: Read file / 第1步：讀取檔案
config = modifier.read_yaml()

# Step 2: View current nc value / 第2步：查看當前nc值
current_nc = modifier.get_nc()
print(f"Current nc value / 當前nc值: {current_nc}")

# Step 3: Modify nc value / 第3步：修改nc值
modifier.modify_nc(new_nc=10)

# Step 4: Save file / 第4步：保存檔案
modifier.save_yaml()
```

#### Method 3: Overwrite Original File / 方法3: 覆蓋原檔案

```python
from yaml_modifier import YAMLModifier

# Do not specify output_path to overwrite original file / 不指定output_path則覆蓋原檔案
modifier = YAMLModifier(input_path='cfg/training/yolov7-tiny.yaml')
modifier.process(new_nc=15)
```

#### Method 4: Batch Modification / 方法4: 批量修改

```python
from yaml_modifier import YAMLModifier

config_files = [
    ('cfg/training/yolov7-tiny.yaml', 10),
    ('cfg/training/yolov7.yaml', 20),
    ('cfg/training/yolov7x.yaml', 5),
]

for input_file, nc_value in config_files:
    try:
        output_file = input_file.replace('.yaml', f'-{nc_value}classes.yaml')
        modifier = YAMLModifier(input_file, output_file)
        modifier.process(new_nc=nc_value)
        print(f"✓ {input_file} -> {output_file}")
    except Exception as e:
        print(f"✗ Processing failed / 處理失敗: {e}")
```

---

## API Documentation / API 文檔

### YAMLModifier Class / YAMLModifier 類

#### Initialization / 初始化

```python
YAMLModifier(input_path: str, output_path: Optional[str] = None)
```

- `input_path`: Path to input YAML file (required) / 輸入YAML檔案路徑（必需）
- `output_path`: Path to output YAML file (optional, default overwrites original file) / 輸出YAML檔案路徑（可選，預設覆蓋原檔案）

#### Methods / 方法

##### read_yaml()

Read YAML file / 讀取YAML檔案

```python
config = modifier.read_yaml()
# Returns / 返回: dict type configuration dictionary / dict 類型的配置字典
```

##### modify_nc(new_nc: int)

Modify nc parameter / 修改nc參數

```python
modifier.modify_nc(new_nc=10)
# Returns / 返回: True (success) / True（成功）
```

##### save_yaml()

Save modified YAML file / 保存修改後的YAML檔案

```python
modifier.save_yaml()
```

##### get_nc()

Get current nc value / 獲取當前的nc值

```python
current_nc = modifier.get_nc()
# Returns / 返回: int type number of classes / int 類型的類別數
```

##### process(new_nc: int)

Complete processing workflow (Read -> Modify -> Save) / 完整的處理流程（讀取 -> 修改 -> 保存）

```python
modifier.process(new_nc=10)
```

---

## Example Scripts / 範例腳本

See `yaml_modifier_examples.py` for more usage examples. / 查看 `yaml_modifier_examples.py` 獲取更多使用範例。

---

## Error Handling / 錯誤處理

The tool includes detailed error handling: / 工具包含詳細的錯誤處理：

- ✓ File existence check / 檔案存在檢查
- ✓ YAML parsing error capture / YAML解析錯誤捕獲
- ✓ nc parameter validation / nc參數驗證
- ✓ Automatic directory creation / 目錄自動創建

---

## FAQ / 常見問題

### Q: Can I modify other parameters? / Q: 可以修改其他參數嗎？

A: The tool currently focuses on modifying the `nc` parameter. If you need to modify other parameters, you can inherit the `YAMLModifier` class or modify the source code.
A: 目前工具專注於修改`nc`參數。如需修改其他參數，可以繼承`YAMLModifier`類或修改原始碼。

### Q: Does it support comment preservation? / Q: 是否支持註解保留？

A: PyYAML removes comments. If you need to preserve comments, you need to use other libraries like `ruamel.yaml`.
A: PyYAML會移除註解。如需保留註解，需要使用其他庫如`ruamel.yaml`。

### Q: How to restore the original file? / Q: 如何恢復原檔案？

A: Make sure to use the `output_path` parameter to save the result to a new file instead of overwriting the original file.
A: 確保使用`output_path`參數將結果保存到新檔案，而不是覆蓋原檔案。

### Q: What Python versions are supported? / Q: 支持哪些Python版本？

A: The tool is compatible with Python 3.6 and higher. It uses standard library modules (argparse, pathlib) and PyYAML.
A: 工具與Python 3.6及更高版本相容。它使用標準庫模組（argparse、pathlib）和PyYAML。

---

## License / 許可證

MIT License

## Author / 作者

YOLOv7 Toolset / YOLOv7 工具集

---

## Notes / 提示

**Before batch modification, it is recommended to test the tool's functionality with a single file first.**

**在批量修改前，建議先用單個檔案測試工具的功能。**

---

## Change Log / 更新日誌

### v1.0 (2026-01-25)
- Initial release with bilingual support / 初始版本，支持雙語
- Supports reading, modifying and saving YAML files / 支持讀取、修改和保存YAML檔案
- Command line and Python API support / 支持命令列和Python API
- Detailed error handling / 詳細的錯誤處理

---

## Troubleshooting / 故障排除

### Issue: "Input file not found / 輸入檔案不存在"

**Solution**: Verify the file path is correct and the file exists.
**解決方案**: 驗證檔案路徑正確且檔案存在。

### Issue: "YAML parsing error / YAML解析錯誤"

**Solution**: The YAML file may have syntax errors. Check the file format is valid YAML.
**解決方案**: YAML檔案可能有語法錯誤。檢查檔案格式是否為有效的YAML。

### Issue: "'nc' parameter does not exist in YAML file / YAML檔案中不存在'nc'參數"

**Solution**: Ensure the YAML file has the 'nc' parameter. This tool is designed for YOLOv7 configuration files.
**解決方案**: 確保YAML檔案有'nc'參數。此工具是為YOLOv7配置檔案設計的。

---

## Contributing / 貢獻

Contributions are welcome! Please feel free to submit issues and pull requests.

歡迎貢獻！請隨時提交問題和拉取請求。
