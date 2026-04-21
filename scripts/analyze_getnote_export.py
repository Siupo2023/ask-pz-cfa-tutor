#!/usr/bin/env python3
"""
Get笔记 CFA 笔记分析工具
分析导出的 Get笔记，识别 CFA 相关内容
"""

import os
import re
import glob
from pathlib import Path
from datetime import datetime

# 源目录和目标目录
SOURCE_DIR = "/Volumes/小宝的硬盘/get 笔记下载/voicenotes_202604210907_getnotes_archive_1a79b37a0004a708trO0CxBW/notes"
TARGET_DIR = os.path.expanduser("~/Library/Mobile Documents/iCloud~com~logseq~logseq/Documents/skills-hub/skills/personal/ask-pz/references/GetNotes导出")

# CFA 相关关键词
CFA_KEYWORDS = [
    'CFA', 'cfa',
    '企业合并', '权益法', 'Acquisition Method',
    '财务报表', 'FRA', 'Financial Reporting',
    'Equity', 'Fixed Income', 'Derivatives',
    'Portfolio', 'Quantitative', 'Economics',
    '品职', 'PZ老师', '李斯克',
    '衍生品', '固定收益', '股票',
    '公司发行人', '道德', 'Ethics',
    '另类投资', '组合管理'
]

def extract_html_content(html_file):
    """从 HTML 文件中提取文本内容"""
    try:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # 移除 HTML 标签
        content = re.sub(r'<[^>]+>', ' ', content)
        # 移除多余的空白
        content = re.sub(r'\s+', ' ', content)
        return content.strip()
    except Exception as e:
        print(f"读取文件错误 {html_file}: {e}")
        return ""

def is_cfa_related(content):
    """判断内容是否与 CFA 相关"""
    content_lower = content.lower()
    for keyword in CFA_KEYWORDS:
        if keyword.lower() in content_lower:
            return True, keyword
    return False, None

def get_content_summary(content, max_length=200):
    """获取内容摘要"""
    # 移除特殊字符
    content = re.sub(r'[^\w\s\u4e00-\u9fff.,!?;:]', ' ', content)
    return content[:max_length].strip()

def analyze_notes():
    """分析所有笔记"""
    print("🔍 开始分析 Get笔记...")
    print("=" * 60)

    # 创建目标目录
    os.makedirs(TARGET_DIR, exist_ok=True)

    # 获取所有 HTML 文件
    html_files = glob.glob(os.path.join(SOURCE_DIR, "*.html"))

    print(f"📁 总计 {len(html_files)} 个笔记文件")
    print()

    # 分析结果
    cfa_notes = []
    other_notes = []

    for i, html_file in enumerate(html_files, 1):
        filename = os.path.basename(html_file)

        # 提取内容
        content = extract_html_content(html_file)

        if not content:
            continue

        # 判断是否 CFA 相关
        is_cfa, matched_keyword = is_cfa_related(content)

        note_info = {
            'filename': filename,
            'filepath': html_file,
            'content': content,
            'matched_keyword': matched_keyword,
            'size': os.path.getsize(html_file)
        }

        if is_cfa:
            cfa_notes.append(note_info)
        else:
            other_notes.append(note_info)

        # 进度显示
        if i % 50 == 0:
            print(f"处理进度: {i}/{len(html_files)}")

    print()
    print("📊 分析结果:")
    print(f"  ✅ CFA 相关笔记: {len(cfa_notes)} 个")
    print(f"  📝 其他笔记: {len(other_notes)} 个")
    print()

    # 生成报告
    generate_report(cfa_notes, other_notes)

    return cfa_notes, other_notes

def generate_report(cfa_notes, other_notes):
    """生成分析报告"""

    # 创建索引文件
    index_file = os.path.join(TARGET_DIR, "Get笔记-CFA笔记分析报告.md")

    with open(index_file, 'w', encoding='utf-8') as f:
        f.write("# Get笔记 CFA 学习笔记分析报告\n\n")
        f.write(f"**分析时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**源目录**: `{SOURCE_DIR}`\n\n")
        f.write("---\n\n")

        # 统计摘要
        f.write("## 📊 统计摘要\n\n")
        f.write(f"- ✅ **CFA 相关笔记**: {len(cfa_notes)} 个\n")
        f.write(f"- 📝 **其他笔记**: {len(other_notes)} 个\n")
        f.write(f"- 📁 **总计笔记**: {len(cfa_notes) + len(other_notes)} 个\n\n")

        # 关键词分布
        f.write("## 🔍 关键词分布\n\n")
        keyword_count = {}
        for note in cfa_notes:
            keyword = note['matched_keyword']
            keyword_count[keyword] = keyword_count.get(keyword, 0) + 1

        # 按频率排序
        sorted_keywords = sorted(keyword_count.items(), key=lambda x: x[1], reverse=True)

        for keyword, count in sorted_keywords:
            f.write(f"- **{keyword}**: {count} 个笔记\n")

        f.write("\n---\n\n")

        # CFA 笔记列表
        f.write("## ✅ CFA 相关笔记列表\n\n")

        for i, note in enumerate(cfa_notes, 1):
            filename = note['filename']
            matched_keyword = note['matched_keyword']
            summary = get_content_summary(note['content'], 150)
            size_kb = note['size'] / 1024

            f.write(f"### {i}. {filename}\n\n")
            f.write(f"**匹配关键词**: `{matched_keyword}`\n\n")
            f.write(f"**文件大小**: {size_kb:.1f} KB\n\n")
            f.write(f"**摘要**: {summary}...\n\n")
            f.write(f"---\n\n")

        # 推荐导出
        f.write("## 💡 推荐操作\n\n")
        f.write("### 高价值笔记（建议优先添加）\n\n")

        # 找出内容较长的高质量笔记
        high_value_notes = [n for n in cfa_notes if n['size'] > 5000]  # 大于 5KB
        high_value_notes.sort(key=lambda x: x['size'], reverse=True)

        for note in high_value_notes[:20]:  # 前 20 个
            filename = note['filename']
            matched_keyword = note['matched_keyword']
            size_kb = note['size'] / 1024

            f.write(f"- **{filename}** ({size_kb:.1f} KB) - `{matched_keyword}`\n")

        f.write("\n### 下一步\n\n")
        f.write("1. ✅ 高价值笔记已自动标记\n")
        f.write("2. 📋 可以手动检查其他笔记\n")
        f.write("3. 🚀 确认后批量导出到 ask-pz references\n\n")

    print(f"📋 分析报告已生成: {index_file}")
    print()

    # 显示高价值笔记摘要
    print("💎 高价值 CFA 笔记（内容 > 5KB）:")
    print("-" * 60)

    for note in high_value_notes[:10]:
        filename = note['filename']
        matched_keyword = note['matched_keyword']
        size_kb = note['size'] / 1024
        summary = get_content_summary(note['content'], 80)

        print(f"\n📄 {filename} ({size_kb:.1f} KB)")
        print(f"   关键词: {matched_keyword}")
        print(f"   摘要: {summary}...")

if __name__ == "__main__":
    cfa_notes, other_notes = analyze_notes()

    print("\n" + "=" * 60)
    print("🎉 分析完成！")
    print(f"\n✅ 找到 {len(cfa_notes)} 个 CFA 相关笔记")
    print(f"📋 详细报告已保存到: {TARGET_DIR}/Get笔记-CFA笔记分析报告.md")
