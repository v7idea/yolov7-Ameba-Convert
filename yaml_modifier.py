#!/usr/bin/env python3
"""
YOLOv7 YAML Configuration File Modifier Tool
YOLOv7 YAML 配置檔案修改工具

Used to read, modify and save the nc (number of classes) parameter in YAML configuration files.
用於讀取、修改和保存YAML配置檔案中的nc（類別數）參數

This version uses text-based replacement to preserve all comments and formatting.
此版本使用基於文字的替換以保留所有註解和格式。
"""

import re
import argparse
from pathlib import Path
from typing import Optional


class YAMLModifier:
    """YAML File Modifier Class / YAML檔案修改器類"""
    
    def __init__(self, input_path: str, output_path: Optional[str] = None):
        """
        Initialize YAMLModifier / 初始化YAMLModifier
        
        Args:
            input_path (str): Path to input YAML file / 輸入YAML檔案的路徑
            output_path (str, optional): Path to output YAML file. If None, overwrites original file / 
                                        輸出YAML檔案的路徑。如果為None，則覆蓋原檔案
        """
        self.input_path = Path(input_path)
        self.output_path = Path(output_path) if output_path else self.input_path
        self.file_content = None
        self.current_nc = None
        
        # Verify input file exists / 驗證輸入檔案存在
        if not self.input_path.exists():
            raise FileNotFoundError(f"Input file not found / 輸入檔案不存在: {self.input_path}")
    
    def read_yaml(self) -> dict:
        """
        Read YAML file and extract nc value / 讀取YAML檔案並提取nc值
        
        Returns:
            dict: Dictionary with 'nc' key containing the value / 包含'nc'鍵的字典
        """
        try:
            with open(self.input_path, 'r', encoding='utf-8') as f:
                self.file_content = f.read()
            
            # Extract nc value using regex / 使用正則表達式提取nc值
            # Matches: nc: 80 or nc:80 (with optional whitespace)
            match = re.search(r'^\s*nc\s*:\s*(\d+)', self.file_content, re.MULTILINE)
            
            if match:
                self.current_nc = int(match.group(1))
                print(f"✓ Successfully read YAML file / 成功讀取YAML檔案: {self.input_path}")
                print(f"  Current nc value / 當前nc值: {self.current_nc}")
                return {'nc': self.current_nc}
            else:
                raise ValueError("'nc' parameter not found in YAML file / YAML檔案中找不到'nc'參數")
                
        except Exception as e:
            raise Exception(f"Failed to read file / 讀取檔案失敗: {e}")
    
    def modify_nc(self, new_nc: int) -> bool:
        """
        Modify nc (number of classes) parameter / 修改nc（類別數）參數
        
        Args:
            new_nc (int): New number of classes / 新的類別數
            
        Returns:
            bool: Whether modification was successful / 是否修改成功
        """
        if self.file_content is None:
            raise RuntimeError("Please call read_yaml() method first to read the file / 請先呼叫read_yaml()方法讀取檔案")
        
        if self.current_nc is None:
            raise ValueError("'nc' parameter not found in YAML file / YAML檔案中找不到'nc'參數")
        
        # Replace nc value using regex while preserving everything else
        # 使用正則表達式替換nc值，同時保留其他所有內容
        # Pattern: nc: <number> or nc:<number> (preserves spacing and comments)
        self.file_content = re.sub(
            r'(^\s*nc\s*:\s*)(\d+)',
            rf'\g<1>{new_nc}',
            self.file_content,
            count=1,
            flags=re.MULTILINE
        )
        
        print(f"✓ Modified nc parameter / 已修改nc參數: {self.current_nc} -> {new_nc}")
        return True
    
    def save_yaml(self) -> None:
        """
        Save modified YAML file / 保存修改後的YAML檔案
        """
        if self.file_content is None:
            raise RuntimeError("No configuration data to save, please call read_yaml() method first / 沒有可保存的組態資料，請先呼叫read_yaml()方法")
        
        try:
            # Ensure output directory exists / 確保輸出目錄存在
            self.output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(self.output_path, 'w', encoding='utf-8') as f:
                f.write(self.file_content)
            print(f"✓ Successfully saved YAML file / 成功保存YAML檔案: {self.output_path}")
        except Exception as e:
            raise Exception(f"Failed to save file / 保存檔案失敗: {e}")
    
    def get_nc(self) -> int:
        """
        Get current nc value / 獲取當前的nc值
        
        Returns:
            int: Number of classes / 類別數
        """
        if self.current_nc is None:
            raise RuntimeError("Please call read_yaml() method first to read the file / 請先呼叫read_yaml()方法讀取檔案")
        return self.current_nc
    
    def process(self, new_nc: int) -> None:
        """
        Complete processing workflow: Read -> Modify -> Save / 完整的處理流程：讀取 -> 修改 -> 保存
        
        Args:
            new_nc (int): New number of classes / 新的類別數
        """
        self.read_yaml()
        self.modify_nc(new_nc)
        self.save_yaml()


def main():
    """Command line entry point / 命令列入口"""
    parser = argparse.ArgumentParser(
        description='YOLOv7 YAML Configuration File Modifier Tool - Modify nc (number of classes) parameter / YOLOv7 YAML配置檔案修改工具 - 修改nc（類別數）參數',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples / 範例:
  # Modify file and overwrite original file / 修改檔案並覆蓋原檔案
  python yaml_modifier.py -i cfg/training/yolov7-tiny.yaml -nc 10
  
  # Modify file and save to new location / 修改檔案並保存到新位置
  python yaml_modifier.py -i cfg/training/yolov7-tiny.yaml -o cfg/training/yolov7-tiny-custom.yaml -nc 5
  
  # View current nc value / 查看當前nc值
  python yaml_modifier.py -i cfg/training/yolov7-tiny.yaml --get-nc
        """
    )
    
    parser.add_argument('-i', '--input', required=True, help='Path to input YAML file / 輸入YAML檔案路徑')
    parser.add_argument('-o', '--output', help='Path to output YAML file (optional, default overwrites original file) / 輸出YAML檔案路徑（選擇性，預設覆蓋原檔案）')
    parser.add_argument('-nc', '--num-classes', type=int, help='New number of classes / 新的類別數')
    parser.add_argument('--get-nc', action='store_true', help='Only read and display current nc value / 僅讀取並顯示當前的nc值')
    
    args = parser.parse_args()
    
    try:
        # Create modifier instance / 建立修改器實例
        modifier = YAMLModifier(args.input, args.output)
        
        if args.get_nc:
            # Only read nc value / 只讀取nc值
            current_nc = modifier.read_yaml()
            print(f"Current nc value / 當前nc值: {modifier.get_nc()}")
        else:
            # Read, modify, save / 讀取、修改、保存
            if args.num_classes is None:
                parser.error("Please specify -nc/--num-classes parameter to set new number of classes / 請指定 -nc/--num-classes 參數來設定新的類別數")
            
            modifier.process(args.num_classes)
            print("✓ Processing complete! / 處理完成！")
    
    except Exception as e:
        print(f"✗ Error / 錯誤: {e}")
        exit(1)


if __name__ == '__main__':
    main()
