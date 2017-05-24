# -*- coding: utf-8 -*-
"""
Created on Wed May 24 11:42:02 2017
_version_ : 0.2
Update:
 - Use yagmail to wrap the email sending scripts.
 - Not saving password in the scripts.
@author: Wenlong
"""
import yagmail
import glob
import time
import os

def _get_filename(path, _type):
    '''
    Obtain the specify files in the target folder.
    Parameter:
    -path, such as 'F:\\'
    -_type, file type, such as: .par
    '''
    files = list()

    for filename in glob.glob(os.path.join(path, '*' + _type)):
        files.append(filename)        
    return files
   
def send_email(username, to, subject, body, attachments):
    '''
    Wrapper of yagmail to send out emails.
    '''
    # for the first time user, a popup will be shown to ask for password.
    # Note the password only need once if you save it in your computer.
    yag = yagmail.SMTP(username)                 
    yag.send(to=to, subject=subject, contents=[body] + attachments)
    
if __name__ == '__main__':
    '''
    Get inputs from the manual input.
    '''
    path = input('Please enter the file path:')
    fileType = input('Please enter the file extention, such as .par:')
    username = input('Please enter the user email address:')
    to = input('Please enter the target address:')
    subject = input('Please enter the subject of email:')
    body = input('Please enter the contents of the email.')
    interval = int(input('Please set the sending interval, unit: second:'))
    
    # To break the loop and exit the program, use CTRL + C.        
    while True:       
        try:
            attachments = _get_filename(path, fileType)
            send_email(username,username,subject=subject, body=body, 
                   attachments=attachments)
            print('Send one email.')
            
        except:
            print('Bad connection, try it again.')       
     
        finally:       
            time.sleep(interval)            
