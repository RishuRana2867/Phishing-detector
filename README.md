# 🔍 Phishing Detector

A lightweight **Python-based phishing domain detection tool** that analyzes URLs and detects suspicious or malicious domains using multiple detection techniques such as typo detection, suspicious TLD analysis, and phishing keyword detection.

The tool is designed for **educational purposes and cybersecurity learning**, helping users understand how phishing domains are identified.

---

# 🚀 Features

* Detects **typo-squatting phishing domains**
* Detects **suspicious Top Level Domains (TLDs)**
* Detects **phishing keywords in URLs**
* Detects **IDN homograph attacks**
* Extracts **root domain automatically**
* Uses a **custom legitimate domain database**
* Clean **command-line interface**
* **Linux-style terminal banner**

---

# 🛠 Technologies Used

* Python
* tldextract
* python-Levenshtein
* colorama

---

# 📂 Project Structure

```
Phishing-detector/
│
├── phishscan.py
├── domains.txt
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

---

# ⚙️ Installation (Linux)

Follow these steps to install and run the tool on **Kali Linux, Ubuntu, Debian, or other Linux distributions**.

## 1️⃣ Clone the repository

```
git clone https://github.com/USERNAME/Phishing-detector.git
```

---

## 2️⃣ Move into the project directory

```
cd Phishing-detector
```

---

## 3️⃣ Install dependencies

```
pip3 install -r requirements.txt --break-system-packages
```

---

# ▶️ Running the Tool

Run the script with a domain or URL:

```
python3 phishscan.py <url>
```

Example:

```
python3 phishscan.py google.com
```

---

# 💻 Example Usage

### Legitimate domain

```
$ python3 phishscan.py google.com

SAFE ✅ Legitimate Website
```

---

### Typo-phishing domain

```
$ python3 phishscan.py goggle.com

PHISHING 🚨 Looks like google.com
```

---

### Suspicious TLD

```
$ python3 phishscan.py paypal-login.xyz

SUSPICIOUS ⚠ Suspicious TLD detected
```

---

# 🌐 Domain Database

The tool uses a **domain database (`domains.txt`)** containing legitimate domains used for comparison.

Example:

```
google.com
facebook.com
amazon.com
github.com
wikipedia.org
```

Users can add more trusted domains to improve phishing detection accuracy.

---

# 📦 Requirements

The following Python libraries are required:

```
tldextract
python-Levenshtein
colorama
```

Install them using:

```
pip3 install -r requirements.txt
```

---

# 🔮 Future Improvements

Planned improvements for the project include:

* Domain age detection using WHOIS
* DNS reputation checks
* Threat intelligence integration
* Machine learning phishing detection

---

# ⚠️ Disclaimer

This tool is intended **for educational and cybersecurity research purposes only**.

Do **not use this tool for illegal activities**.
The author is **not responsible for misuse** of this software.

---

⚡ *Learning cybersecurity by building practical tools.*
