# Import tkinter for GUI creation
import tkinter as tk

# Import messagebox to show popup alerts (error/success)
from tkinter import messagebox

# Import qrcode library to generate QR codes
import qrcode

# Import quote to safely encode text for URLs (spaces → %20 etc.)
from urllib.parse import quote

# Import ImageTk to display images inside Tkinter
from PIL import ImageTk


# Function that runs when "Generate QR Code" button is clicked
def generate_qr():

    # Get UPI ID entered by user and remove extra spaces
    upi_id = upi_entry.get().strip()

    # Get recipient name entered by user
    name = name_entry.get().strip()

    # Get amount (optional)
    amount = amount_entry.get().strip()

    # Validation: UPI ID and Name are mandatory
    if not upi_id or not name:
        messagebox.showerror("Error", "UPI ID and Name are required")
        return  # Stop function execution

    # Encode name so it can be safely used in a URL
    # Example: "Pankaj Jadhav" → "Pankaj%20Jadhav"
    encoded_name = quote(name)

    # Build UPI payment URL
    # If amount is provided, include it
    if amount:
        upi_url = (
            f"upi://pay?"
            f"pa={upi_id}&"        # Payee Address (UPI ID)
            f"pn={encoded_name}&" # Payee Name
            f"am={amount}&"       # Amount
            f"cu=INR&"            # Currency
            f"tn=Payment"         # Transaction Note
        )
    else:
        # If amount is not provided, generate open amount QR
        upi_url = (
            f"upi://pay?"
            f"pa={upi_id}&"
            f"pn={encoded_name}&"
            f"cu=INR&"
            f"tn=Payment"
        )

    # Generate QR code image in memory (NOT saved to disk)
    qr_img = qrcode.make(upi_url)

    # Resize QR image so it fits nicely inside the GUI
    qr_img = qr_img.resize((200, 200))

    # Convert PIL image into Tkinter-compatible image
    qr_photo = ImageTk.PhotoImage(qr_img)

    # Display QR image inside the label
    qr_label.config(image=qr_photo)

    # IMPORTANT: Keep a reference to the image
    # Otherwise Python garbage collector will delete it
    qr_label.image = qr_photo


# ---------------- GUI SETUP ----------------

# Create main window
root = tk.Tk()
root.title("Google Pay QR Generator")

# Set window size
root.geometry("420x480")

# Disable window resizing
root.resizable(False, False)

# App heading label
tk.Label(
    root,
    text="Google Pay QR Code Generator",
    font=("Arial", 14, "bold")
).pack(pady=10)

# Frame to hold input fields
frame = tk.Frame(root)
frame.pack(pady=10)

# UPI ID label and input box
tk.Label(frame, text="UPI ID:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
upi_entry = tk.Entry(frame, width=30)
upi_entry.grid(row=0, column=1)

# Recipient name label and input box
tk.Label(frame, text="Recipient Name:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(frame, width=30)
name_entry.grid(row=1, column=1)

# Amount label and input box (optional)
tk.Label(frame, text="Amount (optional):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
amount_entry = tk.Entry(frame, width=30)
amount_entry.grid(row=2, column=1)

# Button to generate QR code
tk.Button(
    root,
    text="Generate QR Code",
    font=("Arial", 11, "bold"),
    bg="green",
    fg="white",
    command=generate_qr  # Call generate_qr function on click
).pack(pady=15)

# Label to display generated QR code
qr_label = tk.Label(root)
qr_label.pack(pady=10)

# Info text
tk.Label(
    root,
    text="QR will disappear when app closes",
    font=("Arial", 9)
).pack(pady=5)

# Start the Tkinter event loop (keeps window open)
root.mainloop()
