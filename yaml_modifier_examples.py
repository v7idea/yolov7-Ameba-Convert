#!/usr/bin/env python3
"""
YAMLModifier 使用示例
展示如何以编程方式使用YAML修改工具
"""

from yaml_modifier import YAMLModifier


def example1_basic_usage():
    """示例1: 基础使用 - 读取、修改、保存"""
    print("=" * 50)
    print("示例1: 基础使用")
    print("=" * 50)
    
    # 创建修改器
    modifier = YAMLModifier(
        input_path='cfg/training/yolov7-tiny.yaml',
        output_path='cfg/training/yolov7-tiny-10classes.yaml'
    )
    
    # 完整处理流程
    modifier.process(new_nc=10)
    print()


def example2_step_by_step():
    """示例2: 逐步操作"""
    print("=" * 50)
    print("示例2: 逐步操作")
    print("=" * 50)
    
    # 创建修改器
    modifier = YAMLModifier(
        input_path='cfg/training/yolov7-tiny.yaml',
        output_path='cfg/training/yolov7-tiny-5classes.yaml'
    )
    
    # 逐步操作
    print("Step 1: 读取文件")
    modifier.read_yaml()
    
    print(f"Step 2: 查看当前nc值 = {modifier.get_nc()}")
    
    print("Step 3: 修改nc值")
    modifier.modify_nc(new_nc=5)
    
    print("Step 4: 保存文件")
    modifier.save_yaml()
    print()


def example3_overwrite_original():
    """示例3: 覆盖原文件"""
    print("=" * 50)
    print("示例3: 覆盖原文件")
    print("=" * 50)
    
    # 创建修改器（不指定输出路径则覆盖原文件）
    modifier = YAMLModifier(input_path='cfg/training/yolov7-tiny.yaml')
    
    # 读取
    modifier.read_yaml()
    print(f"当前nc值: {modifier.get_nc()}")
    
    # 注意：这会覆盖原文件！
    print("(演示代码不实际执行覆盖操作)")
    # modifier.modify_nc(new_nc=20)
    # modifier.save_yaml()
    print()


def example4_batch_modify():
    """示例4: 批量修改多个文件"""
    print("=" * 50)
    print("示例4: 批量修改多个文件")
    print("=" * 50)
    
    config_files = [
        ('cfg/training/yolov7-tiny.yaml', 10),
        ('cfg/training/yolov7.yaml', 20),
    ]
    
    for input_file, nc_value in config_files:
        try:
            # 生成输出文件名
            output_file = input_file.replace('.yaml', f'-{nc_value}classes.yaml')
            
            modifier = YAMLModifier(input_file, output_file)
            modifier.process(new_nc=nc_value)
            print(f"✓ {input_file} -> {output_file} (nc={nc_value})")
        except FileNotFoundError as e:
            print(f"✗ 跳过不存在的文件: {input_file}")
        except Exception as e:
            print(f"✗ 处理 {input_file} 失败: {e}")
    print()


if __name__ == '__main__':
    print("\n" + "=" * 50)
    print("YAMLModifier 使用示例")
    print("=" * 50 + "\n")
    
    # 运行示例1和2（安全操作）
    # example1_basic_usage()
    # example2_step_by_step()
    example3_overwrite_original()
    example4_batch_modify()
    
    print("\n提示: 取消注释example1_basic_usage()和example2_step_by_step()来执行完整示例")
