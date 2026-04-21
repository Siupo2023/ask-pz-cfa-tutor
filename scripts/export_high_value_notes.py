#!/usr/bin/env python3
"""
Get笔记高价值CFA笔记导出工具
将高价值笔记转换为Markdown并整理到ask-pz references
"""

import os
import re
import glob
import html
from pathlib import Path
from datetime import datetime

# 源目录和目标目录
SOURCE_DIR = "/Volumes/小宝的硬盘/get 笔记下载/voicenotes_202604210907_getnotes_archive_1a79b37a0004a708trO0CxBW/notes"
TARGET_DIR = os.path.expanduser("~/Library/Mobile Documents/iCloud~com~logseq~logseq/Documents/skills-hub/skills/personal/ask-pz/references/GetNotes导出")

# 高价值笔记阈值（字节）
MIN_SIZE = 50000  # 50KB

# 高价值笔记列表（从分析结果中提取）
HIGH_VALUE_NOTES = [
    "23469f09999e5587a8279006b19d09ae.html",  # 企业合并 - 111.7 KB
    "d54c0ded48a39a3884c41a830f9ddc7a.html",  # 机器学习 - 104.5 KB
    "73bcb76646c2ea61662381372fb2c002.html",  # 权益法 - 97.8 KB
    "5b9f9145b07d2a3b5d8df9c03f8bc8c9.html",  # 长期股权投资 - 90.4 KB
    "a21a9cc9f66ccf2afb1335dcc76015ad.html",  # 职工薪酬 - 89.6 KB
    "424645249186895b493597e2ef655c24.html",  # 随机森林 - 87.2 KB
    "d631cb6476ccdc026189912cf4eb4061.html",  # 集成学习 - 86.2 KB
    "89c1e931d1eb4cb2949f74f228164571.html",  # 决策树 - 716.5 KB
    "e21594c54574c6679552cb897f067cdd.html",  # 股权风险溢价 - 129.8 KB
    "28abe804b16a81bc61920f7552cd7f99.html",  # 公司经营 - 124.0 KB
]

def extract_title_from_html(html_content):
    """从HTML中提取标题"""
    # 尝试多种方式提取标题
    title_patterns = [
        r'<title>(.*?)</title>',
        r'<h1[^>]*>(.*?)</h1>',
        r'"title"\s*:\s*"([^"]*)"',
    ]

    for pattern in title_patterns:
        match = re.search(pattern, html_content, re.IGNORECASE | re.DOTALL)
        if match:
            title = match.group(1)
            # 清理标题
            title = re.sub(r'<[^>]+>', '', title)
            title = html.unescape(title)
            title = title.strip()
            if title and len(title) > 2:
                return title

    return "未命名笔记"

def extract_created_time(html_content):
    """从HTML中提取创建时间"""
    # 查找创建时间
    patterns = [
        r'创建于\s*(\d{4}\s*\d{1,2}\s*\d{1,2}\s*\d{1,2}:\d{2}:\d{2})',
        r'"created_at"\s*:\s*"([^"]*)"',
        r'"time"\s*:\s*"([^"]*)"',
    ]

    for pattern in patterns:
        match = re.search(pattern, html_content)
        if match:
            return match.group(1)

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def extract_tags(html_content):
    """从HTML中提取标签"""
    tags = []

    # 查找标签
    patterns = [
        r'"tags"\s*:\s*\[([^\]]+)\]',
        r'标签\s*[:：]\s*([^\n]+)',
    ]

    for pattern in patterns:
        matches = re.finditer(pattern, html_content)
        for match in matches:
            tags_str = match.group(1)
            # 提取标签内容
            tag_matches = re.findall(r'"([^"]*)"', tags_str)
            tags.extend(tag_matches)

    return list(set(tags))  # 去重

def html_to_markdown(html_file):
    """将HTML文件转换为Markdown"""
    try:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            html_content = f.read()

        # 提取元数据
        title = extract_title_from_html(html_content)
        created_time = extract_created_time(html_content)
        tags = extract_tags(html_content)

        # 清理HTML内容
        # 移除script和style标签
        html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
        html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

        # 转换HTML标签为Markdown
        content = html_content

        # 标题转换
        content = re.sub(r'<h1[^>]*>(.*?)</h1>', r'\n# \1\n', content, flags=re.DOTALL)
        content = re.sub(r'<h2[^>]*>(.*?)</h2>', r'\n## \1\n', content, flags=re.DOTALL)
        content = re.sub(r'<h3[^>]*>(.*?)</h3>', r'\n### \1\n', content, flags=re.DOTALL)

        # 段落和换行
        content = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', content, flags=re.DOTALL)
        content = re.sub(r'<br\s*/?>', '\n', content)

        # 列表转换
        content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', content, flags=re.DOTALL)

        # 强调和斜体
        content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', content, flags=re.DOTALL)
        content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', content, flags=re.DOTALL)
        content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', content, flags=re.DOTALL)
        content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', content, flags=re.DOTALL)

        # 代码块
        content = re.sub(r'<pre[^>]*>(.*?)</pre>', r'```\n\1\n```\n', content, flags=re.DOTALL)
        content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', content, flags=re.DOTALL)

        # 移除所有剩余的HTML标签
        content = re.sub(r'<[^>]+>', ' ', content)

        # HTML实体解码
        content = html.unescape(content)

        # 清理多余空白
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        content = re.sub(r' +', ' ', content)

        # 移除CSS和JS代码残留
        content = re.sub(r'body\s*\{[^}]*\}', '', content)
        content = re.sub(r'function\s*\([^)]*\)\s*\{[^}]*\}', '', content)

        return {
            'title': title,
            'content': content.strip(),
            'created_time': created_time,
            'tags': tags
        }

    except Exception as e:
        print(f"❌ 转换文件错误 {html_file}: {e}")
        return None

def export_high_value_notes():
    """导出高价值笔记"""

    print("🚀 开始导出高价值CFA笔记...")
    print("=" * 60)

    # 创建目标目录
    os.makedirs(TARGET_DIR, exist_ok=True)

    exported_notes = []

    # 处理每个高价值笔记
    for i, filename in enumerate(HIGH_VALUE_NOTES, 1):
        html_file = os.path.join(SOURCE_DIR, filename)

        if not os.path.exists(html_file):
            print(f"⚠️  文件不存在: {filename}")
            continue

        print(f"\n[{i}/{len(HIGH_VALUE_NOTES)}] 处理: {filename}")

        # 转换为Markdown
        md_data = html_to_markdown(html_file)

        if not md_data:
            print(f"❌ 转换失败: {filename}")
            continue

        # 生成Markdown文件名
        # 使用日期前缀 + 标题
        date_prefix = datetime.now().strftime('%y%m%d')
        safe_title = re.sub(r'[^\w\s-]', '', md_data['title'])[:50]
        md_filename = f"{date_prefix} {safe_title}.md"
        md_file = os.path.join(TARGET_DIR, md_filename)

        # 写入Markdown文件
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(f"# {md_data['title']}\n\n")
            f.write(f"**来源**: Get笔记\n")
            f.write(f"**原文件**: `{filename}`\n")
            f.write(f"**创建时间**: {md_data['created_time']}\n")

            if md_data['tags']:
                f.write(f"**标签**: {', '.join(md_data['tags'])}\n")

            f.write(f"**导出时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("---\n\n")
            f.write(md_data['content'])

        exported_notes.append({
            'filename': md_filename,
            'title': md_data['title'],
            'original_file': filename,
            'created_time': md_data['created_time'],
            'tags': md_data['tags']
        })

        print(f"✅ 已导出: {md_filename}")

    # 生成索引文件
    generate_index(exported_notes)

    print("\n" + "=" * 60)
    print("🎉 导出完成！")
    print(f"\n✅ 成功导出 {len(exported_notes)} 个高价值笔记")
    print(f"📁 保存位置: {TARGET_DIR}")

    return exported_notes

def generate_index(exported_notes):
    """生成索引文件"""

    index_file = os.path.join(TARGET_DIR, "Get笔记-高价值CFA笔记索引.md")

    with open(index_file, 'w', encoding='utf-8') as f:
        f.write("# Get笔记 高价值CFA笔记索引\n\n")
        f.write(f"**导出时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**总计**: {len(exported_notes)} 个笔记\n\n")
        f.write("---\n\n")

        # 笔记列表
        for i, note in enumerate(exported_notes, 1):
            f.write(f"## {i}. {note['title']}\n\n")
            f.write(f"**文件**: `{note['filename']}`\n")
            f.write(f"**原文件**: `{note['original_file']}`\n")
            f.write(f"**创建时间**: {note['created_time']}\n")

            if note['tags']:
                f.write(f"**标签**: {', '.join(note['tags'])}\n")

            f.write(f"\n---\n\n")

        # 使用说明
        f.write("## 📖 使用说明\n\n")
        f.write("这些笔记已经整合到 ask-pz references 目录中，可以直接使用。\n\n")
        f.write("### 导入方式\n\n")
        f.write("1. 笔记已保存在 `GetNotes导出/` 子目录\n")
        f.write("2. 可以通过 ask-pz 技能直接引用\n")
        f.write("3. 建议定期更新索引\n\n")

    print(f"\n📋 索引文件已生成: {index_file}")

if __name__ == "__main__":
    export_high_value_notes()
