#!/usr/bin/env python3
"""
Get笔记批量CFA笔记导出工具
批量导出所有CFA相关笔记到ask-pz references
"""

import os
import re
import glob
from pathlib import Path
from datetime import datetime

# 源目录和目标目录
SOURCE_DIR = "/Volumes/小宝的硬盘/get 笔记下载/voicenotes_202604210907_getnotes_archive_1a79b37a0004a708trO0CxBW/notes"
TARGET_DIR = os.path.expanduser("~/Library/Mobile Documents/iCloud~com~logseq~logseq/Documents/skills-hub/skills/personal/ask-pz/references/GetNotes导出")

# CFA 相关关键词（扩展版）
CFA_KEYWORDS = [
    'CFA', 'cfa', '品职', 'PZ老师', '李斯克',
    '企业合并', '权益法', 'Acquisition Method', '购买法',
    '财务报表', 'FRA', 'Financial Reporting', 'IFRS',
    'Equity', '股票', '权益', '估值',
    'Fixed Income', '固定收益', '债券',
    'Derivatives', '衍生品', '期货', '期权', '互换',
    'Portfolio', '组合管理', '投资组合',
    'Quantitative', 'Quant', '数量方法', '统计',
    'Economics', '经济学', '宏观', '微观',
    'Corporate Issuers', '公司发行人', '公司金融',
    'Ethics', '道德', '职业伦理',
    'Alternative Investments', '另类投资', 'PE', 'VC', '房地产', '大宗商品',
    '养老金', '职工薪酬', '租赁', '所得税',
    '现金流', '现值', '折现',
    '比率', '财务比率',
    '商誉', ' goodwill',
    '长期股权投资',
    '合并报表',
    '公允价值',
    'WACC', '加权平均资本成本',
    'CAPM', '资本资产定价模型',
    '贝塔', 'beta',
    '机器学习', 'ML',
    '时间序列',
    '概率', '统计'
]

# 科目分类规则
SUBJECT_MAPPING = {
    'FRA': ['财务报表', 'FRA', '企业合并', '权益法', '职工薪酬', '养老金', '租赁', '所得税', '商誉', '合并报表', '公允价值', '现金流', '比率', 'WACC', '长期股权投资'],
    'Equity': ['股票', '权益', 'Equity', '估值', 'CAPM', '贝塔', 'beta', '股权风险溢价'],
    'FixedIncome': ['固定收益', 'Fixed Income', '债券', '久期', '凸性', '利率'],
    'Derivatives': ['衍生品', 'Derivatives', '期货', '期权', '互换', '远期'],
    'Quant': ['数量方法', 'Quant', '统计', '概率', '机器学习', 'ML', '时间序列', '回归'],
    'Economics': ['经济学', 'Economics', '宏观', '微观', '通胀', 'GDP', '汇率'],
    'Portfolio': ['组合管理', 'Portfolio', '投资组合', 'CAPM', 'WACC'],
    'AltInvestments': ['另类投资', 'PE', 'VC', '房地产', '大宗商品', '对冲基金'],
    'CorporateIssuers': ['公司发行人', '公司金融', '资本结构', '股利', '回购'],
    'Ethics': ['道德', 'Ethics', '职业伦理', '利益冲突'],
}

def extract_title_from_html(html_content):
    """从HTML中提取标题"""
    title_patterns = [
        r'<title>(.*?)</title>',
        r'<h1[^>]*>(.*?)</h1>',
        r'"title"\s*:\s*"([^"]*)"',
    ]

    for pattern in title_patterns:
        match = re.search(pattern, html_content, re.IGNORECASE | re.DOTALL)
        if match:
            title = match.group(1)
            title = re.sub(r'<[^>]+>', '', title)
            title = title.strip()
            if title and len(title) > 2:
                return title

    return "未命名笔记"

def extract_created_time(html_content):
    """从HTML中提取创建时间"""
    patterns = [
        r'创建于\s*(\d{4}\s*\d{1,2}\s*\d{1,2}\s*\d{1,2}:\d{2}:\d{2})',
        r'"created_at"\s*:\s*"([^"]*)"',
    ]

    for pattern in patterns:
        match = re.search(pattern, html_content)
        if match:
            return match.group(1)

    return datetime.now().strftime("%Y-%m-%d")

def classify_subject(content):
    """根据内容分类科目"""
    content_lower = content.lower()

    for subject, keywords in SUBJECT_MAPPING.items():
        for keyword in keywords:
            if keyword.lower() in content_lower:
                return subject

    return 'Other'  # 默认分类

def html_to_text(html_content):
    """将HTML转换为纯文本"""
    # 移除script和style
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # 转换HTML标签
    content = html_content
    content = re.sub(r'<h1[^>]*>(.*?)</h1>', r'\n# \1\n', content, flags=re.DOTALL)
    content = re.sub(r'<h2[^>]*>(.*?)</h2>', r'\n## \1\n', content, flags=re.DOTALL)
    content = re.sub(r'<h3[^>]*>(.*?)</h3>', r'\n### \1\n', content, flags=re.DOTALL)
    content = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', content, flags=re.DOTALL)
    content = re.sub(r'<br\s*/?>', '\n', content)
    content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1', content, flags=re.DOTALL)
    content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', content, flags=re.DOTALL)
    content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', content, flags=re.DOTALL)
    content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', content, flags=re.DOTALL)
    content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', content, flags=re.DOTALL)

    # 移除所有剩余HTML标签
    content = re.sub(r'<[^>]+>', ' ', content)

    # 清理空白
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    content = re.sub(r' +', ' ', content)

    return content.strip()

def is_cfa_related(content):
    """判断是否与CFA相关"""
    content_lower = content.lower()
    for keyword in CFA_KEYWORDS:
        if keyword.lower() in content_lower:
            return True
    return False

def export_all_cfa_notes():
    """导出所有CFA相关笔记"""

    print("🚀 开始批量导出CFA相关笔记...")
    print("=" * 60)

    # 创建目标目录结构
    os.makedirs(TARGET_DIR, exist_ok=True)

    # 按科目创建子目录
    for subject in SUBJECT_MAPPING.keys():
        subject_dir = os.path.join(TARGET_DIR, subject)
        os.makedirs(subject_dir, exist_ok=True)

    # 创建 Other 目录
    other_dir = os.path.join(TARGET_DIR, 'Other')
    os.makedirs(other_dir, exist_ok=True)

    # 获取所有HTML文件
    html_files = glob.glob(os.path.join(SOURCE_DIR, "*.html"))

    print(f"📁 总计 {len(html_files)} 个笔记文件")
    print()

    # 统计信息
    stats = {
        'total': len(html_files),
        'cfa_related': 0,
        'exported': 0,
        'subjects': {subject: 0 for subject in SUBJECT_MAPPING.keys()},
        'other': 0,
        'failed': 0
    }

    # 已导出的高价值笔记（跳过）
    high_value_notes = [
        "23469f09999e5587a8279006b19d09ae.html",
        "d54c0ded48a39a3884c41a830f9ddc7a.html",
        "73bcb76646c2ea61662381372fb2c002.html",
        "5b9f9145b07d2a3b5d8df9c03f8bc8c9.html",
        "a21a9cc9f66ccf2afb1335dcc76015ad.html",
        "424645249186895b493597e2ef655c24.html",
        "d631cb6476ccdc026189912cf4eb4061.html",
        "89c1e931d1eb4cb2949f74f228164571.html",
        "e21594c54574c6679552cb897f067cdd.html",
        "28abe804b16a81bc61920f7552cd7f99.html",
    ]

    # 处理每个笔记
    for i, html_file in enumerate(html_files, 1):
        filename = os.path.basename(html_file)

        # 跳过已导出的高价值笔记
        if filename in high_value_notes:
            continue

        try:
            # 读取文件
            with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
                html_content = f.read()

            # 判断是否CFA相关
            if not is_cfa_related(html_content):
                continue

            stats['cfa_related'] += 1

            # 提取信息
            title = extract_title_from_html(html_content)
            created_time = extract_created_time(html_content)
            text_content = html_to_text(html_content)

            # 分类科目
            subject = classify_subject(text_content)

            # 生成文件名
            date_prefix = datetime.now().strftime('%y%m%d')
            safe_title = re.sub(r'[^\w\s-]', '', title)[:40]
            md_filename = f"{date_prefix} {safe_title}.md"

            # 确定保存目录
            if subject == 'Other':
                save_dir = other_dir
                stats['other'] += 1
            else:
                save_dir = os.path.join(TARGET_DIR, subject)
                stats['subjects'][subject] += 1

            md_file = os.path.join(save_dir, md_filename)

            # 写入Markdown文件
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(f"# {title}\n\n")
                f.write(f"**来源**: Get笔记\n")
                f.write(f"**原文件**: `{filename}`\n")
                f.write(f"**创建时间**: {created_time}\n")
                f.write(f"**科目**: {subject}\n")
                f.write(f"**导出时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write("---\n\n")
                f.write(text_content[:3000])  # 限制内容长度，避免文件过大

            stats['exported'] += 1

            # 进度显示
            if stats['exported'] % 10 == 0:
                print(f"✅ 已导出: {stats['exported']} 个笔记 (当前: {subject})")

        except Exception as e:
            stats['failed'] += 1
            print(f"❌ 处理失败 {filename}: {e}")

    # 生成统计报告
    print("\n" + "=" * 60)
    print("📊 导出统计:")
    print(f"  总笔记数: {stats['total']}")
    print(f"  CFA相关: {stats['cfa_related']}")
    print(f"  成功导出: {stats['exported']}")
    print(f"  失败: {stats['failed']}")
    print()

    print("📚 按科目分类:")
    for subject, count in stats['subjects'].items():
        if count > 0:
            print(f"  {subject}: {count} 个")
    if stats['other'] > 0:
        print(f"  Other: {stats['other']} 个")

    print()
    print(f"📁 保存位置: {TARGET_DIR}")

    # 生成总索引
    generate_master_index(stats)

    return stats

def generate_master_index(stats):
    """生成主索引文件"""

    index_file = os.path.join(TARGET_DIR, "Get笔记-完整导出索引.md")

    with open(index_file, 'w', encoding='utf-8') as f:
        f.write("# Get笔记 CFA学习笔记完整导出索引\n\n")
        f.write(f"**导出时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("---\n\n")

        f.write("## 📊 导出统计\n\n")
        f.write(f"- ✅ **成功导出**: {stats['exported']} 个笔记\n")
        f.write(f"- 📝 **CFA相关**: {stats['cfa_related']} 个笔记\n")
        f.write(f"- ❌ **失败**: {stats['failed']} 个笔记\n\n")

        f.write("## 📚 按科目分类\n\n")

        # 高价值笔记
        f.write("### 💎 高价值笔记（已单独导出）\n\n")
        f.write("详见：`Get笔记-高价值CFA笔记索引.md`\n\n")

        # 按科目统计
        f.write("### 📖 各科目笔记\n\n")
        for subject, count in stats['subjects'].items():
            if count > 0:
                f.write(f"- **{subject}**: {count} 个笔记\n")

        if stats['other'] > 0:
            f.write(f"- **Other**: {stats['other']} 个笔记\n")

        f.write("\n---\n\n")

        f.write("## 📖 使用说明\n\n")
        f.write("### 导航方式\n\n")
        f.write("1. **按科目浏览**: 进入对应科目目录查看笔记\n")
        f.write("2. **查看索引**: 参考 `Get笔记-高价值CFA笔记索引.md`\n")
        f.write("3. **搜索**: 使用 ask-pz 技能直接搜索知识点\n\n")

        f.write("### 科目对照\n\n")
        f.write("| 科目代码 | 科目名称 | CFA权重 |\n")
        f.write("|---------|---------|----------|\n")
        f.write("| FRA | 财务报表分析 | 10-15% |\n")
        f.write("| Equity | 股票 | 10-15% |\n")
        f.write("| FixedIncome | 固定收益 | 10-15% |\n")
        f.write("| Derivatives | 衍生品 | 5-10% |\n")
        f.write("| Quant | 数量方法 | 5-10% |\n")
        f.write("| Economics | 经济学 | 5-10% |\n")
        f.write("| Portfolio | 组合管理 | 5-15% |\n")
        f.write("| AltInvestments | 另类投资 | 5-15% |\n")
        f.write("| CorporateIssuers | 公司发行人 | 5-10% |\n")
        f.write("| Ethics | 道德 | 10-15% |\n")
        f.write("| Other | 其他/综合 | - |\n")

    print(f"\n📋 主索引已生成: {index_file}")

if __name__ == "__main__":
    stats = export_all_cfa_notes()

    print("\n" + "=" * 60)
    print("🎉 批量导出完成！")
    print(f"\n✅ 成功导出 {stats['exported']} 个CFA相关笔记")
    print(f"📁 所有笔记已按科目分类整理")
    print(f"📋 详细索引已生成")
