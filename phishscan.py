#!/usr/bin/env python3

import tldextract
import Levenshtein as lv
import argparse
from colorama import Fore, Style, init

init(autoreset=True)

# Suspicious TLDs
suspicious_tlds = ["xyz", "tk", "ml", "ga", "cf"]

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
    except:
        print(Fore.RED + "domains.txt not found!")
        exit()

legitimate_domains = load_domains()


# ===============================
# Extract root domain
# ===============================
def extract_root_domain(url):

    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    extracted = tldextract.extract(url)

    return extracted.domain + "." + extracted.suffix


# ===============================
# Typo detection
# ===============================
def is_typo_domain(domain, threshold=0.85):

    for legit in legitimate_domains:

        similarity = lv.ratio(domain, legit)

        if similarity >= threshold and domain != legit:
            return legit

    return None


# ===============================
# Main detection
# ===============================
def check_url(url):

    root_domain = extract_root_domain(url)

    # Safe domain
    if root_domain in legitimate_domains:
        print(Fore.GREEN + "SAFE ✅ Legitimate Website")
        return

    # Suspicious TLD
    tld = root_domain.split(".")[-1]

    if tld in suspicious_tlds:
        print(Fore.YELLOW + "SUSPICIOUS ⚠ Suspicious TLD detected")

    # Typo phishing
    typo = is_typo_domain(root_domain)

    if typo:
        print(Fore.RED + f"PHISHING 🚨 Looks like {typo}")
        return

    print(Fore.YELLOW + "UNKNOWN ⚠ Domain not in database")


# ===============================
# CLI arguments
# ===============================
def main():

    banner()

    parser = argparse.ArgumentParser(
        description="Phishing Detector - Detect phishing domains"
    )

    parser.add_argument("url", help="Domain or URL to scan")

    args = parser.parse_args()

    check_url(args.url)


if __name__ == "__main__":
    main()
