
def mail():
    import smtplib as smtp
    s = smtp.SMTP('smtp.gmail.com',587)
    s.starttls()
    sender_email_id = input("Enter your email:")
    password = input("Enter your password:")
    s.login(sender_email_id,password)
    receiver_email_id= input("Who should I send the email to :")
    message = input("Enter your message :")
    s.sendmail(sender_email_id,receiver_email_id,message)
    s.quit()
    output = f"Message send to {receiver_email_id}"
    return output
