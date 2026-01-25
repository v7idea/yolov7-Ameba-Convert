#!/usr/bin/env python3
"""
Test script to validate that YAML modification preserves all comments and structure
測試腳本以驗證YAML修改是否保留所有註解和結構
"""

import tempfile
import os
from pathlib import Path
from yaml_modifier import YAMLModifier


def test_yaml_preservation():
    """
    Test that YAML comments and structure are preserved
    測試YAML註解和結構是否被保留
    """
    
    # Create a test YAML content with comments and structure - Full example
    test_yaml_content = """# parameters
nc: 80  # number of classes
depth_multiple: 1.0  # model depth multiple
width_multiple: 1.0  # layer channel multiple

# anchors
anchors:
  - [10,13, 16,30, 33,23]  # P3/8
  - [30,61, 62,45, 59,119]  # P4/16
  - [116,90, 156,198, 373,326]  # P5/32

# yolov7-tiny backbone
backbone:
  [[-1, 1, Conv, [32, 3, 2, None, 1, nn.LeakyReLU(0.1)]],  # 0-P1/2
   [-1, 1, Conv, [64, 3, 2, None, 1, nn.LeakyReLU(0.1)]],  # 1-P2/4
   [-1, 1, MaxPool, [2, 2]],  # 2
   [-1, 2, Conv, [64, 3, 1]]]  # 3

# yolov7-tiny head
head:
  [[-1, 1, Conv, [128, 3, 1]],  # 0
   [-1, 1, Conv, [256, 3, 2]],  # 1
   [[-1, -2], 1, Concat, [1]],  # 2
   [-1, 3, C3, [256]],  # 3
   [-1, 1, Conv, [512, 3, 2]],  # 4
   [[-1, -4], 1, Concat, [1]],  # 5
   [-1, 3, C3, [512]],  # 6
   [-1, -2, nn.Upsample, [None, 2, 'nearest']],  # 7
   [[-1, 3], 1, Concat, [1]],  # 8
   [-1, 3, C3, [256]],  # 9
   [-1, -2, nn.Upsample, [None, 2, 'nearest']],  # 10
   [[-1, 1], 1, Concat, [1]],  # 11
   [-1, 3, C3, [128]],  # 12
   [-1, 2, MP, []],  # 13
   [-1, 1, Conv, [128, 3, 2]],  # 14
   [[-1, 9], 1, Concat, [1]],  # 15
   [-1, 3, C3, [256]],  # 16
   [-1, 2, MP, []],  # 17
   [-1, 1, Conv, [256, 3, 2]],  # 18
   [[-1, 6], 1, Concat, [1]],  # 19
   [-1, 3, C3, [512]],  # 20
   [[12, 16, 20], 1, Detect, [nc, anchors]]]  # 21
"""
    
    print("=" * 80)
    print("YAML File Preservation Test / YAML檔案保留測試")
    print("=" * 80)
    
    # Create temporary files
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        input_file = tmpdir / "test_input.yaml"
        output_file = tmpdir / "test_output.yaml"
        
        # Write test content
        input_file.write_text(test_yaml_content, encoding='utf-8')
        print("\n📝 Original YAML file content / 原始YAML檔案內容:")
        print("-" * 70)
        print(test_yaml_content)
        print("-" * 70)
        
        try:
            # Test modification
            print("\n🔧 Modifying nc value from 80 to 10...")
            print("🔧 將nc值從80改為10...")
            
            modifier = YAMLModifier(str(input_file), str(output_file))
            modifier.read_yaml()
            
            print(f"\n✓ Original nc value / 原始nc值: {modifier.get_nc()}")
            
            modifier.modify_nc(10)
            modifier.save_yaml()
            
            # Read the output and check
            output_content = output_file.read_text(encoding='utf-8')
            
            print("\n📝 Modified YAML file content / 修改後的YAML檔案內容:")
            print("-" * 70)
            print(output_content)
            print("-" * 70)
            
            # Verify
            print("\n✅ Verification / 驗證:")
            
            # Check if comments are preserved
            if "# number of classes" in output_content:
                print("  ✓ Comment for nc parameter preserved / nc參數的註解被保留")
            else:
                print("  ✗ Comment for nc parameter NOT preserved / nc參數的註解未被保留")
            
            if "# anchors" in output_content:
                print("  ✓ Comment for anchors section preserved / anchors部分的註解被保留")
            else:
                print("  ✗ Comment for anchors section NOT preserved / anchors部分的註解未被保留")
            
            if "depth_multiple: 1.0" in output_content:
                print("  ✓ depth_multiple preserved / depth_multiple被保留")
            else:
                print("  ✗ depth_multiple NOT preserved / depth_multiple未被保留")
            
            if "width_multiple: 1.0" in output_content:
                print("  ✓ width_multiple preserved / width_multiple被保留")
            else:
                print("  ✗ width_multiple NOT preserved / width_multiple未被保留")
            
            if "nc: 10" in output_content:
                print("  ✓ nc value correctly modified to 10 / nc值正確修改為10")
            else:
                print("  ✗ nc value NOT modified correctly / nc值未正確修改")
            
            if "anchors:" in output_content:
                print("  ✓ Anchors structure preserved / anchors結構被保留")
            else:
                print("  ✗ Anchors structure NOT preserved / anchors結構未被保留")
            
            if "backbone:" in output_content:
                print("  ✓ Backbone structure preserved / backbone結構被保留")
            else:
                print("  ✗ Backbone structure NOT preserved / backbone結構未被保留")
            
            if "head:" in output_content:
                print("  ✓ Head structure preserved / head結構被保留")
            else:
                print("  ✗ Head structure NOT preserved / head結構未被保留")
            
            print("\n✅ Test completed successfully!")
            print("✅ 測試成功完成！")
            
        except Exception as e:
            print(f"\n❌ Error during test / 測試期間出錯: {e}")
            return False
    
    return True


if __name__ == '__main__':
    success = test_yaml_preservation()
    exit(0 if success else 1)
