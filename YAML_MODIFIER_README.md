# YAMLModifier - YOLOv7 YAML配置修改工具

## 功能说明
这是一个用于YOLOv7配置文件的YAML修改工具，可以：
- 📖 读取YAML配置文件
- ✏️ 修改`nc`（类别数）参数
- 💾 保存到指定位置

## 安装依赖
```bash
pip install pyyaml
```

## 使用方法

### 1. 命令行使用

#### 基础用法 - 修改并覆盖原文件
```bash
python yaml_modifier.py -i cfg/training/yolov7-tiny.yaml -nc 10
```

#### 修改并保存到新位置
```bash
python yaml_modifier.py -i cfg/training/yolov7-tiny.yaml -o cfg/training/yolov7-tiny-custom.yaml -nc 5
```

#### 仅查看当前nc值（不修改）
```bash
python yaml_modifier.py -i cfg/training/yolov7-tiny.yaml --get-nc
```

### 2. 在Python代码中使用

#### 方法1: 完整处理流程
```python
from yaml_modifier import YAMLModifier

# 创建修改器实例
modifier = YAMLModifier(
    input_path='cfg/training/yolov7-tiny.yaml',
    output_path='cfg/training/yolov7-tiny-custom.yaml'
)

# 一次性完成：读取 -> 修改 -> 保存
modifier.process(new_nc=10)
```

#### 方法2: 逐步操作
```python
from yaml_modifier import YAMLModifier

modifier = YAMLModifier(
    input_path='cfg/training/yolov7-tiny.yaml',
    output_path='cfg/training/yolov7-tiny-custom.yaml'
)

# Step 1: 读取文件
config = modifier.read_yaml()

# Step 2: 查看当前nc值
current_nc = modifier.get_nc()
print(f"当前nc值: {current_nc}")

# Step 3: 修改nc值
modifier.modify_nc(new_nc=10)

# Step 4: 保存文件
modifier.save_yaml()
```

#### 方法3: 覆盖原文件
```python
from yaml_modifier import YAMLModifier

# 不指定output_path则覆盖原文件
modifier = YAMLModifier(input_path='cfg/training/yolov7-tiny.yaml')
modifier.process(new_nc=15)
```

#### 方法4: 批量修改
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
        print(f"✗ 处理失败: {e}")
```

## API 文档

### YAMLModifier 类

#### 初始化
```python
YAMLModifier(input_path: str, output_path: Optional[str] = None)
```
- `input_path`: 输入YAML文件路径（必需）
- `output_path`: 输出YAML文件路径（可选，默认覆盖原文件）

#### 方法

##### read_yaml()
读取YAML文件
```python
config = modifier.read_yaml()
# 返回: dict 类型的配置字典
```

##### modify_nc(new_nc: int)
修改nc参数
```python
modifier.modify_nc(new_nc=10)
# 返回: True（成功）
```

##### save_yaml()
保存修改后的YAML文件
```python
modifier.save_yaml()
```

##### get_nc()
获取当前的nc值
```python
current_nc = modifier.get_nc()
# 返回: int 类型的类别数
```

##### process(new_nc: int)
完整的处理流程（读取 -> 修改 -> 保存）
```python
modifier.process(new_nc=10)
```

## 示例脚本

查看 `yaml_modifier_examples.py` 获取更多使用示例。

## 错误处理

工具包含详细的错误处理：
- ✓ 文件不存在检查
- ✓ YAML解析错误捕获
- ✓ nc参数验证
- ✓ 目录自动创建

## 常见问题

**Q: 可以修改其他参数吗？**
A: 目前工具专注于修改`nc`参数。如需修改其他参数，可以继承`YAMLModifier`类或修改源代码。

**Q: 是否支持注释保留？**
A: PyYAML会移除注释。如需保留注释，需要使用其他库如`ruamel.yaml`。

**Q: 如何恢复原文件？**
A: 确保使用`output_path`参数将结果保存到新文件，而不是覆盖原文件。

## 许可证
MIT License

## 作者
YOLOv7 工具集

---

**提示**: 在批量修改前，建议先用单个文件测试工具的功能。
