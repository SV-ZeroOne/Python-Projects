# from https://mail.python.org/pipermail//bangpypers/2012-October/008357.html

import smtplib, os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

def send_mail(send_from, send_to, subject, text, files=[], server="smtp.gmail.com:587"):
    assert type(send_to)==list
    assert type(files)==list

    msg = MIMEMultipart()
    msg['From'] = send_from + ' <' + smtp_login_mail + '>'
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach( MIMEText(text) )
    msg.add_header('reply-to', send_from)
    for f in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(f,"rb").read() )
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
        msg.attach(part)

    smtp = smtplib.SMTP(server)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo
    smtp.login('baskar.krishnan at gmail.com', 'password')
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

    files = ['Config.ini', 'mail_ini.txt']
    send_to = ['baskar.krishnan at gmail.com']
    send_mail('mahadevan.m at gmail.com', send_to, 'test subject', 'body matter', files)