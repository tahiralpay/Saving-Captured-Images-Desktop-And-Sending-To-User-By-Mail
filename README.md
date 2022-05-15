# Saving-Captured-Images-Desktop-And-Sending-To-User-By-Mail
##Circuit Diagram                     
<p align="center">
  <img width="450" height="562" src="https://user-images.githubusercontent.com/75435070/167315567-48cdcf2a-1d5f-4190-b2f9-d45e3e107d6c.png">
</p>

## SMTP
SMTP (Simple Mail Transfer Protocol) service in short; a Requester, sender presentation, field presentation ranking a three-stage process model is used. First; Outlook or Web mail and an email similar to this to send an e-mail message from a client to a sender, the SMTP Protocol is used. Second in the outgoing e-mail presentation stage, the e-mail recipient can use the transition service to go to the e-mail presentation It uses smtp. Finally, the recipient receives an e-mail to download the presentation, incoming mail via IMAP or POP3 the request is used (Outlook, Web mail, etc.).

## NOTE 
In order for the SMTP protocol to work, it must first be viewed from gmail. For this, firstly https://myaccount.google.com/security?gar=1 clicking on the link should enter the gamail settings. After this work The choice of 'less secure application access' should be activated. After these two stages, the SMTP protocol usable.

##
It is designed for continuous recording where there is an internet connection. this mode, which is suitable for outdoor environments, allows the system to be used as a security camera. It can be used in places such as home, apartment. In this function, the images collected with the camera (Raspberry Pi camera ver1.3) are recorded with a name and the images are sent to the user via e-mail from an e-mail address defined via the SMTP protocol,  Since there will be a delay during the mail sending, the time to enter the photo or video is adjusted accordingly in the software.   

<p align="center">
  <img width="419" height="595" src="https://user-images.githubusercontent.com/75435070/167315537-e52ec7c0-4803-4387-aea4-323232f6033b.PNG">
</p>

<p align="center">
  <img width="300" height="450" src="https://user-images.githubusercontent.com/75435070/167403569-95efe3bb-ef6d-4a8d-94ec-07ba85689ce8.PNG">
</p>
