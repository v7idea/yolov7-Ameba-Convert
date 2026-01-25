#!/usr/bin/env python3
"""
YAML NC Value Copy and Modify Tool
YAML NC值複製和修改工具

This script reads the nc value from one YAML file and copies it to another YAML file.
此腳本從一個YAML檔案讀取nc值並將其複製到另一個YAML檔案。

Usage: python yaml_copy_nc.py --data-yaml source.yaml --target-yaml target.yaml --output-yaml output.yaml
使用方法: python yaml_copy_nc.py --data-yaml source.yaml --target-yaml target.yaml --output-yaml output.yaml
"""

import argparse
from pathlib import Path
from yaml_modifier import YAMLModifier


class YAMLNCCopier:
    """
    YAML NC Value Copier Class
    YAML NC值複製器類
    
    Reads nc value from source YAML file and applies it to target YAML file.
    從源YAML檔案讀取nc值並將其應用於目標YAML檔案。
    """
    
    def __init__(self, source_path: str, target_path: str, output_path: str):
        """
        Initialize YAMLNCCopier
        初始化YAMLNCCopier
        
        Args:
            source_path (str): Path to source YAML file to read nc value from
                              要從中讀取nc值的源YAML檔案路徑
            target_path (str): Path to target YAML file to modify
                              要修改的目標YAML檔案路徑
            output_path (str): Path to output YAML file to save result
                              要保存結果的輸出YAML檔案路徑
        """
        self.source_path = Path(source_path)
        self.target_path = Path(target_path)
        self.output_path = Path(output_path)
        
        # Validate input files exist / 驗證輸入檔案存在
        if not self.source_path.exists():
            raise FileNotFoundError(f"Source file not found / 源檔案不存在: {self.source_path}")
        if not self.target_path.exists():
            raise FileNotFoundError(f"Target file not found / 目標檔案不存在: {self.target_path}")
    
    def execute(self) -> int:
        """
        Execute the complete workflow: Read -> Modify -> Save
        執行完整工作流程：讀取 -> 修改 -> 保存
        
        Returns:
            int: The nc value that was copied / 被複製的nc值
        """
        try:
            print("=" * 60)
            print("YAML NC Value Copy and Modify Tool")
            print("YAML NC值複製和修改工具")
            print("=" * 60)
            
            # Step 1: Read nc value from source file / 第1步：從源檔案讀取nc值
            print(f"\n📖 Step 1: Reading source YAML file / 第1步：讀取源YAML檔案")
            print(f"   Source file / 源檔案: {self.source_path}")
            
            source_modifier = YAMLModifier(str(self.source_path))
            source_modifier.read_yaml()
            source_nc = source_modifier.get_nc()
            
            if source_nc is None:
                raise ValueError("'nc' parameter not found in source YAML file / 源YAML檔案中找不到'nc'參數")
            
            print(f"   ✓ Source nc value / 源nc值: {source_nc}")
            
            # Step 2: Modify target file with source nc value / 第2步：用源nc值修改目標檔案
            print(f"\n✏️  Step 2: Modifying target YAML file / 第2步：修改目標YAML檔案")
            print(f"   Target file / 目標檔案: {self.target_path}")
            print(f"   Output file / 輸出檔案: {self.output_path}")
            
            target_modifier = YAMLModifier(str(self.target_path), str(self.output_path))
            target_modifier.read_yaml()
            old_nc = target_modifier.get_nc()
            
            print(f"   Current nc value in target / 目標檔案中的當前nc值: {old_nc}")
            
            target_modifier.modify_nc(source_nc)
            
            # Step 3: Save to output file / 第3步：保存到輸出檔案
            print(f"\n💾 Step 3: Saving modified YAML to output file / 第3步：保存修改後的YAML到輸出檔案")
            target_modifier.save_yaml()
            
            print("\n" + "=" * 60)
            print("✓ Processing Complete! / 處理完成！")
            print("=" * 60)
            print(f"\n📊 Summary / 摘要:")
            print(f"   Source nc value / 源nc值: {source_nc}")
            print(f"   Old target nc value / 舊的目標nc值: {old_nc}")
            print(f"   New target nc value / 新的目標nc值: {source_nc}")
            print(f"   Output file / 輸出檔案: {self.output_path}")
            print()
            
            return source_nc
            
        except Exception as e:
            print(f"\n✗ Error / 錯誤: {e}")
            raise


def main():
    """
    Command line entry point
    命令列入口
    """
    parser = argparse.ArgumentParser(
        description='YAML NC Value Copy and Modify Tool - Read nc from source, modify target, save to output',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples / 範例:

  1. Copy nc value from source to target and save
     從源複製nc值到目標並保存
     python yaml_copy_nc.py --data-yaml cfg/training/yolov7-tiny.yaml \\
                            --target-yaml cfg/training/yolov7.yaml \\
                            --output-yaml cfg/training/yolov7-custom.yaml

  2. Copy nc value and create backup
     複製nc值並創建備份
     python yaml_copy_nc.py --data-yaml source.yaml --target-yaml target.yaml --output-yaml output.yaml

  3. Using verbose output
     使用詳細輸出
     python yaml_copy_nc.py --data-yaml cfg/baseline/yolov7-tiny.yaml \\
                            --target-yaml cfg/training/yolov7.yaml \\
                            --output-yaml cfg/training/yolov7-modified.yaml -v
        """
    )
    
    parser.add_argument(
        '--data-yaml',
        required=True,
        help='Data YAML file path (to read nc value from) / 資料YAML檔案路徑（從中讀取nc值）'
    )
    parser.add_argument(
        '--target-yaml',
        required=True,
        help='Target YAML file path (to be modified) / 目標YAML檔案路徑（要被修改）'
    )
    parser.add_argument(
        '--output-yaml',
        required=True,
        help='Output YAML file path (to save result) / 輸出YAML檔案路徑（保存結果）'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output / 啟用詳細輸出'
    )
    
    args = parser.parse_args()
    
    try:
        # Create copier instance / 創建複製器實例
        copier = YAMLNCCopier(
            source_path=args.data_yaml,
            target_path=args.target_yaml,
            output_path=args.output_yaml
        )
        
        # Execute the copy and modify operation / 執行複製和修改操作
        nc_value = copier.execute()
        
    except FileNotFoundError as e:
        print(f"✗ File not found / 檔案未找到: {e}")
        exit(1)
    except ValueError as e:
        print(f"✗ Value error / 數值錯誤: {e}")
        exit(1)
    except Exception as e:
        print(f"✗ Unexpected error / 意外錯誤: {e}")
        exit(1)


if __name__ == '__main__':
    main()
