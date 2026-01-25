#!/usr/bin/env python3
"""
Examples for yaml_copy_nc.py usage
yaml_copy_nc.py 使用範例

Demonstrates various ways to use the YAML NC Value Copy and Modify Tool.
展示如何使用YAML NC值複製和修改工具的各種方式。
"""

from yaml_copy_nc import YAMLNCCopier


def example1_basic_copy():
    """
    Example 1: Basic NC value copy
    範例1：基本的NC值複製
    """
    print("\n" + "=" * 70)
    print("Example 1: Basic NC value copy / 範例1：基本的NC值複製")
    print("=" * 70)
    
    try:
        copier = YAMLNCCopier(
            source_path='cfg/training/yolov7-tiny.yaml',
            target_path='cfg/training/yolov7.yaml',
            output_path='cfg/training/yolov7-custom.yaml'
        )
        nc_value = copier.execute()
        print(f"\n✓ Successfully copied nc value: {nc_value}")
        
    except Exception as e:
        print(f"✗ Error: {e}")


def example2_copy_from_baseline():
    """
    Example 2: Copy nc from baseline to deploy config
    範例2：從基線複製nc到部署配置
    """
    print("\n" + "=" * 70)
    print("Example 2: Copy from baseline to deploy / 範例2：從基線複製到部署配置")
    print("=" * 70)
    
    try:
        copier = YAMLNCCopier(
            source_path='cfg/baseline/yolov7.yaml',
            target_path='cfg/deploy/yolov7.yaml',
            output_path='cfg/deploy/yolov7-from-baseline.yaml'
        )
        nc_value = copier.execute()
        print(f"\n✓ Successfully synchronized nc values")
        
    except Exception as e:
        print(f"✗ Error: {e}")


def example3_batch_copy_with_processing():
    """
    Example 3: Batch processing with error handling
    範例3：批量處理並進行錯誤處理
    """
    print("\n" + "=" * 70)
    print("Example 3: Batch copy with error handling / 範例3：批量複製並進行錯誤處理")
    print("=" * 70)
    
    # Define copy tasks / 定義複製任務
    copy_tasks = [
        {
            'source': 'cfg/training/yolov7-tiny.yaml',
            'target': 'cfg/training/yolov7.yaml',
            'output': 'cfg/output/yolov7-task1.yaml',
            'description': 'Task 1: tiny to medium / 任務1：tiny到medium'
        },
        {
            'source': 'cfg/training/yolov7.yaml',
            'target': 'cfg/training/yolov7x.yaml',
            'output': 'cfg/output/yolov7x-task2.yaml',
            'description': 'Task 2: medium to large / 任務2：medium到large'
        },
    ]
    
    successful = 0
    failed = 0
    
    for task in copy_tasks:
        print(f"\n{task['description']}")
        try:
            copier = YAMLNCCopier(
                source_path=task['source'],
                target_path=task['target'],
                output_path=task['output']
            )
            nc_value = copier.execute()
            successful += 1
        except FileNotFoundError:
            print(f"  ✗ Files not found (skipped) / 檔案未找到（已跳過）")
            failed += 1
        except Exception as e:
            print(f"  ✗ Error: {e}")
            failed += 1
    
    print(f"\n{'-' * 70}")
    print(f"Batch Processing Summary / 批量處理摘要:")
    print(f"  Successful / 成功: {successful}")
    print(f"  Failed / 失敗: {failed}")


def example4_programmatic_usage():
    """
    Example 4: Using the copier programmatically in other Python code
    範例4：在其他Python代碼中以編程方式使用複製器
    """
    print("\n" + "=" * 70)
    print("Example 4: Programmatic usage / 範例4：編程使用")
    print("=" * 70)
    
    try:
        # You can import and use YAMLNCCopier in your own scripts
        # 您可以在自己的腳本中導入並使用YAMLNCCopier
        
        copier = YAMLNCCopier(
            source_path='cfg/training/yolov7-tiny.yaml',
            target_path='cfg/training/yolov7.yaml',
            output_path='output/result.yaml'
        )
        
        # Get the nc value that will be copied
        # 獲取將要複製的nc值
        nc_value = copier.execute()
        
        print(f"\nCopied nc value: {nc_value}")
        print("You can use this value for further processing / 您可以使用此值進行進一步處理")
        
    except Exception as e:
        print(f"✗ Error: {e}")


def example5_with_error_handling():
    """
    Example 5: Proper error handling patterns
    範例5：適當的錯誤處理模式
    """
    print("\n" + "=" * 70)
    print("Example 5: Error handling patterns / 範例5：錯誤處理模式")
    print("=" * 70)
    
    print("\nAttempting to copy from non-existent source...")
    print("嘗試從不存在的源複製...")
    
    try:
        copier = YAMLNCCopier(
            source_path='cfg/nonexistent/config.yaml',
            target_path='cfg/training/yolov7.yaml',
            output_path='output/result.yaml'
        )
        copier.execute()
        
    except FileNotFoundError as e:
        print(f"✓ Caught expected error / 捕獲預期的錯誤:")
        print(f"  {e}")
        print(f"  This is expected when file doesn't exist / 當檔案不存在時這是預期的")
    
    except Exception as e:
        print(f"✗ Unexpected error / 意外錯誤: {e}")


if __name__ == '__main__':
    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 68 + "║")
    print("║" + "YAML NC Value Copy Tool - Usage Examples".center(68) + "║")
    print("║" + "YAML NC值複製工具 - 使用範例".center(68) + "║")
    print("║" + " " * 68 + "║")
    print("╚" + "=" * 68 + "╝")
    
    print("\nNote: Uncomment the examples you want to run.")
    print("注意：取消註解您要運行的範例。\n")
    
    # Uncomment the examples you want to run / 取消註解您要運行的範例
    # example1_basic_copy()
    # example2_copy_from_baseline()
    # example3_batch_copy_with_processing()
    # example4_programmatic_usage()
    example5_with_error_handling()
    
    print("\n✓ Examples completed / 範例完成\n")
