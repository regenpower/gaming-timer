import tkinter as tk
from tkinter.filedialog import askopenfilename
import winsound as ws

# Window setup
root = tk.Tk()
root.geometry("400x300")
root.title("Gaming Timer")
root.resizable(False, False)

# Set initial alarm sound
global alarm_sound
alarm_sound = "Alarms/sample.wav"

# Open file explorer to select sound file
def get_alarm_sound():
    global alarm_sound
    alarm_sound = askopenfilename(title="Select a sound file, WAV format only", initialdir="Alarms", filetypes=[("WAV Files", "*.wav")])

# Print alarm_sound to console
def print_alarm_sound():
    global alarm_sound
    print(alarm_sound)

# Play alarm sound using winsound, loops it, async to avoid the program bricking
def play_alarm_sound():
    ws.PlaySound(alarm_sound, ws.SND_LOOP | ws.SND_ASYNC)

# Select alarm button
select_alarm_button = tk.Button(root, text="Get alarm sound", command=get_alarm_sound)
select_alarm_button.pack()

# Debug print alarm sound to console
print_alarm_button = tk.Button(root, text="[DEBUG] Print alarm_sound to console", command=print_alarm_sound)
print_alarm_button.pack()

# Play alarm_sound
play_alarm_button = tk.Button(root, text="Play alarm sound", command=play_alarm_sound)
play_alarm_button.pack()

root.mainloop()