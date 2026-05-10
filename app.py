import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/ussd", methods=['POST'])
def ussd_handler():
    # Variables sent by Africa's Talking
    session_id = request.values.get("sessionId", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    if text == "":
        # Main Menu: The first screen a mother sees
        response  = "CON SamaCare Virtual Midwife\n"
        response += "1. Pregnancy Check-up\n"
        response += "2. Emergency Help"

    elif text == "1":
        # First Triage Level: Screening for Red Flags
        response = "CON How do you feel today?\n"
        response += "1. I feel healthy\n"
        response += "2. Severe Headache\n"
        response += "3. Bleeding or Sharp Pain"

    elif text == "1*1":
        # Outcome for healthy mother
        response = "END Great! Remember to take your vitamins. See you next week."

    elif text == "1*2" or text == "1*3":
        # CRITICAL TRIAGE: This is the life-saving logic
        # In a real version, this triggers a notification to the Clinician Dashboard
        print(f"REPORT: Critical Red Flag from {phone_number}")
        response = "END EMERGENCY: Please go to the hospital immediately. A midwife has been notified."

    elif text == "2":
        response = "END Please dial 999 or proceed to the nearest emergency room immediately."

    else:
        response = "END Invalid selection. Please try again."

    return response

if __name__ == "__main__":
    # Get port from environment for deployment compatibility
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
