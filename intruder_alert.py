import cv2
import smtplib
import ssl
from email.message import EmailMessage
import os
from datetime import datetime, timedelta
import time
import win32evtlog  # from pywin32

# ====== Email Configuration ======
FROM_EMAIL = " .............. "  # Enter the sender's email address
FROM_PASSWORD = " ................ "  # Enter the app password of the sender's Gmail account
TO_EMAIL = " ............. " # Enter the recipient's email address to receive the intruder's image
CAPTURED_IMAGE = "intruder.jpg"

# ====== Login Attempt Threshold ======
FAILED_ATTEMPT_THRESHOLD = 2
failed_attempts = []

# ====== Capture Webcam Image ======
def capture_image(filename):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(filename, frame)
        print("[+] Intruder image captured.")
        cap.release()
        return True
    else:
        print("[-] Failed to access webcam.")
        cap.release()
        return False

# ====== Send Email with Image Attachment ======
def send_email_with_attachment(image_path):
    try:
        msg = EmailMessage()
        msg['Subject'] = '🚨 Intruder Alert: Failed Laptop Login Detected'
        msg['From'] = FROM_EMAIL
        msg['To'] = TO_EMAIL
        msg.set_content("Someone failed to unlock your laptop 2 times. Image attached.")

        with open(image_path, 'rb') as f:
            msg.add_attachment(f.read(), maintype='image', subtype='jpeg', filename=os.path.basename(image_path))

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(FROM_EMAIL, FROM_PASSWORD)
            smtp.send_message(msg)
            print("[+] Email sent successfully.")
    except Exception as e:
        print("[-] Failed to send email:", e)

# ====== Monitor Failed Login Attempts from Windows Event Log ======
def monitor_failed_logins():
    global failed_attempts
    print("[*] Monitoring Windows login attempts...")
    server = 'localhost'
    log_type = 'Security'

    while True:
        try:
            handle = win32evtlog.OpenEventLog(server, log_type)
            flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
            events = win32evtlog.ReadEventLog(handle, flags, 0)

            if events:
                for event in events:
                    if event.EventID == 4625:  # Failed login attempt
                        timestamp = event.TimeGenerated
                        print(f"[!] Failed login at {timestamp}")
                        failed_attempts.append(timestamp)

                        # Keep only last 2 minutes' attempts
                        failed_attempts = [t for t in failed_attempts if datetime.now() - t < timedelta(minutes=2)]

                        if len(failed_attempts) >= FAILED_ATTEMPT_THRESHOLD:
                            if capture_image(CAPTURED_IMAGE):
                                send_email_with_attachment(CAPTURED_IMAGE)
                            failed_attempts = []  # Reset
                        break  # Process only latest batch
        except Exception as e:
            print("[-] Error while reading event log:", e)

        time.sleep(5)

# ====== Main Entry Point ======
if __name__ == "__main__":
    try:
        monitor_failed_logins()
    except Exception as main_error:
        print("[-] Fatal Error:", main_error)
