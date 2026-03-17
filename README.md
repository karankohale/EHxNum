# 🕶 EHxNum – Phone Number OSINT Framework

<p align="center">
<b>Fast • Lightweight • Hacker-Style CLI • OSINT Intelligence</b>
</p>

<p align="center">
Created by <b>EHxAnomity</b><br>
YouTube: https://www.youtube.com/@ehxanomity
</p>

---

# 📌 About

**EHxNum** is a lightweight OSINT command-line tool that gathers publicly available information about phone numbers.

It provides useful intelligence such as:

* Country / region
* Carrier information
* Timezone
* Phone number validation
* OSINT search links
* Social media lookup links

The tool is designed to run smoothly on:

* Kali Linux
* Linux distributions
* macOS
* Termux (Android)

and provides a **clean hacker-style interface with animations and formatted output.**

---

# ⚠ Disclaimer

This tool collects **only publicly available OSINT information**.

This tool is created for **educational, research, and cybersecurity awareness purposes only.**

The author is **not responsible for misuse, harassment, or illegal activities performed using this tool.**

---

# ✨ Features

* Phone number validation
* Country detection
* Carrier lookup
* Timezone detection
* Google OSINT search links
* Social media search links
* Hacker-style CLI interface
* Loading animations
* Lightweight and fast

---

# 🖥 Supported Platforms

EHxNum works on:

* Kali Linux
* Ubuntu / Debian
* Arch Linux
* macOS
* Termux (Android)

---

# 📦 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/EHxNum.git
cd EHxNum
```

---

# 🐍 Python Environment Setup (Important)

Some systems block global `pip` installs and show errors.

If that happens, create a **virtual environment (venv)**.

## Create Virtual Environment

```bash
python3 -m venv venv
```

## Activate Virtual Environment

### Linux / Kali / macOS

```bash
source venv/bin/activate
```

### Termux

```bash
source venv/bin/activate
```

After activation your terminal will show:

```
(venv)
```

Now install dependencies.

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Running EHxNum

Run the tool using:

```bash
python ehxnum.py
```

You will see the EHxNum banner and initialization animation.

Then enter a phone number including the country code.

Example:

```
Enter phone number with country code: +919876543210
```

---

# 📊 Example Output

```
Target Number : +919876543210

Country       : India
Carrier       : Airtel
Timezone      : Asia/Kolkata
Valid Number  : True

OSINT Links
-------------------------
Google    : https://www.google.com/search?q="+919876543210"
Facebook  : https://www.facebook.com/search/top?q=+919876543210
Twitter   : https://twitter.com/search?q=+919876543210
LinkedIn  : https://www.linkedin.com/search/results/all/?keywords=+919876543210
```

---

# 📁 Project Structure

```
EHxNum
│
├── ehxnum.py
├── banner.py
├── animations.py
├── requirements.txt
├── README.md
│
└── modules
    ├── phone_lookup.py
    └── social_scan.py
```

---

# 📱 Termux Installation

Install required packages:

```bash
pkg update
pkg install python git
```

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/EHxNum.git
cd EHxNum
```

Create virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tool:

```bash
python ehxnum.py
```

---

# 🐧 Linux / Kali Installation

Install Python and Git if not installed.

```bash
sudo apt update
sudo apt install python3 python3-pip git
```

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/EHxNum.git
cd EHxNum
```

Create virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python ehxnum.py
```

---

# 🍎 macOS Installation

Install dependencies:

```bash
brew install python git
```

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/EHxNum.git
cd EHxNum
```

Create virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

Run tool:

```bash
python ehxnum.py
```

---

# 🧠 Usage Tips

* Always include **country code**
* Example:

```
+91XXXXXXXXXX
+1XXXXXXXXXX
+44XXXXXXXXXX
```

---

# 🤝 Contributing

Contributions, improvements, and ideas are welcome.

Feel free to fork the repository and submit pull requests.

---

# ⭐ Support

If you like this project please consider:

* ⭐ Starring the repository
* Sharing it with others
* Subscribing to the YouTube channel

YouTube: https://www.youtube.com/@ehxanomity

---

# 👤 Author

**EHxAnomity**

YouTube
https://www.youtube.com/@ehxanomity

---
