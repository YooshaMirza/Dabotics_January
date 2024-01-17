import tkinter as tk
from tkinter import messagebox
import random
import smtplib
from email.mime.text import MIMEText

class OTPVerificationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("OTP Verification")
        self.master.geometry("300x150")

        self.email_label = tk.Label(self.master, text="Enter your email:")
        self.email_label.pack(pady=5)

        self.email_entry = tk.Entry(self.master)
        self.email_entry.pack(pady=5)

        self.btn_send_otp = tk.Button(self.master, text="Send OTP", command=self.send_otp)
        self.btn_send_otp.pack(pady=10)

        self.otp_label = tk.Label(self.master, text="Enter OTP:")
        self.otp_label.pack(pady=5)

        self.otp_entry = tk.Entry(self.master)
        self.otp_entry.pack(pady=5)

        self.btn_verify_otp = tk.Button(self.master, text="Verify OTP", command=self.verify_otp)
        self.btn_verify_otp.pack(pady=10)

        self.generated_otp = None

    def send_otp(self):
        email = self.email_entry.get()

        if not email:
            messagebox.showerror("Error", "Please enter your email.")
            return

        # Generate a 6-digit OTP
        self.generated_otp = str(random.randint(100000, 999999))

        # Send OTP via email
        subject = "OTP Verification"
        body = f"Your OTP is: {self.generated_otp}"

        try:
            self.send_email(email, subject, body)
            messagebox.showinfo("OTP Sent", "OTP has been sent to your email.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send OTP. Error: {e}")

    def verify_otp(self):
        entered_otp = self.otp_entry.get()

        if not entered_otp:
            messagebox.showerror("Error", "Please enter the OTP.")
            return

        if entered_otp == self.generated_otp:
            messagebox.showinfo("Success", "OTP verification successful.")
        else:
            messagebox.showerror("Error", "Incorrect OTP. Please try again.")

    def send_email(self, to_email, subject, body):
        # Replace with your email configuration
        sender_email = "your_email@gmail.com"
        sender_password = "your_email_password"

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = to_email

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())

if __name__ == "__main__":
    root = tk.Tk()
    app = OTPVerificationApp(root)
    root.mainloop()
