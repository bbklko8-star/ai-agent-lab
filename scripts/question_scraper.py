import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# ==============================
# Setup Paths
# ==============================
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

data_dir = os.path.join(BASE_DIR, "data")
os.makedirs(data_dir, exist_ok=True)

output_file = os.path.join(data_dir, "scraped_questions.csv")

# ==============================
# Selenium Setup (Kali Linux)
# ==============================
service = Service("/usr/bin/chromedriver")

options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/chromium"
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=service, options=options)

# ==============================
# Target URL
# ==============================
url = "https://www.examveda.com/general-knowledge/practice-mcq-question-on-indian-history/"
driver.get(url)

time.sleep(5)  # wait for page load

# ==============================
# Scraping Logic
# ==============================
questions = []

items = driver.find_elements(By.CLASS_NAME, "question-main")
print("Found questions:", len(items))

for q in items:
    try:
        question_text = q.find_element(By.CLASS_NAME, "question").text.strip()

        options = q.find_elements(By.CLASS_NAME, "option")

        option_a = options[0].text.strip()
        option_b = options[1].text.strip()
        option_c = options[2].text.strip()
        option_d = options[3].text.strip()

        questions.append({
            "exam": "SSC",
            "question": question_text,
            "option_a": option_a,
            "option_b": option_b,
            "option_c": option_c,
            "option_d": option_d,
            "answer": "",
            "explanation": ""
        })

    except Exception as e:
        print("Skipped one question:", e)

# ==============================
# Save to CSV
# ==============================
df = pd.DataFrame(questions)
df.to_csv(output_file, index=False)

driver.quit()

print("✅ Questions saved:", len(df))
print("📁 File saved at:", output_file)