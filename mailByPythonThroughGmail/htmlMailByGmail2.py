#!/usr/bin/python
#-*- coding:utf8 -*-
'''
Created on 2018年4月10日
@author: bhlin

SOURCE: https://docs.python.org/2/library/email-examples.html

'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_html_mail(_me, _you):
    # me == my email address
    # you == recipient's email address
    me = _me    #'cloudhelp168@gmail.com'    #'clouddbx@gmail.com' #"my@email.com"
    you = ('cloudlet001@gmail.com', 'clouddbx@gmail.com')
        #('alex.kuanyuchen@gmail.com','shenforfun@gmail.com','bbjean520@gmail.com','ccms.tingwei@gmail.com','omitoefor1005@gmail.com','yihunglin35@gmail.com')
            #('cloudlet001@gmail.com', 'clouddbx@gmail.com', 'bhlin001@yahoo.com')  #'cloudlet001@gmail.com'   #"your@email.com"
    
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Link"
    msg['From'] = me
    msg['To'] = 'un-disclosed' #you
    
    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
    html = """\
    <html>
      <head></head>
      <body>
        <p>Hi，各位夥伴好：<br>
                                我是 5! 這是 <a href="https://cloud-rc-001.appspot.com">騰雲雲端資料中心</a>.
                                
          <br><br>
                             騰雲自動  email 發送測試。
        </p>
      </body>
    </html>
    """
    
    # Record the MIME types of both parts - text/plain and text/html.
    #part1 = MIMEText(text, 'plain')
    #part2 = MIMEText(html, 'html', 'utf-8')
    
    part1 = MIMEText(text, 'plain', 'utf-8')
    
    part2 = MIMEText(html, 'html', 'utf-8')
    part2.add_header("Content-Type", 'text/plain; charset="utf-8"')
    
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)
    
    try:
    #if True:
        # Send the message via local SMTP server.
        #s = smtplib.SMTP('localhost')
        
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(me, '1234-4321')    #'cl@610110')
        
        s = server
        # sendmail function takes 3 arguments: sender's address, recipient's address
        # and message to send - here it is sent as one string.
        s.sendmail(me, you, msg.as_string())
        s.quit()
        print 'successfully sent the htmlMail by Python Through Gmail'
    except: print "failed to send htmlMail by Python Through Gmail"


def send_email(user, pwd, recipient, subject, body):
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
    #if True:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mailByPythonThroughGmail'
    except:
        print "failed to send mailByPythonThroughGmail"

#if you want to use Port 465 you have to create an SMTP_SSL object:
'''
    # SMTP_SSL Example
    server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server_ssl.ehlo() # optional, called by login()
    server_ssl.login(gmail_user, gmail_pwd)  
    # ssl server doesn't support or need tls, so don't call server_ssl.starttls() 
    server_ssl.sendmail(FROM, TO, message)
    #server_ssl.quit()
    server_ssl.close()
    print 'successfully sent the mailByPythonThroughGmail'
'''

if __name__ == '__main__':
    send_html_mail('cloudhelp168@gmail.com', 'cloudlet001@gmail.com')
    
    exit(0)
    send_email('clouddbx@gmail.com', 'cl@610110', 
               'cloudlet001@gmail.com', 'test mailByPythonThroughGmail from python', 'body of test mailByPythonThroughGmail from python')
