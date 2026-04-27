#!/bin/bash
# ask-pz skill 同步脚本
# 用途：在两台电脑间无痛同步学习进展

set -e  # 遇到错误立即退出

echo "🔄 ask-pz skill 同步脚本"
echo "===================="

# 颜色定义
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Step 1: 拉取最新更改
echo ""
echo "📥 Step 1: 从 GitHub 拉取最新更改..."
git pull origin master

# Step 2: 检查是否有本地更改
if [ -n "$(git status --porcelain)" ]; then
    echo ""
    echo "📝 检测到本地更改："
    git status --short

    echo ""
    read -p "💡 是否要提交这些更改？(y/n): " -n 1 -r
    echo

    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo ""
        echo "📤 Step 2: 提交并推送更改..."

        # 添加所有更改
        git add -A

        # 自动生成提交消息
        read -p "📝 请输入提交消息 (留空使用默认): " commit_msg
        if [ -z "$commit_msg" ]; then
            commit_msg="update: 学习进展更新 - $(date '+%Y-%m-%d %H:%M')"
        fi

        git commit -m "$commit_msg"
        git push origin master

        echo -e "${GREEN}✅ 同步完成！${NC}"
    else
        echo -e "${YELLOW}⚠️  跳过提交，但已拉取最新更改${NC}"
    fi
else
    echo -e "${GREEN}✅ 已经是最新版本${NC}"
fi

echo ""
echo "🎯 同步完成！"
echo ""
echo "📚 当前学习进度："
if [ -f "LEARNING_LOG.md" ]; then
    head -20 LEARNING_LOG.md | grep -E "^\||^\*"
else
    echo "   (暂无学习日志)"
fi
