
🛠️ IT Support Knowledge Base
A structured knowledge base designed to help IT professionals quickly locate troubleshooting steps for common hardware, software, and network issues. 
This project includes clear technical documentation supported by screenshots, along with a Streamlit application for interactive searching.




```text
IT-Support-Knowledge-Base/
├── A_Troubleshooting_guides/
│   ├── hardware.md
│   ├── software.md
│   └── network.md
├── B_images/
│   ├── hardware/
│   ├── software/
│   └── network/
├── C_App/
│   └── app.py
└── venv/ 

✅ Features:
Searchable Knowledge Base – Locate troubleshooting steps by keyword.

Organized Documentation – Hardware, software, and network sections.

Visual References – Screenshots and diagrams to support guidance.

Streamlit Interface – Clean, interactive search UI for quick access.

🚀Getting Started
1. Clone the Repository
git clone https://github.com/thfanpham-sketch/IT-Support-Knowledge-Base.
cd IT-Support-Knowledge-Base

2. Install Dependencies
pip install streamlit

3. Launch the Application
streamlit run app.py

🖼️ Adding Images
Place images inside the appropriate category folder:
images/
  hardware/
      printer-error.png
  software/
      windows-update.png
  network/
      wifi-settings.png


To reference an image in Markdown:
![Printer Error](../images/hardware/printer-error.png)

📚 Example (hardware.md)
# Hardware Troubleshooting Guide
## Issue: Printer Not Working
### Symptoms
- Printer does not respond to print requests.
- An error message appears on the printer display.
![Printer Error](../images/hardware/printer-error.png)
### Steps to Resolve
1. Ensure the power cable is securely connected.
2. Restart the printer.
3. Update or reinstall printer drivers.

🤝 Contributing
Contributions are welcome.
If you wish to propose significant changes, please open an issue to discuss them first.

📜 License
This project is licensed under the MIT License.
