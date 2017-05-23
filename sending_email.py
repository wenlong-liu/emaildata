# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:32:22 2017
This scripts are used to send out data from Pasture to Wenlong from field.

Key features:
- Parse and send out all .par files
- Send out email at certain intervals: such as one day.
@author: wliu14
"""

from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

import smtplib
import time
import glob
import os
import logging

def _get_files(path):
    # parse and find out all the files endwith .par.
    files = list()

    for filename in glob.glob(os.path.join(path, '*.par')):
        files.append(filename)

    return files

def send_email(path):

    #information of the email address.
    from_addr = 'wenlongliu853@gmail.com'
    email_password = 'XXXX'
    to_addr = 'wenlongliu853@gmail.com'

    #send attachment via email.
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'This is a testing email.'

    #Attachement information.
    files = _get_files(path)
    msg.attach(MIMEText('This is a testing email to send out the Plymouth data', 'plain', 'utf-8'))

    for filename in files:
    #Adding attachments.
        with open(filename, 'rb') as f:
        # Set the name and format of the attachment:
            mime = MIMEBase('text', 'plain', filename=filename)
        # Header information:
            mime.add_header('Content-Disposition', 'attachment', filename=filename)
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
        # Read in attachment:
            mime.set_payload(f.read())
        # Decode the information:
            encoders.encode_base64(mime)
        # Add files into attachment.
            msg.attach(mime)

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.set_debuglevel(1)
    server.login(from_addr, email_password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()

if __name__ == '__main__':
    path = 'C:\\s-canV5.0\\Results\\ORIGINAL'
    interval = 600 #Unit: second
    while True:
        try:
            send_email(path)
            print('\n Sending one email!\n')
        except:
            print('\n error, try again later.\n ')
        finally:
            time.sleep(interval)
