from helpers.art import art
from helpers.morse_utils import reverse_translation
from helpers.message_handlers import  custom_message, user_alerts, PREDEFINED_ALERTS
import sys

def main():
    while True:
        # clear_screen()
        print(art)
        print("===  Welcome to the Morse Alert System ===\n")
        for key in PREDEFINED_ALERTS:
            print(f"{key}. {PREDEFINED_ALERTS[key]}")
            if key == 15:
                while True:
                    send_receive = input("\nWould you like to generate or translate a message? Type G or T: ").upper()
                    if send_receive =="Q" or send_receive == "QUIT":
                        print("Goodbye")
                        sys.exit()
                    elif send_receive == "G":
                        user_custom_message = input('Would you like to send a custom message? Type Yes or No: ').lower()
                        if user_custom_message == 'no' or user_custom_message == 'n':
                            user_alerts()
                        elif user_custom_message == 'yes' or user_custom_message =='y':
                            custom_message()
                    elif send_receive == "T":
                        code = input("Type or paste morse code to be translated in English: ")
                        reverse_translation(code)
                    else:
                        break

if __name__ == "__main__":
    main()

#TODO: #sound_output Research winsound (Windows) or pygame to add Morse audio
#TODO: #logging Add a feature to log sent alerts to a file like alerts.log
#TODO: #github_upload Upload code to GitHub with README and sample output


