import smtplib, ssl
from email.message import EmailMessage

def sender():
        email = EmailMessage()

        email["from"] = "Mary Maker"
        email["to"] = "caleandhannah@gmail.com"
        email["subject"] = "T-t-test 1!"

        email.set_content("You can send this!")

        try:
                with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
                        smtp.ehlo()
                        smtp.starttls()
                        smtp.login("marymakerapp@gmail.com", "bnvgdhcwpjpurxgj")
                        smtp.send_message(email)
                        print("It's been sent!")
                        return "Email sent"
        except:
                return "Status of send unclear"


