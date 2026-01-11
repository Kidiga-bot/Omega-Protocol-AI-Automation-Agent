# 🦅 Omega Protocol: AI Automation Agent

**Omega Protocol** is a full-stack AI application designed to automate document analysis and data extraction. Built on the bleeding edge of **Multimodal LLMs**, it turns unstructured data (Invoices, Receipts, Contracts) into structured financial ledgers automatically.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![Groq](https://img.shields.io/badge/Hardware-Groq%20LPU-orange)
![Model](https://img.shields.io/badge/AI-Llama%204%20Maverick-purple)

## 🚀 Features

* **Multimodal Vision:** Uses **Meta Llama 4 Maverick** (via Groq) to "read" images, screenshots, and scanned PDFs with human-level accuracy.
* **Zero-Latency Interface:** Powered by **Groq LPUs**, ensuring near-instant analysis speeds.
* **Automated Clerk:** Automatically extracts key fields (Vendor, Total, Date, Risk Level) and logs them into a persistent CSV ledger.
* **Model Agnostic:** Built with a modular architecture allowing hot-swapping between Llama 3, Llama 4, and Gemini models.
* **Local Privacy:** All database files (`financial_report.csv`) are stored locally on the machine, ensuring data sovereignty.

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Logic:** Python
* **AI Inference:** Groq Cloud API
* **Models:** Llama-4-Maverick-17b, Llama-3.3-70b
* **Data Handling:** Pandas & JSON

## 📦 Installation

1. **Clone the repository:**

    ```bash
    git clone [https://github.com/your-username/omega-protocol.git](https://github.com/your-username/omega-protocol.git)
    cd omega-protocol
    ```

2. **Install dependencies:**

    ```bash
    pip install streamlit groq pandas pillow
    ```

3. **Set up API Keys:**
    * Open `app.py`.
    * Replace `PASTE_YOUR_GROQ_KEY_HERE` with your actual Groq API Key.
    * *(Note: In production, use environment variables or Streamlit secrets).*

## ⚡ Usage

Run the application locally:

```bash
streamlit run app.py
