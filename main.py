import os
import random
from tkinter import ttk, Toplevel, Tk, Button
from tkinter import font as tkFont  # Import font module from tkinter
from PIL import Image, ImageTk, ImageDraw, ImageFont
import pygame

def create_window(message):
    window = Toplevel()  # Use Toplevel() for child window
    window.title("Thông báo")
    
    # Create a new image
    img = Image.new("RGB", (300, 100), color='#FFB6C1')
    
    # Load the custom font
    font_path = os.path.join(os.path.dirname(__file__), 'font', 'UVNVAN_B.ttf')  # Thay đổi đường dẫn tới file font của bạn
    try:
        font = ImageFont.truetype(font_path, 24)
    except OSError:
        print(f"Font not found at {font_path}, using default font.")
        font = ImageFont.load_default()

    # Draw text on the image with the custom font
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), message, font=font, fill=(255, 255, 255))
    
    # Convert the image to tkinter PhotoImage
    tk_image = ImageTk.PhotoImage(img)
    
    # Display image in label
    label = ttk.Label(window, image=tk_image)
    label.image = tk_image  # Keep a reference to avoid garbage collection
    label.pack(padx=20, pady=20)
    
    # Randomly position the window on the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Random position ensuring the window is fully on the screen
    random_x = random.randint(0, screen_width - 300)  # 300 is the window width
    random_y = random.randint(0, screen_height - 100)  # 100 is the window height
    
    window.geometry(f'300x100+{random_x}+{random_y}')  # Set the window size and position

def create_windows(count=200, delay=200):
    if count > 0:
        create_window("Anh nhớ em!")
        root.after(delay, create_windows, count - 1, delay)

def start_creating_windows():
    # Initialize pygame for audio playback
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "tranbonho.wav"))
    pygame.mixer.music.play()
    
    create_windows()

def quit_program(event=None):
    """Handle quitting the program when Ctrl+Q is pressed."""
    root.quit()

# Create main application window
root = Tk()
root.title("Hello em!")
root.geometry("600x400")
root.resizable(False, False)

# Bind the Ctrl+Q shortcut to quit the program
root.bind('<Control-q>', quit_program)

# Center the window on the screen
x = (root.winfo_screenwidth() // 2) - 300
y = (root.winfo_screenheight() // 2) - 300
root.geometry(f'600x400+{x}+{y}')

# Set background image
bg_image_path = os.path.join(os.path.dirname(__file__), 'bg.jpg')
bg_image = ImageTk.PhotoImage(Image.open(bg_image_path).resize((600, 400), Image.LANCZOS))
ttk.Label(root, image=bg_image).place(relwidth=1, relheight=1)

# Use `tkFont` to set font for Button
custom_font = tkFont.Font(family="Helvetica", size=16, weight="bold")  # You can adjust the font as needed

# Create a custom button using `tk.Button` (for background color support)
start_button = Button(root, text="Start", fg="white", font=custom_font, bg="#FF69B4", command=start_creating_windows)
start_button.place(x=250, y=300)

# Start the Tkinter main loop
root.mainloop()
