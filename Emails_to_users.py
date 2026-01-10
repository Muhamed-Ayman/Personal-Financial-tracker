import smtplib # smtplib for sending messages via Email
import random  # random is used to generate random OTP Codes to send to the user
from email.message import EmailMessage # For the structure of the message sent to the user
import os # To create an environment to secure the gmail app password


def send_otp(receiver_email):
    # Generate 6-digit OTP
    otp = random.randint(100000, 999999)

    # Email configuration
    sender_email = "monetra.project@gmail.com"
    app_password = "ejiinntrzcerlock"
    


    msg = EmailMessage()
    msg["Subject"] = "Your OTP Verification Code"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content(f"""
Hello,
Welcome to our python application | Monetra
We hope you enjoy our app.
This is your OTP Verification Code:
{otp}

This code is valid for the next 60 seconds.
Do not share it with anyone.
Thanks,
Monetra Team.
""")

    # Send email using Gmail SMTP
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)


    print("OTP sent successfully!")
    return otp  # Store this OTP for verification later




def send_forgotten_password_to_user(receiver_email, username, password):

    # Email configuration
    sender_email = "monetra.project@gmail.com"
    app_password = "ejiinntrzcerlock"

    if not app_password:
        raise ValueError("App password not found in environment variables")
    msg = EmailMessage()
    msg["Subject"] = "Your Forgotten Password | Security Check"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content(f"""
Hello,
Welcome to our python application | Monetra
We hope you enjoy our app.
This is your username and password after you issued forgetting your credentials:

Username: {username}
Password: {password}

If you don't know what is this, please IGNORE this email.
Do not share it with anyone for your security.
Thanks,
Monetra Team.
""")

    # Send email using Gmail SMTP
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)
    
    print("Credentials sent successfully!")