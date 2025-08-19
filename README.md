# 🩺 Medi Morse

A lightweight CLI tool that helps nurses and caregivers generate or translate patient alerts into **Morse code**.

## 📦 Features

- Translate predefined medical alerts into Morse code  
- Input and send custom alert messages  
- Translate incoming Morse code back to English  
- (Coming Soon) Audio playback of Morse signals  
- (Planned) Logging system for tracking sent alerts  

## 🔧 How It Works

1. Clone the repository and navigate to the project folder:
    ```bash
    git clone https://github.com/HerbSneed/MediMorse.git
    cd MediMorse
    ```

2. Run the app from the command line:
    ```bash
    python main.py
    ```

3. Browse the list of predefined patient alerts, such as "Code Blue" or "Fall Risk."

4. When prompted:
    - Choose to **Generate** a Morse code message  
    - Or **Translate** incoming Morse code back into plain English

5. If generating, choose a **predefined alert** or enter a **custom message**

6. If translating, paste the Morse code into the terminal when prompted

7. Type `Q` or `QUIT` to exit the app at any time

8. ✅ Done!

## Demo

🎬 Watch MediMorse in action!

[![MediMorse Demo](https://img.youtube.com/vi/-32XLTra-YM/0.jpg)](https://youtu.be/-32XLTra-YM)



## 🧠 Use Cases

- Emergency backup communication  
- Training tool for Morse learners in healthcare  
- Portable and offline usage  

## 🛠 Requirements

- Python 3.7+  
- `helpers/` folder with:
  - `art.py` (ASCII art/logo)  
  - `morse_utils.py` (translation logic)  
  - `message_handlers.py` (alert logic)  

## 🚀 Roadmap

- [ ] Add Morse audio output  
- [ ] Create `alerts.log` file for tracking history  
- [ ] Improve CLI interface with color and formatting  
- [ ] Add test coverage  

## 👨‍⚕️ Author

Herb Sneed — [LinkedIn](https://www.linkedin.com/in/herbsneed) | [GitHub](https://github.com/HerbSneed)

---

> **MorseAid** — Because when words can’t reach, the signals can.
