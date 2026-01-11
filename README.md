📱 Google Pay UPI QR Code Generator (Tkinter)

A simple Python GUI application that generates a Google Pay–compatible UPI QR code using Tkinter and qrcode library.
The QR code is generated in memory, displayed inside the GUI, and not saved on the system.

🚀 Features
Takes UPI ID, Recipient Name, and optional Amount
Generates valid UPI payment QR
Displays QR code inside the application

❌ No QR image saved to disk
QR code automatically disappears when app closes
Compatible with Google Pay (UPI standard)

🛠️ Tech Stack
Python
Tkinter – GUI
qrcode – QR code generation
Pillow (PIL) – Image handling

📦 Installation

Clone the repository:
git clone https://github.com/Pankaj24112005/Google-Pay-UPI-QR-Code-Generator-Tkinter-Using-Python


Install required libraries:
pip install qrcode[pil]


Tkinter comes pre-installed with Python.

▶️ How to Run
python app.py


🧾 How It Works (Steps)

Step 1 : Create a Tkinter GUI to take user inputs
         (UPI ID, Recipient Name, optional Amount)

Step 2 : Validate user inputs to ensure
         required fields (UPI ID and Name) are not empty

Step 3 : Encode recipient name using URL encoding
         to make it safe for use in UPI payment URL

Step 4 : Construct a UPI payment URL
         using standard UPI parameters (pa, pn, am, cu, tn)

Step 5 : Generate QR code in memory
         using qrcode.make() without saving it to disk

Step 6 : Resize the generated QR image
         to fit properly inside the GUI window

Step 7 : Convert QR image into Tkinter-compatible format
         using PIL.ImageTk.PhotoImage

Step 8 : Display the generated QR code
         inside the Tkinter application window

Step 9 : Automatically discard the QR code
         when the application is closed (no file saved)

⚠️ Important Notes

UPI ID must be active and registered on Google Pay
QR should be scanned from another Google Pay account
Self-payment is not allowed by Google Pay
App does not verify bank accounts (handled by Google Pay)

📌 Future Enhancements
Show error for invalid UPI format
Auto-clear QR after a time limit
Add PhonePe / Paytm support
Convert app into .exe
Add business logo to QR

👨‍💻 Author

Pankaj Jadhav
Third-year AIML student
Python | GUI | UPI QR Projects
