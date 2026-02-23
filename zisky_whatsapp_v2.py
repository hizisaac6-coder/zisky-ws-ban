#!/usr/bin/env python3
"""
███████╗██╗███████╗██╗  ██╗██╗   ██╗
╚══███╔╝██║██╔════╝██║ ██╔╝╚██╗ ██╔╝
  ███╔╝ ██║███████╗█████╔╝  ╚████╔╝ 
 ███╔╝  ██║╚════██║██╔═██╗   ╚██╔╝  
███████╗██║███████║██║  ██╗   ██║   
╚══════╝╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   
                                    
██╗    ██╗███████╗    ██████╗  █████╗ ███╗   ██╗
██║    ██║██╔════╝    ██╔══██╗██╔══██╗████╗  ██║
██║ █╗ ██║███████╗    ██████╔╝███████║██╔██╗ ██║
██║███╗██║╚════██║    ██╔══██╗██╔══██║██║╚██╗██║
╚███╔███╔╝███████║    ██████╔╝██║  ██║██║ ╚████║
 ╚══╝╚══╝ ╚══════╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝
                                                   
ZISKY WHATSAPP BAN v2.0 - ADVANCED REPORTING TOOL
Telegram: @zisky_dev
"""

import os
import sys
import time
import random
import re
import smtplib
import socket
import socks
import ssl
import requests
import json
import threading
from itertools import cycle
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from colorama import Fore, Style, init
import urllib3
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Import configuration
try:
    from main import *
except ImportError:
    print(f"{Fore.RED}╔══════════════════════════════════════════════════╗")
    print(f"{Fore.RED}║  [❌] ERROR: main.py NOT FOUND!                 ║")
    print(f"{Fore.RED}║  Please create main.py with your credentials    ║")
    print(f"{Fore.RED}║  Run: cp main_EXAMPLE.py main.py                ║")
    print(f"{Fore.RED}║  Then edit: nano main.py                        ║")
    print(f"{Fore.RED}╚══════════════════════════════════════════════════╝")
    sys.exit(1)

# Initialize colorama
init(autoreset=True)

# Animation frames
SPINNER_FRAMES = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']

# ========== ZISKY BANNER ==========
BANNER = f"""
{Fore.RED}███████╗██╗███████╗██╗  ██╗██╗   ██╗
{Fore.RED}╚══███╔╝██║██╔════╝██║ ██╔╝╚██╗ ██╔╝
{Fore.YELLOW}  ███╔╝ ██║███████╗█████╔╝  ╚████╔╝ 
{Fore.YELLOW} ███╔╝  ██║╚════██║██╔═██╗   ╚██╔╝  
{Fore.GREEN}███████╗██║███████║██║  ██╗   ██║   
{Fore.GREEN}╚══════╝╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   
{Fore.CYAN}═══════════════════════════════════════
{Fore.CYAN}    WHATSAPP BAN ENGINE v2.0
{Fore.CYAN}      ZISKY EDITION
{Fore.CYAN}═══════════════════════════════════════
{Fore.WHITE}      Developer: @zisky_dev
{Fore.WHITE}      Status: ✅ ACTIVE
{Fore.CYAN}═══════════════════════════════════════{Style.RESET_ALL}
"""

LOGIN_ART = f"""
{Fore.CYAN}┌─────────────────────────────────────┐
{Fore.CYAN}│     ZISKY WHATSAPP BAN v2.0        │
{Fore.CYAN}│        AUTHORIZED ACCESS ONLY       │
{Fore.CYAN}│          LOGIN REQUIRED             │
{Fore.CYAN}└─────────────────────────────────────┘{Style.RESET_ALL}
"""

MENU_HEADER = f"""
{Fore.MAGENTA}┌─────────────────────────────────────┐
{Fore.MAGENTA}│           MAIN MENU                  │
{Fore.MAGENTA}├─────────────────────────────────────┤{Style.RESET_ALL}
"""

MENU_FOOTER = f"""
{Fore.MAGENTA}└─────────────────────────────────────┘{Style.RESET_ALL}
"""

STATUS_BOX = f"""
{Fore.CYAN}┌─────────────────────────────────────┐
{Fore.CYAN}│         SYSTEM STATUS                │
{Fore.CYAN}└─────────────────────────────────────┘{Style.RESET_ALL}
"""

# ========== WHATSAPP SUPPORT EMAILS ==========
SUPPORT_EMAILS = [
    "support@support.whatsapp.com",
    "appeals@support.whatsapp.com",
    "android_web@support.whatsapp.com",
    "ios_web@support.whatsapp.com",
    "webclient_web@support.whatsapp.com",
    "1483635209301664@support.whatsapp.com",
    "support@whatsapp.com",
    "businesscomplaints@support.whatsapp.com",
    "help@whatsapp.com",
    "abuse@support.whatsapp.com",
    "security@support.whatsapp.com",
    "lawenforcement@support.whatsapp.com",
    "childprotection@whatsapp.com",
    "dmca@whatsapp.com",
    "legal@whatsapp.com",
    "complaints@whatsapp.com",
    "trust@whatsapp.com",
    "safety@whatsapp.com",
    "appeals@whatsapp.com",
    "escalations@whatsapp.com"
]

# ========== PROXY MANAGER - LOAD FROM FILE ==========
class ProxyManager:
    def __init__(self):
        self.proxies = []
        self.current_index = 0
        self.lock = threading.Lock()
        self.load_from_file()
    
    def load_from_file(self):
        """Load proxies from proxies.txt file"""
        proxy_file = "proxies.txt"
        
        if not os.path.exists(proxy_file):
            print(f"{Fore.RED}[❌] proxies.txt not found! Creating empty file.")
            with open(proxy_file, 'w') as f:
                f.write("# Add your proxies here - one per line\n")
                f.write("# Format: ip:port or ip:port:user:pass\n")
                f.write("# For IPv6, use [ipv6]:port format\n")
            self.proxies = []
            return
        
        with open(proxy_file, 'r') as f:
            lines = f.readlines()
        
        for line in lines:
            proxy = line.strip()
            if proxy and not proxy.startswith('#'):
                self.proxies.append(proxy)
        
        print(f"{Fore.GREEN}[✅] Loaded {len(self.proxies)} proxies from proxies.txt")
        
        if len(self.proxies) == 0:
            print(f"{Fore.YELLOW}[⚠️] No proxies found in proxies.txt")
    
    def get_proxy(self):
        """Get next proxy in rotation - FAST, NO TESTING"""
        with self.lock:
            if not self.proxies:
                return None
            
            if self.current_index >= len(self.proxies):
                self.current_index = 0
            
            proxy = self.proxies[self.current_index]
            self.current_index += 1
            return proxy
    
    def get_proxy_count(self):
        return len(self.proxies)

# ========== EMAIL SENDER WITH PROXY ROTATION ==========
class EmailSender:
    def __init__(self, proxy_manager=None):
        self.proxy_manager = proxy_manager
        self.email_accounts = EMAIL_ACCOUNTS
        self.account_cycle = cycle(EMAIL_ACCOUNTS)
        self.sent_count = 0
        self.success_count = 0
        self.fail_count = 0
    
    def parse_proxy(self, proxy_str):
        """Parse proxy string - supports IPv4, IPv6, and authenticated proxies"""
        proxy_str = proxy_str.strip()
        
        # Check for IPv6 with brackets [2001:db8::1]:port
        ipv6_match = re.match(r'^\[([a-fA-F0-9:]+)\]:(\d+)(?::(.+))?$', proxy_str)
        if ipv6_match:
            ip = ipv6_match.group(1)
            port = int(ipv6_match.group(2))
            auth = ipv6_match.group(3)
            
            if auth and ':' in auth:
                username, password = auth.split(':', 1)
                return {
                    'ip': ip,
                    'port': port,
                    'username': username,
                    'password': password,
                    'is_ipv6': True
                }
            else:
                return {
                    'ip': ip,
                    'port': port,
                    'username': None,
                    'password': None,
                    'is_ipv6': True
                }
        
        # Check for IPv6 without brackets (less common, but handle it)
        if proxy_str.count(':') > 1 and '[' not in proxy_str:
            # This is likely an IPv6 address without brackets - try to parse last part as port
            parts = proxy_str.split(':')
            if len(parts) >= 2:
                # Last part might be port
                possible_port = parts[-1]
                if possible_port.isdigit():
                    ip = ':'.join(parts[:-1])
                    port = int(possible_port)
                    return {
                        'ip': ip,
                        'port': port,
                        'username': None,
                        'password': None,
                        'is_ipv6': True
                    }
        
        # Handle IPv4 with possible auth
        parts = proxy_str.split(':')
        
        if len(parts) == 2:
            # ip:port format
            return {
                'ip': parts[0],
                'port': int(parts[1]),
                'username': None,
                'password': None,
                'is_ipv6': False
            }
        elif len(parts) == 4:
            # ip:port:user:pass format
            return {
                'ip': parts[0],
                'port': int(parts[1]),
                'username': parts[2],
                'password': parts[3],
                'is_ipv6': False
            }
        
        return None
    
    def setup_socks_proxy(self, proxy_info):
        """Setup SOCKS proxy for either IPv4 or IPv6"""
        try:
            if proxy_info['username'] and proxy_info['password']:
                # Authenticated proxy
                socks.set_default_proxy(
                    socks.SOCKS5, 
                    proxy_info['ip'], 
                    proxy_info['port'],
                    True,
                    proxy_info['username'],
                    proxy_info['password']
                )
            else:
                # Regular proxy
                socks.set_default_proxy(
                    socks.SOCKS5, 
                    proxy_info['ip'], 
                    proxy_info['port']
                )
            
            # Replace socket with socks socket
            socket.socket = socks.socksocket
            
            # For IPv6, we need to set additional socket options
            if proxy_info.get('is_ipv6', False):
                # Create a test socket to verify IPv6 works
                test_sock = socks.socksocket()
                test_sock.settimeout(5)
                try:
                    # Just test the proxy by creating a connection
                    test_sock.connect(('8.8.8.8', 53))
                    test_sock.close()
                except Exception as e:
                    # If IPv6 fails, reset and raise exception
                    socks.set_default_proxy()
                    socket.socket = socket.socket
                    raise Exception(f"IPv6 proxy connection failed: {e}")
            
            return True
        except Exception as e:
            print(f"{Fore.YELLOW}[⚠️] Proxy setup failed: {e}")
            return False
    
    def send_email(self, to_email, subject, body, use_proxy=True):
        """Send email with proxy rotation - Supports IPv4 & IPv6"""
        
        # Get next email account
        account = next(self.account_cycle)
        
        # Save original socket
        original_socket = socket.socket
        
        # Try up to 3 different proxies if first fails
        max_retries = 3
        
        for retry in range(max_retries):
            proxy_info = None
            proxy_str = "No proxy"
            
            try:
                # Set up proxy if enabled
                if use_proxy and self.proxy_manager:
                    proxy_str = self.proxy_manager.get_proxy()
                    if proxy_str:
                        proxy_info = self.parse_proxy(proxy_str)
                        
                        if proxy_info:
                            # Setup proxy connection
                            if not self.setup_socks_proxy(proxy_info):
                                continue
                
                # Create message
                msg = MIMEMultipart()
                msg['From'] = account['email']
                msg['To'] = to_email
                msg['Subject'] = subject
                
                # Add random headers
                msg['X-Mailer'] = f'Microsoft Outlook 16.0.{random.randint(1000,9999)}'
                msg['X-Priority'] = str(random.randint(1, 3))
                msg['Message-ID'] = f"<{random.randint(1000000,9999999)}.{datetime.now().timestamp()}@{account['email'].split('@')[1]}>"
                
                msg.attach(MIMEText(body, 'plain'))
                
                # Send email
                context = ssl.create_default_context()
                
                with smtplib.SMTP(account['smtp_server'], account['smtp_port'], timeout=30) as server:
                    server.starttls(context=context)
                    server.login(account['email'], account['password'])
                    server.send_message(msg)
                
                # Reset socket
                if use_proxy and self.proxy_manager:
                    socks.set_default_proxy()
                    socket.socket = original_socket
                
                self.sent_count += 1
                self.success_count += 1
                
                # Show which proxy worked
                if proxy_info:
                    proxy_type = "IPv6" if proxy_info.get('is_ipv6', False) else "IPv4"
                    print(f"{Fore.GREEN}✓ Used {proxy_type} proxy: {proxy_info['ip']}:{proxy_info['port']}")
                
                return True
                
            except Exception as e:
                # Reset socket
                try:
                    socks.set_default_proxy()
                    socket.socket = original_socket
                except:
                    pass
                
                # If this was the last retry, fail
                if retry == max_retries - 1:
                    self.fail_count += 1
                    error_msg = str(e)[:50]
                    print(f"{Fore.RED}✗ Failed after {max_retries} proxies: {error_msg}")
                    return False
                
                # Try next proxy immediately
                continue
        
        return False

# ========== WHATSAPP API FUNCTIONS ==========
def check_whatsapp_number(phone):
    """Check if number is registered on WhatsApp using Business API"""
    
    if not WHATSAPP_ACCESS_TOKEN or not WHATSAPP_PHONE_NUMBER_ID:
        print(f"{Fore.YELLOW}[⚠️] WhatsApp API credentials not configured. Skipping check.")
        return None
    
    url = f"https://graph.facebook.com/v19.0/{WHATSAPP_PHONE_NUMBER_ID}/contacts"
    headers = {
        "Authorization": f"Bearer {WHATSAPP_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "blocking": "wait",
        "contacts": [phone],
        "force_check": True
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        
        if response.status_code == 200:
            data = response.json()
            for contact in data.get("contacts", []):
                status = contact.get("status", "unknown")
                wa_id = contact.get("wa_id", "N/A")
                print(f"{Fore.GREEN}✅ Number: {wa_id} is {str(status).upper()} on WhatsApp.")
                return True
            print(f"{Fore.RED}❌ Number is not registered on WhatsApp.")
            return False
        else:
            print(f"{Fore.RED}⚠️ Failed to check number. Status: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"{Fore.RED}⚠️ API check failed: {e}")
        return None

# ========== REPORT TEMPLATES ==========
class ReportTemplates:
    
    @staticmethod
    def get_unban_temp(phone):
        """Temporary unban request template"""
        case_id = random.randint(100000, 999999)
        return f"""
Dear WhatsApp Appeals Team,

I hope this message finds you well.

I am writing with deep respect and concern regarding the temporary ban placed on my WhatsApp account associated with the phone number {phone}. I understand the importance of maintaining a safe and positive community, and I fully support your efforts.

However, I kindly believe this ban may have resulted from a misunderstanding or an unintentional error. WhatsApp is essential for my daily communication with family, friends, and work, and I am sincerely committed to following all community guidelines moving forward.

Phone Number: {phone}
Case Reference: WA-TEMP-{case_id}
WhatsApp Version: 2.25.{random.randint(10,99)}.{random.randint(10,99)}

I humbly request that you consider temporarily lifting the ban on my account to allow me the opportunity to demonstrate responsible use and compliance with your policies. If any issues remain, I would be grateful for guidance so I can fully address them.

Thank you very much for your understanding and consideration. I deeply appreciate your time and support.

With sincere gratitude,
A Loyal WhatsApp User
{datetime.now().strftime('%Y-%m-%d')}
"""

    @staticmethod
    def get_unban_perm(phone):
        """Permanent unban request template"""
        case_id = random.randint(100000, 999999)
        return f"""
Dear WhatsApp Appeals Team,

I am reaching out with a heavy heart regarding the permanent ban on my WhatsApp account linked to the phone number {phone}. I was deeply saddened to learn about this restriction and genuinely believe there might have been a misunderstanding or an unintentional mistake on my part.

I acknowledge that there may have been a violation and sincerely apologize for any inconvenience caused. I assure you that I fully understand the importance of adhering to the platform's guidelines and am committed to using WhatsApp responsibly in the future.

Phone Number: {phone}
Appeal Reference: WA-PERM-{case_id}
Device: {random.choice(['Samsung Galaxy S23', 'iPhone 14 Pro', 'Google Pixel 7', 'OnePlus 11'])}

WhatsApp is incredibly important to me—it connects me with my loved ones, friends, and colleagues daily. I truly respect the rules and community guidelines set forth by your team.

I humbly ask for your kindness and understanding in reviewing my case. If given the chance, I commit to strictly adhering to all policies moving forward and ensuring that my usage aligns fully with your standards.

Thank you very much for your time, patience, and consideration. I would be extremely grateful for the opportunity to regain access to my account.

With sincere gratitude,
A Dedicated WhatsApp User
{datetime.now().strftime('%Y-%m-%d')}
"""

    @staticmethod
    def get_fraud_report(phone):
        """Fraud/scam report template"""
        case_id = random.randint(100000, 999999)
        return f"""
URGENT: FRAUD REPORT - Phone Number: {phone}

To WhatsApp Security Team,

I am writing to report a WhatsApp number that is actively involved in fraudulent activities and scams targeting innocent users.

Phone Number: {phone}
Report Reference: WA-FRAUD-{case_id}
Date of First Contact: {(datetime.now() - timedelta(days=random.randint(2,14))).strftime('%Y-%m-%d')}

This number is being used for the following fraudulent activities:
- Impersonating legitimate businesses
- Requesting advance payments for fake products/services
- Phishing attempts to steal personal information
- Fake investment schemes promising unrealistic returns
- Attempting to obtain banking details and OTPs

I have collected evidence including screenshots of conversations, payment requests, and the scammer's tactics. Multiple victims have come forward reporting similar experiences with this same number.

This activity violates WhatsApp's Terms of Service regarding:
- Fraud and Deception (Section 8)
- Impersonation (Section 3.4)
- Illegal Activities (Section 9)

I request immediate investigation and permanent ban of this number to prevent further victims. Please preserve all data for potential law enforcement involvement.

Thank you for your prompt attention to this matter.

Sincerely,
Concerned User
{datetime.now().strftime('%Y-%m-%d')}
"""

    @staticmethod
    def get_hard_report(phone):
        """Hard/strong fraud report template (escalated)"""
        case_id = random.randint(100000, 999999)
        return f"""
╔══════════════════════════════════════════════════════════╗
║           EMERGENCY: CRITICAL FRAUD REPORT               ║
╚══════════════════════════════════════════════════════════╝

To WhatsApp Legal Department & Trust & Safety Team,

This is an URGENT and CRITICAL report regarding phone number {phone} which is being used for SERIOUS CRIMINAL ACTIVITY and poses an IMMEDIATE THREAT to user safety.

═══════════════════════════════════════════════════════════
CRITICAL VIOLATIONS DETECTED:
═══════════════════════════════════════════════════════════
🔴 CRIMINAL IMPERSONATION: This account is impersonating a public figure to defraud victims
🔴 SOPHISTICATED SCAM OPERATION: Multi-stage fraud scheme with documented victims
🔴 IDENTITY THEFT: Using fake identity to gain trust and extract sensitive information
🔴 FINANCIAL FRAUD: Requests for money, cryptocurrency, and banking details
🔴 PATTERN OF ABUSE: Multiple complaints from different users about the same number

═══════════════════════════════════════════════════════════
VICTIM IMPACT:
═══════════════════════════════════════════════════════════
- Elderly victims being targeted specifically
- Financial losses documented (screenshots attached)
- Psychological distress reported by multiple victims
- Personal information compromised

═══════════════════════════════════════════════════════════
LEGAL REFERENCE:
═══════════════════════════════════════════════════════════
This activity violates:
- WhatsApp's Acceptable Use Policy (Section: Fraud/Deception)
- International cybercrime laws
- Identity theft statutes
- Wire fraud regulations

Number: {phone}
Case Number: WA-CRITICAL-{case_id}
Reports Received: {random.randint(5,15)} from unique users
Evidence Package: Available upon request

I DEMAND immediate account termination and preservation of ALL data for law enforcement investigation. This account represents a clear and present danger to the WhatsApp community.

Failure to act immediately will result in:
1. More victims being defrauded
2. Escalation to law enforcement agencies
3. Public disclosure of WhatsApp's failure to act

This is a TIME-SENSITIVE matter requiring URGENT action.

Reporting Party: Concerned Citizen
Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Priority: CRITICAL

Please confirm receipt and action taken within 24 hours.
"""

# ========== CLEAR SCREEN ==========
def clear():
    os.system("clear" if os.name == "posix" else "cls")

# ========== LOGIN SYSTEM ==========
def login():
    clear()
    print(LOGIN_ART)
    print(f"{Fore.CYAN}┌─────────────────────────────────────┐")
    print(f"{Fore.CYAN}│           SYSTEM LOGIN              │")
    print(f"{Fore.CYAN}├─────────────────────────────────────┤")
    print(f"{Fore.CYAN}│  Default: ziskyhimself / admins     │")
    print(f"{Fore.CYAN}│  (Change in main.py)                │")
    print(f"{Fore.CYAN}└─────────────────────────────────────┘{Style.RESET_ALL}\n")
    
    attempts = 3
    while attempts > 0:
        username = input(f"{Fore.YELLOW}👤 Username: {Style.RESET_ALL}")
        password = input(f"{Fore.YELLOW}🔒 Password: {Style.RESET_ALL}")
        
        if username == TOOL_USERNAME and password == TOOL_PASSWORD:
            print(f"{Fore.GREEN}\n✅ Login successful! Loading tool...")
            time.sleep(1)
            return True
        else:
            attempts -= 1
            print(f"{Fore.RED}\n❌ Incorrect credentials! {attempts} attempts remaining.\n")
    
    print(f"{Fore.RED}┌─────────────────────────────────────┐")
    print(f"{Fore.RED}│  Too many failed attempts. Exiting  │")
    print(f"{Fore.RED}└─────────────────────────────────────┘")
    return False

# ========== MAIN APPLICATION ==========
class ZiskyWhatsAppBan:
    def __init__(self):
        self.proxy_manager = None
        self.email_sender = None
        self.running = True
        
        # Initialize proxy manager if enabled
        try:
            if USE_PROXIES:
                self.proxy_manager = ProxyManager()
        except NameError:
            print(f"{Fore.YELLOW}[⚠️] USE_PROXIES not defined. Using default: True")
            self.proxy_manager = ProxyManager()
        
        self.email_sender = EmailSender(self.proxy_manager)
    
    def initialize(self):
        """Initialize tool"""
        clear()
        print(BANNER)
        print(f"{Fore.CYAN}┌─────────────────────────────────────┐")
        print(f"{Fore.CYAN}│  Initializing Zisky Engine...       │")
        print(f"{Fore.CYAN}└─────────────────────────────────────┘{Style.RESET_ALL}\n")
        
        # Show proxy status
        if self.proxy_manager:
            proxy_count = self.proxy_manager.get_proxy_count()
            print(f"{Fore.CYAN}[🌐] Proxy rotation: ENABLED")
            print(f"{Fore.CYAN}[📊] Proxies loaded: {proxy_count}")
            if proxy_count == 0:
                print(f"{Fore.YELLOW}[⚠️] No proxies in proxies.txt - will use direct connection")
        else:
            print(f"{Fore.YELLOW}[⚠️] Proxy rotation: DISABLED")
        
        print(f"{Fore.GREEN}[✅] Email accounts loaded: {len(EMAIL_ACCOUNTS)}")
        print(f"{Fore.GREEN}[✅] WhatsApp support emails: {len(SUPPORT_EMAILS)}")
        print(f"{Fore.GREEN}[✅] Initialization complete!")
        time.sleep(2)
    
    def show_menu(self):
        clear()
        print(BANNER)
        print(MENU_HEADER)
        print(f"{Fore.MAGENTA}│  [1] 📩 Unban Request (Temporary)     │")
        print(f"{Fore.MAGENTA}│  [2] 🚫 Unban Request (Permanent)     │")
        print(f"{Fore.MAGENTA}│  [3] 🔍 Check Number Status           │")
        print(f"{Fore.MAGENTA}│  [4] ⚠️ Report Fraud/Scam             │")
        print(f"{Fore.MAGENTA}│  [5] 💀 Hard Report (Critical)        │")
        print(f"{Fore.MAGENTA}│  [6] 📊 System Status                 │")
        print(f"{Fore.MAGENTA}│  [0] ❌ Exit                          │")
        print(MENU_FOOTER)
        
        # Status bar
        print(f"{Fore.CYAN}┌─────────────────────────────────────┐")
        if self.proxy_manager:
            print(f"{Fore.CYAN}│  Proxies: {self.proxy_manager.get_proxy_count()} available{' ' * (20 - len(str(self.proxy_manager.get_proxy_count())))}│")
        print(f"{Fore.CYAN}│  Emails: {self.email_sender.sent_count} sent ({self.email_sender.success_count} ok, {self.email_sender.fail_count} failed)│")
        print(f"{Fore.CYAN}└─────────────────────────────────────┘{Style.RESET_ALL}")
        print()
    
    def get_phone_number(self):
        """Get and validate phone number"""
        while True:
            phone = input(f"{Fore.YELLOW}📞 Enter number with country code (e.g., +2348123456789): {Style.RESET_ALL}").strip()
            if re.match(r"^\+\d{10,15}$", phone):
                return phone
            else:
                print(f"{Fore.RED}❌ Invalid format! Must start with + and contain 10-15 digits.")
    
    def send_mass_emails(self, phone, template_func, count=30):
        """Send multiple emails with proxy rotation"""
        
        # Get count from main.py
        try:
            count = EMAILS_PER_TARGET
        except NameError:
            count = 30
        
        print(f"\n{Fore.CYAN}┌─────────────────────────────────────┐")
        print(f"{Fore.CYAN}│  Sending {count} emails to WhatsApp     │")
        print(f"{Fore.CYAN}└─────────────────────────────────────┘{Style.RESET_ALL}\n")
        
        success = 0
        fail = 0
        
        for i in range(count):
            # Rotate through support emails
            to_email = random.choice(SUPPORT_EMAILS)
            
            # Generate unique subject
            ref = random.randint(10000, 99999)
            subject = f"Case #{ref}: WhatsApp Report - {phone[:5]}***{phone[-3:]}"
            
            # Get template
            body = template_func(phone)
            
            # Check if USE_PROXIES exists
            use_proxy = True
            try:
                use_proxy = USE_PROXIES
            except NameError:
                use_proxy = True
            
            # Show sending animation
            spinner = SPINNER_FRAMES[i % len(SPINNER_FRAMES)]
            print(f"{Fore.YELLOW}{spinner} Sending email {i+1}/{count}...", end="\r")
            
            # Send email
            result = self.email_sender.send_email(to_email, subject, body, use_proxy=use_proxy)
            
            if result:
                success += 1
                status = f"{Fore.GREEN}✅"
            else:
                fail += 1
                status = f"{Fore.RED}❌"
            
            # Show progress
            progress = (i + 1) / count * 100
            bar_length = 30
            filled = int(bar_length * (i + 1) / count)
            bar = '█' * filled + '░' * (bar_length - filled)
            
            print(f"{Fore.CYAN}[{bar}] {progress:.1f}% {status} Success: {success} Failed: {fail}", end="\r")
            
            # Delay between emails
            try:
                min_delay = MIN_DELAY_SECONDS
                max_delay = MAX_DELAY_SECONDS
            except NameError:
                min_delay = 5
                max_delay = 10
            
            delay = random.uniform(min_delay, max_delay)
            time.sleep(delay)
        
        print(f"\n\n{Fore.GREEN}┌─────────────────────────────────────┐")
        print(f"{Fore.GREEN}│  Emails sent: {success}/{count}          │")
        print(f"{Fore.GREEN}│  Successful: {success}  Failed: {fail}    │")
        print(f"{Fore.GREEN}└─────────────────────────────────────┘{Style.RESET_ALL}")
        return success
    
    def run_report(self, report_type):
        """Generic report function"""
        
        phone = self.get_phone_number()
        
        # Check number status
        print(f"\n{Fore.CYAN}[🔍] Checking number status...")
        exists = check_whatsapp_number(phone)
        
        if exists is False:
            print(f"{Fore.YELLOW}[⚠️] Number may not be registered on WhatsApp. Continue? (y/n): ")
            if input().lower() != 'y':
                return
        
        # Map report types
        templates = {
            'temp': ReportTemplates.get_unban_temp,
            'perm': ReportTemplates.get_unban_perm,
            'fraud': ReportTemplates.get_fraud_report,
            'hard': ReportTemplates.get_hard_report
        }
        
        template_func = templates.get(report_type)
        
        # Get email count
        try:
            email_count = EMAILS_PER_TARGET
        except NameError:
            email_count = 30
        
        # Confirm
        print(f"\n{Fore.YELLOW}┌─────────────────────────────────────┐")
        print(f"{Fore.YELLOW}│  Ready to send {email_count} emails     │")
        print(f"{Fore.YELLOW}│  Target: {phone}                      │")
        print(f"{Fore.YELLOW}└─────────────────────────────────────┘{Style.RESET_ALL}\n")
        confirm = input(f"{Fore.YELLOW}Continue? (y/n): {Style.RESET_ALL}").lower()
        
        if confirm == 'y':
            success = self.send_mass_emails(phone, template_func)
            
            # Calculate success rate
            try:
                total = EMAILS_PER_TARGET
            except NameError:
                total = 30
            
            rate = (success/total)*100
            
            print(f"\n{Fore.GREEN}╔═══════════════════════════════════════╗")
            print(f"{Fore.GREEN}║         REPORT COMPLETE!             ║")
            print(f"{Fore.GREEN}╠═══════════════════════════════════════╣")
            print(f"{Fore.GREEN}║ Target: {phone}                      ║")
            print(f"{Fore.GREEN}║ Emails sent: {success}/{total}        ║")
            print(f"{Fore.GREEN}║ Success rate: {rate:.1f}%            ║")
            print(f"{Fore.GREEN}╠═══════════════════════════════════════╣")
            
            if rate > 70:
                print(f"{Fore.RED}║ 💀 High chance of ban within 24-48h! ║")
            elif rate > 40:
                print(f"{Fore.YELLOW}║ ⚠️ Moderate chance of action       ║")
            else:
                print(f"{Fore.BLUE}║ ℹ️ Low success rate - add more emails║")
            
            print(f"{Fore.GREEN}╚═══════════════════════════════════════╝{Style.RESET_ALL}")
        
        input(f"\n{Fore.YELLOW}Press Enter to continue...")
    
    def show_status(self):
        """Show system status"""
        clear()
        print(STATUS_BOX)
        
        print(f"\n{Fore.GREEN}📧 Email Accounts: {len(EMAIL_ACCOUNTS)}")
        for i, acc in enumerate(EMAIL_ACCOUNTS, 1):
            masked = acc['email'][:3] + "***" + acc['email'][acc['email'].find('@'):]
            print(f"  {i}. {masked}")
        
        print(f"\n{Fore.GREEN}📧 Support Emails: {len(SUPPORT_EMAILS)}")
        
        if self.proxy_manager:
            print(f"\n{Fore.GREEN}🌐 Proxies: {self.proxy_manager.get_proxy_count()} available")
        else:
            print(f"\n{Fore.YELLOW}🌐 Proxies: DISABLED")
        
        print(f"\n{Fore.GREEN}📊 Statistics:")
        print(f"  Total emails sent: {self.email_sender.sent_count}")
        print(f"  Successful: {self.email_sender.success_count}")
        print(f"  Failed: {self.email_sender.fail_count}")
        success_rate = (self.email_sender.success_count/max(1,self.email_sender.sent_count))*100
        print(f"  Success rate: {success_rate:.1f}%")
        
        print(f"\n{Fore.GREEN}⚙️ Settings:")
        try:
            print(f"  Emails per target: {EMAILS_PER_TARGET}")
            print(f"  Delay range: {MIN_DELAY_SECONDS}-{MAX_DELAY_SECONDS}s")
            print(f"  Proxy rotation: {USE_PROXIES}")
        except NameError:
            print(f"  Emails per target: 30 (default)")
            print(f"  Delay range: 5-10s (default)")
            print(f"  Proxy rotation: True (default)")
        
        input(f"\n{Fore.YELLOW}Press Enter to continue...")
    
    def run(self):
        """Main application loop"""
        
        if not login():
            return
        
        self.initialize()
        
        while self.running:
            self.show_menu()
            
            try:
                choice = input(f"{Fore.GREEN}Select option: {Style.RESET_ALL}").strip()
                
                if choice == '1':
                    self.run_report('temp')
                elif choice == '2':
                    self.run_report('perm')
                elif choice == '3':
                    phone = self.get_phone_number()
                    print(f"\n{Fore.CYAN}[🔍] Checking...")
                    check_whatsapp_number(phone)
                    input(f"\n{Fore.YELLOW}Press Enter to continue...")
                elif choice == '4':
                    self.run_report('fraud')
                elif choice == '5':
                    self.run_report('hard')
                elif choice == '6':
                    self.show_status()
                elif choice == '0':
                    print(f"{Fore.YELLOW}\n┌─────────────────────────────────────┐")
                    print(f"{Fore.YELLOW}│  👋 Goodbye from Zisky!             │")
                    print(f"{Fore.YELLOW}└─────────────────────────────────────┘{Style.RESET_ALL}")
                    self.running = False
                else:
                    print(f"{Fore.RED}❌ Invalid option!")
                    time.sleep(1)
                    
            except KeyboardInterrupt:
                print(f"\n{Fore.YELLOW}┌─────────────────────────────────────┐")
                print(f"{Fore.YELLOW}│  👋 Interrupted. Exiting...         │")
                print(f"{Fore.YELLOW}└─────────────────────────────────────┘{Style.RESET_ALL}")
                self.running = False
            except Exception as e:
                print(f"{Fore.RED}❌ Error: {e}")
                time.sleep(2)

# ========== ENTRY POINT ==========
if __name__ == "__main__":
    try:
        app = ZiskyWhatsAppBan()
        app.run()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}👋 Goodbye from Zisky!{Style.RESET_ALL}")
