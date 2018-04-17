#!/usr/bin/python
#-*- coding:utf8 -*-
'''
Created on 2018年4月10日
@author: bhlin

SOURCE: https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python
'''
import smtplib

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
    send_email('clouddbx@gmail.com', 'cl@610110', 
               'cloudlet001@gmail.com', 'test mailByPythonThroughGmail from python', 'body of test mailByPythonThroughGmail from python')
