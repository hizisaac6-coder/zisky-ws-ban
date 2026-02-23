#!/usr/bin/env python3
"""
ZISKY WHATSAPP BAN v2.0 - MAIN TOOL
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
import queue
from itertools import cycle
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup
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
    print(f"{Fore.RED}[❌] main.py not found! Please create main.py with your email credentials")
    sys.exit(1)

# Initialize colorama
init(autoreset=True)

# ========== ASCII ART ==========
BANNER = f"""
{Fore.RED}███████╗██╗███████╗██╗  ██╗██╗   ██╗
{Fore.RED}╚══███╔╝██║██╔════╝██║ ██╔╝╚██╗ ██╔╝
{Fore.YELLOW}  ███╔╝ ██║███████╗█████╔╝  ╚████╔╝ 
{Fore.YELLOW} ███╔╝  ██║╚════██║██╔═██╗   ╚██╔╝  
{Fore.GREEN}███████╗██║███████║██║  ██╗   ██║   
{Fore.GREEN}╚══════╝╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   
{Fore.CYAN}=====================================
{Fore.CYAN}    WHATSAPP BAN ENGINE v2.0
{Fore.CYAN}=====================================
{Fore.WHITE}Developer: @zisky_dev
{Fore.CYAN}====================================={Style.RESET_ALL}
"""

LOGIN_ART = f"""
{Fore.CYAN}╔═══════════════════════════════════════╗
{Fore.CYAN}║     WHATSAPP UNBAN TOOL v2.0        ║
{Fore.CYAN}║        AUTHORIZED ACCESS ONLY        ║
{Fore.CYAN}╚═══════════════════════════════════════╝{Style.RESET_ALL}
"""

MENU_ART = f"""
{Fore.MAGENTA}████████╗ ██████╗  ██████╗ ██╗     ███████╗
{Fore.MAGENTA}╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
{Fore.BLUE}   ██║   ██║   ██║██║   ██║██║     ███████╗
{Fore.BLUE}   ██║   ██║   ██║██║   ██║██║     ╚════██║
{Fore.GREEN}   ██║   ╚██████╔╝╚██████╔╝███████╗███████║
{Fore.GREEN}   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝{Style.RESET_ALL}
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

# ========== PROXY MANAGER ==========
class ProxyManager:
    def __init__(self):
        self.all_proxies = []
        self.working_proxies = []
        self.current_index = 0
        self.lock = threading.Lock()
        self.test_urls = [
            "http://httpbin.org/ip",
            "http://api.ipify.org?format=json",
            "http://ident.me"
        ]
        
        self.proxy_sources = [
            "https://www.sslproxies.org/",
            "https://free-proxy-list.net/",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
            "https://www.proxy-list.download/api/v1/get?type=http",
            "https://www.proxy-list.download/api/v1/get?type=https",
            "https://www.proxy-list.download/api/v1/get?type=socks4",
            "https://www.proxy-list.download/api/v1/get?type=socks5",
        ]
    
    def harvest_proxies(self):
        """Harvest proxies from all sources"""
        print(f"{Fore.CYAN}[🌐] Harvesting proxies from {len(self.proxy_sources)} sources...")
        
        harvested = []
        for i, source in enumerate(self.proxy_sources):
            try:
                print(f"{Fore.YELLOW}[{i+1}/{len(self.proxy_sources)}] Fetching...", end="\r")
                
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'}
                response = requests.get(source, headers=headers, timeout=15, verify=False)
                
                if response.status_code == 200:
                    if 'api.proxyscrape.com' in source or 'raw.githubusercontent' in source:
                        proxies = response.text.strip().split('\n')
                        for proxy in proxies:
                            proxy = proxy.strip()
                            if proxy and ':' in proxy:
                                harvested.append(proxy)
                    else:
                        soup = BeautifulSoup(response.text, 'html.parser')
                        rows = soup.find_all('tr')
                        for row in rows:
                            cols = row.find_all('td')
                            if len(cols) >= 2:
                                ip = cols[0].text.strip()
                                port = cols[1].text.strip()
                                if ip and port and re.match(r'^\d+\.\d+\.\d+\.\d+$', ip):
                                    harvested.append(f"{ip}:{port}")
                
                time.sleep(0.5)
                
            except Exception as e:
                continue
        
        self.all_proxies = list(set(harvested))
        print(f"{Fore.GREEN}[✅] Harvested {len(self.all_proxies)} unique proxies      ")
        return self.all_proxies
    
    def test_proxy(self, proxy):
        """Test if a proxy works"""
        try:
            proxy_parts = proxy.split(':')
            if len(proxy_parts) != 2:
                return False
            
            ip, port = proxy_parts
            port = int(port)
            
            for test_url in self.test_urls:
                try:
                    proxies = {
                        'http': f'http://{proxy}',
                        'https': f'http://{proxy}'
                    }
                    
                    response = requests.get(
                        test_url, 
                        proxies=proxies, 
                        timeout=PROXY_TEST_TIMEOUT,
                        verify=False
                    )
                    
                    if response.status_code == 200:
                        return True
                        
                except:
                    continue
            
            return False
            
        except:
            return False
    
    def test_proxies_concurrent(self):
        """Test proxies concurrently"""
        print(f"{Fore.CYAN}[🔍] Testing {min(len(self.all_proxies), MAX_PROXIES_TO_TEST)} proxies...")
        
        to_test = self.all_proxies[:MAX_PROXIES_TO_TEST]
        self.working_proxies = []
        
        def test_worker(proxy):
            if self.test_proxy(proxy):
                with self.lock:
                    self.working_proxies.append(proxy)
                    print(f"{Fore.GREEN}[✅] Working: {proxy} ({len(self.working_proxies)})", end="\r")
        
        threads = []
        for proxy in to_test:
            thread = threading.Thread(target=test_worker, args=(proxy,))
            thread.start()
            threads.append(thread)
            
            if len(threads) >= 30:
                for t in threads:
                    t.join()
                threads = []
        
        for t in threads:
            t.join()
        
        print(f"\n{Fore.GREEN}[✅] Found {len(self.working_proxies)} working proxies")
        return self.working_proxies
    
    def get_proxy(self):
        """Get next working proxy in rotation"""
        with self.lock:
            if not self.working_proxies:
                return None
            
            if self.current_index >= len(self.working_proxies):
                self.current_index = 0
            
            proxy = self.working_proxies[self.current_index]
            self.current_index += 1
            return proxy

# ========== EMAIL SENDER WITH PROXY ROTATION ==========
class EmailSender:
    def __init__(self, proxy_manager=None):
        self.proxy_manager = proxy_manager
        self.email_accounts = EMAIL_ACCOUNTS
        self.account_cycle = cycle(EMAIL_ACCOUNTS)
        self.sent_count = 0
        self.success_count = 0
    
    def send_email(self, to_email, subject, body, use_proxy=True):
        """Send email with optional proxy rotation"""
        
        # Get next email account
        account = next(self.account_cycle)
        
        # Save original socket
        original_socket = socket.socket
        
        try:
            # Set up proxy if enabled and available
            if use_proxy and self.proxy_manager:
                proxy = self.proxy_manager.get_proxy()
                if proxy:
                    proxy_parts = proxy.split(':')
                    proxy_ip, proxy_port = proxy_parts[0], int(proxy_parts[1])
                    
                    # Set SOCKS proxy
                    socks.set_default_proxy(socks.SOCKS5, proxy_ip, proxy_port)
                    socket.socket = socks.socksocket
            
            # Create message
            msg = MIMEMultipart()
            msg['From'] = account['email']
            msg['To'] = to_email
            msg['Subject'] = subject
            
            # Add random headers to look legit
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
            
            return True
            
        except Exception as e:
            # Reset socket on error
            try:
                socks.set_default_proxy()
                socket.socket = original_socket
            except:
                pass
            
            return False

# ========== WHATSAPP API FUNCTIONS ==========
def check_whatsapp_number(phone):
    """Check if number is registered on WhatsApp using Business API"""
    
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
EMERGENCY: CRITICAL FRAUD REPORT - {phone}

To WhatsApp Legal Department & Trust & Safety Team,

This is an URGENT and CRITICAL report regarding phone number {phone} which is being used for SERIOUS CRIMINAL ACTIVITY and poses an IMMEDIATE THREAT to user safety.

CRITICAL VIOLATIONS DETECTED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔴 CRIMINAL IMPERSONATION: This account is impersonating a public figure to defraud victims
🔴 SOPHISTICATED SCAM OPERATION: Multi-stage fraud scheme with documented victims
🔴 IDENTITY THEFT: Using fake identity to gain trust and extract sensitive information
🔴 FINANCIAL FRAUD: Requests for money, cryptocurrency, and banking details
🔴 PATTERN OF ABUSE: Multiple complaints from different users about the same number

VICTIM IMPACT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Elderly victims being targeted specifically
- Financial losses documented (screenshots attached)
- Psychological distress reported by multiple victims
- Personal information compromised

LEGAL REFERENCE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
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
    print(f"{Fore.CYAN}╔═══════════════════════════════════════╗")
    print(f"{Fore.CYAN}║           SYSTEM LOGIN                ║")
    print(f"{Fore.CYAN}╚═══════════════════════════════════════╝{Style.RESET_ALL}\n")
    
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
    
    print(f"{Fore.RED}Too many failed attempts. Exiting...")
    return False

# ========== MAIN APPLICATION ==========
class ZiskyWhatsAppBan:
    def __init__(self):
        self.proxy_manager = None
        self.email_sender = None
        self.running = True
        
        if USE_PROXIES:
            self.proxy_manager = ProxyManager()
        
        self.email_sender = EmailSender(self.proxy_manager)
    
    def initialize(self):
        """Initialize tool - harvest and test proxies if enabled"""
        clear()
        print(BANNER)
        print(f"{Fore.CYAN}[⚡] Initializing Zisky WhatsApp Ban Engine v2.0...")
        
        if USE_PROXIES and self.proxy_manager:
            print(f"{Fore.CYAN}[🌐] Proxy rotation: ENABLED")
            self.proxy_manager.harvest_proxies()
            self.proxy_manager.test_proxies_concurrent()
            
            if len(self.proxy_manager.working_proxies) == 0:
                print(f"{Fore.YELLOW}[⚠️] No working proxies found! Continuing without proxies...")
                USE_PROXIES = False
        else:
            print(f"{Fore.YELLOW}[⚠️] Proxy rotation: DISABLED")
        
        print(f"{Fore.GREEN}[✅] Email accounts loaded: {len(EMAIL_ACCOUNTS)}")
        print(f"{Fore.GREEN}[✅] WhatsApp support emails: {len(SUPPORT_EMAILS)}")
        print(f"{Fore.GREEN}[✅] Initialization complete!")
        time.sleep(2)
    
    def show_menu(self):
        clear()
        print(BANNER)
        print(MENU_ART)
        print(f"{Fore.CYAN}╔═══════════════════════════════════════╗")
        print(f"{Fore.CYAN}║           MAIN MENU                   ║")
        print(f"{Fore.CYAN}╚═══════════════════════════════════════╝{Style.RESET_ALL}\n")
        
        print(f"{Fore.GREEN}[1]{Style.RESET_ALL} 📩 Unban Request (Temporary)")
        print(f"{Fore.GREEN}[2]{Style.RESET_ALL} 🚫 Unban Request (Permanent)")
        print(f"{Fore.GREEN}[3]{Style.RESET_ALL} 🔍 Check WhatsApp Number Status")
        print(f"{Fore.GREEN}[4]{Style.RESET_ALL} ⚠️ Report Fraud/Scam Number")
        print(f"{Fore.GREEN}[5]{Style.RESET_ALL} 💀 Hard Report (Critical/Escalated)")
        print(f"{Fore.GREEN}[6]{Style.RESET_ALL} 📊 System Status")
        print(f"{Fore.RED}[0]{Style.RESET_ALL} ❌ Exit\n")
        
        if USE_PROXIES and self.proxy_manager:
            print(f"{Fore.CYAN}📊 Proxies: {len(self.proxy_manager.working_proxies)} working")
        print(f"{Fore.CYAN}📧 Emails: {self.email_sender.sent_count} sent ({self.email_sender.success_count} successful)")
        print()
    
    def get_phone_number(self):
        """Get and validate phone number"""
        while True:
            phone = input(f"{Fore.YELLOW}📞 Enter number with country code (e.g., +2348123456789): {Style.RESET_ALL}").strip()
            if re.match(r"^\+\d{10,15}$", phone):
                return phone
            else:
                print(f"{Fore.RED}❌ Invalid format! Must start with + and contain 10-15 digits.")
    
    def send_mass_emails(self, phone, template_func, count=EMAILS_PER_TARGET):
        """Send multiple emails with different templates"""
        
        print(f"\n{Fore.CYAN}[📧] Sending {count} emails...")
        
        success = 0
        for i in range(count):
            # Rotate through support emails
            to_email = random.choice(SUPPORT_EMAILS)
            
            # Generate unique subject with random reference
            ref = random.randint(10000, 99999)
            subject = f"Case #{ref}: WhatsApp Report - {phone[:5]}***{phone[-3:]}"
            
            # Get template (slightly different each time)
            body = template_func(phone)
            
            # Send email
            result = self.email_sender.send_email(to_email, subject, body, use_proxy=USE_PROXIES)
            
            if result:
                success += 1
            
            # Show progress
            progress = (i + 1) / count * 100
            bar_length = 30
            filled = int(bar_length * (i + 1) / count)
            bar = '█' * filled + '░' * (bar_length - filled)
            
            status = f"{Fore.GREEN}✅" if result else f"{Fore.RED}❌"
            print(f"{Fore.CYAN}[{bar}] {progress:.1f}% {status}", end="\r")
            
            # Random delay
            delay = random.uniform(MIN_DELAY_SECONDS, MAX_DELAY_SECONDS)
            time.sleep(delay)
        
        print(f"\n{Fore.GREEN}[✅] Emails sent: {success}/{count}")
        return success
    
    def run_report(self, report_type):
        """Generic report function"""
        
        phone = self.get_phone_number()
        
        # Optional: Check if number exists on WhatsApp
        print(f"\n{Fore.CYAN}[🔍] Checking number status...")
        exists = check_whatsapp_number(phone)
        
        if exists is False:
            print(f"{Fore.YELLOW}[⚠️] Number may not be registered on WhatsApp. Continue anyway? (y/n): ")
            if input().lower() != 'y':
                return
        
        # Map report types to template functions
        templates = {
            'temp': ReportTemplates.get_unban_temp,
            'perm': ReportTemplates.get_unban_perm,
            'fraud': ReportTemplates.get_fraud_report,
            'hard': ReportTemplates.get_hard_report
        }
        
        template_func = templates.get(report_type)
        
        # Confirm
        print(f"\n{Fore.YELLOW}[⚠️] Ready to send {EMAILS_PER_TARGET} emails for {phone}")
        confirm = input(f"{Fore.YELLOW}Continue? (y/n): {Style.RESET_ALL}").lower()
        
        if confirm == 'y':
            success = self.send_mass_emails(phone, template_func)
            
            print(f"\n{Fore.GREEN}{'='*50}")
            print(f"{Fore.GREEN}[✅] REPORT COMPLETE!")
            print(f"{Fore.GREEN}{'='*50}")
            print(f"{Fore.CYAN}Target: {phone}")
            print(f"{Fore.CYAN}Emails sent: {success}/{EMAILS_PER_TARGET}")
            print(f"{Fore.CYAN}Success rate: {(success/EMAILS_PER_TARGET)*100:.1f}%")
            
            if success > EMAILS_PER_TARGET * 0.7:
                print(f"{Fore.RED}[💀] High chance of ban within 24-48 hours!")
            elif success > EMAILS_PER_TARGET * 0.4:
                print(f"{Fore.YELLOW}[⚠️] Moderate chance of action")
            else:
                print(f"{Fore.BLUE}[ℹ️] Low success rate - try adding more email accounts")
            
            print(f"{Fore.GREEN}{'='*50}")
        
        input(f"\n{Fore.YELLOW}Press Enter to continue...")
    
    def show_status(self):
        """Show system status"""
        clear()
        print(f"{Fore.CYAN}╔═══════════════════════════════════════╗")
        print(f"{Fore.CYAN}║         SYSTEM STATUS                 ║")
        print(f"{Fore.CYAN}╚═══════════════════════════════════════╝{Style.RESET_ALL}\n")
        
        print(f"{Fore.GREEN}📧 Email Accounts: {len(EMAIL_ACCOUNTS)}")
        for i, acc in enumerate(EMAIL_ACCOUNTS, 1):
            masked = acc['email'][:3] + "***" + acc['email'][acc['email'].find('@'):]
            print(f"  {i}. {masked}")
        
        print(f"\n{Fore.GREEN}📧 Support Emails: {len(SUPPORT_EMAILS)}")
        
        if USE_PROXIES and self.proxy_manager:
            print(f"\n{Fore.GREEN}🌐 Proxies: {len(self.proxy_manager.working_proxies)} working")
        else:
            print(f"\n{Fore.YELLOW}🌐 Proxies: DISABLED")
        
        print(f"\n{Fore.GREEN}📊 Statistics:")
        print(f"  Total emails sent: {self.email_sender.sent_count}")
        print(f"  Successful: {self.email_sender.success_count}")
        print(f"  Success rate: {(self.email_sender.success_count/max(1,self.email_sender.sent_count))*100:.1f}%")
        
        print(f"\n{Fore.GREEN}⚙️ Settings:")
        print(f"  Emails per target: {EMAILS_PER_TARGET}")
        print(f"  Delay range: {MIN_DELAY_SECONDS}-{MAX_DELAY_SECONDS}s")
        
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
                    print(f"{Fore.YELLOW}\n[👋] Goodbye!")
                    self.running = False
                else:
                    print(f"{Fore.RED}❌ Invalid option!")
                    time.sleep(1)
                    
            except KeyboardInterrupt:
                print(f"\n{Fore.YELLOW}[👋] Interrupted. Exiting...")
                self.running = False
            except Exception as e:
                print(f"{Fore.RED}[❌] Error: {e}")
                time.sleep(2)

# ========== ENTRY POINT ==========
if __name__ == "__main__":
    app = ZiskyWhatsAppBan()
    app.run()
