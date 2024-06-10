import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# Email credentials
EMAIL_ADDRESS = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_password'

# Recipients list
recipients = ['recipient1@example.com', 'recipient2@example.com']

def send_email(subject, body, to_emails):
    try:
        # Setting up the MIME
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = ", ".join(to_emails)
        msg['Subject'] = subject
        
        # Attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))
        
        # Create SMTP session for sending the mail
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Use Gmail with port 587
        server.starttls()  # Enable security
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login with mail_id and password
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, to_emails, text)
        server.quit()
        
        print(f"Email sent successfully to {to_emails}")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")

def generate_report():
    # Here you would generate or fetch the actual report data
    report_date = datetime.now().strftime("%Y-%m-%d")
    report_body = f"Daily report for {report_date}:\n\n"
    report_body += "This is where your report data would go."
    return report_body

def main():
    report_body = generate_report()
    subject = f"Daily Report - {datetime.now().strftime('%Y-%m-%d')}"
    send_email(subject, report_body, recipients)

if __name__ == "__main__":
    main()
