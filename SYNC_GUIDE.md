# 两台电脑无痛同步指南

## 🎯 目标

在 macOS 和 Linux 之间无缝同步：
- **ask-pz skill**（CFA 学习进展）
- **llm-wiki**（Wiki 知识库）

---

## 📋 方案架构

```
macOS                      Linux
ask-pz/    ←→  GitHub  ←→  ask-pz/
llm-wiki/  ←→  GitHub  ←→  llm-wiki/
```

**关键文件**：
- `LEARNING_LOG.md` - 学习进展日志（会同步）
- `sync.sh` - 自动同步脚本（会同步）
- `sessions/` - 会话记录（不同步）
- `progress/` - 详细追踪（不同步）

---

## 🚀 快速开始

### 在 Linux 电脑上首次设置

```bash
# 1. 克隆 ask-pz skill
cd ~/.claude/skills/
git clone https://github.com/Siupo2023/ask-pz-cfa-tutor.git ask-pz
cd ask-pz

# 2. 查看学习进展
cat LEARNING_LOG.md

# 3. 运行同步脚本（测试）
./sync.sh
```

---

## 🔄 日常使用

### macOS → Linux（学习后同步）

**在 macOS 上**：
```bash
cd ~/.claude/skills/ask-pz

# 学习后更新日志
vim LEARNING_LOG.md  # 或用任何编辑器

# 同步到 GitHub
./sync.sh
```

**在 Linux 上**：
```bash
cd ~/.claude/skills/ask-pz

# 拉取最新进展
git pull origin master

# 查看学习进展
cat LEARNING_LOG.md
```

---

### Linux → macOS（继续学习后同步）

**在 Linux 上**：
```bash
cd ~/.claude/skills/ask-pz

# 学习后更新日志
vim LEARNING_LOG.md

# 同步到 GitHub
./sync.sh
```

**在 macOS 上**：
```bash
cd ~/.claude/skills/ask-pz

# 拉取最新进展
git pull origin master

# 查看学习进展
cat LEARNING_LOG.md
```

---

## 📚 llm-wiki 同步

**同样使用 Git 同步**：

```bash
# 在 macOS 上
cd ~/llm-wiki
git add .
git commit -m "update: 添加新知识"
git push origin master

# 在 Linux 上
cd ~/llm-wiki
git pull origin master
```

---

## 🎯 sync.sh 脚本功能

### 自动执行

1. ✅ **拉取最新更改** - `git pull`
2. ✅ **检测本地更改** - `git status`
3. ✅ **询问是否提交** - 交互式确认
4. ✅ **自动生成提交消息** - 默认格式
5. ✅ **推送到 GitHub** - `git push`
6. ✅ **显示学习进度** - 读取 LEARNING_LOG.md

### 使用示例

```bash
# 基本使用
./sync.sh

# 手动输入提交消息
./sync.sh
# > 📝 请输入提交消息 (留空使用默认):
# > 完成 FRA 权益法学习
```

---

## 📝 LEARNING_LOG.md 维护

### 更新频率

- **学习后**：记录新掌握的知识点
- **每周**：更新复习计划和进度
- **考试前**：查看已掌握内容，查漏补缺

### 更新内容

```markdown
## 2026-04-27 | FRA - 养老金

**核心概念**：
- ✅ 养老金是"延迟薪酬"
- ✅ PBO = 未来支付的现值
- ✅ Service Cost vs Interest Cost

**理解程度**: 70% 🟡
**记忆要点**: "养老金就像房贷，本金+利息"
```

---

## ⚠️ 注意事项

### 1. Git 冲突处理

**如果遇到冲突**：
```bash
# 查看冲突
git status

# 手动解决冲突文件
vim LEARNING_LOG.md

# 标记为已解决
git add LEARNING_LOG.md

# 完成合并
git commit
git push
```

### 2. 学习时机

**建议**：
- **macOS**：主要用于学习（有完整资料）
- **Linux**：用于复习和查看进展

### 3. 不同步的文件

**为什么 sessions/ 和 progress/ 不同步？**
- 这些文件是**动态的**，频繁更新
- 会在每次学习时修改
- 不同步可以避免大量 Git 提交

---

## 🎉 总结

### 无痛同步的关键

1. ✅ **使用 LEARNING_LOG.md** - 追踪关键进展
2. ✅ **使用 sync.sh** - 自动化同步流程
3. ✅ **定期同步** - 学习后立即同步
4. ✅ **查看 GitHub** - 在线查看学习历史

### 工作流

```
学习 → 更新日志 → 运行 sync.sh → GitHub
                ↓
            拉取最新 → 继续学习
```

---

**最后更新**: 2026-04-27
**维护者**: ask-pz skill
