# 债券利差指标介绍：I Spread、Z Spread、TED Spread和LIBOR OIS Spread

## 课程信息
- **领域**：CFA 其他
- **标签**：

---

## 笔记内容


## 债券利差指标介绍：I Spread、Z Spread、TED Spread和LIBOR OIS Spread




### 📑 智能总结

#### 录音信息
- **时长**：约 0小时15分钟
- **参与人数**：约 1人
- **内容类型**：课程讲解

#### 录音总结

本次课程讲解了多种利差指标（I spread、Z spread、TED spread、LIBOR-OIS spread）的定义、计算方法、适用场景及意义。

**I Spread（插值利差）**
* **定义与名称由来**：I代表Interpolated（插值），指债券到期收益率与特定期限互换固定利率之间的利差，计算时可能需要对互换利率进行线性插值。
* **互换利率的线性插值方法**：当债券期限处于两个已知互换利率期限之间时，需通过线性插值得到对应期限的互换利率。例如，1.5年期互换利率1.35%，2年期1.50%，计算1.6年期互换利率时，先算delta（1.50%-1.35%=0.15%），再算短距离（1.6-1.5=0.1年）与总距离（2.0-1.5=0.5年）的比率（0.1/0.5=0.2），最后1.35% + 0.15%*0.2 = 1.38%。
* **I Spread的计算示例**：某债券（Zinny bonds）票面利率6%，1.6年到期，收益率2.35%，经插值得到1.6年期互换利率1.38%，则I Spread为2.35% - 1.38% = 0.97%（97个基点），该利差反映了 corporate bond 相对低风险互换利率的额外风险。

**Z Spread（零波动率利差）**
* **定义与核心假设**：Z代表Zero Volatility（零波动率），假设利率无波动，不存在利率模型，当前利率结构是唯一考虑的结构。
* **适用范围**：仅适用于不含嵌入式期权的债券（straight bonds），不适用于可赎回债券、可回售债券、抵押贷款支持证券等含嵌入式期权的债券，因为Z spread会包含期权风险溢价导致结果有偏。
* **计算逻辑**：在每个无风险即期利率上增加一个恒定的基点（Z spread），使得债券未来现金流（票息和本金）按此调整后利率折现的现值等于债券市场价格。计算通常需借助计算器或Excel的GoSeek/Solver功能，考试中一般不要求手动计算，但需理解原理。
* **反映的风险**：Z spread是对 corporate bond 相对于国债的额外信用风险和流动性风险的补偿。

**TED Spread（TED利差）**
* **构成与定义**：T指Treasury Bill（短期国库券）收益率，ED指Euro Dollar（欧洲美元）利率（基于LIBOR），TED spread是LIBOR与同期限T-bill收益率的差值。
* **风险对比**：T-bill被认为是无风险的（美国政府发行，不会违约），LIBOR反映大型银行间的短期借贷利率，存在一定信用风险（如AA级银行仍有违约可能），因此LIBOR通常高于T-bill收益率。
* **计算示例**：3个月LIBOR为0.33%，同期限T-bill收益率为0.03%，则TED spread为0.33% - 0.03% = 0.30%（30个基点）。
* **经济意义**：TED spread是衡量经济信用风险和市场紧张程度的指标。市场紧张时，投资者会转向安全资产（flight to quality），导致利差扩大；利差上升表明银行相对国债被认为风险更高，也可能与流动性不足有关（如次贷危机时期利差处于历史高位）。

**LIBOR-OIS Spread（LIBOR-OIS利差）**
* **构成与定义**：OIS指Overnight Index Swap（隔夜指数互换）利率，如美国的Fed funds rate、英国的Sonia、欧元区的Eonia，反映银行间超短期（隔夜）借贷利率，风险极低（几乎无交易对手风险）。LIBOR-OIS spread是LIBOR与OIS利率的差值。
* **风险对比**：OIS利率风险低于LIBOR，因为隔夜借贷风险最小，所以LIBOR通常高于OIS利率，利差为正。
* **经济意义**：利差扩大表明市场紧张情绪加剧，银行间借贷的信用风险和流动性风险感知上升。

### 📅 章节概要
[00:00:02](https://getnotes.seek:2) **课程引入：利差指标模块开始**

课程开始，介绍本次模块将学习利差指标，包括I spread、Z spread、TED spread等，说明课程非技术性且内容简短。

[00:00:27](https://getnotes.seek:27) **I Spread的定义与名称由来**

解释I Spread的“I”代表Interpolated（插值），说明有时需要使用线性插值来确定两个端点之间的正确位置。

[00:00:41](https://getnotes.seek:41) **I Spread的基本概念**

I Spread是债券到期收益率与特定期限互换固定利率之间的利差，互换固定利率基于大型AA级银行，而公司债券可能风险更高，该利差捕捉公司债券相对低风险主体的额外风险。

[00:01:02](https://getnotes.seek:62) **I Spread计算前的插值问题**

以6%票面利率、1.6年到期、收益率2.35%的Zinny债券为例，说明计算I Spread前需解决的问题：已知1.5年互换利率1.35%和2年互换利率1.50%，需对1.6年的互换利率进行线性插值。

[00:02:00](https://getnotes.seek:120) **线性插值的几何直观方法**

建议通过几何直观而非公式学习插值，以时间为横轴（1.5年和2年为端点），互换利率为纵轴（1.35%和1.50%），1.6年更接近1.5年，因此插值结果应在1.35%和1.50%之间且更接近1.35%。

[00:03:13](https://getnotes.seek:193) **线性插值的计算步骤**

计算delta（1.50% - 1.35% = 0.15%），确定短距离（1.6 - 1.5 = 0.1年）与总距离（2.0 - 1.5 = 0.5年）的比率（0.1/0.5 = 0.2），然后1.35% + 0.15% * 0.2 = 1.38%，得到1.6年期插值互换利率。

[00:04:42](https://getnotes.seek:282) **插值结果的合理性检验**

强调需对插值结果进行合理性检查，1.38%在1.35%和1.50%之间且接近1.35%，符合预期，避免计算错误（fat finger risk）。

[00:05:00](https://getnotes.seek:300) **I Spread的计算结果**

Zinny债券收益率2.35%减去插值得到的1.6年期互换利率1.38%，得到I Spread为0.97%（97个基点）。

[00:05:49](https://getnotes.seek:349) **Z Spread的定义与核心假设**

Z Spread即Zero Volatility Spread（零波动率利差），假设利率无波动，没有利率模型，仅考虑当前利率结构。

[00:06:19](https://getnotes.seek:379) **Z Spread的适用范围限制**

Z Spread不适用于含嵌入式期权的债券（如可赎回、可回售债券、抵押贷款支持证券），因为这些债券有借款人的提前还款权等期权。

[00:06:44](https://getnotes.seek:404) **Z Spread的正确适用对象**

Z Spread必须用于不含嵌入式期权的债券（straight bonds）。

[00:07:00](https://getnotes.seek:420) **Z Spread的计算逻辑**

通过在无风险即期利率上增加一个恒定利差（Z spread），使债券未来现金流（票息和本金）的折现值等于市场价格。

[00:07:35](https://getnotes.seek:455) **市场价格与无风险折现的关系**

风险公司债券的市场价格，如果用无风险即期利率折现其现金流，会高估债券价值，因此需要增加利差来调整折现率。

[00:08:20](https://getnotes.seek:500) **Z Spread的本质**

Z Spread是在每个国债即期利率上增加的恒定基点，目的是使模型计算的债券价格等于市场价格，反映公司债券的额外信用风险和流动性风险。

[00:08:48](https://getnotes.seek:528) **Z Spread的计算工具**

Z Spread可通过计算器或Excel的GoSeek/Solver功能计算，考试中一般不要求手动计算（因需试错法），但需理解原理。

[00:09:14](https://getnotes.seek:554) **Z Spread的风险补偿内涵**

Z Spread是对公司债券相对于国债的额外信用风险和流动性风险的补偿。

[00:10:00](https://getnotes.seek:600) **再次强调Z Spread的适用限制**

对含嵌入式期权的债券使用Z Spread会因包含期权风险溢价而导致结果有偏，因此不应使用。

[00:10:16](https://getnotes.seek:616) **Z Spread关键要点总结**

“零波动率”指假设利率无波动；不适用于可赎回和可回售债券；用于含嵌入式期权的债券时，指标会包含期权风险溢价而产生偏差。

[00:10:59](https://getnotes.seek:659) **TED Spread的定义**

TED Spread中，T指Treasury Bill（短期国库券）收益率，ED指Euro Dollar（欧洲美元）利率（基于LIBOR），是LIBOR与同期限T-bill收益率的利差。

[00:11:24](https://getnotes.seek:684) **LIBOR的性质**

LIBOR（伦敦银行间同业拆借利率）反映大型银行间的短期借贷利率。

[00:11:40](https://getnotes.seek:700) **T-bill与LIBOR的风险对比**

T-bill由美国政府发行，被认为无风险；大型银行（如AA级）有一定信用风险，可能违约，因此LIBOR通常高于T-bill收益率。

[00:12:11](https://getnotes.seek:731) **TED Spread的计算示例**

3个月LIBOR为0.33%，同期限T-bill收益率为0.03%，TED spread为0.33% - 0.03% = 0.30%（30个基点）。

[00:12:48](https://getnotes.seek:768) **TED Spread的经济意义**

TED Spread是经济信用风险和市场紧张程度的指标，市场紧张时会出现“flight to quality”，导致利差扩大。

[00:13:09](https://getnotes.seek:789) **TED Spread与市场情绪的关系**

T-bill被认为是安全的，LIBOR包含风险；利差扩大表明银行相对国债被认为风险更高，也可能与流动性不足有关（如次贷危机时期利差处于历史高位）。

[00:13:52](https://getnotes.seek:832) **LIBOR-OIS Spread的定义**

LIBOR-OIS Spread中，OIS指Overnight Index Swap（隔夜指数互换）利率，如美国的Fed funds rate，反映银行间隔夜借贷利率。

[00:14:12](https://getnotes.seek:852) **OIS的背景**

美国银行需在美联储保持一定存款准备金，有时需隔夜拆借以满足准备金要求，这种借贷风险极低。

[00:14:32](https://getnotes.seek:872) **OIS与LIBOR的风险对比**

OIS（隔夜借贷）风险低于LIBOR，几乎无交易对手风险，因此LIBOR通常高于OIS利率，利差为正。

[00:14:51](https://getnotes.seek:891) **LIBOR-OIS Spread的经济意义**

利差扩大表明市场紧张情绪加剧，银行间借贷的信用风险和流动性风险感知上升。

[00:15:14](https://getnotes.seek:914) **其他国家/地区的隔夜利率**

英国的隔夜利率为Sonia，欧元区为Eonia，美国为联邦基金利率（Fed funds rate）。

[00:15:40](https://getnotes.seek:940) **课程结束**

本次模块结束，感谢参与，预告下次模块。

### ✨ 金句精选

- “I spread is basically gonna be looking at the spread between a bond's yield to maturity and the swap fix rate for a particular maturity.” (方法技巧)
- “Z spread stands for zero volatility spread. Okay? Well that sounds really technical and very very scary, but essentially what we mean is that we are assuming there is no interest rate volatility.” (方法技巧)
- “Z spread must be used for bonds without embedded options, straight bonds.” (执行策略)
- “TED spread is seen as an indication of the credit risk of the economy... In times of trouble, there'll be a flight to quality and therefore spreads will tend to widen.” (战略洞见)
- “A rising TED spread will suggest that banks are increasingly viewed as riskier relative to Treasuries again, and that also can be linked to lack of liquidity.” (战略洞见)
- “LIBOR-OIS spread... if this spread widens, it means that there's more nervousness in the market.” (战略洞见)

### 📋 待办事项

- 无明确提及的待办事项。


---

## 元数据
- **来源**：Get笔记（未分类审查后导入）
- **笔记ID**：`1901757426778593904`
- **导入时间**：2026-03-12 09:33:32
