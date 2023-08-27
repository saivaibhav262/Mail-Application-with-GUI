import smtplib
import tkinter as tk
from tkinter import messagebox
def send_email():
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"
    receiver_email = receiver_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END)
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)

            email_body = f"Subject: {subject}\n\n{message}"
            server.sendmail(sender_email, receiver_email, email_body)

            messagebox.showinfo("Success", "Email sent successfully.")
            receiver_entry.delete(0, tk.END)
            subject_entry.delete(0, tk.END)
            message_text.delete("1.0", tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
window = tk.Tk()
window.title("Mail Application")
receiver_label = tk.Label(window, text="Receiver Email:")
receiver_label.pack()
receiver_entry = tk.Entry(window, width=30)
receiver_entry.pack()
subject_label = tk.Label(window, text="Subject:")
subject_label.pack()
subject_entry = tk.Entry(window, width=30)
subject_entry.pack()
message_label = tk.Label(window, text="Message:")
message_label.pack()
message_text = tk.Text(window, width=40, height=10)
message_text.pack()
send_button = tk.Button(window, text="Send Email", command=send_email)
send_button.pack()
window.mainloop()
