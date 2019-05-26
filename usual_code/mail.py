import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr
import os
from email.mime.application import MIMEApplication


def send_mail(server=None, port=None, psw=None, sender=None, receivers=None, cc=None, bcc=None, subject=None,
              body=None, attachments=None):
    '''
    SMTP发送邮件
        server：smtp服务器  port:端口号   psw：登陆密码  sender：发送方  receivers：接收者
        cc：抄送  bcc:密抄  subject:标题  body：邮件正文  attachments：附件路径
    '''

    re = []

    msgRoot = MIMEMultipart()
    # msgRoot['Subject'] = subject   构造标题
    msgRoot['Subject'] = Header(subject, 'utf-8').encode()
    msgRoot['Cc'] = "".join(str(cc))
    msgRoot['Bcc'] = "".join(str(bcc))
    msgRoot['From'] = formataddr(["", sender])
    msgRoot['To'] = formataddr(["", receivers])
    msgRoot.attach(MIMEText(body, 'plain', 'utf-8'))

    if attachments != None:
        for attachment in attachments.split(','):
            rst = os.path.exists(attachment)
            if rst:
                excelFile = open(attachment, 'rb').read()
                fileName = os.path.basename(os.path.realpath(attachment))
                att = MIMEApplication(excelFile)
                att.add_header('Content-Disposition', 'attachment', fileName=('gbk', '', fileName))
                msgRoot.attach(att)
            else:
                print('附件路径不存在')

    if receivers != None and receivers != '':
        re = receivers.split(',')
    if cc != None and cc != '':
        re = re + str(cc).split(',')
    if bcc != None and bcc != '':
        re = re + str(bcc).split(',')

    smtp = smtplib.SMTP()
    if port != 25:
        smtp = smtplib.SMTP_SSL()
    smtp.connect(server, port)
    smtp.login(sender, psw)
    smtp.sendmail(sender, re, msgRoot.as_string())
    smtp.quit()


if __name__ == '__main__':
    for x in range(5):
        send_mail(server='smtp.qq.com', port=25, psw='', sender='', receivers=
                  '', subject='surprise', body='thanks for ur junk emails',
                  attachments=None, cc=None, bcc=None)
       

