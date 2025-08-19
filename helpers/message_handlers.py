from helpers.morse_utils import morse_conversion

PREDEFINED_ALERTS = {
    1: "Code Blue",
    2: "Need Supplies: IV Fluids",
    3: "Emergency: Patient in Distress",
    4: "Call Anesthesiologist",
    5: "Patient Requires Blood Transfusion",
    6: "Fire Alarm Activated",
    7: "Security Alert: Unauthorized Access",
    8: "Patient Allergic Reaction",
    9: "Need Transport to ICU",
    10: "Staff Meeting in Conference Room",
    11: "Equipment Failure",
    12: "Oxygen Supply Low",
    13: "Contagious Patient Alert",
    14: "Medication Delivery Needed",
    15: "Power Outage Warning",
}

def custom_message():
    """
    Prompts the user to enter a custom alert message and room number.
    Translates the combined message to Morse code and displays the result.
    """
    message = input("Enter Custom Message: ")
    while True:
        try:
            room_number = int(input('Input room number. Type 100-150: '))
            if 100 <= room_number <= 150:
                break
            else:
                print("Enter a valid number between 100-150: ")
        except ValueError:
            print("Please enter a number.")
    combined_message = f"{message} {room_number}"
    coded_message = morse_conversion(combined_message.upper())
    print(f"Coded Message: {coded_message}")
    input("Copy message then press Enter to return to the main menu...")

def user_alerts():
    """
    Prompts the user to choose an alert message and room number.
    Translates the combined message to Morse code and displays the result.
    """
    while True:
        try:
            user_alert = int(input('Choose an alert. Type 1-15: '))
            if 1 <= user_alert <= 15:
                break
            else:
                print("Enter a valid number between 1-15. ")
        except ValueError:
            print("Please enter a number. ")
    while True:
        try:
            room_number = int(input('Input room number. Type 100-150: '))
            if 100 <= room_number <= 150:
                break
            else:
                print("Enter a valid number between 100-150. ")
        except ValueError:
            print("Please enter a number. ")
    combined_message = f"{PREDEFINED_ALERTS[user_alert]} {room_number}"
    coded_message = morse_conversion(combined_message.upper())
    print(f"Coded Message: {coded_message}")
    input("Copy message then press Enter to return to the main menu...")
