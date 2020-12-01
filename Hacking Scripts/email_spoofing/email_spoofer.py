import smtplib

# Create an instace of an SMTP server, google allows you to use theirs
# Spoofying via google smtp does not seem to work, it will always display the original from address
# Need to turn on less secure app acccess in google account security

email = "test420@gmail.com"
password = "password"
toEmail = "test@gmail.com"
message = "Hello Steve"
fromEmail = "steve@spoof.com"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email, password)
# Params (From, To, Message)
server.sendmail(fromEmail, toEmail, message)
server.quit()