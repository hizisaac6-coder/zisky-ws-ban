
markdown
# 🚀 ZISKY WHATSAPP BAN v2.0
███████╗██╗███████╗██╗ ██╗██╗ ██╗
╚══███╔╝██║██╔════╝██║ ██╔╝╚██╗ ██╔╝
███╔╝ ██║███████╗█████╔╝ ╚████╔╝
███╔╝ ██║╚════██║██╔═██╗ ╚██╔╝
███████╗██║███████║██║ ██╗ ██║
╚══════╝╚═╝╚══════╝╚═╝ ╚═╝ ╚═╝

text

> 🔥 **Advanced WhatsApp reporting tool with proxy rotation and multi-email support**

---

## ✨ **FEATURES**
┌─────────────────────────────────────┐
│ ✓ Proxy harvesting (12+ sources) │
│ ✓ 5 rotating email accounts │
│ ✓ 4 professional report types │
│ ✓ WhatsApp API number verification │
│ ✓ Login protection system │
│ ✓ Colorful ASCII interface │
│ ✓ Termux & Linux optimized │
│ ✓ Fast mode (reduced proxy testing) │
└─────────────────────────────────────┘

text

---

## ⚡ **QUICK FIX - Speed Up Proxy Testing**

The tool tests many proxies which takes time. To make it faster, edit your `main.py`:

```bash
nano main.py
Change this line:

python
MAX_PROXIES_TO_TEST = 50  # Changed from 200 to 50 (much faster!)
Save with Ctrl+X, Y, Enter

📥 INSTALLATION
📱 For Termux:
bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/hizisaac6-coder/zisky-ws-ban.git
cd zisky-ws-ban
pip install -r requirements.txt
python zisky_whatsapp_v2.py
🐧 For Linux:
bash
sudo apt update
sudo apt install python3 python3-pip git -y
git clone https://github.com/hizisaac6-coder/zisky-ws-ban.git
cd zisky-ws-ban
pip3 install -r requirements.txt
python3 zisky_whatsapp_v2.py
⚙️ CONFIGURATION
1️⃣ Edit your email accounts:
bash
nano main.py
2️⃣ Get App Passwords (for Gmail):
text
┌─────────────────────────────────────┐
│  🔐 HOW TO GET APP PASSWORDS        │
├─────────────────────────────────────┤
│  1. Enable 2FA on Google account    │
│  2. Go to: myaccount.google.com      │
│  3. Search "App passwords"           │
│  4. Select "Mail" + "Other"          │
│  5. Copy 16-character password       │
└─────────────────────────────────────┘
3️⃣ Add your credentials in main.py:
python
EMAIL_ACCOUNTS = [
    {
        'email': 'youremail@gmail.com',
        'password': 'your-16-char-app-password',
    }
]
🚀 QUICK START
bash
python zisky_whatsapp_v2.py
