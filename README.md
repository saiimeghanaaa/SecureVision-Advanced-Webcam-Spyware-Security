# SecureVision-Advanced-Webcam-Spyware-Security

SecureVision is a comprehensive cybersecurity solution designed to provide real-time intrusion detection and webcam access control on personal laptops. This system helps safeguard the user’s privacy and data by detecting suspicious activity and empowering the user with control over their device’s camera functionality.

🧠 Core Objectives
Detect and respond to unauthorized login attempts.

Provide the user with full control over webcam usage to prevent spying or misuse.

Offer an automated and user-friendly security experience.

🕵️‍♂️ 1. Intruder Detection and Email Alert System
🔸 Functionality Overview:
The system keeps track of login attempts made on the laptop.

If more than two consecutive wrong passwords are entered:

The system assumes a potential intruder scenario.

It activates the webcam, takes a clear snapshot of the person.

The captured image is then automatically sent via email to the legitimate user's registered email address.

🔸 Key Features:
Runs silently in the background once launched.

Works independently of internet access, triggering the camera and saving evidence even if offline (email sent once connected).

Instant real-time alerts give users the ability to respond to threats quickly.

🔸 Technologies Used:
Python – Core programming language.

OpenCV – Webcam image capture.

smtplib & email.mime – Secure email transmission.

pywin32 – For accessing system-level Windows functionalities.

pickle – For session/state handling.

🎥 2. Webcam Enable/Disable Control
🔸 Functionality Overview:
SecureVision allows users to manually control webcam accessibility through a simple GUI built with Tkinter. This feature acts as a privacy shield against background applications or malware trying to use the webcam without permission.

🔸 Key Features:
“Enable Camera” Button: Reactivates webcam hardware or drivers, making it available for video calls, meetings, etc.

“Disable Camera” Button: Instantly disables the webcam to prevent spying or recording.

Works without needing to uninstall drivers.

Prevents apps from secretly activating the camera when the user is unaware.

🔸 Use Cases:
Ideal for remote workers, students attending online classes, or any laptop user concerned about webcam surveillance.

Protects against threats like Remote Access Trojans (RATs) that silently record via webcam.

🔸 Technologies Used:
Tkinter – User-friendly GUI for manual control.

os or subprocess – For executing system-level commands to toggle webcam access.

pywin32 or registry modifications – For hardware control depending on Windows version.

🌟 Unique Selling Points (USPs):
Dual protection: Combines automated detection with manual privacy control.

Lightweight and efficient – Can run on low-end systems without performance drop.

Plug-and-play style: Just run the script, and it starts protecting you.

Customizable for enterprise laptops or personal usage with minimal setup.

📌 Real-Life Scenario:
You're away from your laptop and someone tries to guess your password multiple times. SecureVision detects this and immediately:

Takes a photo using the webcam.

Sends it to your email so you know who tried and when.

You can later choose to keep your camera disabled to avoid further misuse.
