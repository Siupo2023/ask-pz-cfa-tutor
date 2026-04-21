#!/usr/bin/env python3
"""
发送八字命理分析HTML邮件
Usage: python3 send_bazi_email.py
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# 邮件配置
SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 587
SENDER_EMAIL = "sibylwly@qq.com"
SENDER_PASSWORD = "qmaljanzdmvibfbf"
RECEIVER_EMAIL = "sibylwly@qq.com"


def create_bazi_html_email():
    """创建八字命理分析的HTML邮件"""

    html_content = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>方之俊小朋友 - 八字命理全面分析报告</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Hiragino Sans GB',
                         'Microsoft YaHei', 'Helvetica Neue', Helvetica, Arial, sans-serif;
            line-height: 1.8;
            color: #2c3e50;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        }

        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 50px 40px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        .header::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            animation: pulse 15s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.1); }
        }

        .header h1 {
            font-size: 32px;
            margin-bottom: 10px;
            position: relative;
            z-index: 1;
        }

        .header .subtitle {
            font-size: 16px;
            opacity: 0.95;
            position: relative;
            z-index: 1;
        }

        .content {
            padding: 40px;
        }

        .info-box {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 25px;
            border-radius: 15px;
            margin: 25px 0;
            border-left: 5px solid #667eea;
        }

        .info-box h3 {
            color: #667eea;
            margin-bottom: 15px;
            font-size: 20px;
        }

        .bazi-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
            margin: 25px 0;
        }

        .bazi-column {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
        }

        .bazi-column .label {
            font-size: 14px;
            opacity: 0.9;
            margin-bottom: 10px;
        }

        .bazi-column .gan-zhi {
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 8px;
        }

        .bazi-column .wu-xing {
            font-size: 12px;
            opacity: 0.85;
        }

        .section {
            margin: 35px 0;
        }

        .section h2 {
            color: #667eea;
            font-size: 24px;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 3px solid #667eea;
        }

        .section h3 {
            color: #764ba2;
            font-size: 18px;
            margin: 20px 0 10px 0;
        }

        .highlight-box {
            background: #fff9e6;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #ffc107;
            margin: 20px 0;
        }

        .highlight-box.warning {
            background: #ffeaea;
            border-left-color: #dc3545;
        }

        .highlight-box.success {
            background: #e8f5e9;
            border-left-color: #4caf50;
        }

        .star-rating {
            color: #ffc107;
            font-size: 18px;
        }

        ul, ol {
            margin: 15px 0;
            padding-left: 25px;
        }

        li {
            margin: 10px 0;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);
        }

        table th {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }

        table td {
            padding: 12px 15px;
            border-bottom: 1px solid #e0e0e0;
        }

        table tr:hover {
            background: #f5f7fa;
        }

        .badge {
            display: inline-block;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            margin: 5px 5px 5px 0;
        }

        .badge.fire {
            background: #ffebee;
            color: #f44336;
        }

        .badge.water {
            background: #e3f2fd;
            color: #2196f3;
        }

        .badge.wood {
            background: #e8f5e9;
            color: #4caf50;
        }

        .badge.gold {
            background: #fff8e1;
            color: #ffc107;
        }

        .badge.earth {
            background: #f5f5f5;
            color: #757575;
        }

        .footer {
            background: #f5f7fa;
            padding: 30px;
            text-align: center;
            color: #666;
            font-size: 14px;
        }

        .emoji {
            font-size: 24px;
            margin-right: 8px;
        }

        .conclusion {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            margin: 30px 0;
        }

        .conclusion h2 {
            color: white;
            border-bottom: none;
        }

        @media (max-width: 600px) {
            .bazi-grid {
                grid-template-columns: repeat(2, 1fr);
            }

            .content {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎯 方之俊小朋友</h1>
            <p class="subtitle">八字命理全面分析报告</p>
            <p style="margin-top: 15px; opacity: 0.9; font-size: 14px;">分析时间：2026年4月5日</p>
        </div>

        <div class="content">
            <!-- 基本信息 -->
            <div class="info-box">
                <h3>📋 基本信息</h3>
                <ul>
                    <li><strong>姓名：</strong>方之俊（原名建议）</li>
                    <li><strong>出生时间：</strong>2023年12月5日 晚上10点多（亥时）</li>
                    <li><strong>性别：</strong>男</li>
                    <li><strong>分析日期：</strong>2026年4月5日</li>
                </ul>
            </div>

            <!-- 八字排盘 -->
            <div class="section">
                <h2>📊 八字排盘</h2>

                <h3>四柱八字</h3>
                <div class="bazi-grid">
                    <div class="bazi-column">
                        <div class="label">年柱</div>
                        <div class="gan-zhi">癸卯</div>
                        <div class="wu-xing">水木</div>
                    </div>
                    <div class="bazi-column">
                        <div class="label">月柱</div>
                        <div class="gan-zhi">辛亥</div>
                        <div class="wu-xing">金水</div>
                    </div>
                    <div class="bazi-column">
                        <div class="label">日柱</div>
                        <div class="gan-zhi">戊午</div>
                        <div class="wu-xing">土火</div>
                    </div>
                    <div class="bazi-column">
                        <div class="label">时柱</div>
                        <div class="gan-zhi">癸亥</div>
                        <div class="wu-xing">水水</div>
                    </div>
                </div>

                <h3>五行统计</h3>
                <div style="margin: 20px 0;">
                    <span class="badge gold">金：1个（辛）</span>
                    <span class="badge wood">木：1个（卯）</span>
                    <span class="badge water">水：3个（癸、亥、亥）</span>
                    <span class="badge fire">火：1个（午）</span>
                    <span class="badge earth">土：1个（戊）</span>
                </div>
                <div class="highlight-box">
                    <strong>初步判断：</strong>五行俱全，水旺，土身弱
                </div>
            </div>

            <!-- 核心分析 -->
            <div class="section">
                <h2>🌟 核心分析</h2>

                <h3>1. 日主属性</h3>
                <p><strong>日主戊土</strong>，生于<strong>亥月（冬天）</strong>，水旺土冻。</p>
                <div class="highlight-box warning">
                    <strong>强弱判断：</strong>身弱
                    <ul style="margin-top: 10px;">
                        <li>生于冬月，不得令（水旺土冻）</li>
                        <li>天干无火帮扶（仅日支午火暗藏）</li>
                        <li>水势强盛（3个水+天干透出）</li>
                    </ul>
                </div>

                <h3>2. 格局判断</h3>
                <p><strong>伤官生财格：</strong></p>
                <ul>
                    <li>月干<strong>辛金</strong>伤官透出</li>
                    <li>年干、时干<strong>癸水</strong>偏财双透</li>
                    <li>伤官生财，财气通门户</li>
                </ul>

                <h3>3. 调候用神</h3>
                <div class="highlight-box success">
                    <p><strong>第一用神：火</strong></p>
                    <ul>
                        <li>冬天戊土必需火来温暖</li>
                        <li>日支<strong>午火</strong>为关键（丁火为灯烛之火，温暖全局）</li>
                    </ul>
                    <p style="margin-top: 15px;"><strong>第二用神：燥土</strong></p>
                    <ul>
                        <li>未土、戌土为佳</li>
                        <li>帮身且止水</li>
                    </ul>
                </div>
            </div>

            <!-- 家族天赋 -->
            <div class="section">
                <h2>👨‍⚖️ 家族天赋传承分析</h2>

                <h3>三代法律背景的八字印证</h3>
                <div class="highlight-box">
                    <p><strong>年支卯木 = 七杀（法律星）</strong></p>
                    <ul>
                        <li>七杀代表：法律、制度、公检法</li>
                        <li><strong>癸年见卯 = 天乙贵人</strong>（贵人代表法律、贵人相助）</li>
                        <li>年柱代表祖辈/长辈，<strong>卯木七杀</strong>说明家族有法律基因！</li>
                    </ul>
                </div>

                <div class="highlight-box">
                    <p><strong>月干辛金 = 伤官（辩护星）</strong></p>
                    <ul>
                        <li>伤官代表：口才、辩才、表达能力</li>
                        <li><strong>律师的核心能力：</strong>既懂法律（官杀），又会辩护（伤官）</li>
                    </ul>
                </div>

                <table>
                    <thead>
                        <tr>
                            <th>组合</th>
                            <th>含义</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>官杀 + 伤官</td>
                            <td>完美律师配置</td>
                        </tr>
                        <tr>
                            <td>官杀</td>
                            <td>法律条文、规则制度</td>
                        </tr>
                        <tr>
                            <td>伤官</td>
                            <td>能言善辩、挑战不公</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- 金融天赋 -->
            <div class="section">
                <h2>💰 爸爸对金融感兴趣</h2>

                <h3>八字印证：财星双透</h3>
                <ul>
                    <li>年干<strong>癸</strong> = 偏财（第一金融星）</li>
                    <li>时干<strong>癸</strong> = 偏财（第二金融星）</li>
                </ul>

                <div class="highlight-box">
                    <p><strong>偏财代表：</strong></p>
                    <ul>
                        <li>金融、投资、经商、股市</li>
                        <li>不固定的财富（投资收益）</li>
                        <li><strong>财商高、善于理财</strong></li>
                    </ul>
                </div>

                <p><strong>伤官生财格：</strong></p>
                <ul>
                    <li>月干辛金（伤官）→ 生年干/时干癸水（财）</li>
                    <li><strong>辛金生水</strong> = 靠智慧/口才赚钱</li>
                    <li><strong>财气通门户</strong> = 财星透出，有根气（亥水）</li>
                </ul>
            </div>

            <!-- 情商分析 -->
            <div class="section">
                <h2>💧 情商高的八字印证</h2>

                <h3>1. 水旺 = 智商 + 情商双高</h3>
                <p><strong>水旺的特质：</strong></p>
                <ul>
                    <li>✅ <strong>聪明灵活</strong>（智商）</li>
                    <li>✅ <strong>善于察言观色</strong>（情商）</li>
                    <li>✅ <strong>敏感、细腻</strong>（感知他人情绪）</li>
                    <li>✅ <strong>变通能力强</strong>（不固执）</li>
                </ul>

                <h3>2. 戊癸合火（情商关键！）</h3>
                <div class="highlight-box success">
                    <p><strong>什么是戊癸合火？</strong></p>
                    <ul>
                        <li>日主<strong>戊土</strong>与财星<strong>癸水</strong>相合</li>
                        <li><strong>戊+癸 = 火</strong>（化火）</li>
                        <li><strong>火</strong>代表：热情、温暖、社交能力、人际魅力、情商表达</li>
                    </ul>
                    <p style="margin-top: 15px;"><strong>戊癸合 = "会做人"</strong></p>
                    <ul>
                        <li>善于处理人际关系</li>
                        <li>以和为贵，善于协调、圆融</li>
                        <li>外圆内方（外表温和，内心有原则）</li>
                    </ul>
                </div>

                <table>
                    <thead>
                        <tr>
                            <th>八字要素</th>
                            <th>情商表现</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>戊癸合火</td>
                            <td>化出温暖的火，待人亲切</td>
                        </tr>
                        <tr>
                            <td>水旺（3个）</td>
                            <td>敏感、善于察言观色</td>
                        </tr>
                        <tr>
                            <td>辛金伤官</td>
                            <td>口才好，说话讨人喜欢</td>
                        </tr>
                        <tr>
                            <td>卯为贵人</td>
                            <td>人缘好，得人帮助</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- 未来天赋 -->
            <div class="section">
                <h2>👶 孩子未来天赋预测</h2>

                <h3>1. 法律天赋 <span class="star-rating">★★★★★</span></h3>
                <div class="highlight-box">
                    <strong>理由：</strong>
                    <ul>
                        <li>✅ 年支<strong>卯木七杀</strong>（法律星）</li>
                        <li>✅ 月干<strong>辛金伤官</strong>（辩护星）</li>
                        <li>✅ <strong>官杀配伤官</strong> = 天生律师配置</li>
                        <li>✅ 家族三代法律背景加持</li>
                    </ul>
                    <p style="margin-top: 15px;"><strong>预测：</strong>继承家族法律基因的可能性很大，口才好、逻辑强、善于辩论，适合律师、法官、检察官、法务。</p>
                </div>

                <h3>2. 金融天赋 <span class="star-rating">★★★★☆</span></h3>
                <div class="highlight-box">
                    <strong>理由：</strong>
                    <ul>
                        <li>✅ 年干/时干<strong>癸水偏财双透</strong></li>
                        <li>✅ <strong>伤官生财格</strong>（辛金→癸水）</li>
                        <li>✅ 水旺主智（聪明、算计）</li>
                        <li>✅ 爸爸的金融兴趣可能影响孩子</li>
                    </ul>
                    <p style="margin-top: 15px;"><strong>预测：</strong>财商高，善于理财，可能从事<strong>法律+金融</strong>交叉领域（金融合规、证券法律师、投行法务、企业并购法律顾问）。</p>
                </div>
            </div>

            <!-- 职业预测 -->
            <div class="section">
                <h2>🎯 更精准的职业预测</h2>

                <p>结合<strong>法律背景 + 金融兴趣 + 高情商</strong>：</p>

                <h3>最佳职业方向（Top 3）</h3>

                <div class="highlight-box success">
                    <p><strong>1. 🥇 商务律师 / 并购律师</strong> <span class="star-rating">★★★★★</span></p>
                    <p><strong>原因：</strong></p>
                    <ul>
                        <li>法律基础（三代传承）</li>
                        <li>金融兴趣（双偏财）</li>
                        <li>高情商（善于谈判、协调）</li>
                    </ul>
                    <p><strong>优势：</strong>能处理复杂的商业谈判，懂人心，善于促成交易，人脉广，资源多。</p>
                </div>

                <div class="highlight-box">
                    <p><strong>2. 🥈 诉讼律师</strong> <span class="star-rating">★★★★☆</span></p>
                    <p><strong>原因：</strong>官杀+伤官 = 天生辩护人；高情商 = 善于说服法官、陪审团；水旺 = 反应快、逻辑强。</p>
                    <p><strong>优势：</strong>庭审表现好，客户沟通能力强，善于寻找和解机会。</p>
                </div>

                <div class="highlight-box">
                    <p><strong>3. 🥉 企业法务总监 / 法务高管</strong> <span class="star-rating">★★★★☆</span></p>
                    <p><strong>原因：</strong>需要法律+商业+人情；戊癸合 = 会做人、会协调；双偏财 = 懂商业逻辑。</p>
                    <p><strong>优势：</strong>能协调各部门关系，既懂法律又懂业务，情商高，升职快。</p>
                </div>
            </div>

            <!-- 取名分析 -->
            <div class="section">
                <h2>📛 取名分析</h2>

                <h3>方之俊 vs 方功谦</h3>

                <table>
                    <thead>
                        <tr>
                            <th>名字</th>
                            <th>八字契合</th>
                            <th>寓意</th>
                            <th>总分</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>方之俊</strong></td>
                            <td><span class="star-rating">⭐⭐⭐⭐⭐</span></td>
                            <td><span class="star-rating">⭐⭐⭐⭐⭐</span></td>
                            <td><strong>第一名</strong></td>
                        </tr>
                        <tr>
                            <td>方功谦</td>
                            <td>⭐⭐</td>
                            <td>⭐⭐⭐⭐</td>
                            <td>不推荐</td>
                        </tr>
                    </tbody>
                </table>

                <div class="highlight-box success">
                    <h3>🏆 最终取名建议：方之俊</h3>

                    <h4>推荐理由：</h4>
                    <ol>
                        <li><strong>八字契合度完美：</strong><strong>俊字属火</strong>，补八字最缺的火；火能调候：温暖冬天的戊土；火生土：帮助身弱的日主。</li>
                        <li><strong>寓意优秀：</strong>才智出众、俊杰、英俊潇洒。</li>
                        <li><strong>符合家族背景：</strong>俊杰 = 法律界的才俊 = 金融界的精英。</li>
                        <li><strong>音律优美：</strong>方之俊（阴平、阴平、去声），声调起伏，朗朗上口。</li>
                    </ol>

                    <p style="margin-top: 20px;"><strong>方之俊这个名字：</strong></p>
                    <ul>
                        <li>✅ 既有传统文化的底蕴</li>
                        <li>✅ 又符合八字命理</li>
                        <li>✅ 还契合家族的法律+金融基因</li>
                        <li>✅ 更配合孩子的高情商特质</li>
                    </ul>
                    <p style="margin-top: 15px; font-size: 18px; color: #667eea;"><strong>是个好名字！👍</strong></p>
                </div>
            </div>

            <!-- 培养建议 -->
            <div class="section">
                <h2>📚 培养建议</h2>

                <h3>1. 发挥情商优势</h3>
                <ul>
                    <li><strong>社交训练：</strong>多参加集体活动，学习如何处理矛盾，培养领导力</li>
                    <li><strong>口才训练：</strong>演讲、辩论、模拟法庭（结合法律背景），学习沟通技巧</li>
                    <li><strong>情绪管理：</strong>教他认识情绪，学习如何表达情绪，培养同理心</li>
                </ul>

                <h3>2. 法律+情商结合</h3>
                <ul>
                    <li><strong>从小看法律故事：</strong>看真实案例，分析各方立场，讨论如何和解</li>
                    <li><strong>模拟谈判游戏：</strong>扮演律师、法官，学习双赢思维，培养商业意识</li>
                </ul>

                <h3>3. 金融启蒙</h3>
                <ul>
                    <li><strong>财商培养：</strong>零花钱管理，了解投资概念，学习理财</li>
                    <li><strong>商业意识：</strong>了解商业模式，观察市场变化，培养商业嗅觉</li>
                </ul>

                <h3>4. 健康调养</h3>
                <ul>
                    <li>✅ <strong>多晒太阳</strong>（补火调候）</li>
                    <li>✅ <strong>注意保暖</strong>（冬天戊土怕冷）</li>
                    <li>✅ <strong>少吃生冷</strong>（护脾胃）</li>
                </ul>
            </div>

            <!-- 总结 -->
            <div class="conclusion">
                <h2>🎉 最终结论</h2>
                <p style="font-size: 18px; line-height: 2; margin-top: 20px;">
                    这个宝宝是<strong>法律天赋 + 金融潜力 + 高情商</strong>的三重优势命格：
                </p>
                <ul style="text-align: left; display: inline-block; margin-top: 20px;">
                    <li>✅ <strong>法律传承：</strong>三代法律背景，八字完美印证</li>
                    <li>✅ <strong>金融兴趣：</strong>双偏财透干，财商高</li>
                    <li>✅ <strong>高情商：</strong>水旺+戊癸合，善于处理人际关系</li>
                    <li>✅ <strong>健康很好：</strong>先天体质不错</li>
                </ul>
                <p style="font-size: 20px; font-weight: bold; margin-top: 30px;">
                    这是非常罕见的优秀命格！🚀
                </p>
                <p style="margin-top: 20px;">
                    有法律的专业性（官杀）<br>
                    有金融的敏锐度（财星）<br>
                    有高情商的协调能力（戊癸合+水旺）<br>
                    未来可能在<strong>商务法律、并购、谈判</strong>领域大有作为！
                </p>
                <p style="margin-top: 30px; font-size: 18px;">
                    <strong>爷爷奶奶/外公外婆爸爸妈妈可以重点培养他的：</strong><br>
                    口才 + 逻辑 + 情商 + 财商
                </p>
                <p style="margin-top: 20px; font-size: 16px; opacity: 0.95;">
                    这四个维度都发展好，未来不可限量！
                </p>
            </div>
        </div>

        <div class="footer">
            <p style="font-size: 16px; margin-bottom: 10px;">— 方之俊小朋友命理分析报告 —</p>
            <p>分析时间：2026年4月5日</p>
            <p>分析工具：传统四柱八字命理</p>
            <p>参考书籍：《穷通宝鉴》《三命通会》《滴天髓》《子平真诠》《渊海子平》</p>
            <p style="margin-top: 15px; color: #999;">愿方之俊小朋友健康快乐成长！🎈</p>
        </div>
    </div>
</body>
</html>
"""

    return html_content


def send_email(subject, html_content):
    """发送HTML邮件"""
    try:
        # 创建邮件
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = subject

        # 添加HTML正文
        msg.attach(MIMEText(html_content, 'html', 'utf-8'))

        # 发送邮件
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()

        return True, "邮件发送成功！"

    except Exception as e:
        return False, f"邮件发送失败：{str(e)}"


if __name__ == "__main__":
    # 创建HTML邮件
    html_content = create_bazi_html_email()

    # 发送邮件
    subject = "🎯 方之俊小朋友 - 八字命理全面分析报告（精美HTML版）"
    success, message = send_email(subject, html_content)

    if success:
        print(f"✅ {message}")
        print("📧 邮件已发送到：sibylwly@qq.com")
        print("🎨 本次邮件采用精美HTML格式，包含渐变背景、动画效果、响应式设计")
    else:
        print(f"❌ {message}")
