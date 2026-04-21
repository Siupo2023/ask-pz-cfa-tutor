#!/usr/bin/env python3
"""
Get笔记导出工具
导出 CFA 相关笔记到 ask-pz references 目录
"""

import os
import json
import requests
from datetime import datetime

# API 配置
API_KEY = os.getenv("GETNOTE_API_KEY")
BASE_URL = "https://open-api.biji.com/getnote/openapi"

# 输出目录
OUTPUT_DIR = os.path.expanduser("~/Library/Mobile Documents/iCloud~com~logseq~logseq/Documents/skills-hub/skills/personal/ask-pz/references/GetNotes导出")

def search_notes(keyword="CFA"):
    """搜索笔记"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # 尝试多个搜索端点
    endpoints = [
        f"{BASE_URL}/note/search?keyword={keyword}&pageSize=100",
        f"{BASE_URL}/notes?search={keyword}&limit=100",
        f"{BASE_URL}/v1/notes?q={keyword}"
    ]

    for endpoint in endpoints:
        try:
            print(f"尝试端点: {endpoint}")
            response = requests.get(endpoint, headers=headers, timeout=10)

            if response.status_code == 200:
                print(f"✅ 成功！状态码: {response.status_code}")
                return response.json()
            else:
                print(f"❌ 失败。状态码: {response.status_code}")
                print(f"响应: {response.text[:200]}")
        except Exception as e:
            print(f"❌ 异常: {e}")

    return None

def export_notes(notes_data):
    """导出笔记到 Markdown 文件"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 创建索引文件
    index_file = os.path.join(OUTPUT_DIR, "GetNotes-CFA笔记索引.md")

    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(f"# Get笔记 CFA 相关笔记索引\n\n")
        f.write(f"导出时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"---\n\n")

        # 解析笔记数据（需要根据实际 API 响应调整）
        if isinstance(notes_data, dict):
            notes = notes_data.get('data', notes_data.get('notes', []))
        elif isinstance(notes_data, list):
            notes = notes_data
        else:
            notes = []

        print(f"找到 {len(notes)} 条笔记")

        for i, note in enumerate(notes, 1):
            title = note.get('title', note.get('name', f'笔记{i}'))
            content = note.get('content', note.get('body', ''))
            note_id = note.get('id', note.get('_id', str(i)))

            f.write(f"## {i}. {title}\n\n")
            f.write(f"**ID**: {note_id}\n\n")
            f.write(f"**导出时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            # 保存单独的笔记文件
            filename = f"{datetime.now().strftime('%y%m%d')} {title}.md"
            filepath = os.path.join(OUTPUT_DIR, filename)

            with open(filepath, 'w', encoding='utf-8') as note_file:
                note_file.write(f"# {title}\n\n")
                note_file.write(f"**来源**: Get笔记\n")
                note_file.write(f"**ID**: {note_id}\n")
                note_file.write(f"**导出时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                note_file.write(f"---\n\n")
                note_file.write(content)

            f.write(f"📄 [查看完整笔记]({filename})\n\n")
            f.write(f"**摘要**: {content[:100]}...\n\n")
            f.write(f"---\n\n")

            print(f"✅ 已导出: {title}")

    print(f"\n🎉 导出完成！")
    print(f"📁 输出目录: {OUTPUT_DIR}")
    print(f"📋 索引文件: {index_file}")

def main():
    """主函数"""
    print("🔍 Get笔记导出工具")
    print("=" * 50)

    if not API_KEY:
        print("❌ 错误: 未设置 GETNOTE_API_KEY 环境变量")
        print("请先设置: export GETNOTE_API_KEY='your_api_key'")
        return

    print(f"📑 搜索关键词: CFA")
    print(f"🔑 API Key: {API_KEY[:20]}...")

    # 搜索笔记
    notes_data = search_notes("CFA")

    if notes_data:
        print("✅ 搜索成功！")
        export_notes(notes_data)
    else:
        print("❌ 搜索失败，请检查 API Key 和网络连接")
        print("\n💡 建议：")
        print("1. 检查 Get笔记 API Key 是否正确")
        print("2. 确认网络连接正常")
        print("3. 或者使用 Get笔记 客户端手动导出")

if __name__ == "__main__":
    main()
