from helpers.art import art
from helpers.morse_utils import reverse_translation
from helpers.message_handlers import  custom_message, user_alerts, PREDEFINED_ALERTS
# from pydub import generators, AudioSegment


# Write a function to convert . and - into tones (using pydub.generators.Sine).
# Use pydub.silence for spacing.
# Combine the tones into a single audio segment.

# Dot (.): 1 unit long (e.g. 100 ms)
# dot = generators.Sine[:100]
# Dash (-): 3 units long (e.g. 300 ms)
# dash = generators.Sine[:300]

# Silence between parts of same letter: 1 unit
# let_silence = AudioSegment.silent(duration=100)
# Silence between letters: 3 units
# between_let_silence = AudioSegment.silent(duration=300)
# Silence between words: 7 units
# word_silence = AudioSegment.silent(duration=700)



# Play the audio using simpleaudio.

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
                        break
                    elif send_receive == "G":
                        user_custom_message = input('Would you like to send a custom message? Type Yes or No: ').lower()
                        if user_custom_message == 'no' or user_custom_message == 'n':
                            user_alerts()
                        elif user_custom_message == 'yes' or user_custom_message =='y':
                            custom_message()
                    elif send_receive == "T":
                        code = input("Type or paste morse code to be translated in English.")
                        reverse_translation(code)
                    else:
                        break

if __name__ == "__main__":
    main()

#TODO: #sound_output Research winsound (Windows) or pygame to add Morse audio
#TODO: #logging Add a feature to log sent alerts to a file like alerts.log
#TODO: #github_upload Upload code to GitHub with README and sample output


