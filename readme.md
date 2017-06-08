# sending_email
Retrieve and send out data automatically via emails.


The goal of this package is to automatically push notifications using Gmail, and/or update sensor measurements at specific intervals.
This package is written and tested in Python 3.5.2.  


### Download the packages


a. EXE packages

   If you would like to run the scripts without coding experiences, please download the pre-wrapped packages and run the scripts using .exe file.
   Link: https://github.com/wliu2016/sending_email/blob/exe-package/sending_email.zip?raw=true
   
b. Python packages

 * Please install yagmail before using the package. https://github.com/kootenpv/yagmail
   
      
        Pip install yagmail[all]
      
    
 * Download the Python scripts into your computer for further usage.
   
   
### Configure your parameters

 Please find your configuration.json file in the exe packages or downloaded Python files.  THe file should look like:

    {
      "SendAddress": "youremail@gmail.com",
      "ReceiveAddress": "youremail@gmail.com",
      "Subject": "Data update from your site",
      "Content": "This email is to update the data measured your site.",
      "Attachments":{
        "Scan":{
               "Path":"C:\\samples",
               "FileType":".par"
               },
    
         "Meta":{
                "Path":"C:\\samples\\file",
                "FileType":".csv"
              }
         },
  
      "Interval":600
    }
   | Parameters | Explanations|
   |------------------------|------------------------------------------------------------|
   |SendAddress|  the email address you use to send notifications|   
   |ReceiveAddress| the email address to receive notifications|  
   |Subject | Subject of the email|
   |Content | Content of the email |
   |Attachments (optional) | if you want to update data through emails. |
   |Path | the inventory to store the measurements.|
   |FileType | the type of data files. | 
   |Interval | the interval to send notifications. Unit: second. 600 means that the email will be send every 10 minutes.|
   
 After configuration, you are free to push notifications.

* if you are using exe file, please double click the exe file.
* if you are using Python package, please open cmd.exe to add

        cd 'the path of your python file'
        python sending_email.py
* You should see the following words if the email is sent successfully. 
 
        Send one email! 

If it is the first time to use the sending email address, the program will ask you to input the password.  

        Password for <youremailaddress@gmail.com>:
   After your enter the password, it will show:
      
        Save username and password in keyring? [y/n]:
   Please choose y so the program can remember your password.
             
Note: if you are sure your password is correct but fail to log in, please see the Q&A.

### Questions:
- Fail to log in your Gmail account.

    * If your password is correct but fail to log in, please try to login via web browser. This should solve most problems.
    * If still not working, you can try to activate _less secure apps_ in your gmail account via https://myaccount.google.com/lesssecureapps?pli=1. 
Warning: Do not do it on your university account or any other important email address as it will decrease the security of your account. 

- What if my email address is not Gmail?

    Right now the program only supports Gmail.  In the future, the users would be able to choose other popular email service providers.

- How to close the program?

  Close the pop-out windows or just click "CTRL + C"

  
### For more questions, comments or suggestions, please contact Wenlong Liu via wliu14@ncsu.edu
