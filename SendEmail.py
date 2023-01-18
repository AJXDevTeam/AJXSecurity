from email.message import EmailMessage
import ssl
import smtplib
class Sender:
    def __init__(self,null):
        self.null = null
    @staticmethod
    def sender(new_email):
        #outlook = {'@outlook.com','@hotmail.com','@live.com','@msn.com',".edu"}
        #for i in outlook:
            #if i in new_email:
                #print("hi")
        email_sender = f'ajxdevcontact@gmail.com'
        email_password = 'vdwn btli jtgm gsvo'
#https://stackoverflow.com/questions/70261815/smtplib-smtpauthenticationerror-534-b5-7-9-application-specific-password-req
        email_receiver = f'{new_email}'

        subject = "Password Login Change!"
        body = """
        We noticed that you changed your password information for our login. If this wasnt you, then please contact @ajxdevcontact@gmail.com
        """

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
