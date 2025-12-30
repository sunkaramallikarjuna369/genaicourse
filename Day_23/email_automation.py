"""Day 23: Email Automation"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List

class EmailAutomation:
    def __init__(self, sender_email: str, password: str, smtp_server="smtp.gmail.com", port=587):
        self.sender_email = sender_email
        self.password = password
        self.smtp_server = smtp_server
        self.port = port
    
    def send_email(self, recipient_email: str, subject: str, body: str, is_html=False):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'html' if is_html else 'plain'))
        
        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.starttls()
            server.login(self.sender_email, self.password)
            server.send_message(msg)
    
    def send_bulk_emails(self, recipients: List[str], subject: str, body: str):
        for recipient in recipients:
            self.send_email(recipient, subject, body)

if __name__ == "__main__":
    email = EmailAutomation("your_email@gmail.com", "your_password")
    email.send_email("recipient@example.com", "Test", "Hello World")
