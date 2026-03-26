#!/usr/bin/env python3
"""
发送CFA学习会话记录到邮箱
Usage: python3 send_session_email.py "会话主题" "会话内容"
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import sys
import os
from datetime import datetime

# 邮件配置（从环境变量或使用默认配置）
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.qq.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SENDER_EMAIL = os.getenv("SENDER_EMAIL", "sibylwly@qq.com")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD", "qmaljanzdmvibfbf")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL", "sibylwly@qq.com")


def send_email(subject, content, attachments=None):
    """
    发送邮件到指定邮箱

    Args:
        subject: 邮件主题
        content: 邮件内容（HTML格式）
        attachments: 附件文件路径列表（可选）
    """
    try:
        # 创建邮件
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = subject

        # 添加邮件正文
        msg.attach(MIMEText(content, 'html', 'utf-8'))

        # 添加附件
        if attachments:
            for attachment_path in attachments:
                if os.path.exists(attachment_path):
                    with open(attachment_path, 'rb') as f:
                        part = MIMEApplication(f.read())
                        filename = os.path.basename(attachment_path)
                        part.add_header('Content-Disposition', 'attachment', filename=filename)
                        msg.attach(part)

        # 发送邮件
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()

        return True, "邮件发送成功！"

    except Exception as e:
        return False, f"邮件发送失败：{str(e)}"


def create_session_email(topic, conversation_text):
    """
    创建CFA学习会话邮件

    Args:
        topic: 会话主题/知识点
        conversation_text: 会话内容

    Returns:
        (subject, html_content): 邮件主题和HTML内容
    """
    now = datetime.now().strftime("%Y年%m月月%d日 %H:%M")
    subject = f"📚 CFA学习会话 - {topic} ({now})"

    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
        .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; border-radius: 10px 10px 0 0; text-align: center; }}
        .content {{ background: #f9f9f9; padding: 30px; border-radius: 0 0 10px 10px; }}
        h1 {{ margin: 0; font-size: 24px; }}
        p {{ margin: 10px 0; }}
        .topic {{ background: #fff3cd; padding: 15px; border-left: 4px solid #ffc107; margin: 20px 0; font-weight: bold; }}
        .footer {{ text-align: center; margin-top: 30px; color: #666; font-size: 14px; }}
        .conversation {{ background: white; padding: 20px; border-radius: 8px; margin: 20px 0; white-space: pre-wrap; font-family: monospace; font-size: 14px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📚 CFA学习会话记录</h1>
            <p style="margin: 10px 0 0 0; opacity: 0.9;">品职PZ智能私教助手</p>
        </div>
        <div class="content">
            <div class="topic">
                📌 本次会话主题：{topic}
            </div>
            <p><strong>时间：</strong>{now}</p>

            <h3 style="margin-top: 30px;">💬 会话内容：</h3>
            <div class="conversation">{conversation_text}</div>

            <div class="footer">
                <p>— CFA学习助手 —</p>
                <p>祝你学习顺利！🎓</p>
            </div>
        </div>
    </div>
</body>
</html>
"""

    return subject, html_content


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 send_session_email.py \"会话主题\" \"会话内容\"")
        sys.exit(1)

    topic = sys.argv[1]
    content = sys.argv[2]

    subject, html_content = create_session_email(topic, content)
    success, message = send_email(subject, html_content)

    if success:
        print(f"✅ {message}")
    else:
        print(f"❌ {message}")
        sys.exit(1)
