import smtplib
import key
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()

smtpObj.login('th.ucsy@gmail.com', key.password)
smtpObj.sendmail('th.ucsy@gmail.com', 'th.ucsy@gmail.com', 'Subject: Hey.\nDear Neon')
smtpObj.quit()
