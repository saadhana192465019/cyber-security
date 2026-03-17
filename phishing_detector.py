# Simple Keyword-Based Phishing Detector

suspicious_keywords = [
    "urgent",
    "verify",
    "suspended",
    "click here",
    "reset password",
    "act now",
    "account locked"
]

def check_email(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read().lower()

        found_keywords = []
        score = 0

        for word in suspicious_keywords:
            if word in content:
                found_keywords.append(word)
                score += 1

        print("\n--- Analysis Result ---")

        if score > 0:
            print("⚠ Suspicious Email Detected!")
            print("Found Keywords:")
            for k in found_keywords:
                print("-", k)
        else:
            print("✅ Email Looks Normal (No Suspicious Keywords Found)")

        print("Phishing Score:", score)

    except FileNotFoundError:
        print("File not found! Please check file name.")

# Main
file_input = input("Enter email file name (example: test_email.txt): ")
check_email(file_input)
