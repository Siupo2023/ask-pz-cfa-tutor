# done 集成学习与随机森林算法讲解

## 课程信息
- **领域**：CFA 数量方法
- **标签**：

---

## 笔记内容

### 📑 智能总结

#### 录音信息

-   **录音时间**：2026-02-13 11:40:35 ~ 2026-02-13 12:03:20
    
-   **时长**：约 0小时22分钟
    
-   **参与人数**：约 1人
    
-   **内容类型**：课程讲解
    

#### 录音总结

本次课程讲解了集成学习（Ensemble Learning）的基本概念、核心思想、分类方法及具体应用，重点介绍了投票分类器（Voting Classifier）和装袋法（Bagging）。

**集成学习基础概念**

-   **集成学习的定义与核心思想**：集成学习（Ensemble Learning）的核心思想是“博采众长”，它本身并非单一机器学习算法，而是通过构建多个机器学习算法（模型），综合其预测结果以提升准确性和稳定性。例如，在对公司是否违约（default 或 not default）进行分类时，可同时使用SVM、KNN、决策树（如CART分类树）等多种算法，通过多数投票（少数服从多数）决定最终标签。
    
-   **集成学习的优势**：集成学习能够产生更准确、更稳定的预测结果，并有助于避免过拟合（overfitting）问题。即使某个分类器预测错误，其他分类器也可能纠正该错误；同时，它能平均多个模型的结果，削弱单个模型因学习训练集噪音而导致的过拟合影响。
    

**集成学习的分类与关键问题**

-   **个体学习器的类型**：根据个体学习器是否为同一类型，集成学习可分为异质学习器（heterogenous learner）和同质学习器（homogeneous learner）。异质学习器指集成不同种类的算法（如SVM、KNN、决策树、逻辑回归等）；同质学习器则指集成同一类型的算法（如全部使用决策树）。
    
-   **集成学习的两个关键问题**：一是如何训练每个个体学习器（即选择何种模型）；二是如何综合多个模型的预测结果。对于分类问题，常用多数投票（majority vote）；对于回归问题，常用结果均值。
    

**集成学习的具体方法**

-   **Voting Classifier（投票分类器）**：这是最简单的集成学习方法，通常针对异质学习器。通过综合不同类型算法的预测结果，分类问题采用少数服从多数原则，回归问题采用均值原则。其挑战在于需要精通多种不同算法并训练多个模型，且聚集的个体模型数量需适中，存在最优数量以避免过犹不及。
    
-   **Bagging（Bootstrap Aggregating，装袋法）**：针对同质学习器，核心在于使用相同算法但不同训练集。通过自助抽样法（Bootstrap Sampling，有放回抽样）从原始训练集中生成多个相互独立的子训练集，每个子训练集训练一个模型，最后综合所有模型的预测结果（分类用多数投票，回归用均值）。该方法在实际中应用更广泛。
    

### 📅 章节概要

[00:00:50](https://getnotes.seek:50) **开场问候**

课程以“嗨小宝”开场。  
[00:00:56](https://getnotes.seek:56) **引入集成学习与随机森林**

提及公司打标签任务，并引出集成学习（ENSEMBLE LEARNING）和随机森林（RANDOM FOREST），指出随机森林是集成学习的常用算法。  
[00:01:03](https://getnotes.seek:63) **集成学习的定义**

解释ENSEMBLE LEARNING即集成学习，意为“集合”，并提问其含义。  
[00:01:15](https://getnotes.seek:75) **集成学习的核心思想**

明确集成学习的核心思想是“博采众长”，它不是单一算法，而是构建多个机器学习算法。以公司违约分类为例，可使用SVM、KNN、决策树（CART分类树）等多种算法。  
[00:02:41](https://getnotes.seek:161) **集成学习的预测方式**

说明集成学习通过多个模型投票进行预测，如SVM和KNN预测为not default，决策树预测为default，则最终标签为NOT DEFAULT。  
[00:03:09](https://getnotes.seek:189) **集成学习的细节与教材评价**

指出集成学习看似简单，但涉及细节深入，CF教材对此有较好且易于理解的阐述。  
[00:03:30](https://getnotes.seek:210) **集成学习与人类决策的类比**

类比人类决策，如决定是否看电影会咨询多个朋友，说明集成学习综合多方意见的思想。  
[00:03:55](https://getnotes.seek:235) **集成学习的基本名词**

介绍基本名词ensemble learning和ensemble method，两者意思相近。ensemble learning指综合多个模型预测，少数服从多数；ensemble method指多个算法的组合。  
[00:04:27](https://getnotes.seek:267) **集成学习的优势**

阐述集成学习的优势：产生更准确、更稳定的预测，解决单个算法缺点，纠正错误预测，避免过拟合。  
[00:05:16](https://getnotes.seek:316) **集成学习优势的考点提示**

提示原版书课后题可能会考查集成学习的优势，需记住其能产生更准确稳定预测、避免过拟合、优于单个模型。  
[00:05:41](https://getnotes.seek:341) **集成学习的具体做法概述**

概述集成学习的过程：找到个体学习器（single model），每个模型产生预测，综合所有预测得到最终结果。  
[00:06:16](https://getnotes.seek:376) **集成学习的两个关键问题**

提出集成学习需解决的两个问题：如何训练每个算法（个体学习器是什么）；如何综合多个结果。  
[00:06:40](https://getnotes.seek:400) **分类与回归问题的结果综合**

说明分类问题通过多数投票（majority vote）综合结果，回归问题通过求均值综合结果。  
[00:07:26](https://getnotes.seek:446) **个体学习器的类型划分**

根据个体学习器是否为同一类型，将集成学习分为异质学习器（heterogenous learner）和同质学习器（homogeneous learner）。  
[00:07:53](https://getnotes.seek:473) **异质学习器示例**

举例异质学习器：第一个模型是SVM，第二个是CART决策树，第三个是KNN，第四个是logistic regression等。  
[00:08:14](https://getnotes.seek:494) **heterogenous learner的含义**

解释heterogenous learner即异质学习器，指综合不同性质的学习器。  
[00:08:50](https://getnotes.seek:530) **同质学习器的问题**

指出若所有个体学习器是同一算法（同质学习器），使用相同训练集和输入会导致预测结果相同，失去集成意义。  
[00:09:52](https://getnotes.seek:592) **同质学习器的解决方法**

说明同质学习器需使用不同的training set，甚至不同的features，以确保各分类器预测结果不同，具有投票意义。  
[00:10:37](https://getnotes.seek:637) **同质学习器中特征选择的例子**

举例：10维数据，每个分类器随机选择5个特征进行训练，确保结果不同。  
[00:11:05](https://getnotes.seek:665) **集成学习类型的决定因素**

说明集成学习的两种类型基于个体学习器是同质还是异质决定。  
[00:11:44](https://getnotes.seek:704) **同质学习器的常用工具**

指出同质学习器结合时常用的工具是bagging，并表示稍后详细讲解。  
[00:12:00](https://getnotes.seek:720) **常见集成学习方法**

介绍常见的集成学习方法：voting classifier、bagging（bootstrap aggregating）、随机森林（bagging的特例）。  
[00:12:29](https://getnotes.seek:749) **Voting Classifier的定义**

Voting Classifier是最简单的集成学习方法，针对异质学习器（不同类型算法）。  
[00:12:42](https://getnotes.seek:762) **Voting Classifier的应用示例**

举例：集成SVM、KNN、CART判断股票是outperformance还是underperformance，通过多数投票决定最终标签。  
[00:13:14](https://getnotes.seek:794) **投票方式的扩展**

指出少数服从多数是最简单的投票方式，实际中可能根据模型准确率进行加权投票，如专业评委投票权重高于观众。  
[00:14:09](https://getnotes.seek:849) **Voting Classifier的原则与模型数量**

说明Voting Classifier针对分类问题用少数服从多数，回归问题用均值；聚集的个体模型越多通常越准，但存在最优数量，避免过犹不及。  
[00:14:37](https://getnotes.seek:877) **Voting Classifier的缺点**

指出Voting Classifier的难点在于找到不同算法、训练每个模型及精通每种算法的假设。  
[00:15:44](https://getnotes.seek:944) **Bagging（Bootstrap Aggregating）的重要性**

强调Bagging方法很重要，需理解其基本含义，指使用相同算法但不同训练数据。  
[00:16:22](https://getnotes.seek:982) **获取不同训练数据的方法**

提出问题：如何得到不同的training data，引出bootstrapping sampling（自助抽样法）。  
[00:16:43](https://getnotes.seek:1003) **Bootstrap Sampling的定义**

解释bootstrap sampling是有放回的抽样，源自“自力更生”的含义。  
[00:17:21](https://getnotes.seek:1041) **Bootstrap Sampling示例**

举例：原始训练集有1000个数据，每次有放回随机抽取700个，得到多个相互独立的子训练集。  
[00:17:57](https://getnotes.seek:1077) **子训练集的独立性**

说明有放回抽样确保子训练集相互独立，因为每次抽样都从总样本中随机抽取，与之前结果无关。  
[00:18:47](https://getnotes.seek:1127) **Bootstrap Sampling名称的由来**

解释其称为bootstrap sampling是因为用原始数据集产生子训练集，即“自力更生”、自己生成自己。  
[00:19:16](https://getnotes.seek:1156) **Bootstrap Aggregating的步骤**

将Bootstrap Aggregating分为三个步骤：1. 自助抽样（有放回抽样）生成n个训练集；2. 用每个训练集训练n个模型；3. 综合n个模型的预测结果。  
[00:19:45](https://getnotes.seek:1185) **Bagging名称的由来**

说明将多个训练集“装在袋子里”，故称为Bagging（装袋法）。  
[00:20:00](https://getnotes.seek:1200) **抽样中的数据重复与缺失**

指出抽样时可能有些数据被多次抽到，有些数据未被抽到，增加抽样次数可缓解此现象。  
[00:20:23](https://getnotes.seek:1223) **Bagging的模型训练与预测综合**

说明用n个训练集训练n个模型，每个模型产生预测，再综合预测结果（分类用多数投票，回归用均值）。  
[00:21:50](https://getnotes.seek:1310) **Voting Classifier与Bagging的对比**

对比两者：Voting Classifier用异质学习器，Bagging用同质学习器；Bagging在实际中应用更多，通过不同训练数据保证模型预测结果不同。  
[00:22:16](https://getnotes.seek:1336) **Bagging中不同数据的获取方法**

总结Bagging通过bootstrap（有放回抽样）得到n个子训练集，训练n个模型，综合n个预测结果。

### ✨ 金句精选

-   “集成学习的核心思想就是博采众长，它本身并不是一个单独的机器学习的算法，而是构建多个机器学习的算法。” (方法技巧)
    
-   “集成学习可以产生一个更加准确以及更加稳定的 prediction，可以避免 overfitting 的问题。” (方法技巧)
    
-   “如果你用的算法都是一个种类的，就是 homogeneous 的 learner，这个时候我们就必然要用到不同的 training set。” (方法技巧)
    
-   “少数服从多数的这种投票方式是最简单的一种投票方式，实际上在有些情况下，我们更加合理的投票方式应该是有权重的投票方式。” (思考启发)
    
-   “bootstrap sampling 指的是一种有放回的抽样，它体现的是自力更生的思想，用自己来产生自己。” (方法技巧)
    

### 📋 待办事项

-   学员：掌握集成学习的核心思想、优势、两种主要类型（异质学习器和同质学习器）及关键问题。
    
-   学员：理解并记忆Voting Classifier的基本原理、适用场景及优缺点。
    
-   学员：重点掌握Bagging（Bootstrap Aggregating）的步骤、自助抽样法的含义及结果综合方式。
    
-   学员：完成原版书课后关于集成学习优势的相关习题。

---

## 元数据
- **来源**：Get笔记
- **笔记ID**：`1901548891082334032`
- **导入时间**：2026-03-12 09:31:09
