import os

ENTRY = "Showergument \u2014 an argument you rehearse in the shower that you will never actually have."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
