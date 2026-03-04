# Phishing URL Detector 🔐

A Python-based phishing URL detector that identifies suspicious and malicious links using domain extraction and similarity analysis.

This tool analyzes domain names, detects possible typo-squatting attacks, and checks if a URL resembles well-known legitimate websites.

---

# 🚀 Features

* Detects phishing URLs
* Automatic subdomain detection
* Root domain extraction
* Typo-domain detection using Levenshtein similarity
* User input URL scanning
* Lightweight and fast

---

# 🛠 Technologies Used

* Python
* tldextract
* python-Levenshtein

---

---

# ⚙️ Installation (Linux)

Follow these steps to install and run the tool on Linux (Kali Linux, Ubuntu, Debian, etc.).

## 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/phishing-detector.git
```

## 2️⃣ Move into the project directory

```bash
cd phishing-detector
```

## 3️⃣ Install Python and pip (if not already installed)

```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

## 4️⃣ Install required Python libraries

Using the requirements file:

```bash
pip3 install -r requirements.txt
```

If your Linux shows **externally managed environment error**, run:

```bash
pip3 install -r requirements.txt --break-system-packages
```

Or install libraries manually:

```bash
pip3 install tldextract
pip3 install python-Levenshtein
```

---

# ▶️ Running the Tool

Run the Python script:

```bash
python3 phishscan.py
```

---

# 💻 Example Usage

```
Enter URL (or type exit): google.com
Result: SAFE ✅ Legitimate Website

Enter URL (or type exit): goggle.com
Result: PHISHING 🚨 Looks like google.com

Enter URL (or type exit): amazon-secure-login.xyz
Result: SUSPICIOUS ⚠️ Unknown Domain
```

---

# 📦 Requirements

requirements.txt

```
tldextract
python-Levenshtein
```



# 🔍 How It Works

1. The tool extracts the **root domain** from the given URL.
2. It checks if the domain matches a **known legitimate domain**.
3. If not, it calculates **similarity using Levenshtein distance**.
4. If similarity is high, the domain may be a **typo-phishing domain**.
5. Otherwise, the domain is marked as **suspicious**.



# ⚠️ Disclaimer

This tool is created for **educational and cybersecurity research purposes only**.

Do **not** use this tool for illegal activities.

The developer is **not responsible for misuse** of this software.
