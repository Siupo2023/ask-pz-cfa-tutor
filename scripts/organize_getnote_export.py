#!/usr/bin/env python3
"""
Get笔记导出文件整理工具
将手动导出的笔记整理到 ask-pz references 目录
"""

import os
import shutil
import glob
from datetime import datetime

# 源目录和目标目录
SOURCE_DIR = None  # 用户指定
TARGET_DIR = os.path.expanduser("~/Library/Mobile Documents/iCloud~com~logseq~logseq/Documents/skills-hub/skills/personal/ask-pz/references/GetNotes导出")

def organize_notes(source_path):
    """整理导出的笔记文件"""
    global SOURCE_DIR
    SOURCE_DIR = os.path.expanduser(source_path)

    if not os.path.exists(SOURCE_DIR):
        print(f"❌ 源目录不存在: {SOURCE_DIR}")
        return

    # 创建目标目录
    os.makedirs(TARGET_DIR, exist_ok=True)

    # 查找所有 Markdown 文件
    md_files = glob.glob(os.path.join(SOURCE_DIR, "*.md"))
    txt_files = glob.glob(os.path.join(SOURCE_DIR, "*.txt"))

    all_files = md_files + txt_files

    if not all_files:
        print(f"❌ 在 {SOURCE_DIR} 中未找到笔记文件")
        return

    print(f"📁 找到 {len(all_files)} 个文件")
    print(f"🎯 开始整理...\n")

    # 创建索引
    index_content = f"# Get笔记 CFA 相关笔记索引\n\n"
    index_content += f"**导出时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    index_content += f"**源目录**: {SOURCE_DIR}\n\n"
    index_content += f"---\n\n"

    # 处理每个文件
    cfa_count = 0
    for i, filepath in enumerate(all_files, 1):
        filename = os.path.basename(filepath)
        name, ext = os.path.splitext(filename)

        # 读取文件内容，判断是否与 CFA 相关
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # 检查是否包含 CFA 相关关键词
        cfa_keywords = ['CFA', 'cfa', '企业合并', '权益法', 'Acquisition',
                       '财务报表', 'FRA', 'Equity', 'Fixed Income',
                       'Derivatives', 'Portfolio', '品职', 'PZ老师']

        is_cfa_related = any(keyword in content for keyword in cfa_keywords)

        if is_cfa_related:
            cfa_count += 1
            # 复制到目标目录
            target_file = os.path.join(TARGET_DIR, f"{datetime.now().strftime('%y%m%d')} {filename}")
            shutil.copy2(filepath, target_file)

            # 添加到索引
            index_content += f"## {cfa_count}. {name}\n\n"
            index_content += f"**文件名**: `{filename}`\n"
            index_content += f"**导出文件**: `{os.path.basename(target_file)}`\n"
            index_content += f"**大小**: {os.path.getsize(filepath)} bytes\n\n"

            # 提取摘要（前200字符）
            summary = content.replace('\n', ' ').strip()[:200]
            index_content += f"**摘要**: {summary}...\n\n"
            index_content += f"---\n\n"

            print(f"✅ [{cfa_count}] {filename}")
        else:
            print(f"⏭️  跳过: {filename} (非CFA相关)")

    # 保存索引
    index_file = os.path.join(TARGET_DIR, "GetNotes-CFA笔记索引.md")
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(index_content)

    print(f"\n🎉 整理完成！")
    print(f"📊 总计: {len(all_files)} 个文件")
    print(f"✅ CFA相关: {cfa_count} 个文件")
    print(f"📁 目标目录: {TARGET_DIR}")
    print(f"📋 索引文件: {index_file}")

def main():
    """主函数"""
    if len(os.sys.argv) < 2:
        print("🔧 Get笔记导出文件整理工具")
        print("\n使用方法:")
        print("  python3 organize_getnote_export.py <导出文件目录>")
        print("\n示例:")
        print('  python3 organize_getnote_export.py "~/Desktop/GetNotes导出"')
        print("\n或者直接运行此脚本，然后输入目录路径:")
        return

    source_path = os.sys.argv[1]
    organize_notes(source_path)

if __name__ == "__main__":
    main()
