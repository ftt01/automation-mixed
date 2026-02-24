import smtplib
import os
from email.message import EmailMessage
from pathlib import Path

msg = EmailMessage()
msg["Subject"] = "File processati"
msg["From"] = os.environ["SMTP_USERNAME"]

# multiple recipients separated by comma
recipients = [email.strip() for email in os.environ["EMAIL_TO"].split(",")]
msg["To"] = ", ".join(recipients)

msg.set_content("In allegato i file processati.")

# attach all files in output/
output_dir = Path("output")
for file_path in output_dir.glob("*"):
    with open(file_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename=file_path.name
        )

with smtplib.SMTP(os.environ["SMTP_SERVER"], int(os.environ["SMTP_PORT"])) as server:
    server.starttls()
    server.login(os.environ["SMTP_USERNAME"], os.environ["SMTP_PASSWORD"])
    server.send_message(msg)
