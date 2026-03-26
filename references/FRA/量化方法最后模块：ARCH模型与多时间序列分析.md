# 量化方法最后模块：ARCH模型与多时间序列分析

## 课程信息
- **领域**：CFA 财务报告分析
- **标签**：

---

## 笔记内容

### 📑 智能总结

#### 录音信息
- **时长**：约 0小时11分钟
- **参与人数**：约 1人
- **内容类型**：课程讲解

#### 录音总结
本次课程为CFA数量方法最后模块，讲解了ARCH模型和多时间序列分析，包括ARCH模型的步骤、应用及随机游走回归的注意事项。

**ARCH模型概述**
* **ARCH模型定义**：全称为自回归条件异方差模型（Auto Regressive Conditional Heteroskedastic Models），主要用于波动率预测。
* **异方差性回顾**：异方差性指误差项方差非恒定，条件异方差会导致标准误过低、t统计量过高，违反回归假设。解决方法包括广义最小二乘回归或利用误差间关系进行预测。

**ARCH模型步骤**
* **步骤一：ARCH(1)模式检验**：通过将当期平方残差对前一期平方残差进行回归，检验斜率系数A1的统计显著性。若A1显著，表明误差间存在线性关系，时间序列符合ARCH(1)模式。
* **步骤二：未来方差预测**：在A1显著的前提下，利用模型（截距A0+斜率A1×当期平方残差）预测未来误差的方差，方差是波动率（标准差的平方）的代理变量。

**ARCH模型应用场景**
* **金融市场应用**：ARCH模型作为波动率预测模型，受期权卖方、对冲基金（从事短期波动率策略）、银行等金融市场参与者关注，因为他们需通过预测波动率管理风险（如期权卖方的Vega风险）。
* **实例分析**：给定当前平方误差为0.5625，若截距和斜率的t统计量均大于2（或p值小于显著性水平），则A0和A1显著，可代入模型预测下一期方差。

**多时间序列分析**
* **单位根与随机游走问题**：单位根存在于随机游走中，导致时间序列非协方差平稳，是严重问题。
* **随机游走回归的有效性**：若两个时间序列均协方差平稳（无单位根），则回归的beta估计可信；若仅有一个为随机游走（有单位根），beta估计不可信；若两者均为随机游走，需检验协整性。
* **协整性概念**：协整指两个时间序列受相同宏观经济变量影响或遵循相同趋势（如同时上升或下降），可通过Engle-Granger检验判断。若协整，则beta估计可靠，模型可用。

### 📅 章节概要
[00:00:02](https://getnotes.seek:2) **课程引入与主题介绍**

欢迎回到CFA课程，本次是数量方法最后模块，将讲解自回归条件异方差模型（ARCH模型）和多时间序列分析，例如将一个随机游走对另一个随机游走回归时，beta估计是否可信。

[00:00:29](https://getnotes.seek:29) **异方差性回顾**

若对异方差性和异方差误差感到生疏，需回顾多元回归相关模块。异方差性指误差项方差非恒定，例如当x增加时误差和方差也增加，这被称为条件异方差，不仅违反回归假设，还会导致标准误过低、t统计量过高。

[00:01:00](https://getnotes.seek:60) **异方差性解决方法**

解决异方差问题的一种方法是重新设定回归模型，例如使用广义最小二乘回归替代普通最小二乘回归（OLS）以减轻异方差误差的影响。

[00:01:51](https://getnotes.seek:111) **利用误差关系进行预测**

另一方面，若误差非随机且相互关联，可利用这一事实进行预测。因为非随机的事物可以预测其序列中的下一个变量。

[00:02:12](https://getnotes.seek:132) **ARCH分析步骤一：ARCH(1)模式检验**

ARCH分析有两个步骤。第一步是检验时间序列是否符合ARCH(1)模式，方法是将当期平方残差对前一期平方残差进行回归，然后检验斜率系数A1的统计显著性。

[00:02:27](https://getnotes.seek:147) **ARCH(1)模式的意义**

若A1显著，意味着昨日误差与今日误差之间存在线性关系。

[00:02:54](https://getnotes.seek:174) **ARCH步骤一的目的**

若存在这种线性关系，则可利用今日误差值预测未来误差值。记住，ARCH过程的第一步仅是检验时间序列是否遵循ARCH(1)模式。

[00:03:13](https://getnotes.seek:193) **ARCH分析步骤二：未来方差预测**

ARCH框架的第二步是预测未来，但前提是已确定A1显著。若A1显著，则可预测未来误差的方差。

[00:03:40](https://getnotes.seek:220) **预测对象：方差而非误差值**

需要明确的是，我们不是预测误差值，而是预测未来误差的方差，方法是将当期平方残差代入模型。

[00:03:54](https://getnotes.seek:234) **方差与波动率的关系**

已知A1显著，截距A0也会给出。将当期平方残差代入模型，可了解未来的波动率（方差）。记住，方差是标准差的平方，而标准差即波动率。

[00:04:16](https://getnotes.seek:256) **ARCH模型本质：波动率预测模型**

ARCH本质上是一种波动率预测模型。金融市场中许多参与者关心波动率，如期权卖方（Vega为负，波动率上升会亏损）、从事短期波动率策略的对冲基金、银行等，他们可能使用ARCH模型预测未来波动率。

[00:04:49](https://getnotes.seek:289) **ARCH模型实例引入**

通过具体例子说明：判断给定结果是否表明ARCH(1)，并在当前平方误差为0.5625时预测下一期方差。注意这里给出的是已平方的误差，可直接代入ARCH模型。

[00:05:05](https://getnotes.seek:305) **ARCH模型参数显著性判断**

查看截距A0和斜率A1的绝对值，通过t统计量判断显著性。t统计量5和4.7均大于2，说明截距和斜率均显著。若未提供t统计量，也可使用p值，若p值小于显著性水平则拒绝原假设（系数为0），表明参数显著。

[00:05:47](https://getnotes.seek:347) **ARCH模型预测前提**

t统计量和p值均表明A1显著，这是进行未来方差预测的第一步，只有A1显著才能预测未来方差。

[00:06:10](https://getnotes.seek:370) **下一期方差预测公式**

已知A1显著，下一期的估计方差为A0 + A1×当期平方残差（epsilon squared），这里预测的是epsilon的方差，方差是波动率的代理变量。

[00:06:56](https://getnotes.seek:416) **多时间序列分析引入**

模块第二点是关于多时间序列。从之前的模块可知，单位根是严重问题，存在于随机游走中，导致模型没有均值回复水平，不具有协整平稳性。

[00:07:11](https://getnotes.seek:431) **股票收益与市场收益的回归**

基于一级知识，若将股票收益对市场收益进行回归，得到的简单线性回归斜率即为股票的beta。股票收益和市场收益本身都是时间序列，观察它们随时间的演变。

[00:08:10](https://getnotes.seek:490) **随机游走与单位根**

若股票收益是随机游走（因为包含单位根），市场收益也是随机游走（包含单位根），此时将一个随机游走对另一个随机游走回归，得到的beta估计是否可信？

[00:08:45](https://getnotes.seek:525) **不同情况下beta估计的可靠性**

若两个时间序列均协整平稳（非随机游走，无单位根），则beta估计可信；若仅有一个是随机游走（有单位根），无论其是x还是y，beta估计均不可信。

[00:09:16](https://getnotes.seek:556) **两个随机游走的协整性检验**

若两个时间序列均非协整平稳（均为随机游走），仍有一线希望，需检验协整性。可使用Engle-Granger协整检验，考试可能不考名称，但会涉及协整概念。

[00:10:00](https://getnotes.seek:600) **协整性的含义**

协整在通俗意义上指两个时间序列对相同的宏观经济变量（如GDP、利率、失业率、通胀率）做出反应，或至少遵循相同趋势（如同时上升或下降）。

[00:10:27](https://getnotes.seek:627) **协整性与beta估计的可靠性**

若两个随机游走协整（可通过Engle-Granger检验），则beta估计可靠，模型可用。此处仅做定性讨论。

[00:10:43](https://getnotes.seek:643) **课程结束与祝福**

感谢参与所有数量方法模块的学习，希望未来在其他主题领域再见，祝大家在数量方法学习和考试中一切顺利，再见。

### ✨ 金句精选

- “ARCH is nothing but a volatility forecasting model.” (方法技巧)
- “Hetero-skedasticity occurs when the variance of our errors is non constant.” (方法技巧)
- “If A one is significant then what we can predict is the variance of the error in the future.” (方法技巧)
- “Unit roots are a serious, serious problem. They are present in random walks; they cause the model to not have a mean reverting level. They cause the model to not be covariance stationary.” (战略洞见)
- “If both time series are covariance stationary... we can trust the beta estimate. If only one of them is a random walk... the beta estimate cannot be trusted.” (执行策略)
- “If you regressed one random walk against another random walk, there is still a glimpse of hope because statistical theory states that you need a check for co-integration.” (战略洞见)
- “Co-integration means that the two time series respond to the same macroeconomic variables... or at least follow the same trend.” (方法技巧)

### 📋 待办事项

- 学员：若对异方差性和异方差误差感到生疏，需回顾多元回归相关模块。
- 学员：学习使用Engle-Granger检验判断时间序列的协整性。

---

## 元数据
- **来源**：Get笔记
- **笔记ID**：`1901753333673187952`
- **导入时间**：2026-03-12 09:31:10
