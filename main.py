import yagmail

def send_emails():
    yag = yagmail.SMTP('your_email@gmail.com', 'your_password')

    recipients = [
        'recipient1@example.com',
        'recipient2@example.com',
        'recipient3@example.com'
    ]

    subject = "example subject" #email subject here
    body = "this is an automated email sent from a python script" #body of the email

    for recipient in recipients:
        yag.send(to=recipient, subject=subject, contents=body)
        print(f"email sent to {recipient}")

    print("all emails sent!")

if __name__ == "__main__":
    send_emails()
