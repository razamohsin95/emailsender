import smtplib as s
ob=s.SMTP("smtp.gmail.com",587)

ob.starttls

ob.login("mohsin95raza@gmail.com",***************)

subject="sending email using python"

body="This is tutorial for sending email using python"

message="Subject:{}\n\n{}".format(subject,body)
#print(message)

listOfAddress=["mohsinraza248@gmail.com"]
ob.sendmail("mohsin95raza@gmail.com",listOfAddress,message)
print("sent successfully")
ob.quit()