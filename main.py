from flask import Flask, request
import subprocess
import platform
import os
import signal

app = Flask(__name__)

player_process = None  # збережемо процес плеєра

def play_music(file_path):
    global player_process
    stop_music()  # зупиняємо, якщо вже щось грає

    system = platform.system()
    abs_path = os.path.abspath(file_path)

    try:
        if system == "Windows":
            # Відкриваємо стандартний плеєр Windows
            player_process = subprocess.Popen(['start', '', abs_path], shell=True)
        elif system == "Linux":
            # Спробуємо через xdg-open (відкриє за замовчуванням)
            player_process = subprocess.Popen(['xdg-open', abs_path])
        else:
            return False
        return True
    except Exception as e:
        print(f"Error launching player: {e}")
        return False

def stop_music():
    global player_process
    if player_process:
        try:
            if platform.system() == "Windows":
                # На Windows складно вбити процес через Popen, тому поки просто ігноруємо
                pass
            else:
                player_process.terminate()
            player_process = None
        except Exception as e:
            print(f"Error stopping player: {e}")

@app.route("/webhook2", methods=["GET", "POST"])
def webhook():
    file_path = "Try.mp3"
    if play_music(file_path):
        return "Music started!"
    else:
        return "Failed to start music", 500

@app.route("/stop", methods=["GET", "POST"])
def stop():
    stop_music()
    return "Music stopped!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002, debug=True)
