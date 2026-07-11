import os
EMAIL = os.environ.get("STUDENT_EMAIL", "your_email@ds.study.iitm.ac.in")
AIPIPE_TOKEN = os.environ.get("AIPIPE_TOKEN", "PASTE_YOUR_AIPIPE_TOKEN")

# Fixed — do not change
AIPIPE_BASE = "https://aipipe.org/openai/v1"
TEXT_MODEL = "gpt-4o"
