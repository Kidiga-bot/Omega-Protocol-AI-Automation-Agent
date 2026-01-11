import streamlit as st
import os
from groq import Groq
from PIL import Image
import json
import base64
import pandas as pd
from datetime import datetime

# 1. APP CONFIG
st.set_page_config(page_title="Omega AI: Auto-Clerk", layout="wide", page_icon="🤖")

# 2. CLIENT SETUP
# REPLACE WITH YOUR GROQ KEY
client = Groq(api_key="PASTE_YOUR_GROQ_KEY_HERE")

# 3. CSV DATABASE MANAGER
DB_FILE = "financial_report.csv"

def save_to_database(data_json):
    """
    Saves the extracted data into a CSV file (Excel compatible).
    """
    # Add a timestamp so we know WHEN it happened
    data_json["Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Convert single JSON object to a DataFrame (Table row)
    df_new = pd.DataFrame([data_json])
    
    # If file doesn't exist, create it with headers
    if not os.path.exists(DB_FILE):
        df_new.to_csv(DB_FILE, index=False)
    else:
        # Append to existing file without rewriting headers
        df_new.to_csv(DB_FILE, mode='a', header=False, index=False)
    
    return df_new

# 4. VISION ENGINE (Maverick)
def analyze_image_groq(image_file):
    base64_image = base64.b64encode(image_file.getvalue()).decode('utf-8')
    model_id = "meta-llama/llama-4-maverick-17b-128e-instruct"
    
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": "Analyze this document. Extract: Document_Type, Total_Amount, Vendor_Name, Risk_Level (Low/Med/High). Return ONLY JSON."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        }
    ]
    
    try:
        completion = client.chat.completions.create(
            model=model_id, 
            messages=messages,
            temperature=0.1,
            max_tokens=2048,
            stream=False,
            response_format={"type": "json_object"}
        )
        return completion.choices[0].message.content
    except Exception as e:
        raise e

# --- UI ---
st.title("🤖 Omega Protocol: The Digital Clerk")
st.caption("Auto-Saving Intelligence")

# SIDEBAR
with st.sidebar:
    st.header("Upload Station")
    uploaded_file = st.file_uploader("Drop Document Here", type=["jpg", "png", "jpeg"])
    
    st.divider()
    
    # DOWNLOAD BUTTON
    if os.path.exists(DB_FILE):
        st.subheader("Database")
        with open(DB_FILE, "rb") as f:
            st.download_button("Download Excel Report", f, file_name="financial_report.csv")

# MAIN AREA
col1, col2 = st.columns([1, 1])

if uploaded_file:
    with col1:
        image = Image.open(uploaded_file)
        st.image(image, caption="Current Document", use_container_width=True)
    
    with col2:
        st.subheader("Processing")
        if st.button("Process & Save"):
            with st.spinner("Maverick is reading and logging..."):
                try:
                    # 1. Analyze
                    response_text = analyze_image_groq(uploaded_file)
                    data = json.loads(response_text)
                    
                    # 2. Save to Disk
                    save_to_database(data)
                    
                    st.success("✅ Data Saved to Database!")
                    st.json(data)
                    
                except Exception as e:
                    st.error(f"Error: {e}")

    # LIVE DATABASE VIEW
    st.divider()
    st.subheader("📊 Live Ledger (financial_report.csv)")
    if os.path.exists(DB_FILE):
        df = pd.read_csv(DB_FILE)
        st.dataframe(df)
    else:
        st.info("No records yet. Process a document to start the ledger.")

else:
    st.info("Upload an image to start automation.")