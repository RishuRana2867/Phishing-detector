# 🔍 Phishing Detector

A lightweight **Python-based phishing domain detection tool** that identifies suspicious domains using **domain extraction, typo similarity detection, and suspicious TLD analysis**.

This tool helps detect phishing websites by comparing domains against a **trusted domain database** and analyzing domain similarity.

---

# 🚀 Features

* Detects **phishing domains**
* **Typo-squatting detection** using Levenshtein similarity
* **Automatic root domain extraction**
* Detection of **suspicious TLDs** often used in phishing
* Uses a **custom domain database (`domains.txt`)**
* **Command-line interface**
* **Linux terminal banner output**
* Lightweight and fast

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
└── .gitignore
```

---

# ⚙️ Installation (Linux)

Follow these steps to install and run the tool on **Kali Linux, Ubuntu, Debian, or other Linux distributions**.

## 1️⃣ Clone the repository

```
git clone https://github.com/RishuRana2867/Phishing-detector.git
```

---

## 2️⃣ Move into the project directory

```
cd Phishing-detector
```

---

## 3️⃣ Install required dependencies

```
pip3 install -r requirements.txt --break-system-packages
```

---

# ▶️ Running the Tool

Run the tool using:

```
python3 phishscan.py <domain>
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

# 📦 Requirements

The project uses the following Python libraries:

```
tldextract
python-Levenshtein
colorama
```

Install them with:

```
pip3 install -r requirements.txt
```

---

# 🌐 Domain Database

The tool uses a **domain database (`domains.txt`)** containing legitimate domains.

Example:

```
google.com
facebook.com
amazon.com
github.com
wikipedia.org
```

You can add more trusted domains to **improve phishing detection accuracy**.

---

# ⚠️ Disclaimer

This project is intended **for educational purposes and cybersecurity research only**.

Do **not use this tool for illegal activities**.
The developer is **not responsible for misuse** of this software.

---

# 👨‍💻 Author

**Rishu Rana**

LinkedIn
https://www.linkedin.com/in/rishu-rana-32429a376/

---

⚡ *Learning cybersecurity by building real tools.*
