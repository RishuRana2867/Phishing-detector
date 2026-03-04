#!/usr/bin/env python3

import tldextract
import Levenshtein as lv
import argparse
from colorama import Fore, Style, init
import re

init(autoreset=True)

# Suspicious TLDs often used in phishing
suspicious_tlds = [
    "xyz", "tk", "ml", "ga", "cf", "gq", "top", "work", "click"
]

# Suspicious phishing keywords
phishing_keywords = [
    "login", "secure", "verify", "update",
    "account", "bank", "wallet", "signin",
    "confirm", "password", "auth"
]

# ===============================
# Banner
# ===============================
def banner():
    print(Fore.CYAN + """
██████╗ ██╗  ██╗██╗███████╗██╗  ██╗
██╔══██╗██║  ██║██║██╔════╝██║  ██║
██████╔╝███████║██║███████╗███████║
██╔═══╝ ██╔══██║██║╚════██║██╔══██║
██║     ██║  ██║██║███████║██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝

        Phishing Detector 🔍
""")


# ===============================
# Load legitimate domains
# ===============================
def load_domains():
    try:
        with open("domains.txt") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(Fore.RED + "domains.txt not found!")
        exit()


legitimate_domains = load_domains()


# ===============================
# Extract domain info
# ===============================
def extract_domain(url):

    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    extracted = tldextract.extract(url)

    domain = extracted.domain
    suffix = extracted.suffix

    root_domain = domain + "." + suffix

    return root_domain, domain, suffix


# ===============================
# Typo detection
# ===============================
def typo_detection(domain):

    for legit in legitimate_domains:

        legit_name = legit.split(".")[0]

        similarity = lv.ratio(domain, legit_name)

        if similarity >= 0.8 and domain != legit_name:
            return legit

    return None


# ===============================
# Suspicious keyword detection
# ===============================
def keyword_detection(url):

    for word in phishing_keywords:
        if word in url.lower():
            return word

    return None


# ===============================
# IDN / Homograph detection
# ===============================
def idn_detection(domain):

    if domain.startswith("xn--"):
        return True

    return False


# ===============================
# Main detection
# ===============================
def detect(url):

    root_domain, domain, suffix = extract_domain(url)

    # Legitimate domain
    if root_domain in legitimate_domains:
        print(Fore.GREEN + "SAFE ✅ Legitimate Website")
        return

    # IDN attack
    if idn_detection(domain):
        print(Fore.RED + "PHISHING 🚨 Possible IDN homograph attack")
        return

    # Suspicious TLD
    if suffix in suspicious_tlds:
        print(Fore.YELLOW + f"SUSPICIOUS ⚠ Suspicious TLD: .{suffix}")

    # Typo detection
    typo = typo_detection(domain)

    if typo:
        print(Fore.RED + f"PHISHING 🚨 Looks like {typo}")
        return

    # Keyword detection
    keyword = keyword_detection(url)

    if keyword:
        print(Fore.YELLOW + f"SUSPICIOUS ⚠ Contains phishing keyword: {keyword}")

    print(Fore.YELLOW + "UNKNOWN ⚠ Domain not in database")


# ===============================
# CLI
# ===============================
def main():

    banner()

    parser = argparse.ArgumentParser(
        description="Phishing Detector - Detect phishing domains"
    )

    parser.add_argument("url", help="URL or domain to scan")

    args = parser.parse_args()

    detect(args.url)


if __name__ == "__main__":
    main()
