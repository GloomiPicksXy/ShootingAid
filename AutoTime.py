import customtkinter
import keyboard
import time

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()
app.title("Shooting Aid")  

def on_q_pressed(event):
    delay_q = int(entry_q.get()) / 1000 
    keyboard.press('e')
    time.sleep(delay_q)
    keyboard.release('e')

def on_r_pressed(event):
    delay_r = int(entry_r.get()) / 1000  
    keyboard.press('e')
    time.sleep(delay_r)
    keyboard.release('e')

frame = customtkinter.CTkFrame(master=app)
frame.pack(expand=True, fill="both")  
label = customtkinter.CTkLabel(master=frame, text="Autotime", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry_q = customtkinter.CTkEntry(master=frame, placeholder_text="Shooting (ms)")
entry_q.pack(pady=6, padx=10)

button_q = customtkinter.CTkButton(master=frame, text="Submit", command=on_q_pressed)
button_q.pack(pady=6, padx=10)

entry_r = customtkinter.CTkEntry(master=frame, placeholder_text="Layup (ms)")
entry_r.pack(pady=6, padx=10)

button_r = customtkinter.CTkButton(master=frame, text="Submit", command=on_r_pressed)
button_r.pack(pady=6, padx=10)

keyboard.on_press_key('q', on_q_pressed)
keyboard.on_press_key('r', on_r_pressed)

# Calculate the center of the screen
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
window_width = 300
window_height = 250
x_pos = (screen_width - window_width) // 2
y_pos = (screen_height - window_height) // 2

app.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")  # Set window position

app.mainloop()
