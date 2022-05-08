"""
                       October 2020 TALPAY                  
"""

from picamera import PiCamera
from time import sleep
from gpiozero import MotionSensor
from datetime import datetime
import time
import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
global server

camera = PiCamera()
pir = MotionSensor(4)
i = 0
k = 0

flag = "Date:{0:%d}-{0:%m}-{0:%y} Time:{0:%H}-{0:%M}-{0:%S}".format(datetime.now())

def foto():
    camera.start_preview()
    sleep(1)
    camera.capture('/home/pi/Desktop/foto.jpg')
    camera.stop_preview()

def video():
    camera.start_preview()
    camera.start_recording('/home/pi/Desktop/video.h264')
    sleep(10)
    camera.stop_recording()
    camera.stop_preview()

def mailfoto():
    username = "tahiralpay98@gmail.com"
    password = "161101045"
    mail_adress_to_send = "tahiralpay.mdbf16@iste.edu.tr"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    
    def send_mail( send_from, send_to, subject, text, file, isTls=True):
        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['To'] = "".join(send_to)
        msg['Date'] = formatdate(localtime = True)
        msg['Subject'] = subject
        msg.attach( MIMEText(text) )
  
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(file,"rb").read() )
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(file)))
        msg.attach(part)  
        server.sendmail(send_from, send_to, msg.as_string())
   
    send_from = ""
    subject = "UYARI"
    text = """
    Hareket Algılandı.
    """

    fileName = "/home/pi/Desktop/foto.jpg"

    send_mail(send_from, mail_adress_to_send, subject, text, fileName, isTls = True)
    print("mail foto başarıyla gönderildi")
    server.quit()


def mailvideo():
    username = "tahiralpay98@gmail.com"
    password = "161101045"
    mail_adress_to_send = "tahiralpay.mdbf16@iste.edu.tr"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    
    def send_mail( send_from, send_to, subject, text, file, isTls=True):
        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['To'] = "".join(send_to)
        msg['Date'] = formatdate(localtime = True)
        msg['Subject'] = subject
        msg.attach( MIMEText(text) )
  
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(file,"rb").read() )
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(file)))
        msg.attach(part)  
        server.sendmail(send_from, send_to, msg.as_string())
   
    send_from = ""
    subject = "UYARI"
    text = """
    Hareket Algılandı.
    """
    
    fileName = "/home/pi/Desktop/video.h264"

    send_mail(send_from, mail_adress_to_send, subject, text, fileName, isTls = True)
    print("MAİL VİDEO BAŞARIYLA GÖNDERİLDİ")
    server.quit()
   

           
while True:
    if pir.wait_for_no_motion:
        print("hareket_yok=", k)
        k += 1
        time.sleep(1)
        
        if k>60:
            k = 0
            i = 0
            
    if pir.motion_detected:
        print("hareket_var=", i)
        i += 1
        time.sleep(1.7)
            
        if i == 1:
            foto()
            mailfoto()
        
        if i == 7:
            video()
            time.sleep(5)
            i = 0
            k = 0
            mailvideo()
            
