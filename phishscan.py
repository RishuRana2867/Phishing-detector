import tldextract
import Levenshtein as lv

# Only add ROOT DOMAINS here
legitimate_domains = [
    "google.com",
    "facebook.com",
    "amazon.com",
    "amazon.in",
    "microsoft.com",
    "paypal.com",
    "apple.com",
    "netflix.com",
    "github.com",
    "wikipedia.org",
    "sbi.co.in",
    "hdfcbank.com",
    "icicibank.com",
    "axisbank.com",
    "idfcfirst.bank.in",
    "paytm.com",
    "phonepe.com",
    "flipkart.com"
]


# Extract root domain automatically
def extract_root_domain(url):

    if not url.startswith("http"):
        url = "http://" + url

    extracted = tldextract.extract(url)

    root_domain = extracted.domain + "." + extracted.suffix

    return root_domain


# Typo detection
def is_typo_domain(domain, threshold=0.8):

    for legit in legitimate_domains:

        similarity = lv.ratio(domain, legit)

        if similarity >= threshold:
            return legit

    return None


# Main detector
def check_url(url):

    root_domain = extract_root_domain(url)

    # Safe domain check (subdomains automatically allowed)
    if root_domain in legitimate_domains:

        return "SAFE ✅ Legitimate Website"


    # Typo phishing detection
    typo_match = is_typo_domain(root_domain)

    if typo_match:

        return f"PHISHING 🚨 Looks like {typo_match}"


    return "SUSPICIOUS ⚠️ Unknown Domain"



# User input loop
while True:

    url = input("\nEnter URL (or type exit): ")

    if url.lower() == "exit":
        break

    result = check_url(url)

    print("Result:", result)