#!/usr/bin/env python3
"""
ZISKY WHATSAPP BAN v2.0 - YOUR CONFIGURATION
EDIT THIS FILE WITH YOUR REAL EMAIL ACCOUNTS AND PASSWORDS
"""

# ========== TOOL LOGIN CREDENTIALS ==========
# Change these to whatever you want
TOOL_USERNAME = "ziskyhimself"
TOOL_PASSWORD = "admins"

# ========== YOUR EMAIL ACCOUNTS ==========
# REPLACE these with YOUR REAL email and app passwords
EMAIL_ACCOUNTS = [
    {
        'email': 'managerhimself032@gmail.com',     # ← CHANGE TO YOUR EMAIL
        'password': 'inagtgypnpyweleu',              # ← CHANGE TO YOUR APP PASSWORD
        'smtp_server': 'smtp.gmail.com',
        'smtp_port': 587
    },
    {
        'email': 'arsheeqarsheeqq@gmail.com',        # ← CHANGE TO YOUR EMAIL
        'password': 'pkkqfactxwkpvzgc',               # ← CHANGE TO YOUR APP PASSWORD
        'smtp_server': 'smtp.gmail.com',
        'smtp_port': 587
    },
    {
        'email': 'kingbadboi069@gmail.com',        # ← CHANGE TO YOUR EMAIL
        'password': 'qgifnqlsthrbzgbb',               # ← CHANGE TO YOUR APP PASSWORD
        'smtp_server': 'smtp.gmail.com',
        'smtp_port': 587
    },
    {
        'email': 'badboistill@gmail.com',         # ← CHANGE TO YOUR EMAIL
        'password': 'svwcrostswgapevv',               # ← CHANGE TO YOUR APP PASSWORD
        'smtp_server': 'smtp.gmail.com',
        'smtp_port': 587
    },
    {
        'email': 'aynation700@gmail.com',          # ← CHANGE TO YOUR EMAIL
        'password': 'ctteysjmdssgadnp',               # ← CHANGE TO YOUR APP PASSWORD
        'smtp_server': 'smtp.gmail.com',
        'smtp_port': 587
    }
]

# ========== WHATSAPP BUSINESS API ==========
# If you don't have these, the number check feature won't work
# You can leave them as empty strings
WHATSAPP_ACCESS_TOKEN = "EAAJgi17vyDYBPTGf8m4LNp0xFdUozhBKS6PTnrElQdSZCIRZCnuLFmBigzRvB4ZCUI8EBNuNZCFZBfG5e11ehZBujToi9S6zYQ3HSmDZBPNQHZBFFrd3ntSZAl6lRZAOa86mOZCp60VaaCMhgUN6s68EEvYSEJXlaIk9iiB7xe1rlZBKbEVf7YiIADUZA0kHuO9nr0QZDZD"  # Optional
WHATSAPP_PHONE_NUMBER_ID = "669101662914614"  # Optional

# ========== REPORT SETTINGS ==========
EMAILS_PER_TARGET = 30           # Number of emails to send per target
MIN_DELAY_SECONDS = 2          # Minimum delay between emails
MAX_DELAY_SECONDS = 5         # Maximum delay between emails
USE_PROXIES = True                # Set to False if you don't want proxy rotation

# ========== PROXY SETTINGS ==========
MAX_PROXIES_TO_TEST = 200        # Maximum proxies to harvest and test
PROXY_TEST_TIMEOUT = 10           # Seconds to wait for proxy test
PROXY_SOURCES_ENABLED = True      # Set to False to use only your own proxies
