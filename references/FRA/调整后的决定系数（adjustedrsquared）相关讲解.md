# 调整后的决定系数（adjustedrsquared）相关讲解

## 课程信息
- **领域**：CFA 财务报告分析
- **标签**：

---

## 笔记内容

### 📑 智能总结

#### 课程信息
- **授课时间**：2026-01-05 08:05:38
- **时长**：0小时24分钟
- **领域**：统计学 / 计量经济学

#### 知识精讲

本节课核心讲解了用于解决R²无法识别过拟合问题的修正指标：调整后R²（Adjusted R-squared），包括其公式推导、与R²的关系、核心性质及优缺点。

**调整后R²（Adjusted R-squared）的引入背景**
* **解决的问题**：普通R²（R-squared）无法识别模型过拟合（overfitting）问题，因为增加自变量（K）会导致R²非递减。
   - 🚩重点：过拟合是指模型因包含过多自变量（K过大）而过度拟合样本噪音，导致模型泛化能力下降。

**调整后R²的公式与原理**
* **公式推导**：基于普通R²的自由度修正。
   - *公式*：$$ Adjusted \ R^2 = 1 - \frac{SSE/(N-K-1)}{SST/(N-1)} $$
     其中：
     - SSE：残差平方和（Sum of Squared Errors）
     - SST：总平方和（Total Sum of Squares）
     - N：样本量
     - K：自变量个数（解释变量数量）
   - *补充说明*：修正逻辑是将SSE和SST分别除以各自的自由度（残差自由度N-K-1，总自由度N-1），从而引入对K的惩罚。
* **核心性质**：Adjusted R²与自变量个数K呈反向关系，K越大，Adjusted R²可能越小，从而实现对模型复杂度的惩罚。
   - 🚩重点：Adjusted R²的目标是寻找“拟合优度高且自变量少”的简约模型，其取值**越大越好**。

**调整后R²与普通R²的关系**
* **相等条件**：当K=0（无自变量）时，Adjusted R² = R²。
* **大小关系**：当K≥1时，Adjusted R² < R²，因为自由度修正项会降低指标值。
* **取值范围**：Adjusted R²可能小于0（当K过大时），而R²取值范围为[0,1]。
   - 🚩重点：考试可能考察“Adjusted R²是否可能小于0”，答案为**是**。

**调整后R²的经验法则**
* **新增自变量对Adjusted R²的影响**：当新增自变量X的T统计量绝对值>1时，Adjusted R²会上升；反之则下降。
   - *补充说明*：T统计量计算公式为 $$ t = \frac{\hat{\beta}_j}{SE(\hat{\beta}_j)} $$，其中$\hat{\beta}_j$为系数估计值，SE($\hat{\beta}_j$)为标准误。
   - 🚩重点：此法则仅为经验判断，T统计量>1不代表该自变量显著（假设检验需与临界值对比，如α=5%时约为2.1）。

**调整后R²的缺点**
* **缺乏清晰解释**：无法像R²那样解释为“模型解释Y变异的比例”。
* **无法判断系数显著性**：需通过T检验判断单个系数是否显著。
* **无法检验模型整体显著性**：需通过F检验判断模型整体是否显著。
   - 🚩重点：Adjusted R²的首要缺点是**缺乏清晰的经济含义**。

#### 📖 课堂实录

[00:00:08](https://getnotes.seek:8) **引入新指标的目的**
为解决R²无法识别过拟合（overfitting）的问题，引入三个指标：Adjusted R-squared、AIC、BIC。本节课重点讲解Adjusted R-squared。

[00:00:28](https://getnotes.seek:28) **Adjusted R-squared的公式记忆**
普通R²公式为 $ R^2 = 1 - \frac{SSE}{SST} $，但未考虑自由度。Adjusted R-squared通过修正自由度，将K（自变量个数）纳入考量。

[00:01:00](https://getnotes.seek:60) **自由度修正的原理**
计算均方（Mean Square）时需除以自由度：残差自由度为N-K-1，总自由度为N-1。因此Adjusted R-squared公式为 $ 1 - \frac{SSE/(N-K-1)}{SST/(N-1)} $。

[00:02:18](https://getnotes.seek:138) **对K的惩罚机制**
K（自变量个数）越大，分母N-K-1越小，导致 $ \frac{SSE/(N-K-1)}{SST/(N-1)} $ 越大，Adjusted R-squared越小，从而惩罚复杂模型，避免过拟合。

[00:05:58](https://getnotes.seek:358) **Adjusted R-squared的判断标准**
与R²一致，Adjusted R-squared越大越好，需同时兼顾拟合优度（SSE小）和模型简洁性（K小）。

[00:07:35](https://getnotes.seek:455) **Adjusted R-squared与R²的关系**
当K=0时两者相等；K≥1时Adjusted R-squared < R²。Adjusted R-squared可能为负（K过大时），而R²恒非负。

[00:12:16](https://getnotes.seek:736) **新增自变量的经验法则**
新增自变量X后，若其T统计量绝对值>1，Adjusted R-squared上升；反之下降。此为经验规律，不代表X显著（需与临界值对比）。

[00:18:08](https://getnotes.seek:1088) **T统计量与显著性的区别**
T统计量>1仅影响Adjusted R-squared，判断X是否显著需与T分布临界值（如α=5%时约2.1）对比，进行假设检验。

[00:21:45](https://getnotes.seek:1305) **Adjusted R-squared的缺点**
1. 缺乏清晰解释（无“解释变异比例”的含义）；
2. 无法判断系数显著性（需T检验）；
3. 无法检验模型整体显著性（需F检验）。

### 🖍️ 重点速览

#### 🚩 考点重点
- [00:02:34](https://getnotes.seek:154) **过拟合问题**：模型因K过大（自变量过多）导致过度拟合样本噪音，泛化能力差。Adjusted R-squared通过惩罚K解决此问题。
- [00:11:32](https://getnotes.seek:692) **Adjusted R-squared的取值**：可能小于0（当K过大时），而R²恒≥0。
- [00:12:33](https://getnotes.seek:753) **新增自变量的经验法则**：T统计量绝对值>1时，Adjusted R-squared上升；反之下降（仅为经验判断，不直接等同于显著性）。
- [00:21:58](https://getnotes.seek:1318) **Adjusted R-squared的首要缺点**：缺乏清晰的经济解释，无法像R²那样表述为“解释Y变异的比例”。

#### 💡 核心概念
- **Adjusted R-squared**：对普通R²进行自由度修正，引入对自变量个数K的惩罚，用于衡量模型拟合优度并避免过拟合的指标。
- **公式**：$$ Adjusted \ R^2 = 1 - \frac{SSE/(N-K-1)}{SST/(N-1)} $$
- **T统计量**：$$ t = \frac{\hat{\beta}_j}{SE(\hat{\beta}_j)} $$（用于判断系数估计的可靠性）

#### ✨ 课堂金句
- “我们希望指标能实现：K越大，指标越小，从而避免K过大导致的过拟合。”
- “Adjusted R-squared综合了拟合优度和模型简洁性，越大越好。”
- “T统计量>1仅说明Adjusted R-squared上升，不代表自变量显著，显著性需与临界值对比。”

#### 📝 待办事项
- **复习重点**：Adjusted R-squared公式推导、与R²的关系、经验法则及缺点。
- **下次预习**：AIC和BIC指标（本节课提及但未讲解）。

---

## 元数据
- **来源**：Get笔记
- **笔记ID**：`1897917082842966616`
- **导入时间**：2026-03-12 09:31:10
