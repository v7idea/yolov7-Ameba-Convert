# YAML NC Value Copy and Modify Tool
# YAML NC值複製和修改工具

## Overview / 概述

The **YAML NC Value Copier** tool reads the `nc` (number of classes) parameter from a source YAML configuration file and applies it to a target YAML configuration file, then saves the modified file to an output location.

**YAML NC值複製器**工具從源YAML配置檔案讀取`nc`（類別數）參數，並將其應用於目標YAML配置檔案，然後將修改後的檔案保存到輸出位置。

**Key Features / 主要特性:**
- ✅ Read nc value from any YAML file / 從任何YAML檔案讀取nc值
- ✅ Apply nc value to target YAML file / 將nc值應用於目標YAML檔案
- ✅ Save modified file to specified output location / 將修改後的檔案保存到指定的輸出位置
- ✅ Built on top of `yaml_modifier.py` / 基於`yaml_modifier.py`構建
- ✅ Comprehensive error handling / 全面的錯誤處理
- ✅ Bilingual support (English/Traditional Chinese) / 雙語支持（英文/繁體中文）

---

## Prerequisites / 前置條件

```bash
# Install required packages / 安裝所需的套件
pip install pyyaml ruamel.yaml
```

**Note / 注意:**
- `ruamel.yaml`: Preserves comments and formatting / 保留註解和格式
- `pyyaml`: Fallback for basic YAML operations / YAML基本操作的備用庫

---

## Installation / 安裝

Place these files in your YOLOv7 project directory:
將這些檔案放在您的YOLOv7專案目錄中：

```
yolov7-Ameba-Convert/
├── yaml_modifier.py              # Core YAML modifier / 核心YAML修改器
├── yaml_copy_nc.py               # NC value copy tool / NC值複製工具 ← 新檔案
├── yaml_copy_nc_examples.py      # Usage examples / 使用範例 ← 新檔案
└── cfg/
    ├── training/
    ├── deploy/
    └── baseline/
```

---

## Usage / 使用方法

### Command Line Usage / 命令列使用

#### Basic Syntax / 基本語法

```bash
python yaml_copy_nc.py --data-yaml <data_yaml> --target-yaml <target_yaml> --output-yaml <output_yaml>

python yaml_copy_nc.py --data-yaml <資料yaml> --target-yaml <目標yaml> --output-yaml <輸出yaml>
```

#### Parameters / 參數

- `--data-yaml`: Data YAML file path (to read nc value from) / 資料YAML檔案路徑（從中讀取nc值）
- `--target-yaml`: Target YAML file path (to be modified) / 目標YAML檔案路徑（要被修改）
- `--output-yaml`: Output YAML file path (to save result) / 輸出YAML檔案路徑（保存結果）
- `-v, --verbose`: Enable verbose output (optional) / 啟用詳細輸出（可選）

#### Examples / 範例

**Example 1: Copy nc from yolov7-tiny to yolov7**
**範例1：將nc從yolov7-tiny複製到yolov7**

```bash
python yaml_copy_nc.py \
  --data-yaml cfg/training/yolov7-tiny.yaml \
  --target-yaml cfg/training/yolov7.yaml \
  --output-yaml cfg/training/yolov7-custom.yaml
```

**Example 2: Copy nc from baseline to deploy**
**範例2：將nc從基線複製到部署**

```bash
python yaml_copy_nc.py \
  --data-yaml cfg/baseline/yolov7.yaml \
  --target-yaml cfg/deploy/yolov7.yaml \
  --output-yaml cfg/deploy/yolov7-from-baseline.yaml
```

**Example 3: Create synchronized config for multiple models**
**範例3：為多個模型創建同步配置**

```bash
# First, copy nc from tiny to small / 首先，將nc從tiny複製到small
python yaml_copy_nc.py \
  --data-yaml cfg/training/yolov7-tiny.yaml \
  --target-yaml cfg/training/yolov7-small.yaml \
  --output-yaml cfg/output/yolov7-small-sync.yaml

# Then, copy to medium / 然後，複製到medium
python yaml_copy_nc.py \
  --data-yaml cfg/training/yolov7-tiny.yaml \
  --target-yaml cfg/training/yolov7-medium.yaml \
  --output-yaml cfg/output/yolov7-medium-sync.yaml
```

---

## Python API Usage / Python API 使用

### Import and Create Instance / 導入並創建實例

```python
from yaml_copy_nc import YAMLNCCopier

# Create copier instance / 創建複製器實例
copier = YAMLNCCopier(
    source_path='cfg/training/yolov7-tiny.yaml',      # Source to read from / 讀取源
    target_path='cfg/training/yolov7.yaml',            # Target to modify / 要修改的目標
    output_path='cfg/training/yolov7-custom.yaml'      # Where to save / 保存位置
)
```

### Execute the Copy Operation / 執行複製操作

```python
# Execute the complete workflow / 執行完整工作流程
nc_value = copier.execute()

print(f"Copied nc value: {nc_value}")
```

### Complete Example / 完整範例

```python
from yaml_copy_nc import YAMLNCCopier

try:
    # Read nc from source, modify target, save to output
    # 從源讀取nc，修改目標，保存到輸出
    copier = YAMLNCCopier(
        source_path='source.yaml',
        target_path='target.yaml',
        output_path='output.yaml'
    )
    
    nc_value = copier.execute()
    print(f"Successfully copied nc value: {nc_value}")
    
except FileNotFoundError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Invalid YAML file: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

## Workflow / 工作流程

The tool performs the following steps:
工具執行以下步驟：

```
1. Read Source YAML File / 讀取源YAML檔案
   └─ Extract nc value from source configuration
      └─ 從源配置中提取nc值

2. Read Target YAML File / 讀取目標YAML檔案
   └─ Load target configuration
      └─ 加載目標配置

3. Modify Target Configuration / 修改目標配置
   └─ Replace nc value in target with source nc value
      └─ 用源nc值替換目標中的nc值

4. Save Output File / 保存輸出檔案
   └─ Write modified configuration to output location
      └─ 將修改後的配置寫入輸出位置
```

---

## Workflow Diagram / 工作流程圖

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│            YAML NC Value Copy & Modify Tool                │
│            YAML NC值複製和修改工具                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘

        ┌──────────────────┐
        │  Source YAML     │
        │  (read nc value) │
        │  源YAML           │
        │  (讀取nc值)       │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │  Extract nc=X    │
        │  提取 nc=X       │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────────────────┐
        │  Target YAML                 │
        │  (modify with nc=X)          │
        │  目標YAML                     │
        │  (用nc=X修改)                │
        └────────┬─────────────────────┘
                 │
                 ▼
        ┌──────────────────┐
        │  Output YAML     │
        │  (save result)   │
        │  輸出YAML        │
        │  (保存結果)      │
        └──────────────────┘
```

---

## Use Cases / 使用案例

### Use Case 1: Synchronize Class Count Across Models
### 使用案例1：在模型間同步類別計數

When you have multiple YAML configuration files for different models but want them to use the same number of classes:
當您有多個不同模型的YAML配置檔案，但希望它們使用相同的類別數量時：

```bash
# Set all models to use the same nc as yolov7-tiny / 將所有模型設置為使用與yolov7-tiny相同的nc
python yaml_copy_nc.py --data-yaml cfg/training/yolov7-tiny.yaml --target-yaml cfg/training/yolov7.yaml --output-yaml models/yolov7-sync.yaml
python yaml_copy_nc.py --data-yaml cfg/training/yolov7-tiny.yaml --target-yaml cfg/training/yolov7x.yaml --output-yaml models/yolov7x-sync.yaml
```

### Use Case 2: Deploy Configuration Update
### 使用案例2：部署配置更新

When you want to create a deployment configuration based on your training configuration:
當您想根據訓練配置創建部署配置時：

```bash
# Copy nc from training config to deployment config / 將nc從訓練配置複製到部署配置
python yaml_copy_nc.py \
  --data-yaml cfg/training/yolov7-trained.yaml \
  --target-yaml cfg/deploy/yolov7-template.yaml \
  --output-yaml cfg/deploy/yolov7-production.yaml
```

### Use Case 3: Configuration Backup and Versioning
### 使用案例3：配置備份和版本控制

When you want to create versioned copies of configurations:
當您想創建配置的版本控制副本時：

```bash
# Create version 2.0 based on version 1.0 / 基於版本1.0創建版本2.0
python yaml_copy_nc.py \
  --data-yaml cfg/v1.0/yolov7.yaml \
  --target-yaml cfg/template/yolov7-base.yaml \
  --output-yaml cfg/v2.0/yolov7.yaml
```

---

## Error Handling / 錯誤處理

The tool provides detailed error messages:
工具提供詳細的錯誤訊息：

### Common Errors / 常見錯誤

1. **FileNotFoundError - Source file not found**
   ```
   Error: Source file not found / 源檔案不存在: cfg/training/missing.yaml
   ```
   **Solution**: Check the source file path is correct / 檢查源檔案路徑是否正確

2. **FileNotFoundError - Target file not found**
   ```
   Error: Target file not found / 目標檔案不存在: cfg/training/missing.yaml
   ```
   **Solution**: Check the target file path is correct / 檢查目標檔案路徑是否正確

3. **ValueError - nc parameter not found**
   ```
   Error: 'nc' parameter not found in source YAML file
   ```
   **Solution**: Make sure source is a valid YOLOv7 config with nc parameter / 確保源是有效的YOLOv7配置且包含nc參數

4. **YAML parsing error**
   ```
   Error: YAML parsing error: ...
   ```
   **Solution**: Check YAML file syntax is valid / 檢查YAML檔案語法是否有效

---

## Examples / 範例

See `yaml_copy_nc_examples.py` for more detailed examples:
查看`yaml_copy_nc_examples.py`獲取更詳細的範例：

```bash
# Run examples / 運行範例
python yaml_copy_nc_examples.py
```

---

## Advanced Usage / 進階使用

### Batch Processing / 批量處理

```python
from yaml_copy_nc import YAMLNCCopier
import json

# Load copy tasks from configuration / 從配置加載複製任務
tasks = [
    {'source': 'cfg/baseline/tiny.yaml', 'target': 'cfg/training/tiny.yaml', 'output': 'output/tiny.yaml'},
    {'source': 'cfg/baseline/small.yaml', 'target': 'cfg/training/small.yaml', 'output': 'output/small.yaml'},
    {'source': 'cfg/baseline/medium.yaml', 'target': 'cfg/training/medium.yaml', 'output': 'output/medium.yaml'},
]

results = []
for task in tasks:
    try:
        copier = YAMLNCCopier(task['source'], task['target'], task['output'])
        nc_value = copier.execute()
        results.append({'status': 'success', 'nc': nc_value, **task})
    except Exception as e:
        results.append({'status': 'failed', 'error': str(e), **task})

# Save results / 保存結果
with open('copy_results.json', 'w') as f:
    json.dump(results, f, indent=2)
```

---

## Troubleshooting / 故障排除

### Q: How do I know if the copy was successful?
### Q: 如何知道複製是否成功？

**A:** The tool provides clear console output with status messages. Look for the "✓" checkmark indicating success.
**A:** 工具提供清晰的控制台輸出和狀態訊息。查找表示成功的"✓"符號。

### Q: Can I use this with non-YOLOv7 YAML files?
### Q: 我可以將其用於非YOLOv7 YAML檔案嗎？

**A:** Yes, as long as they contain an 'nc' parameter. The tool is generic and works with any YAML file that has this parameter.
**A:** 是的，只要它們包含'nc'參數即可。該工具是通用的，適用於任何具有此參數的YAML檔案。

### Q: Will this overwrite my original files?
### Q: 這會覆蓋我的原始檔案嗎？

**A:** No. You must specify an output path, so original files are never overwritten unless you explicitly set output path to be the same.
**A:** 否。您必須指定輸出路徑，因此原始檔案永遠不會被覆蓋，除非您明確將輸出路徑設置為相同。

---

## Related Tools / 相關工具

- **yaml_modifier.py** - Core tool for modifying individual YAML files / 用於修改單個YAML檔案的核心工具
- **yaml_modifier_examples.py** - Examples for yaml_modifier / yaml_modifier的範例
- **YAML_MODIFIER_README.md** - Documentation for yaml_modifier / yaml_modifier的文檔

---

## Version History / 版本歷史

### v1.0 (2026-01-25)
- Initial release of YAML NC Value Copy tool / YAML NC值複製工具初始版本
- Supports reading nc from source and applying to target / 支持從源讀取nc並應用於目標
- Bilingual interface (English/Traditional Chinese) / 雙語界面（英文/繁體中文）
- Comprehensive error handling / 全面的錯誤處理

---

## License / 許可證

MIT License

## Author / 作者

YOLOv7 Toolset / YOLOv7 工具集

---

**Happy YAML configuration managing! / 祝YAML配置管理愉快！**
