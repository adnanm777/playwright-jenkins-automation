# Playwright AI Self-Healing Automation

A Python-based Playwright automation project that demonstrates **AI-powered locator self-healing**.

The project detects when a Playwright locator fails, analyzes the page for possible matching elements, uses AI to identify the most suitable replacement, and applies the replacement only when the confidence score meets a defined safety threshold.

## 🛠️ Tech Stack

* Python
* Playwright
* Pytest
* Google Gemini API
* Git & GitHub
* SequenceMatcher
* AI-based Locator Healing

---

## 🎯 Project Objective

In normal UI automation, a test can fail when a locator changes.

For example:

```text
Original locator:
Build your cheap computer
```

If the website changes the text to:

```text
Build your own cheap computer
```

the original locator may fail.

This project attempts to automatically find a suitable replacement instead of immediately failing the test.

---

## 🔄 How Self-Healing Works

```text
Playwright Test
       ↓
Original Locator
       ↓
Locator Fails
       ↓
Failure Analysis
       ↓
Search Page for Candidates
       ↓
Compare Possible Matches
       ↓
AI Evaluates Candidate
       ↓
Confidence Score
       ↓
Safety Check
       ↓
Accept or Reject
       ↓
Execute Healed Locator
```

---

## 🤖 AI Locator Healing

The project uses Google Gemini to analyze possible locator replacements.

Example:

```text
Broken Text:
Build your cheap computer

AI Suggested Text:
Build your own cheap computer

Confidence:
0.95

Result:
Healed locator accepted
```

The AI suggestion is not automatically trusted.

A confidence threshold is used to reduce the chance of selecting an incorrect element.

---

## 🛡️ Safe Healing

The project includes a safety mechanism for AI-generated locator suggestions.

For example:

```text
Confidence = 0.95
Threshold  = 0.85

Result:
ACCEPT
```

But:

```text
Confidence = 0.10
Threshold  = 0.85

Result:
REJECT
```

This prevents low-confidence AI suggestions from being used automatically.

---

## 🔎 Candidate Locator Search

The project can search the page for possible matching elements such as:

* Links
* Buttons
* Inputs
* Labels
* Headings
* Text elements

The candidates are compared with the failed locator to identify possible replacements.

---

## 📁 Project Structure

```text
playwright_demo1/
│
├── healing/
│   ├── __init__.py
│   ├── ai_healer.py
│   ├── safe_ai_healer.py
│   ├── locator_healer.py
│   ├── generic_locator_healer.py
│   └── failure_analyzer.py
│
├── test_self_healing.py
├── test_ai.py
├── test_low_confidence.py
├── test_playwright_healing.py
├── test_playwright_healing_backup.py
│
├── demoshop.py
├── demoshop_backup.py
│
├── page/
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── admin_page.py
│   ├── pim_page.py
│   ├── leave_page.py
│   └── time_page.py
│
├── tests/
│   ├── conftest.py
│   └── test_ornghrm.py
│
└── .gitignore
```

---

## 🌐 Demo Application

The self-healing demonstration uses the **Tricentis Demo Web Shop**:

```text
https://demowebshop.tricentis.com/
```

The test intentionally works with a locator that can be changed or made invalid so that the healing mechanism can be demonstrated.

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/adnanm777/playwright-jenkins-automation.git
```

Open the project:

```bash
cd playwright-jenkins-automation
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install Playwright and Pytest:

```bash
pip install playwright pytest
```

Install Chromium:

```bash
python -m playwright install chromium
```

---

## 🔐 Gemini API Key

The project reads the Gemini API key from an environment variable.

The code uses:

```python
os.getenv("GEMINI_API_KEY")
```

Set the environment variable on your local machine before running the AI tests.

### Windows CMD

```cmd
set GEMINI_API_KEY=YOUR_API_KEY
```

For permanent configuration, add `GEMINI_API_KEY` through Windows Environment Variables.

**Never commit your real API key to GitHub.**

---

## ▶️ Run the Self-Healing Test

Run:

```bash
python -m pytest test_self_healing.py -s --headed
```

The test runs the browser in headed mode so the healing process can be observed.

---

## 🧪 Example Result

A successful healing run can look like:

```text
Original locator failed
Failure screenshot saved

AI Suggested:
Build your own cheap computer

Confidence:
0.95

SAFE HEALING:
Healing accepted

Healed locator clicked successfully

1 passed
```

---

## 🧠 Main Components

### `ai_healer.py`

Responsible for communicating with the AI model and getting a possible locator replacement.

### `safe_ai_healer.py`

Adds a confidence-based safety check before accepting the AI suggestion.

### `generic_locator_healer.py`

Searches different types of elements on the page and compares their text with the failed locator.

### `locator_healer.py`

Provides locator-healing logic based on similarity matching.

### `failure_analyzer.py`

Helps analyze information related to the failed automation step.

### `test_self_healing.py`

Demonstrates the complete self-healing flow from locator failure to healed locator execution.

---

## 📌 Key Learning

This project demonstrates how AI can be used with Playwright automation to:

* Detect locator failures
* Analyze possible replacement elements
* Compare candidate elements
* Generate AI-based locator suggestions
* Assign confidence to suggestions
* Reject low-confidence suggestions
* Execute a healed locator when the suggestion passes the safety check

---

## ⚠️ Limitations

AI-based self-healing does not guarantee that every failed locator can be fixed correctly.

A wrong element may sometimes look similar to the intended element.

For this reason, the project uses a confidence threshold before accepting an AI suggestion.

This project is intended as a **learning and demonstration project**, not as a replacement for properly designed and maintained automation locators.

---

## 👨‍💻 Author

**Mohammad Adnan**

GitHub: https://github.com/adnanm777

---

## 📌 Project Focus

**Playwright + Python + Pytest + AI Locator Self-Healing**
